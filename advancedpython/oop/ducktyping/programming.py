#functionality same
class Pycharm:
    def compile(self):
        print("Compile using Pycharm")

    def execute(self):
        print("execute using Pycharm")

    def debug(self):
        print("debug using pycharm")

class Vscode:
    def compile(self):
        print("Compile using Vscode")

    def execute(self):
        print("execute using Vscode")

    def debug(self):
        print("debug using vscode")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
pr=Programmer()
py=Pycharm()
vs=Vscode()
pr.coding(py)
pr.coding(vs)