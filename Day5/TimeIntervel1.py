class TimeIntervel1:
    def __init__(self,*,hours=0,minutes=0,seconds=0):
        if not isinstance(hours,int) or not isinstance(minutes,int) or not isinstance(seconds,int):
            raise TypeError("hours,minutes,and seconds must be integers")
        self.total_seconds=hours*3600+minutes*60+seconds

    def __str__(self):
        hrs=self.total_seconds//3600
        mins=(self.total_seconds%3600)//60
        secs=self.total_seconds%60
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"


    def __add__(self,other):
        if isinstance(other,TimeIntervel1):
            total=self.total_seconds+other.total_seconds
        elif isinstance(other,int):
            total =self.total_seconds+other
        else:
            raise TypeError("can only add TimeIntervel1 or int(seconds)")
        return TimeIntervel1(seconds=total)
    __radd__=__add__
        


    def __sub__(self,other):
        if isinstance(other,TimeIntervel1):
            total=self.total_seconds-other.total_seconds
        elif isinstance(other,int):
            total=self.total_seconds-other
        else:
            raise TypeError("can only add TimeIntervel1 or int(seconds)")
        return TimeIntervel1(seconds=total)
    __rsub__=__sub__

    def __mul__(self, value):
        if not isinstance(value, int):
            raise TypeError("Can only multiply TimeIntervel1 by an integer")
        total = self.total_seconds * value
        return TimeIntervel1(seconds=total)

    __rmul__ = __mul__   # support reverse: 2 * t1

t1=TimeIntervel1(hours=1,minutes=20,seconds=30)
t2=TimeIntervel1(hours=1,minutes=20,seconds=30)
print(t1.total_seconds)
print(t1+t2)
print(t1+40)
print(t1-t2)
print(t2-40)
print(t1*2)
print(30-t2)
print(40+t1)
