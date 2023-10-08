```python
def main():
    text = input("Введите чисела, разделенные пробелами: ")

    number = [int(num) for num in text.split()]

    tupl = tuple(number)

    print("Список:", number)
    print("Кортеж:", tupl)

if __name__ == "__main__":
    main()
```
