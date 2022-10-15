import eel
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from datetime import date

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('5e0d8e38a0c8e2491f54774b16f3db1c', config_dict)

@eel.expose
def get_place(place):
    return place.title()

@eel.expose
def get_day():
    current_date = date.today()
    if current_date.weekday() + 1 == 1:
        weekday = "ПОНЕДЕЛЬНИК"
    elif current_date.weekday() + 1 == 2:
        weekday = "ВТОРНИК"
    elif current_date.weekday() + 1 == 3:
        weekday = "СРЕДА"
    elif current_date.weekday() + 1 == 4:
        weekday = "ЧЕТВЕРГ"
    elif current_date.weekday() + 1 == 5:
        weekday = "ПЯТНИЦА"
    elif current_date.weekday() + 1 == 6:
        weekday = "СУББОТА"
    elif current_date.weekday() + 1 == 7:
        weekday = "ВОСКРЕСЕНЬЕ"
    return weekday

@eel.expose
def get_date():
    current_date = date.today()
    if current_date.month == 1:
        month = "ЯНВАРЯ"
    elif current_date.month == 2:
        month = "ФЕВРАЛЯ"
    elif current_date.month == 3:
        month = "МАРТА"
    elif current_date.month == 4:
        month = "АПРЕЛЯ"
    elif current_date.month == 5:
        month = "МАЯ"
    elif current_date.month == 6:
        month = "ИЮНЯ"
    elif current_date.month == 7:
        month = "ИЮЛЯ"
    elif current_date.month == 8:
        month = "АВГУСТА"
    elif current_date.month == 9:
        month = "СЕНТЯБРЯ"
    elif current_date.month == 10:
        month = "ОКТЯБРЯ"
    elif current_date.month == 11:
        month = "НОЯБРЯ"
    elif current_date.month == 12:
        month = "ДЕКАБРЯ"
    return str(current_date.day) + " " + month + " " + str(current_date.year) + "г."

@eel.expose
def get_temp(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp =round(w.temperature("celsius")["temp"])
    return str(temp)+chr(176)

@eel.expose
def get_status(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    status = w.detailed_status
    return status.capitalize()

@eel.expose
def get_clouds(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    clouds = w.clouds
    return "Количество облаков " + str(clouds) + " %"

@eel.expose
def get_wind(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    wind = w.wind()["speed"]
    return str(wind) + " м/с."

@eel.expose
def get_humidity(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    humidity = w.humidity
    return str(humidity) + " %"

@eel.expose
def get_barometric(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    barometric = round((w.barometric_pressure()['press']) * 100 / 133.32)
    return str(barometric) + " мм. рт. ст."

@eel.expose
def get_rain(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    rain = w.rain
    if rain == {}:
        return "0 мм."
    else:
        return str(rain['1h']) + " мм."

@eel.expose
def get_distance(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    distance = w.visibility_distance
    if distance <= 1000:
        return "Дальность видимости " + str(distance) + " м."
    else:
        distance = round(distance / 1000)
        return "Дальность видимости " + str(distance) + " км."


eel.init('web')
eel.start('main.html', size=(450, 640))


