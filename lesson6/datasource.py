#建立module資料庫

import requests

#建立function
#定義函式get_sitename()，回傳值的類型標註為 list[str]，表示應回傳一個字串列表
def get_sitename()->list[str]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    #發送請求並處理例外：
    try:
        #發送GET請求
        response = requests.get(url)
        #.raise_for_status()用於檢查請求是否成功。如果發生 HTTP 錯誤（如 404 或 500），將會拋出例外(Exception)。
        response.raise_for_status()
        data = response.json()
    #請求失敗會執行例外(Exception)，e為內建功能錯誤訊息
    except Exception as e:
        print(e)
    #請求成功會執行else
    else:
        sitenames = set()
        for items in data['records']:
            sitenames.add(items['sitename'])

        sitenames = list(sitenames)
        return sitenames
    
#建立function
def get_selected_data(sitename:str)->list[list]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
    else:
        outerlist=[]
        for items in data['records']:
            #如果輸入的站名和資料裡的站名相同時
            if items['sitename']==sitename:
                innerlist=[items['datacreationdate'],items['county'],items['aqi'],items['pm2.5'],items['status'],items['latitude'],items['longitude']]
                outerlist.append(innerlist)
        return outerlist