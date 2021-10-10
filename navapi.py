import requests
import pymongo

#----------------웹에서 입력을 받아야 하는 uri 파라미터정보--------------------
search_title = input('제목 : ')
search_yearfrom = input('몇년도부터? :')
search_yearto = input('몇년도까지? : ')
#--------------추후에 input 대신에 웹에서 불러온 정보를 대입하여 사용------------- 

#MongoDB 정보
conn = pymongo.MongoClient("localhost",27017)
db = conn.movie
col = db.foundmovie
#uri정보
headers = {'X-Naver-Client-Id' : '_emDW747XTNkGrS69ARU','X-Naver-Client-Secret':'a1hsFw_cOO'}
url = 'https://openapi.naver.com/v1/search/movie.json'
params = {'query' : search_title , 'yearfrom':search_yearfrom , 'yearto':search_yearto , 'display':'5'}

response = requests.get(url,headers=headers,params=params)
rescode = response.status_code
result = list(response.json().values())[4]



if(rescode == 200):
    print('Saved at DB!')
    col.insert_many(result)
    #print(result)                                       #원할 시, 영화 관련 정보만 출력
    #print(response.content.decode('utf-8'))           #원할 시, 정제하지 않은 전체 응답 내용을 출력
else:
    print("Error code:"+rescode)