```python
from datetime import datetime #Импортируем класс datetime из модуля datetime
from math import sqrt #Импортируем класс sqrt из модуля math

#Опреатор ** упаковывает аргументы, переданные по имени, в словарь.
#Имена параметров служат ключами.
def main (**kwargs):
    """Функция принимает произвольное количество аргументов в виде словаря,
    цикл перебирает элементы словаря, а после выводится результат
    квадратного корня из суммы квадратов двух чисел взятых из словаря."""
    for key in kwargs.items():
        result = sqrt(key[1][0]**2+key[1][1]**2)
        print(result)

if __name__ == '__main__': #Точка входа, выполнение программы
    start_time = datetime.now() #Фиксация времени - начало
    main( #Вызов функции main с аргментами из словаря
        one=[10,3], # [0]=10, [1] = 3 и так со всеми аргументами
        two=[5,4],
        three=[15,13],
        four=[93,53],
        five=[133,15]
    )
    time_costs = datetime.now() - start_time #Разница между текущим временем и начальным
    print(f"Время выполнения программы - {time_costs}") #Вывод окончательного времени в консоль
```
