from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int

p = Person("Akil",12)
print(p.name)