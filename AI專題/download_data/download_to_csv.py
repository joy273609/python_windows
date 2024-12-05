from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# 初始化 Selenium 驅動
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 打開目標網站
    driver.get("https://www.pet.gov.tw/Web/O302.aspx")
    driver.maximize_window()

    # 定義目標縣市和時間範圍
    counties = ["台北市", "新北市"]  # 目標縣市
    years = range(2015, 2025)  # 目標年份
    months = [str(i).zfill(2) for i in range(1, 13)]  # 01 到 12 月

    all_data = []

    for county in counties:
        for year in years:
            for month in months:
                try:
                    # 設定日期和縣市
                    start_date = f"{year}/{month}/01"
                    end_date = f"{year}/{month}/31"

                    # 使用 JavaScript 設定開始日期和結束日期
                    driver.execute_script(f"document.getElementById('txtSDATE').value = '{start_date}';")
                    driver.execute_script(f"document.getElementById('txtEDATE').value = '{end_date}';")

                    # 使用 JavaScript 設定縣市
                    county_js = f"""
                    let select = document.getElementById('CountyID');
                    for (let i = 0; i < select.options.length; i++) {{
                        if (select.options[i].text === '{county}') {{
                            select.selectedIndex = i;
                            break;
                        }}
                    }}
                    """
                    driver.execute_script(county_js)

                    # 點擊查詢按鈕
                    search_button = driver.find_element(By.CLASS_NAME, "btn-main")
                    search_button.click()

                    # 等待表格加載完成
                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "table"))
                    )

                    # 解析表格數據
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    table = soup.find('table', {'class': 'table'})

                    headers = [th.text.strip() for th in table.find('thead').find_all('th')]
                    rows = table.find('tbody').find_all('tr')

                    for row in rows:
                        cols = [td.text.strip() for td in row.find_all('td')]
                        record = dict(zip(headers, cols))
                        record["County"] = county
                        record["Year-Month"] = f"{year}-{month}"
                        all_data.append(record)

                    print(f"抓取完成: {county}, {year}-{month}")

                except Exception as e:
                    print(f"錯誤: {county}, {year}-{month}, {e}")

    # 將所有數據轉換為 DataFrame
    df = pd.DataFrame(all_data)

    # 儲存為 CSV 文件
    df.to_csv('taipei_newtaipei_data_2015_2024.csv', index=False, encoding='utf-8-sig')
    print("資料已儲存為 taipei_newtaipei_data_2015_2024.csv")

finally:
    # 關閉瀏覽器
    driver.quit()
