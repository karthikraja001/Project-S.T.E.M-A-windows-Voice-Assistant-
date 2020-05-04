import pyowm

api_key = "eea55d1ca9004b900a096814f86fe0a3"

owm = pyowm.OWM(api_key)  

def weather_status(city): 
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    return(w.get_temperature('fahrenheit'))