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

from flask_restplus import fields
from acumos_model_management.api.namespaces import modelmanager_v2_namespace as api

create_model_catalog = api.model('CreateModelCatalog', {
    'projectKey': fields.String(required=True, description='', exampe=''),
    'versionId': fields.String(required=True, description='', exampe=''),
    'modelComment': fields.String(required=False, description='', exampe=''),
    'documentComment': fields.String(required=False, description='', exampe='')

})

metadata_fields = api.model('Metadata', {
    'key': fields.String(required=True, description='Key used in metadata entry.', example='K8S_POD_REPLICAS'),
    'value': fields.Raw(required=True, description='Value used in metadata entry.', example='2')
})

ser_models_comments = api.model('ModelsComments', {
    'comment': fields.String(required=False, description='', example='This model solves problem x.')
})
