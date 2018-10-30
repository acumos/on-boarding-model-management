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
from unittest.mock import patch

import json
import tempfile

app = Flask(__name__)


with mongo_test_context():
    from acumos_model_management.app import initialize_app
    initialize_app(app)
    temporary_directory = tempfile.mkdtemp()
    app.config['UPLOAD_FOLDER'] = temporary_directory


def test_endpoints():
    metadata = {
        'name': 'endpointstestmodel',
        'modelFormat': 'Custom',
        'description': 'initial'
    }

    data = {
        'model': (BytesIO(b'test'), 'model.txt'),
        'metadata': (BytesIO(json.dumps(metadata).encode()), 'model.txt')
    }

    model_key = None
    with app.test_client() as c:
        r = c.post('/v2/models', data=data)
        assert r.status_code == 201
        model_key = json.loads(r.get_data().decode()).get('key')

        r = c.get('/v2/models')
        assert r.status_code == 200
        assert len(json.loads(r.get_data().decode())) > 0

        r = c.get('/v2/models')
        assert r.status_code == 200
        assert len(json.loads(r.get_data().decode())) > 0

        r = c.get('/v2/models/{}'.format(model_key))
        assert r.status_code == 200
        assert json.loads(r.get_data().decode()).get('name') == 'endpointstestmodel'

        r = c.get('/v2/models/{}/contents'.format(model_key))
        assert r.status_code == 200
        assert r.get_data().decode() == 'test'

        metadata['description'] = 'test updating description'
        headers = {
            'content-type': 'application/json'
        }
        r = c.put('/v2/models/{}/attributes'.format(model_key), headers=headers, data=json.dumps(metadata))
        assert r.status_code == 200
        assert json.loads(r.get_data().decode()).get('description') == 'test updating description'
