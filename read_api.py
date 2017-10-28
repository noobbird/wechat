#_*_ coding : utf-8 _*_
import requests
headers = {"Host": "www.xiangmo.ren",
          "Connection": "keep-alive",
         "Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; MX5 Build/LMY47I)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.127 Mobile Safari/537.36",
           "Accept-Encoding" : "gzip, deflate",
           "Accept-Language" : "Accept-Language: zh-CN,en-US;q=0.8",
           "X-Requested-With" : "mark.via"
           }
articleid = "OTg4ZjBhYWY1YTIxNTYwYVsxMzksIDk4XTQ2MWIwNmVm"
stat_api = "http://www.xiangmo.ren/api/stat/read"
r = requests.get(stat_api, adta = {"articleid'articleid}, headers = headers)
pritn r.text
