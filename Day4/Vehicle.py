class Vehicle:
    counter=0
    def __init__(self,brandName):
        self.brandName=brandName

class Car(Vehicle):
    last_SN=0
    def __init__(self,brandName):
        super().__init__(brandName)
        Car.last_SN+=1
        self.SN=f"CAR-{Car.last_SN}"
        print(f"Car created with serial {self.SN}")
class Bike(Vehicle):
    last_SN=0
    def __init__(self,brandName):
        super().__init__(brandName)
        Bike.last_SN=+1
        self.SN=f"Bike-{Bike.last_SN}"
        print(f"Bike created with serial {self.SN}")
c1 = Car("Toyota")
c2 = Car("Honda")
b1 = Bike("Yamaha") 
print(c1.brandName,c1.SN)    
print(c2.brandName,c2.SN)
print(b1.brandName,b1.SN)

normally we do like this def __init__(self,brand,SN)
    self.brand=brand
    self.SN=SN