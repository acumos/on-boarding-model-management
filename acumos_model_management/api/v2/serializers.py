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

model_resource = api.model('Model', {
    'key': fields.String(),
    'name': fields.String(),
    'versionId': fields.String(),
    'modelFormat': fields.String(),
    'description': fields.String(),
    'createdTimestamp': fields.String()
})
