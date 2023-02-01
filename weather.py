# для GET запросов к openweathermap.org
import requests

# для считывания api_key
import config

# для раоты с JSON файлами
import json

#-------------------------------------------------------------------------------------
# метод проверки наличия города в БД
def is_in_list(city):
    # переменная, которую возвращаем в конце
    flag = False
    # считывем БД в фрмате JSON
    with open("city_list.json", "r", encoding = "utf8") as file:
        data = json.load(file)
    # смотрим есть ли город в списке
    for item in data:
        if city == item["name"]:
            flag = True
    return flag
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# метод получения ID города из БД
def get_id(city):
    # считывем БД в фрмате JSON
    with open("city_list.json", "r", encoding = "utf8") as file:
        data = json.load(file)
    # ищем город
    for item in data:
        if city == item["name"]:
            # возвращаем id
            return item["id"]
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# метод проверки наличия города в БД
def get_list_by_country(country):
    # считывем БД в фрмате JSON
    with open("city_list.json", "r", encoding = "utf8") as file:
        data = json.load(file)
    # смотрим есть ли страна в списке
    for item in data:
        if country == item["country"]:
            print(item["name"])
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# метод получения данных по городу
#
# На данный момент метод возвращает целую кучу параметров в формате JSON.
# Надо обсудить, что нужно возвращать. Возможно добавить еще методов с конкретными параметрами.
#
def get_weather_by_city(city):
    # забираем api ключ сгенерированный на сайте api.openweathermap.org
    api_key = config.key
    # формируем GET запрос к api.openweathermap.org
    request_text = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # отпрвлем запрос и получаем ответ
    my_request = requests.get(request_text)
    # переводим данные в JSON
    data = my_request.json()
    return data
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# метод получения данных по городу
def get_weather_by_id(city_id):
    # забираем api ключ сгенерированный на сайте api.openweathermap.org
    api_key = config.key
    # формируем GET запрос к api.openweathermap.org
    request_text = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"
    # отпрвлем запрос и получаем ответ
    my_request = requests.get(request_text)
    # переводим данные в JSON
    data = my_request.json()
    return data
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Проверка работоспособности методов
#-------------------------------------------------------------------------------------
# print(is_in_list("Tomsk"))
# print(get_id("Tomsk"))
# print(get_weather_by_city("Tomsk"))
# print(get_weather_by_id("1489425"))
# print(is_in_list("Vladivostok"))
# print(get_id("Vladivostok"))
# print(get_weather_by_city("Vladivostok"))
# print(get_weather_by_id("2013348"))
# get_list_by_country("RU")