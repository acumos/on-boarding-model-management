#
# ===============LICENSE_START=======================================================
# Acumos
# ===================================================================================
# Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
from flask import Flask
from api.restplus import api_v2, blueprint_v2
from api.v2.endpoints import api as model_builder_v2_namespace

app = Flask(__name__)


def initialize_app(flask_app):
    api_v2.namespaces.clear()
    api_v2.add_namespace(model_builder_v2_namespace)
    app.register_blueprint(blueprint_v2)


def main():
    initialize_app(app)
    app.run(host='0.0.0.0', debug=True, port=8061)


if __name__ == '__main__':
    main()
