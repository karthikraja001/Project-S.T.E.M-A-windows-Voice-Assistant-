import webbrowser
import urllib
from urllib.request import urlopen

def mapfn(query):
    if 'locate me' in query or 'where am i' in query:
        url = 'www.google.com/maps/search/my location/'
        webbrowser.open_new_tab(url)
        return("You're here sir")
    elif 'nearby' in query:
        hotword = 'nearby'
        q = query[query.find(hotword)+len(hotword): ]
        url = "www.google.com/maps/search/"+q+"/"
        webbrowser.open_new_tab(url)
        return('Here is your search result')
    elif 'direction' in query or 'route' in query or 'way to' in query:
        source = query[query.find('from')+len('from'):query.rfind('to')]
        destination = query[query.rfind('to')+len('to'): ]
        url = "www.google.com/maps/dir/"+source+"/"+destination+"/"
        webbrowser.open_new_tab(url)
        return('I found the route for you sir')