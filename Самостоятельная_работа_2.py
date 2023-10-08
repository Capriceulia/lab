```python
def remove_element_from_tuple(input):
    if isinstance(input, tuple) and len(input) >= 2:
        input_tuple = input[0]
        remove = input[1]

        if remove in input_tuple:
            updated_tuple = tuple(item for item in input_tuple if item != remove)
            return updated_tuple
        else:
            return input_tuple

    return input

input1 = (1, 2, 3), 1
result1 = remove_element_from_tuple(input1)
print(result1) 

input2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3
result2 = remove_element_from_tuple(input2)
print(result2)  

input3 = (2, 4, 6, 6, 4, 2), 9
result3 = remove_element_from_tuple(input3)
print(result3) 
```
