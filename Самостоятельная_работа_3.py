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

class House(Pet):
    def __init__(self, type, breed, name, house_num):
        super().__init__( type, breed, name)
        self.house_num = house_num
    def home(self):
        print(f"Pets {self.type} {self.breed} {self.name} live at {self.house_num}")
my_pet_home = House("Dog","Husky","Zefir", 86)
my_pet_home.walk()
my_pet_home.home()
```
