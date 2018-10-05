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

import werkzeug
from flask_restplus import reqparse

model_file_upload = reqparse.RequestParser()
model_file_upload.add_argument('model', type=werkzeug.datastructures.FileStorage, location='files', required=True,
                               help='Model File')

metadata_file_upload = reqparse.RequestParser()
metadata_file_upload.add_argument('metadata', type=werkzeug.datastructures.FileStorage, location='files', required=True,
                                  help='Metadata about the model file')
