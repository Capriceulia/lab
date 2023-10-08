```python
def geographic_info(func):
    def wrapper(*args, **kwargs):
        if args:
            geographic_object = args[0]
            print(f"Анализируем географический объект: {geographic_object}")
        result = func(*args, **kwargs)
        if result:
            print(f"Географический объект {geographic_object} находится в {result}")
        return result
    return wrapper

@geographic_info
def locate_city(city_name): 
    city_locations = {  
        "Moscow": "Moscow region",
        "Saint Petersburg": "Leningrad region",
        "Ekaterinburg": "Sverdlovsk region",
    }
    return city_locations.get(city_name, "неизвестно")

locate_city("Ekaterinburg")
```
