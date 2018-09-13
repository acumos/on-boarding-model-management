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

from acumos_model_management.api.v2.serializers import ser_models_comments, ser_modeltypes_catalog
from acumos_model_management.api.namespaces import modelmanager_v2_namespace as api
from acumos_model_management.api.parser import model_file_upload, document_file_upload, catalog_file_upload


def placeholder():
    abort(400, 'TODO: This API is just a stub. Method not yet implemented')


@api.route('/models')
class ModelCollection(Resource):
    @api.response(200, 'OK')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error')
    @api.doc(params={'searchCriteria': ('If searchType is basic, format is a string. If searchType is advanced, '
                                        'format is JSON-encoded key:value pairs, where key is attribute name'),
                     'searchType': 'The type of search. Either basic or advanced.',
                     'patternType': 'The pattern type. Either regex or glob; defaults to regex.'})
    def get(self):
        """
        Retrieve Models using a text search

        Retrieve Models for namespace using textSearch or Retrieve Model with primary key modelKey or
        Retrieve Models with textSearch in comma separated modelSearchKey[s]
        """
        placeholder()

    @api.response(201, 'Created')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(409, 'Conflict')
    @api.response(413, 'Payload Too Large')
    @api.response(415, 'Unsupported Media Type')
    @api.response(500, 'Internal Server Error')
    @api.expect(model_file_upload,
                document_file_upload,
                catalog_file_upload, validate=False)
    def post(self):
        """
        Create a new Model

        :param predictor:

        :return:
        """
        placeholder()


@api.route('/models/<string:modelKey>')
class ModelItem(Resource):
    @api.response(204, 'No Content')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Not Authorized')
    # @api.response(403, 'Forbidden')
    @api.response(404, 'Not Found')
    @api.response(500, 'Unexpected Error')
    def delete(self, modelKey):
        """
        Delete Model with modelKey
        """
        placeholder()

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
        placeholder()

    @api.response(200, 'OK')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(404, 'Not Found')
    @api.response(415, 'Unsupported Media Type')
    @api.response(500, 'Unexpected Error')
    def put(self, modelKey):
        """
        Update Model with modelKey
        """
        placeholder()


@api.route('/models/<string:modelKey>/attributes')
class ModelCatalogItem(Resource):
    @api.response(200, 'OK')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(404, 'Not Found')
    @api.response(415, 'Unsupported Media Type')
    @api.response(500, 'Unexpected Error')
    def put(self, modelKey):
        """
        Update Model attributes for the model using the specified modelKey
        """
        placeholder()
