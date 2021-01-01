# This project give you 10 news of the Day
# It will also read the news for you

import pyttsx3                      # Use this module for reading
import requests                     # Use this module to request the url
import json                         # Use to convert the data

def speck(s):
    """ This Function read the string  """
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')                   # Getting details of current voice
    # engine.setProperty('voice', voices[0].id)             # Changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)               # Changing index, changes voices. 1 for female

    rate = engine.getProperty('rate')                       # Getting details of current speaking rate
    # print(rate)                                           # Printing current voice rate
    engine.setProperty('rate', 125)                         # Setting up new voice rate

    engine.say(s)
    engine.runAndWait()


if __name__ == '__main__':
    speck("Today's News")

    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=f32598e99963461595f10bdf65111c39"

    # Getting the data from the URL in string form
    news = requests.get(url).text

    # converting the string data to python object
    news_json = json.loads(news)
    art = news_json["articles"]
    no_news = news_json["totalResults"]
    print(no_news)
    for item in art:
        if no_news > 0:
            speck(item["title"])
            no_news = no_news - 1
            speck("Next News is")