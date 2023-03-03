class First:
    def run(self):
        print("running from first")

class Second:
    def run(self):
        print("running from second")

class Third(First):
    ...
    ...