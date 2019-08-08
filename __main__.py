# -*- coding: utf8 -*-

import asyncio
import logging

from aiohttp import web

from views.issue import handle_issue
from views.query_grade import query_grade
from views.notice import handle_notice

if __name__ == '__main__':
    app = web.Application()

    app.router.add_post('/query_grade', query_grade)
    app.router.add_put('/issue', handle_issue)
    app.router.add_get('/notice', handle_notice)
    app.router.add_static('/', path='static/')
    web.run_app(app, host='127.0.0.1', port=7000)
