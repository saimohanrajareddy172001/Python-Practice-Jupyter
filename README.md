# Python Practice Jupyter

This repository contains my Python practice programs, organized by days.  
Each folder (Day1 → Day5) includes complete working programs I wrote while practicing.

---

## 📂 Folder Contents

- **Day1**
  - Duplicate check programs (brute force + optimized)
  - Anagram checker
- **Day2**
  - Beginner practice: loops, conditions, simple OOP examples
- **Day4**
  - Custom class exercises:
    - `MyList.py`
    - `Person.py`
    - `Phone.py`
    - `Vehicle.py`
- **Day5**
  - `TimeIntervel1.py` → operator overloading with `+`, `-`, `*`
  - Other OOP practice programs

---

## 🚀 Example: TimeIntervel1
```python
from Day5.TimeIntervel1 import TimeIntervel1

t1 = TimeIntervel1(hours=1, minutes=20, seconds=30)
t2 = TimeIntervel1(minutes=40, seconds=40)

print(t1 + t2)   # 02:01:10
print(t1 - 45)   # 01:19:45
print(2 * t1)    # 02:41:00
