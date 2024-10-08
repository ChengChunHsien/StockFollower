import datetime #about the date and the time.
import json
import typing

import pandas as pd
import requests


# URL = 'https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20241008&type=ALLBUT0999&response=json&_=1728395583705'
URL = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={}&type=ALLBUT0999&_={}"

HEADER = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.twse.com.tw",
    "Referer": "https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html",
    "sec-ch-ua": '"Not;A=Brand";v="24", "Google Chrome";v="128", "Chromium";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Linux",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

def crawler(parameters:typing.Dict[str, str]) -> pd.DataFrame:
    # for URL
    crawler_date = parameters.get("crawler_date", "") #獲取參數crawler_date
    crawler_date = crawler_date.replace("-", "") #移除-
    crawler_timestamp = int(datetime.datetime.now().timestamp())

    resp = requests.get(
        url=URL.format(crawler_date, crawler_timestamp), headers=HEADER
    )
    
    columns = [
        "stock_id",
        "stock_name",
        "open",
        "max",
        "min",
        "close",
    ]
    
    if resp.ok:
        resp_data = json.loads(resp.text)
        data = pd.DataFrame(resp_data["data9"])
        data = data[[0, 1, 5, 6, 7, 8]]
        data.columns = columns
        data["date"] = parameters.get("crawler_date", "")
    else:
        data = pd.DataFrame()
    return data

if __name__ == "__main__":   
    parameters = {
        "crawler_date": "2024-10-08",
    }
    data = crawler(parameters) 
    print(data)
    