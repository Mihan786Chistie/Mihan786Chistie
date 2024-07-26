import requests
import re

# Fetch a random meme URL from an API
response = requests.get("https://meme-api.com/gimme/programmerhumour")
data = response.json()
try:
    meme_url = data['preview'][3]
except:
    meme_url = data['preview'][2]
finally:
    meme_url = data['preview'][1]

print(meme_url)

f = open("README.md", "w")

f.write(f"![]({meme_url})\n\n Memes from [r/programmerhumour](https://www.reddit.com/r/programmerhumour/?onetap_auto=true&one_tap=true)\n")
