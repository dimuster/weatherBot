import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")

place = input("В каком городе/стране?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print( "Вас обслуживает deathbell, и его приложение на Python")
print( "В городе " + place + " сейчас " + w.get_detailed_status())
print( "Температура сейчас в районе " + str(temp))

if temp < 10:
	print("Сейчас ппц как холодно, одевай куртку")
elif temp < 20:
	print("Сейчас прохладно, одень кофту")
else:
	print("Сейчас тепло, одевайся как хочешь")

input()