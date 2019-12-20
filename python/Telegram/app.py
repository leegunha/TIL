from flask import Flask , render_template, request
from decouple import config
import requests
import random

app = Flask(__name__)
token = config('TOKEN')
chat_id = config('chat_id')
app_url = f"https://api.telegram.org/bot{token}"



@app.route('/')
def hello():
    return "안녕하세요!"


@app.route('/write')
def write():
    #HTML
    return render_template("write.html")

@app.route('/send')
def send():
    message = request.args.get("message")
    message_url = app_url + f"/sendmessage?chat_id={chat_id}&text={message}"
    
    requests.get(message_url)
    return "메시지 전송 완료 했어요"

#Webhook 텔레그램에서 전송받은 내용을 플라스크로 옮겨주기 위한 기능 200도 꼭 유의미한 기능입니다
#잘 전송됐는지 확인하는게 200이라서 200을 꼭 해줘야함 status_code
@app.route(f"/{token}", methods = ['POST'])
def telegram():
    response = request.get_json()
    
    chat_id =response["message"]["chat"]["id"]
    text = response["message"]["text"]

    message_url = app_url + f"/sendmessage?chat_id={chat_id}&text={text}"
    
    
    l_list = random.sample(range(1,46),6)
    if(text == "lotto"):
        message_url = app_url + f"/sendmessage?chat_id={chat_id}&text={str(l_list)}"
        requests.get(message_url)

    return '',200




#debug 
if(__name__ == "__main__"):
    app.run(debug = True)

