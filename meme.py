import requests
import re

def request_meme():
    while True:
        try:
            response = requests.get("https://meme-api.com/gimme/programmerhumour")
            data = response.json()
            meme_url = data['preview'][3]
            return meme_url
        except:
            pass
    
meme_url = request_meme()

f = open("README.md", "w")

f.write(f"![]({meme_url})\n\n Memes from [r/programmerhumour](https://www.reddit.com/r/programmerhumour/?onetap_auto=true&one_tap=true)\n")
