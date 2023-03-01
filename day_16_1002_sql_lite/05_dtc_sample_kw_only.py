from dataclasses import dataclass, field
import uuid


# for Python 3.10 and next
@dataclass(frozen=True, kw_only=True)
class Ubezpieczony:
    name: str = "Some person"  # will become arg in __init__
    salary: int = 0  # will become kwarg in __init__, default value!
    id: str = field(init=False, repr=False, default_factory=uuid.uuid4)
    def __post_init__(self):
        print(f"UUID: {self.id}")


person1 = Ubezpieczony(name="Adam Jurkiewicz", salary=235)
person2 = Ubezpieczony(name="Beata Jurkiewicz", salary=2000)
print(person1)
print(person2)


print(person1.name, person1.salary)
print(person2.name, person2.salary)

