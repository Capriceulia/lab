```python
def fib():
    a, b = 1, 1
    count = 0
    while count < 10:
        if a >= 200:
            yield a
            count += 1
        a, b = b, a + b

fibonacci= fib()
for number in fibonacci:
    print(number)

    with open("file.txt", "w") as file:
        fibonacci = fib()
        for number in fibonacci:
            print(number)
            file.write(str(number) + "\n")
```
