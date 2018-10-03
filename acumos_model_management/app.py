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

from acumos_model_management import settings
from acumos_model_management.api.restplus import api_v2, blueprint_v2
from acumos_model_management.api.v2.endpoints import api as modelmanager_v2_namespace
from acumos_model_management.database.models import db


def initialize_app(flask_app):
    """Initializes the REST interfaces and database"""
    flask_app.config['ERROR_404_HELP'] = settings.ERROR_404_HELP

    api_v2.add_namespace(modelmanager_v2_namespace)
    flask_app.register_blueprint(blueprint_v2)
    db.init_app(flask_app)
