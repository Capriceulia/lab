```python
def numbers(digits):
    num_count = {}

    for i in digits:
        if i.isdigit():
            num_count[i] = num_count.get(i, 0) + 1

    sort = dict(sorted(num_count.items(), key=lambda x: int(x[0])))
    sort = dict(sorted(sort.items(), key=lambda x: x[1], reverse=True))
    top_three = dict(list(sort.items())[:3])

    return top_three

random_digits = "83978126542365123567867648936572984756"
result = numbers(random_digits)

print("Самые частые числа:")
for key, value in result.items():
    print(f"{key}: {value}")
```
