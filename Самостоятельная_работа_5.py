```python
def main (lst):
    result = set()
    for x in lst:
        count = lst.count(x)
        if count>1:
            izm= str(x)*count
            result.add(izm)
        result.add(x)
    return list(result)
if __name__ == '__main__':
    list1 = [1, 1, 3, 3, 1]
    list2 = [5, 5, 5, 5, 5, 5, 5]
    list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

    tl1 =main(list1)
    tl2 =main(list2)
    tl3 =main(list3)

    print(tl1)
    print(tl2)
    print(tl3)
```
