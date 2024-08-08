import requests
import re

def request_meme():
    while True:
        try:
            response = requests.get("https://meme-api.com/gimme/ProgrammerHumor")
            data = response.json()
            meme_url = data['preview'][3] if len(data['preview']) > 3 else data['preview'][2]
            return meme_url
        except:
            pass
    
meme_url = request_meme()

f = open("README.md", "w")

f.write(f"![]({meme_url})\n\n Random memes from [r/ProgrammerHumor](https://www.reddit.com/r/ProgrammerHumor/)\n")
