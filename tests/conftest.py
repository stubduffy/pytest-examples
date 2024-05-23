import pytest
from helpers.taskw import TaskW

@pytest.fixture(scope="session")
def taskw():
    return TaskW()