# -*- coding: utf-8 -*-
# filename: basic.py
import requests
import json
from basic import Basic



 
# json数据格式请求参数
data = {
  "touser": "oz1Xn4opoA19fTqSCPciZXcLwWmc", # 接收用户的openid
  "template_id": "ZQ8OKHUs78ga24tSsNJUv0AWxiBmrHKJMAMzbLT41Pk", # 模板id
  "page": "pages/index/index",
  "miniprogram_state":"formal",
  "lang":"zh_CN",
  "data": {
      "thing1": {
          "value": "name"
      },
      "time2": {
          "value": "2021-08-01"
      },
      "thing3": {
          "value": "Python推送小程序订阅消息"
      }
  }
}
 
# 设置请求头
header = {'Content-Type': 'application/json'}

#获取access_token
access_token = Basic().get_access_token()

# 请求地址
url = "https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=" + access_token

# 请求体
response = requests.post(url, headers=header, data = json.dumps(data))

# 打印请求结果
print(response.text)
