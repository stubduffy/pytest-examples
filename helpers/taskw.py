import subprocess

class TaskW:
    def __init__(self):
        self.last_result = ""

    def command(self, *args):
        result = subprocess.run(['/Users/stuart.duffy/Projects/taskwarrior/build/src/task'] + list(args), stdout=subprocess.PIPE)
        return result.stdout
