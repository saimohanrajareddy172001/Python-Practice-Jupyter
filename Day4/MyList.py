class MyList:
    def __init__(self):
        self.data=[]
    def __len__(self):
        return len(self.data)
    def __getitem__(self,key):
        return self.data[key]
    def __setitem__(self,key,value):
        self.data[key]=value
    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return item in self.data

    def add(self, value):
        self.data.append(value)

m1=MyList()
m1.add(10)
m1.add(20)
m1.add(30)

print(len((m1)))
print(m1[1])
m1[1]=200
print(m1[1])
del m1[1]
print(m1[m1])
