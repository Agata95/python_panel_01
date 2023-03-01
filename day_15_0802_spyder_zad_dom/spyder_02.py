from dataclasses import dataclass

@dataclass
class Ubezpieczony:
    name: str
    salary: int = 0
    
    def __post_init__(self):
        if self.salary==0:
            self.salary = 234
    
person1 = Ubezpieczony("Pszczółka Maja")
person2 = Ubezpieczony("Gucio", salary = 2000)

print(person1.name, person1.salary)
print(person2.name, person2.salary)
print(person1)
