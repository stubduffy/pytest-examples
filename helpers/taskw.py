import subprocess

class TaskW:
    def __init__(self, build_path):
        self.build_path = build_path
        self.last_result = ""

    def command(self, *args):
        result = subprocess.run(["%s/task" % self.build_path] + list(args), stdout=subprocess.PIPE)
        return result.stdout
