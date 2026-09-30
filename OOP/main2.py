# Câu 2: Dùng __add__() để cộng lị age hai Peron đối tương lại với nhau.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age

p1 = Person("Emil", 22)
p2 = Person("Tobias", 19)    

print(p1 + p2) 