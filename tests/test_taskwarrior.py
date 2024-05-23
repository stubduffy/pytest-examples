def test_add_task(taskw):
    print(taskw.command("add", "hello"))
    print(taskw.command("list"))
    print(taskw.command("_get", "1.description"))
