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

from flask_restplus import Resource, abort

from acumos_model_management.api.v2.business import get_models, get_model, delete_model, create_model, \
    update_model_attributes, get_model_contents
from acumos_model_management.api.v2.serializers import ser_models_comments
from acumos_model_management.api.namespaces import modelmanager_v2_namespace as api
from acumos_model_management.api.parser import model_file_upload, document_file_upload, catalog_file_upload


@api.route('/models')
@api.response(500, 'Internal Server Error')
class ModelCollection(Resource):
    def get(self):
        """
        Retrieve all existing models
        """
        return get_models()

    @api.response(201, 'Created')
    @api.response(400, 'Bad Request')
    @api.expect(model_file_upload,
                document_file_upload,
                catalog_file_upload, validate=False)
    def post(self):
        """
        Create a new Model entry
        """
        return create_model()


@api.route('/models/<string:modelKey>')
@api.response(500, 'Unexpected Error')
class ModelItem(Resource):
    @api.response(204, 'No Content')
    def delete(self, modelKey):
        """
        Delete Model with modelKey
        """
        return delete_model(modelKey)

    @api.response(200, 'Predictor successfully retrieved')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Not Authorized')
    @api.response(403, 'Forbidden')
    @api.response(404, 'Invalid Key')
    @api.response(500, 'Unexpected Error')
    def get(self, modelKey):
        """
        Retrieves Model with modelKey
        """
        return get_model(modelKey)


@api.route('/models/<string:modelKey>/attributes')
@api.response(500, 'Unexpected Error')
class ModelAttributesResource(Resource):
    @api.response(200, 'OK')
    @api.response(400, 'Bad Request')
    @api.response(404, 'Not Found')
    def put(self, modelKey):
        """
        Update Model attributes for the model using the specified model key
        """
        return update_model_attributes(modelKey)


@api.route('/models/<string:modelKey>/contents')
@api.response(500, 'Unexpected Error')
class ModelContentsResource(Resource):
    @api.response(200, 'OK')
    @api.response(404, 'Not Found')
    @api.response(500, 'Unexpected Error')
    def get(self, modelKey):
        """Gets the contents of the model file"""
        return get_model_contents(modelKey)
