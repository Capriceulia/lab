```python
from math import sqrt
def square (a, b, c):
    p = (a+b+c)/2
    result = sqrt(p*(p-a)*(p-b)*(p-c))
    return result
```
```python
from main import square
def main():
    a = float(input("Введить длинну a:"))
    b = float(input("Введить длинну b:"))
    c = float(input("Введить длинну c:"))
    
    if a+b>c and a+c>b and b+c>a:
        result = square(a,b,c)
        print(f"Площадь треугольника {result})")
    else:
        print(f"Такого треугольника не существует!)
if __name__ == '__main__':
    main()
```
