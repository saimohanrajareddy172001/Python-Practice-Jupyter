class Person:
    def __init__(self,height,weight,age):
        self.height=height
        self.weight=weight
        self.age=age
    def __add__(self, other):
        return Person(
            self.height + other.height,
            self.weight + other.weight,
            self.age + other.age
        )
    def __str__(self):
        return f"Person(height={self.height},weight={self.weight},age={self.age})"
                                                                       
p1 = Person(22, 22, 22)
p2 = Person(33, 33, 33)
p3 = p1 + p2
print(p3)
help(10)
