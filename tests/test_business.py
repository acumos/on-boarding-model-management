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

from .mock_context import mongo_test_context
from contextlib import contextmanager
from flask import Flask
from io import BytesIO
from werkzeug.exceptions import NotFound

import json
import pytest
import uuid
import tempfile

app = Flask(__name__)
temporary_directory = tempfile.mkdtemp()
app.config['UPLOAD_FOLDER'] = temporary_directory


@contextmanager
def business_test_context(**kwargs):
    """Custom test context for mocking out MongoEngine"""

    with mongo_test_context():
        with app.test_request_context(**kwargs):
            from acumos_model_management.api.v2 import business
            yield business

def test_get_models():
    with business_test_context() as business:
        models = business.get_models()
        assert isinstance(models, list)


def test_crud_workflow():
    with business_test_context() as business:
        with pytest.raises(NotFound):
            # not found should be returned for a model that does not exist
            business.get_model(str(uuid.uuid4()))

    metadata = {
        'name': 'testmodel',
        'modelFormat': 'Custom',
        'description': 'initial'
    }

    data = {
        'model': (BytesIO(b'test'), 'model.txt'),
        'metadata': (BytesIO(json.dumps(metadata).encode()), 'model.txt')
    }
    model_key = None
    with business_test_context(data=data) as business:
        model, status_code = business.create_model()
        assert status_code == 201
        model_key = model['key']

    with business_test_context() as business:
        model = business.get_model(model_key)
        assert model['name'] == 'testmodel'
        assert model['modelFormat'] == 'Custom'
        assert model['description'] == 'initial'


    with business_test_context() as business:
        response = business.get_model_contents(model_key)

        # disable direct_passthrough for testing
        response.direct_passthrough = False

        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'test'

    metadata['description'] = 'second'
    headers = {
        'content-type': 'application/json'
    }
    with business_test_context(method='PUT', headers=headers, data=json.dumps(metadata)) as business:
        model = business.update_model_attributes(model_key)
        assert model['name'] == 'testmodel'
        assert model['modelFormat'] == 'Custom'
        assert model['description'] == 'second'

    with business_test_context(method='DELETE') as business:
        model = business.delete_model(model_key)

    with business_test_context() as business:
        with pytest.raises(NotFound):
            business.get_model(str(uuid.uuid4()))
