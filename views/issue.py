# -*- coding: utf8 -*-

from aiohttp import web
from common.commons import save_issue

async def handle_issue(request):
    data = await request.json()
    try:
        jscode = data['code']
        text = data['text']
        save_issue(jscode, text)
        return web.json_response({'msg': '反馈成功', 'code': '0'})
    except:
        return web.json_response({'msg': '参数非法', 'code': '1001'})