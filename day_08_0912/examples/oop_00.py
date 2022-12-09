class Klasa:
    sex = 'Female'


# __main__ wykonywana bezpośrednio <- znaczy, że klasa o typie klasa jest w tym skrypcie wykonywana

# obiekt typu klasy
obiekt_x = Klasa()

# kopia klasy <- tego się nie stosuje
# obiekt_y = Klasa
obiekt_y = Klasa()

print(type(obiekt_x))
# print(type(obiekt_y))

print(dir(obiekt_x))
obiekt_x.name = 'Pszczółka Maja'
obiekt_y.age = 12

print(dir(obiekt_x))
print(dir(obiekt_y))

print(obiekt_x.sex)
obiekt_y.sex = 'Male'
print(obiekt_y.sex)
