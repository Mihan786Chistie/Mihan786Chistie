import requests
import re

# Fetch a random meme URL from an API
response = requests.get("https://meme-api.com/gimme/programmerhumour")
data = response.json()
meme_url = data['preview'][4]

# Read the README.md file
with open("README.md", "r") as file:
    readme_content = file.read()

# Update the meme URL in README.md
updated_content = re.sub(r'!\[]\(.*\)', f'![]({meme_url})', readme_content)

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.write(updated_content)
