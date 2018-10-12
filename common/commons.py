# =*- coding: utf-8 -*-

import json
import random
import time
from datetime import datetime, timedelta

import requests

access_token = None
expire_time = None

def wrap_response(msg):
    if not msg:
        return {'msg': '查询失败', 'code': '1004'}
    elif '密码错误' in msg:
        return {'msg': '密码错误', 'code': '1003'}
    elif '参数非法' in msg:
        return {'msg': '参数非法', 'code': '1001'}
    else:
        return {"msg": msg, "code": '0'}

def get_openid(jscode):
    url_begin = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx7f3f1e1fccc809c5&secret=b809e27794fdc2be3715a86b3680fbc0&js_code='
    url_end = '&grant_type=authorization_code'
    res = requests.get(url_begin + str(jscode) + url_end)
    return json.loads(res.text)['openid']


def get_token():
    global access_token
    global expire_time
    if (access_token == None) or (datetime.now() + timedelta(seconds=5) > expire_time) or (expire_time == None):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx7f3f1e1fccc809c5&secret=b809e27794fdc2be3715a86b3680fbc0'
        res = requests.get(url)
        res_data = json.loads(res.text)
        access_token = res_data['access_token']
        expire_time = datetime.now() + timedelta(seconds=res_data['expires_in'])
    # print(access_token)
    # print(expire_time)

def send_message(jscode, text, formid):
    toid = get_openid(jscode)
    post_data = {
        'touser': 'oZJzy0I0eMItOvvaySdLYovVs7ug', # 管理员openid
        'template_id': 'AgwnA5WJHRwZOnHnxKtK9tYNgFKbFPr8KiAOZXvBe10',
        'form_id': formid,
        'page': '',
        'data':{
            'keyword1': {
                'value': text
            },
            'keyword2': {
                'value': str(datetime.now())
            },
            'keyword3': {
                'value': toid
            }
        }
    }
    get_token()
    # 注意，这个请求必须用json
    res = requests.post('https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=' + access_token, json=post_data)
    return json.loads(res.text)#['errcode'] == 0

def save_issue(jscode, issue_text):
    openid = get_openid(jscode)
    if ',' in openid:
        openid = '"' + openid + '"'
    if ',' in issue_text:
        issue_text = '"' + issue_text + '"'
    text_to_write = [openid, issue_text.replace('\n', ' '), '"' + str(datetime.now()) + '"\n']
    with open('issue.csv', 'a+', encoding='utf8') as f:
        f.write(','.join(text_to_write))

if __name__ == '__main__':
    salt = 'Y8LUwrOx6G/cHnH6/8qlJ2XzTFIkmzmow4PU7zZEDy'
    # print(get_md5('2016301777Hkljdslkafj' + salt))
    # for i in range(10):
    #     time.sleep(3)
    #     get_token()
    # print(get_openid('023Aoa0r1W2lMo0p3OZq1cee0r1Aoa0R'))
    # print(send_message('001mkUAg1yoxFy0mNoAg1XcRAg1mkUAB', 'Hello', '1538379098365'))
    print(save_issue('021mkqYe1pveNr00maXe17T8Ye1mkqYA', 'hwllo,world'))
