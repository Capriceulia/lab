```python
from math import sqrt
one = [12,25,3,48,71]
two = [5,18,40,62,98]
three = [4,21,37,56,84]
a1 = max(one)
a2 = min(one)
b1 = max(two)
b2 = min(two)
c1 = max(three)
c2 = min(three)
p_max = (a1+b1+c1)/2
p_min = (a2+b2+c2)/2
s_max=sqrt(p_max*(p_max-a1)*(p_max-b1)*(p_max-c1))
s_min=sqrt(p_min*(p_min-a2)*(p_min-b2)*(p_min-c2))
print(f"Максимальная площадь треугольника: {s_max}")
print(f"Минимальная площадь треугольника: {s_min}")
```
