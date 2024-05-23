def test_add_task(taskw):
    taskw.command("add", "hello")
    count = taskw.command("count")
    assert count == 1
