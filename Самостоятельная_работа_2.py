```python
w=input("Введите данные:")
with open ("file.txt", "a") as file:
    file.write(w+"\n")
with open("file.txt", "r") as file:
    file_contents = file.read()
    print("Данные из файла:")
    print(file_contents)
```
