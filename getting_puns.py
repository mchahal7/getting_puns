# download and print puns from API

import requests
import json

# download a random pun from https://www.punapi.rest/
pun_request = requests.get("https://www.punapi.rest/api/pun")
pun_data = json.loads(pun_request)

print(pun_data)
