from dataclasses import dataclass

"""
@dataclass(
    *, 
    init=True, 
    repr=True, 
    eq=True, 
    order=False, 
    unsafe_hash=False, 
    frozen=False,
    ...
)
"""
# klasa zamrożona, nie można zmieniać agrumentów
@dataclass(frozen=True)
class Ubezpieczony:
    name: str  # will become arg in __init__
    salary: int = 0  # will become kwarg in __init__, default value!
    # nie można zrobić poniższego, gdy jest frozen
    # def __post_init__(self):
    #     if self.salary == 0:
    #         self.salary = 234

person1 = Ubezpieczony("Adam Jurkiewicz")
person2 = Ubezpieczony("Beata Jurkiewicz", salary=2000)


print(person1.name, person1.salary)
print(person2.name, person2.salary)
print(person1)

person1.salary = 10
