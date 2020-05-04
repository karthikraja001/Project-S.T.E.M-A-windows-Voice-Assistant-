import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio 
import wikipedia
import webbrowser
import subprocess
import re
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import os
import psutil
import sys
import calendar
import weather
import applaunch
import searchengine
import mapengine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]  
    monthNum=now.month
    dayNum=now.day

    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December']
    ordinalNumbers=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                      '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1]

def getTime():
    now=datetime.datetime.now()
    meridiem = ''
    if now.hour>=12:
        meridiem = 'pm' 
        hour = now.hour - 12
        if hour==0:
            hour=12
    else:
        meridiem = 'am'
        hour = now.hour
    if now.minute < 10:
        minute = '0'+str(now.minute)
    else:
        minute = str(now.minute)
    return 'It is '+ str(hour)+ ':'+minute+' '+meridiem

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:
        speak("Good Early Morning")
    elif hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("good Afternoon")
    else:
        speak("Good Evening")
    speak("I Am STEM. Please tell me How can I Help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
     
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("i cant understand....please say that again....")
        print("Say that Again please....")
        return "None"
    return query

def wakeWord(text):
    WAKE_WORDS = ['stem', 'okay stem', 'hey stem','hey'] 
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False

if __name__ == "__main__":
    while True:
        text = takeCommand().lower()
        if wakeWord(text)==True:
            wishMe()
            while True:
                query = takeCommand().lower()
                if 'search for' in query:
                    if 'google' in query:
                        searchengine.google_search(query)
                        print(searchengine.google_search(query))
                        speak(searchengine.google_search(query))
                    elif 'wikipedia' in query:
                        searchengine.wiki_search(query)
                        print(searchengine.wiki_search(query))
                        speak(searchengine.wiki_search(query))
                    else:
                        searchengine.google_search(query)
                        print(searchengine.google_search(query))
                        speak(searchengine.google_search(query))
                elif 'open youtube' in query:
                    speak("opening youtube.com sir....")
                    webbrowser.Chrome('youtube.com')
                elif 'open google' in query:
                    speak("opening google.com sir.....")
                    webbrowser.Chrome('google.com')
                elif 'play'in query:
                    new_query = query.replace("play","")
                    song = urllib.parse.urlencode({"search_query" : new_query})
                    print(song)
                    result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
                    print(result)
                    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
                    print(search_results)
                    url = "http://www.youtube.com/watch?v="+search_results[0]
                    speak(f"playing the song sir.....")
                    webbrowser.open_new(url)
                elif 'the time' in query:
                    Time = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The Time is {Time}")
                elif 'news for today' in query:
                    try:
                        news_url="https://news.google.com/news/rss"
                        Client=urlopen(news_url)
                        xml_page=Client.read()
                        Client.close()
                        soup_page=soup(xml_page,"xml")
                        news_list=soup_page.findAll("item")
                        for news in news_list[:15]:
                            speak(news.title.text.encode('utf-8'))
                    except Exception as e:
                            print(e)
                elif 'battery status' in query:
                    battery = psutil.sensors_battery()
                    plug = battery.power_plugged
                    percent = (battery.percent)
                    if plug == False:
                        power = "Not Plugged In"
                    else:
                        power = "Plugged In"
                    speak(f"Your Battery Percent is {percent}% and the power is {power}")
                    if percent <= 25 :
                        speak("sir...I Suggest you to Plug in your Device in The Charger")
                elif 'the date' in query:
                    date=getDate()
                    speak(f"Sir, {date}")                   
                elif 'the time' in query:
                    time=getTime()
                    speak(f"Sir, {time}")
                elif 'launch' in query:
                    app = query.replace("launch","")
                    applaunch.launch(app)
                    speak("With Pleasure") 
                elif 'thank you' in query:
                    speak('Glad that I could help you. What would you like me to do next?')
                elif 'quit' in query or 'bye' in query or 'take rest' in query:
                    speak("Goodbye sir!")
                    sys.exit()      
                elif 'weather in' in query:
                    city = query.replace("weather in","")
                    x=weather.weather_status(city)
                    speak(f"The weather in{city}is{x['temp']} degree Fahrenheit")
                elif 'locate' in query or 'where am i' in query or 'nearby' in query or 'direction' in query or 'route' in query or 'way to' in query:
                    mapengine.mapfn(query)
                    print(mapengine.mapfn(query))
                    speak(mapengine.mapfn(query))
