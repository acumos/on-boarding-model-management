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
model_file_upload.add_argument('file',
                               type=werkzeug.datastructures.FileStorage,
                               location='files',
                               required=True,
                               help='Model File')

document_file_upload = reqparse.RequestParser()
document_file_upload.add_argument('document',
                                  type=werkzeug.datastructures.FileStorage,
                                  location='files',
                                  required=True,
                                  help='Document File')

catalog_file_upload = reqparse.RequestParser()
catalog_file_upload.add_argument('catalog',
                                 type=werkzeug.datastructures.FileStorage,
                                 location='files',
                                 required=True,
                                 help='Catalog File')
