class Duck:
    counter = 0
    species = "duck"

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter += 1

    def walk(self):
        pass

    def quack(self):
        print("quack")


class Chicken:
    species = "chicken"

    def walk(self):
        pass

    def cluck(self):
        print("clucks")


d1 = Duck(height=10, weight=2.2, sex="Male")
d2 = Duck(height=12, weight=2.8, sex="Male")
d3 = Duck(height=14, weight=4.2, sex="Female")

c1 = Chicken()

print("So many ducks were born:", Duck.counter)

for poultry in d1, d2, d3, c1:
    print(poultry.species, end=" ")
    if poultry.species == "duck":
        poultry.quack()
    elif poultry.species == "chicken":
        poultry.cluck()