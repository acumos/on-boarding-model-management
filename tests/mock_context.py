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
