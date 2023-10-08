```python
list1 = [2,3,4,5,3,4,5,2,2,5,3,4,3,5,4]
list2 = [4,2,3,5,3,5,4,2,2,5,4,3,5,3,4]
list3 = [5,4,3,3,4,3,3,4,4,3,3,3,3,4,4]
while 2 in list1:
    list1.remove(2)
for i in range(len(list1)):
    if list1[i] == 3:
        list1[i] =4
print(list1)
while 2 in list2:
    list2.remove(2)
for i in range(len(list2)):
    if list2[i] == 3:
        list2[i] =4
print(list2)
while 2 in list3:
    list3.remove(2)
for i in range(len(list3)):
    if list3[i] == 3:
        list3[i] =4
print(list3)
```
