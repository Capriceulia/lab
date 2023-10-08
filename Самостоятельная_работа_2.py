```python
list = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9,
        21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8,
        24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
sort = sorted(list)
top = sort[:3]
worst = sort[-3:]
ten = []
for item in list:
        if str(item).startswith('10'):
                ten.append(item)
print(top)
print(worst)
print(ten)
```
