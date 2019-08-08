# -*- coding: utf8 -*-

from aiohttp import web
from common.commons import save_issue

async def handle_notice(request):
    try:
        content = ''
        with open('notice.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        return web.json_response({'content': content, 'code': '0'})
    except:
        return web.json_response({'content': '', 'code': '1001'})