## STEP.1-匯入檔案
import requests
url="https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
respone=requests.get(url)

### STEP.2-讀取檔案
data=respone.json()

### STEP.3-使用迴圈依序將值存入串列中
eachdata=[]
#items為字典
for items in data["records"]:
    #取出所需的欄位值，並將這些值組成一個元組，再將該元組添加到串列中
    eachdata.append((items['sitename'],
                        items['county'],
                        items['aqi'],
                        items['status'],
                        items['pm2.5'],
                        items['datacreationdate'],
                        items['latitude'],
                        items['longitude']))
    
    # print(items)
print(eachdata)

### STEP.4-新增資料庫
#為date和sitename欄位設置UNIQUE約束，避免插入重複的記錄
sql = '''
CREATE TABLE IF NOT EXISTS records (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	sitename TEXT NOT NULL,
	county TEXT,
	aqi INTEGER,
	status TEXT,
	pm25 NUMERIC,
	date TEXT,
	lat NUMERIC,
	lon NUMERIC,
    UNIQUE (sitename,date)
);
'''

import sqlite3
conn = sqlite3.connect("AQI_issue.db")

cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()

### STEP.5-匯入資料
#####使用INSERT OR REPLACE，當發生重複時覆蓋原本的記錄
######也可以使用 INSERT OR IGNORE，忽略重複的值
insertSQL = '''
INSERT OR REPLACE INTO records(sitename,county,aqi,status,pm25,date,lat,lon)
VALUES (?,?,?,?,?,?,?,?)
'''
conn = sqlite3.connect("AQI_issue.db")

cursor = conn.cursor()
#使用executemany插入多筆資料
cursor.executemany(insertSQL,eachdata)
conn.commit()
cursor.close()
conn.close()