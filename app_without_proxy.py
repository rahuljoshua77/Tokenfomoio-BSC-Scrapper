import requests, config, json, time
from bs4 import BeautifulSoup
from datetime import datetime
target_telegram = config.username_target
token_telegram = config.token_bot
header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
     
    "cookie": "_ga=GA1.1.1107709396.1638452040; h=58288152257d54ff2b26078b1837aba262af37c7e293f71924fa5b797469aa3460ad64f541150e60964b28f11a5693c2fdc775e00562bd34eec8853281effd072623ba6119148b5abf639d562ef49487c5c79712cdb5803569448f5b5069a429a61ed628090d19c1a398329bf1199d5c6c992dbba286d8962d9045d0674ef1cb694c08a10ac874562ab21b02a7c08d999d65c542b83d6b8120454fab46645cc71ff82f3b69664824325bf70759bb459909e4a1d2488253859edb4659e1fd2ceee2abbf29a36386918a272272a160a702add1d17f2f4da39c877c5de81788f4f6d69f5d55c13aaecc7ae96f937d20ebe7ad915bfb2f74f30ff0c8439cde3b94ec083a3c32735ee514d71a141ae81cfd4e66f850de23ba5f844cd12fae22b63ec39359a487bc1dc31d6ea4bfed7954962c5ac1e8931ba4092c789afd364465e7a11bee2b04289fdace78f76206cef08ea93da6f4ea76827f47a4f6921e5ce1db0ed67f5399cc12c0b665503c7517ad390762f6a39b1d649555fdf5b8789f155c6fe101c0a6e7db334a68f92728afb5e675ee88a76377c6d1b69e6bd6ece92e83ce5d1aab7db2270f74a525622a2fe7dfce0f9deb759ea0b9f5180bda1b47ed37e3c881a50e8d7937378d033f31c22f416f965fed50917ec2af5dc72220599987a6b16ec16642c4ab74cc8fb4e4bfeb5921af8dd9c0409530f815421a9196b4e301; _ga_ZNZ9W5Y8HZ=GS1.1.1638452040.1.1.1638452062.0",

    "host": "tokenfomo.io",

    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
}

container = []

while True:
  try:
    res = requests.get("https://tokenfomo.io/",headers=header)
    print(f"[{time.strftime('%d-%m-%y %X')}] The status code is ", res.status_code)
    
    soup = BeautifulSoup(res.content, 'html.parser')
    
    get_data = soup.prettify()
    
    datas = get_data.split(':{"tokens":')
    
    new_data = datas[1].split(',"__N_SSP":true},')
    get_data = new_data[0]
    validation = get_data[2:5]
    if "BSC" == get_data[2:5]:
    
      final_data = new_data[0]
      final_data = final_data.split('{"BSC":[[')
      json_string = '{"BSC":[['+final_data[1]
      json_string = json_string.split(']]}}')
      json_string = json_string[0]+']]}'
      # print(json_string)
      stud_obj = json.loads(json_string)
      
      if any(f'{stud_obj["BSC"][0][1]}' in s for s in container): 
        pass
      else:
        dt_object = datetime.fromtimestamp(int(stud_obj["BSC"][0][4]))
        address = stud_obj["BSC"][0][1]
        name_token = stud_obj["BSC"][0][2]
        simbol = stud_obj["BSC"][0][3]
        date = dt_object
        telegram_grup = 't.me/'+name_token.replace(" ", "")
        print(f"[{time.strftime('%d-%m-%y %X')}] {address} | {name_token} | {simbol} | {date}")
        container.append(stud_obj["BSC"][0][1])
        requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token_telegram, "sendMessage"),
        data={
          'chat_id': target_telegram, 
          'text': f'New Token!\nAddress: {address}\nName Token: {name_token}\nSymbol: {simbol}\nTelegram Group: {telegram_grup}\nDate: {date}'}
        ).json()
    
    else:
      pass
  except Exception as e:
    print(e) 
