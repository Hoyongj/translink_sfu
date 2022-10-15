import requests
from bs4 import BeautifulSoup
import bs4
import json


with open("translink_apikey.txt", 'r') as f:
    api_key = f.read()

def get_data(stop_id) -> bs4.BeautifulSoup:
    '''
    parameter: int `stop_id`\n
    return: soup `Response`
    '''
    url = f"https://api.translink.ca/rttiapi/v1/stops/{stop_id}/estimates?apikey={api_key}"
    r = requests.get(url)
    res = BeautifulSoup(r.content,'xml')
    return res

if __name__ == "__main__":
    stop_bay2 = 52806 # SFU Transportation Centre @ Bay 2-1
    stop_bay2 = 53096 # SFU Transportation Centre @ Bay 2-2
    stop_bay1 = 51861 # SFU Transit Exchange @ Bay 1
    with open('Work Space.xml', 'w+', encoding='utf-8') as f:
        f.write(str(get_data(stop_bay1)))