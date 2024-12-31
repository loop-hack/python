import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

object = response.json()  #we are storing jason file in variable named object
for result in object["results"]:
    print(result["trackName"])
