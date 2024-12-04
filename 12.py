import json
import requests
from pprint import pprint
username = "Automattic"
url = f"https://api.github.com/users/{username}"
user_data1 = requests.get(url).json()
pprint(user_data1)
c1 = json.dumps(user_data1)
pprint(c1)
user_data = json.loads(c1)
pprint(user_data)
info = {'company'   : (user_data["company"]),'created_at': (user_data["created_at"]),'email'     : (user_data["email"]), 'id'        : (user_data["id"]),'name'      : (user_data["name"]),'url'       : (user_data["url"])}
pprint(info)
