# Fomotoken-BSC-Scrapper
A tool can scrape Fomotoken BSC New Token then send to telegram

![image](https://user-images.githubusercontent.com/73378179/145968464-1edc545a-e963-476a-8197-89c0e18d45db.png)

# Usage:

    1. Install Python 3.9
    
    2. Open CMD on Bot Folder: pip install -r requirements.txt
    
    3. Fill the config.py
    
    4. Run the script
    
    
# Config.py

token_bot: read the docs https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot

username_target: use username channel/grup for public, for private you can use chat id like below:

      1. Open Telegram K version WEB with PC (chrome): https://web.telegram.org/k/

      2. Open inspect element, click arrow icon like in the screenshot 

![image](https://user-images.githubusercontent.com/73378179/145967159-a5f7f6eb-1457-40aa-ab09-7169ec22571a.png)

      3. Pointing to group/Channel private that you want to send the notification
![image](https://user-images.githubusercontent.com/73378179/145967273-d1b228b3-618c-4446-bc16-e551f5748aed.png)

      4. Check element in inpect element, find the peer, excample peer="-123456790", like screenshot below:

![image](https://user-images.githubusercontent.com/73378179/145967456-55dcf4f1-4092-47f2-a623-96089ffb6638.png)         

      5. Find the peer, and then add 100 in the first after -, example the peer="-123456790", add 100 after -, then become: -100123456790

      6. Then Paste it in the config file

      7. Run the script
      
proxy_conf = "YOUR PROXY API HERE"

# Note:

If you use app_without_proxy.py you will detect as spam by Tokenfomo.io after -+ 15 minutes. Use the proxy instead,
