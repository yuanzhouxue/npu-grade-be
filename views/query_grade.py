# -*- coding: utf8 -*-

from aiohttp import web
from common.get_grade import get_grade
from common.encrypt import rsa_decrypt
from common.commons import wrap_response

async def query_grade(request):
    data = await request.json()
    print(data)
    try:
        stu_id = data['id']
        password = data['passwd']
        password = rsa_decrypt(password)
        grade = await get_grade(stu_id, password)
        return web.json_response(wrap_response(grade))
    except:
        return web.json_response(wrap_response({'参数非法'}))