```python
from math import sqrt
class Theorem:
    def equation(self):
        pass
class Pythagoras(Theorem):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def equation(self):
        return sqrt(self.a**2+self.b**2)
class Height(Theorem):
    def __init__(self, m, n, p):
        self.m = m
        self.n = n
        self.p = p
    def equation(self):
        return self.m*self.n/self.p
theorems = [Pythagoras(3,4), Height(3,4,5)]
for theorem in theorems:
    print(theorem.equation())
```
