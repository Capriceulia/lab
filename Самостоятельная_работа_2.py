```python
class Pet:
    def __init__(self, type, breed, name):
        self.type = type
        self.breed = breed
        self.name = name

    def walk(self):
         print(f"Walks {self.type} {self.breed} {self.name}")

my_pet = Pet("Cat","Sphinx","Glasha")
my_pet.walk()
```
