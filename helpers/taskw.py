import subprocess
import re


class TaskW:
    def __init__(self, build_path: str):
        self.build_path = build_path

    def command(self, *args) -> str:
        result = subprocess.run(
            ["%s/task" % self.build_path] + list(args), stdout=subprocess.PIPE
        )
        return result.stdout.strip().decode("utf-8")

    def get_task_info(self, id: int) -> str:
        result = self.command(str(id))
        parsed_detail = str(result).split("\n")[3:]
        return parsed_detail
