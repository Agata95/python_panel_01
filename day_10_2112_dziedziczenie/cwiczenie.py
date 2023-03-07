class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def metoda_1(self):
        return self.a


class B(A):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def metoda_2(self):
        return self.b


a1 = A(1, 2)
b1 = B(3, 4)

print(a1.metoda_1())
print(b1.metoda_1())
print(b1.metoda_2())
