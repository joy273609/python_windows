import requests
from requests import Response 

#建立main(function)
#方法一 利用if判斷是否請求成功
# def main():
#     url_csv = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=5481753E-52AF-40DA-9A8A-9E192B245E13'
#     res:Response = requests.request("GET",url_csv)

#     if res.status_code == 200:
#         print("下載成功")
#         res.encoding = 'utf-8'
#         content:str = res.text
#         with open('ai_ans.csv',newline='',encoding='utf-8',mode='w') as file:
#             print(type(file))
#             file.write(content)
#     else:
#             print("下載失敗")
    

# if __name__ == '__main__':
#     main()

#方法二 利用try判斷是否有異常並回傳異常訊息
def main():
    url_csv = 'https://data.moi.gov.tw/MoiOD/System/DoVwnloadFile.aspx?DATA=5481753E-52AF-40DA-9A8A-9E192B245E13'    

    try:
        res:Response = requests.request("GET",url_csv)
        res.raise_for_status()        
        res.encoding = 'utf-8'
        content:str = res.text
        with open('a1.csv',newline='',encoding='utf-8',mode='w') as file:
            print(type(file))
            file.write(content)
    except Exception as e:
            print(e)
    else:
         print("下載,儲存檔成功")
    

if __name__ == '__main__':
    main()