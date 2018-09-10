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

from flask import Blueprint
from flask_restplus import Api

import logging

logger = logging.getLogger(__name__)


authorizations = {
    'basicAuth': {
        'type': 'basic',
    }
}

blueprint_v2 = Blueprint('Acumos', __name__, url_prefix='/v2')


api_v2 = Api(blueprint_v2, version='2.0.0', title='Acumos Model Catalog REST Service',
             default_label='Acumos Model Manager', validate=True,
             description='The Acumos Catalog provides RESTful interfaces to manage the lifecycle of a model.',
             authorizations=authorizations, security='basicAuth')
