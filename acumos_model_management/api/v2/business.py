# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================

from acumos_model_management.api.responses import not_found, no_content_response, created_response, bad_request
from acumos_model_management.api.v2.parsers import ModelDocumentParser
from acumos_model_management.database.models import ModelDocument, ModelFormat
from flask import request, send_file, current_app as app
from json.decoder import JSONDecodeError
from werkzeug.utils import secure_filename

import json
import logging
import os
import uuid

logger = logging.getLogger(__name__)


def _get_model_object(model_key):
    item = ModelDocument.objects.filter(key=model_key).first()
    if item is None:
        not_found("Model with key {} not found".format(model_key))
    return item


def _get_model_metadata():
    try:
        metadata = json.loads(request.files['metadata'].read())
    except JSONDecodeError as jde:
        bad_request('Unable to decode model metadata. Expected JSON; failed with error {}'.format(jde))

    required_keys = ['name', 'modelFormat']
    for key in required_keys:
        if key not in metadata:
            bad_request('Metadata JSON body missing required key {}'.format(key))

    model_format = metadata.get('modelFormat')
    accepted_formats = ModelFormat.get_formats()
    if model_format not in accepted_formats:
        str_accepted_formats = ', '.join(accepted_formats)
        bad_request('Invalid Model format. Got "{}". Expected one of: {}.'.format(model_format, str_accepted_formats))
    return metadata


def create_model():
    required_files = ['model', 'metadata']
    for required_file in required_files:
        if required_file not in request.files:
            bad_request('File "{}" required as part of multipart request'.format(required_file))

    model_file = request.files['model']
    filename = secure_filename(model_file.filename)
    model_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    model_file.save(model_path)

    metadata = _get_model_metadata()
    model = ModelDocument(key=str(uuid.uuid4()))

    model.name = metadata.get('name')
    model.description = metadata.get('description', '')
    model.model_format = metadata.get('modelFormat')
    model.version_id = str(uuid.uuid4())
    model.model_path = model_path
    model.save()

    return created_response(ModelDocumentParser(model).as_dict())


def get_models():
    models = ModelDocument.objects.all()
    return [ModelDocumentParser(model).as_dict() for model in models]


def get_model(model_key):
    model = _get_model_object(model_key)
    return ModelDocumentParser(model).as_dict()


def delete_model(model_key):
    model = _get_model_object(model_key)
    os.remove(model.model_path)
    model.delete()
    return no_content_response()


def update_model_attributes(model_key):
    model = _get_model_object(model_key)
    obj = request.get_json()
    if obj is None:
        bad_request('Request must be application/json')

    # only updating the description is currently allowed
    model.description = obj.get('description')
    model.save()

    return ModelDocumentParser(model).as_dict()

def get_model_contents(model_key):
    model = _get_model_object(model_key)
    return send_file(model.model_path)
