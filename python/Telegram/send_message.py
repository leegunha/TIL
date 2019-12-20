import requests
from decouple import config

token = config('TOKEN')
app_url = f"https://api.telegram.org/bot{token}"


update_url = app_url + "/getUpdates"

response = requests.get(update_url).json()
# print(response)
chat_id =config("chat-id")
#chat_id = reqsponse["result"][0]["message"]["id"]
text = f"하위"
message_url = app.url +f"sendMassage?chat_id={chat_id}&text={text}"
requests.get(message_url)

