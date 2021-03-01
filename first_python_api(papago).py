import os
import sys
import urllib.request
import json

client_id = "Agf7Y7CO4SC8nlg90156" # 개발자센터에서 발급받은 Client ID 값
client_secret = "3ynmMKrIHf" # 개발자센터에서 발급받은 Client Secret 값

text = input("번역하고자 하는 문장을 입력하세요 : ")
encText = urllib.parse.quote(text)
src_lang = 'kr' # 번역할 언어
target_lang = 'en' # 번역 결과 언어
data = f"source={src_lang}&target={target_lang}&text=" + encText

url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))

rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    trans_data = response_body.decode('utf-8')
    trans_data = json.loads(trans_data)
    trans_text = trans_data['message']['result']
else:
    print("Error Code:" + rescode)

print("번역된 내용 : " , trans_text)