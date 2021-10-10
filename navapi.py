import urllib.request
import pymongo

conn = pymongo.MongoClient("localhost",27017)
db = conn.movie
col = db.foundmovie

client_id = '_emDW747XTNkGrS69ARU'
client_secret = 'a1hsFw_cOO'

url = 'https://openapi.naver.com/v1/search/movie.json'
query = "?query="+urllib.parse.quote(input("질의:"))
query1 = "&yearfrom="+urllib.parse.quote(input("몇년도부터?:"))
query2 = "&yearto="+urllib.parse.quote(input("몇년도까지?:"))
option = '&display=5'

url_query = url + query + query1 + query2 + option

request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error code:"+rescode)


result = response_body.decode('utf-8')

print('result : ',type(response))
