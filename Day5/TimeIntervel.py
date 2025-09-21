class TimeInterval:
    def __init__(self, *, hours=0, minutes=0, seconds=0):
        if not isinstance(hours,int) or not isinstance(minutes,int) or not isinstance(seconds,int):
            raise TypeError("Hours, minutes, and seconds must be integers")
        self.total_seconds = hours*3600 + minutes*60 + seconds

    def __str__(self):
        hrs = self.total_seconds // 3600
        mins = (self.total_seconds % 3600) // 60
        secs = self.total_seconds % 60
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    
    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval")
        return TimeInterval(seconds=self.total_seconds + other.total_seconds)
    
    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only subtract TimeInterval")
        return TimeInterval(seconds=self.total_seconds - other.total_seconds)
    
    def __mul__(self, value):
        if not isinstance(value, int):
            raise TypeError("Can only multiply TimeInterval by an integer")
        return TimeInterval(seconds=self.total_seconds * value)
    
    __rmul__ = __mul__   # allow 2 * t1


# 🔎 Testing
t1 = TimeInterval(hours=1, minutes=0, seconds=0)
t2 = TimeInterval(hours=1,minutes=0, seconds=0)

print("t1:", t1)   # 01:20:30
print("t2:", t2)   # 00:40:40

print("t1 + t2 =", t1 + t2)   # 02:01:10
print("t1 - t2 =", t1 - t2)   # 00:39:50
print("t2 * 3 =", t2 * 3)     # 02:02:00
print("2 * t1 =", 2 * t1)     # 02:41:00