from dataclasses import dataclass


@dataclass
class Ubezpieczony:
    name: str  # will become arg in __init__
    salary: int = 0  # will become kwarg in __init__, default value!


person1 = Ubezpieczony("Adam Jurkiewicz")
person2 = Ubezpieczony("Beata Jurkiewicz", salary=2000)


# => hello 0
print(person1.name, person1.salary)
print(person2.name, person2.salary)
print(person1)
# error, a not specified
Ubezpieczony()
# => TypeError: __init__() missing 1 required positional argument: 'a'