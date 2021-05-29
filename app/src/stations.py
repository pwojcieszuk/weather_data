import requests

def get():
    url = 'https://airquality.ie/assets/php/get-monitors.php'
    headers = {'Referer': 'https://airquality.ie/stations'}
    r = requests.get(url, headers=headers)
    return r.json()
