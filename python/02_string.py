'''String 조작하기

1. 글자합체
#글자 삽입'''

name = "토니토니"
age = 20

text = "안녕하세요 제 이름은 {}입니다.".format(name)
print(text)

f_text = f"안녕하세요 제 이름은 {name}입니다. 나이는 {age}살 입니다"
#fstring
print(f_text)

#3. 글자 자르기


text_name = text[:10]
print(text_name)
text_split = text.split(" ")
for i in range(0, len(text_split)):
    print(text_split[i])

for i in text_split:
    print(i)