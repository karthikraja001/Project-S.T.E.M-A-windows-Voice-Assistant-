import wikipedia
import webbrowser

def wiki_search(obj):
    query = obj.replace("search for","")
    query = query.replace("in wikipedia","")
    results = wikipedia.summary( query, sentences = 3)
    return results

def google_search(obj):
    query = obj.replace("search for","")
    query = query.replace("in google","")
    url = "www.google.com/search?q="+query+"/"
    webbrowser.open_new_tab(url)
    return('Your search result is ready....have a look at it sir')
