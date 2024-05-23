import datetime
import uuid


def test_add_minimal_task(taskw):
    result = taskw.command("add", "do it now")
    assert result == "Created task 1."
    task_info_list = taskw.get_task_info(id=1)
    count = int(taskw.command("count", "status:pending"))
    assert count == 1


def test_add_many_tasks_in_parallel(taskw):
    for i in range(1, 100):
        result = taskw.command("add", "do item %s" % i)
    count = int(taskw.command("count", "status:pending"))
    assert count == 99


def test_add_task_with_due_date(taskw):
    result = taskw.command("add", "do it later", "due:tomorrow")
    due = taskw.command("_get", "1.due")
    due_as_date = datetime.date.fromisoformat(str(due)[0:10])
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    assert due_as_date == tomorrow


def test_get_and_use_uuid(taskw):
    result = taskw.command("add", "my task", "due:eoy")
    uuid_str = taskw.command("_get", "1.uuid")
    real_uuid = uuid.UUID(uuid_str)
    assert taskw.command("1") == taskw.command(uuid_str)


def test_annotation_for_existing_task(taskw):
    result = taskw.command("add", "plain task")
    taskw.command("1", "annotate", "now with more info")
    task_info_list = taskw.get_task_info(1)
    found = False
    for info in task_info_list:
        if "now with more info" in info:
            found = True
            break
    assert found
