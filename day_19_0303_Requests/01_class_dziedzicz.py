class First:
    def __init__(self, parameter1):
        self.parameter1 = parameter1

    def run(self):
        print(f"running from first - {self.parameter1=}")


class Second:
    def run(self):
        print("running from second")


class Third(First):
    def __init__(self, parameter3, parameter1):
        super().__init__(parameter1)
        self.parameter3 = parameter3
        # self.parameter1 = parameter1

    def third_run(self):
        print(f"running from third - {self.parameter3} - {self.parameter1}")

    def run(self):
        # najpierw wykonuje się run z First, potem run z Third
        super().run()
        print("Teraz run 3")


first = First("Gucio")
second = Second()
third = Third("Pszczolka", "Maja")

first.run()
second.run()

third.third_run()
third.run()
