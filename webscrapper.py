import requests
from mlc4 import momlovecafe


url = "https://momlovecafe.com"


response = requests.get(url)


cafe = momlovecafe(response.text, "html.parser")


for p in cafe.find_all("p"):
    print(p.text.strip())
