```python
class Tomato:

    def __init__(self, _index):
        self._index = _index #Динамическое свойство, защищенный атрибут - номер томата
        self._state = 0 #Динамическое свойство, защищенный атрибут - стадии созревания
    def grow(self):
        states = ['отсутствует', 'цветение', 'зеленый', 'красный']
        for i in range(len(states)):
            if self._state < len(states) - 1:
                self._state +=1
    def is_ripe(self):
        return self._state ==3

class TomatoBush(Tomato):
    def __init__(self, n_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1,n_tomatoes+1)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    def give_away_all(self):
        self.tomatoes.clear()

class Gardener(TomatoBush):
    def __init__(self, name,_plan):
        self.name = name #Динамическое свойство, публичный атрибут - имя садовника
        self._plan = _plan #Динамическое свойство, защищенный атрибут - хранит объект класса TomatoBush
    def work(self):
        self._plan.grow_all()
    def harvest(self):
        if self._plan.all_are_ripe():
            print(f"{self.name} собирает урожай.")
        else:
            print(f"{self.name} продолжает ухаживать, томаты еще не дозрели.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Поливайте растение регулярно.")
        print("2. Удобряйте по необходимости.")
        print("3. Следите за стадией созревания плодов.")
        print("4. Собирайте урожай, когда все плоды созрели.")
#Вызываем справку по садовотству
Gardener.knowledge_base()
#Создаем объекты классов TomatoBush и Gardener
tomato_bush = TomatoBush(7)
gardener = Gardener("Lui", tomato_bush)
#Пробуем собрать урожай
gardener.harvest()
#Садовник работает
gardener.work()
#Собираем урожай
gardener.harvest()
```
