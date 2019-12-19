import requests
from bs4 import BeautifulSoup as bs
import webbrowser

url = "https://www.naver.com"
response = requests.get(url).text
#html.parser  -> 받아올 형식
doc = bs(response, 'html.parser')

result = doc.select('.ah_k')
print(result)
search_url = "https://search.naver.com/search.naver?query="
for i in range(5):
    webbrowser.open(search_url+result[i].text)



