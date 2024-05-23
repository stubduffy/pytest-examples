import pytest
import os
from helpers.taskw import TaskW


@pytest.fixture(scope="session")
def taskw():
    return TaskW(os.environ.get("TASKW_PATH"))