```python
def main (*args):
    if len(args) == 0:
        return 0
    return sum(args)/len(args)
if __name__ == '__main__':
    result = main(5, 15, 22, 13)
    print(result)
```
