```python
import random

def cube():
    x = random.randint(1, 6)
    print(f"Выпало:{x}")
    if x in (5, 6):
        print("Вы победиди!")
    if x in (3, 4):
        print("У вас есть еще попытка!")
        cube()
    if x in (1, 2):
        print("Вы проиграли!")
if __name__ == '__main__':
    cube()
```
