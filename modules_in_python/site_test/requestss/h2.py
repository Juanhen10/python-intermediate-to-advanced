#  requests parar requisições HTTP
from os import system

import requests
from requests.exceptions import ConnectionError

system('cls')

# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/'
try:
    response = requests.get(url)
    print(response)
    print(response.status_code)
    # print(response.headers)
    # print(response.json)
    # print(response.content)
    print(response.text)
except ConnectionError as e:
    print(e)
    r = 'No response'
