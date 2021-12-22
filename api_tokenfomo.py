import requests, config, json, time
from requests.api import get
from bs4 import BeautifulSoup
from datetime import datetime
target_telegram = config.username_target
token_telegram = config.token_bot
proxy = config.proxy_conf
from requests import Session

s = Session()

 
from requests.structures import CaseInsensitiveDict

url = "https://tokenfomo.io/api/tokens/bsc?limit=1"
token_api = "YOUR TOKEN HERE"
header = CaseInsensitiveDict()
header["Accept"] = "application/json"
header["Authorization"] = f"Bearer {token_api}"
s.headers.update(header) 

container = []
while True:
  
  try:
    res = s.get(url,headers=header)
    print(f"[{time.strftime('%d-%m-%y %X')}] The status code is ", res.status_code)

    soup = BeautifulSoup(res.content, 'html.parser')

    get_data = soup.prettify()
    get_data = json.loads(get_data)
    get_data = get_data[0]
 
    if any(f'{get_data["addr"]}' in s for s in container): 
        pass
    else:
        dt_object = datetime.fromtimestamp(int(get_data["timestamp"]))
        address = get_data["addr"]
        name_token = get_data["name"]
        simbol = get_data["symbol"]
        date = dt_object
        telegram_grup1 = 't.me/'+name_token.replace(" ", "")
        telegram_grup2 = 't.me/'+name_token.replace(" ", "")+"Bsc"
        telegram_grup3 = 't.me/'+name_token.replace(" ", "")+"Token"
        print(f"[{time.strftime('%d-%m-%y %X')}] {address} | {name_token} | {simbol} | {date}")
        container.append(address)
        requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token_telegram, "sendMessage"),
        data={
          'chat_id': target_telegram, 
          'text': f'New Token!\nAddress: {address}\nName Token: {name_token}\nSymbol: {simbol}\nTelegram Group:\n+ {telegram_grup1}\n+ {telegram_grup2}\n+ {telegram_grup3}\nDate: {date}'}
        ).json()
    
 
  except Exception as e:
    print(e) 
