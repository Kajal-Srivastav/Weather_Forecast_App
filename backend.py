import requests

Api_key = "6998889215b1bb924a88d4fe7e95b2c4"


def get_data(place, days):
    urls = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={Api_key}"
    response = requests.get(urls)
    data = response.json()
    list_data = data["list"]
    no_of_values = 8 * int(days)
    list_data = list_data[:no_of_values]
    return list_data

