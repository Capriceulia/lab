```python
def extract_subtuple(input_t, id):
    start_index = -1
    end_index = -1

    for i, item in enumerate(input_t):
        if item == id:
            if start_index == -1:
                start_index = i
            else:
                end_index = i

    if start_index != -1 and end_index != -1:
        return input_t[start_index:end_index + 1]
    elif start_index != -1:
        return input_t[start_index:]
    else:
        return ()

input1 = (1, 2, 3)
id1 = 8
result1 = extract_subtuple(input1, id1)
print(result1)

input2 = (1, 8, 3, 4, 8, 8, 9, 2)
id2 = 8
result2 = extract_subtuple(input2, id2)
print(result2)

input3 = (1, 2, 8, 5, 1, 2, 9)
id3 = 8
result3 = extract_subtuple(input3, id3)
print(result3)
```
