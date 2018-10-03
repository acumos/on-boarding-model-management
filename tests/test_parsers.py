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


from acumos_model_management.api.v2.parsers import ModelDocumentParser
from datetime import datetime

import pytz


class MockedModelDocument():
    def __init__(self):
        self.key = '1234'
        self.name = 'name1'
        self.version_id = '1234'
        self.model_format = 'Custom'
        self.description = 'Mock Desc'
        self.created_timestamp = datetime.utcnow().replace(tzinfo=pytz.utc)


def test_as_dict():
    parsed_dict = ModelDocumentParser(MockedModelDocument()).as_dict()
    assert parsed_dict.get('key') == '1234'
    assert parsed_dict.get('name') == 'name1'
    assert parsed_dict.get('versionId') == '1234'
    assert parsed_dict.get('modelFormat') == 'Custom'
    assert parsed_dict.get('description') == 'Mock Desc'
    assert parsed_dict.get('createdTimestamp', None) is not None
