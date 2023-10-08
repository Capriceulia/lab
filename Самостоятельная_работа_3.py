```python
def addition():
    try:
        inp = input("Введите число: ")
        number = float(inp)
        result = 2 + number
        return result
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число")
        return None

result = addition()
if result is not None:
    print(f"Результат: {result}")
