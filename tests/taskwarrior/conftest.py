import pytest
import os
import time
from helpers.taskw import TaskW


@pytest.fixture(scope="session")
def taskw():
    return TaskW(os.environ.get("TASKW_PATH"))


@pytest.fixture(scope="function", autouse=True)
def mark_all_tasks_done(taskw):
    count = int(taskw.command("count", "status:pending"))
    for i in range(1, count + 1):
        taskw.command("done", str(i))

    i = 1
    while int(taskw.command("count", "status:pending")) > 0 and i < 10:
        i += 1
        time.sleep(0.5)
