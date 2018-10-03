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

from contextlib import contextmanager
from datetime import datetime
from unittest.mock import patch

import pytz


class MockedFilteredResult():
    def __init__(self, objects=None):
        self.objects = objects

    def first(self):
        if self.objects is not None:
            return self.objects[0]
        return None


class MockedFilter():
    def __init__(self):
        self.mocked_models = {}

    def filter(self, key=None):
        if key in self.mocked_models:
            return MockedFilteredResult([self.mocked_models[key]])
        return MockedFilteredResult()

    def all(self):
        return self.mocked_models.values()

    def put(self, key, model):
        self.mocked_models[key] = model

    def delete(self, key):
        del self.mocked_models[key]


class MockedModelDocument():
    objects = MockedFilter()

    def __init__(self, key=None):
        self.key = key
        self.created_timestamp = datetime.utcnow().replace(tzinfo=pytz.utc)

    def save(self):
        self.objects.put(self.key, self)

    def delete(self):
        self.objects.delete(self.key)


@contextmanager
def mongo_test_context():
    """Custom test context for mocking out MongoEngine"""

    with patch('flask_mongoengine.MongoEngine'):
        with patch('acumos_model_management.database.models.ModelDocument', new=MockedModelDocument):
            yield
