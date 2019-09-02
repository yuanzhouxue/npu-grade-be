# -*- coding: utf8 -*-

from aiohttp import web
from common.get_grade import get_grade
from common.encrypt import rsa_decrypt
from common.commons import wrap_response


async def query_grade(request):
    data = await request.json()
    print(data)
    try:
        stu_id = data["id"]
        password = data["passwd"]
        password = rsa_decrypt(password)
        # 测试账号
        if stu_id == "2016001234" and password == "password":
            return web.json_response(
                wrap_response(
                    {
                        "semister": ["2016-2017 秋", "2016-2017 春"],
                        "grades": [
                            [
                                {"name": "C程序设计II实验", "grade": "95", "score": "1.5"},
                                {"name": "体育1（羽毛球）", "grade": "92", "score": "1"},
                                {"name": "高等数学（上）", "grade": "97", "score": "5.5"},
                            ],
                            [
                                {"name": "体育1（武术）", "grade": "85", "score": "1"},
                                {"name": "思想道德修养与法律基础", "grade": "82", "score": "3"},
                                {"name": "形势与政策", "grade": "90", "score": "2"},
                                {"name": "大学英语（Ⅱ）", "grade": "85", "score": "2"},
                            ],
                        ],
                    }
                )
            )
        grade = await get_grade(stu_id, password)
        return web.json_response(wrap_response(grade))
    except:
        return web.json_response(wrap_response({"参数非法"}))