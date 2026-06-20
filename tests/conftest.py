import pytest
from copy import deepcopy
from fastapi.testclient import TestClient

from src.app import app, activities as app_activities

@pytest.fixture
def client():
    original_activities = deepcopy(app_activities)
    client = TestClient(app)

    yield client

    app_activities.clear()
    app_activities.update(original_activities)
