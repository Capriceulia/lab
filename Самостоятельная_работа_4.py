```python
class Pet:
    def __init__(self, type, breed, name):
        self._type = type
        self._breed = breed
        self.__name = name

    def walk(self):
         print(f"Walks {self._type} {self._breed} {self.__name}")

my_pet = Pet("Cat","Sphinx","Glasha")
print(my_pet._type)
print(my_pet._breed)
my_pet.walk()
```
