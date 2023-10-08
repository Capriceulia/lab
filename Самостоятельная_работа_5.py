```python
class CityNotFoundError(Exception):
    pass
city_locations = {
    "Moscow": "Moscow region",
    "Saint Petersburg": "Leningrad region",
    "Ekaterinburg": "Sverdlovsk region",
}

def locate_city(city_name):
    if city_name in city_locations:
        return city_locations[city_name]
    else:
        raise CityNotFoundError(f"Город {city_name} не найден в базе данных местоположений.")
try:
    city_name = "Saratov" 
    location = locate_city(city_name)
    print(f"{city_name} находится в {location}")
except CityNotFoundError as ex:
    print(ex) 
```
