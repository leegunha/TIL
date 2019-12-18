
dust = int(input("오늘의 미세먼지 농도를 입력하세요 : "))

if dust > 150:
    print("매우 나쁨")
elif(dust>100):
    print("나쁨")
else:
    print("좋음")

