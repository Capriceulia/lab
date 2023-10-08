```python
def tuple_sort(tupl):
    for element in tupl:
        if not isinstance(element,int):
            return tupl
    return tuple(sorted(tupl))

if __name__ == '__main__':
    print(tuple_sort((76, 98, 54, 2, 47, 9, 21)))
    print(tuple_sort((35, 62.32, 7.0, 9, 33)))
    print(tuple_sort((56, 71, 6, 24, '27', 8)))
```
