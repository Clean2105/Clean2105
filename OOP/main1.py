# Câu 1: Mặc định cho các tham số trong __init__() phương thức: 
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)