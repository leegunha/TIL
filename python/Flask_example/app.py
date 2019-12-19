from flask import Flask, render_template, request
import datetime
import random
# 지금부터 flask 서버의 이름이 app

app = Flask(__name__)
#url을 관리해주는 친구 > app.route()
@app.route('/')
def hello():
    return "#안녕"
def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day
    
@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    fanal = datetime.datetime(2020,6,9)
    result = fanal - today
    print(result)
    return f"{result}남았습니다."



@app.route('/christmas')
def christmas():
    today = datetime.datetime.now()
    christmas = datetime.datetime(today.year,12,25)
    
  
    if(today.day - christmas.day == 0):
        return "<h1> 네</h1>"
    else:
        return f" <h1>아니요 {christmas.day-today.day}.남음</h1> "
    
    
    #"/christmas"

@app.route("/movies")
def movies():
    movies= ["겨울왕국2", "클라우스", "어바웃타임","나홀로집에"]
    
    return render_template("movies.html",movies=movies, text = "영화목록")
@app.route("/greeting/<name>")
def greeting(name):
    return f"안녕하세요! {name}님! "
@app.route("/cube/<int:num>")
def cube(num):
    result = num**3
    return str(result)
#식사 메뉴 추천
#1. random
#2. DR_url : @app.route(/lunch/1 2 3 4)//
#   - List : ["자장면", "짬뽕", "오므라이스", "볶음밥"]
#   - <int:num> 숫자 만큼 뽑기


 




@app.route("/launch/<int:numb>")
def launch(numb):
    launch_list = ["자장면", "짬뽕", "오므라이스", "볶음밥", "고르곤졸라 피자","파스타"]
    food_list = []
    food_num = random.sample(range(0,5),numb)
    for food in food_num:

        food_list.append(launch_list[food])
    
    return render_template("movies.html",movies=food_list, text = "음식목록")


@app.route("/vonvon")
def vonvon():
    return render_template("vonvon.html")

@app.route("/godmademe")
def godmademe():
    name = request.args.get("name")
    f_list = ["매력", "못생김", "이쁨" ]
    s_list = ["애교","잘난척", "쑥스러움", "허세"]
    l_list = ["허세","성욕","잠욕","식욕"]
    
    return render_template("godmademe.html", name = name, m1="매력", m2 = "매력", m3 = "매력")


if __name__== "__main__":
    app.run(debug=True)

    #is it christmas 실습