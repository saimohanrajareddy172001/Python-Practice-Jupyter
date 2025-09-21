class Phone:
    counter=0

    def __init__(self,number):
        self.number=number
        Phone.counter+=1
        print(f"Phone created with number {self.number}")

class FixedPhone(Phone):
    last_SN=0

    def __init__(self,number):
        super().__init__(number)
        FixedPhone.last_SN+=1
        self.SN=f"FP-{FixedPhone.last_SN}"
        print(f"FixedPhone created with serial {self.SN}")
class MobilePhone(Phone):
    last_SN=0

    def __init__(self,number):
        super().__init__(number)
        MobilePhone.last_SN+=1
        self.SN=f"MP-{MobilePhone.last_SN}"
        print(f"MobilePhone created with serial {self.SN}")
f1=FixedPhone("123-233")
f2=FixedPhone("232-213")
m2=MobilePhone("233-333")
print(f1.number)
print(f2.number)
print(m2.number)