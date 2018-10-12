# -*- coding: utf8 -*-

import aiohttp
import asyncio
import bs4
from bs4 import BeautifulSoup as bs
# import uvloop # 不支持windows平台

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(encoding='utf-8')

async def post_data(session, url, data):
    async with session.post(url, data=data) as response:
        return await response.text(encoding='utf-8')

async def login(session, stu_id, password):
    post_login = {
        "username": stu_id,
        "password": password,
        "encodedPassword": "",
        "session_locale": "zh_CN",
    }
    login_url = 'http://us.nwpu.edu.cn/eams/login.action'
    text = await post_data(session, login_url, post_login)
    return '密码错误' not in text

async def logout(session):
    logout_url = "http://us.nwpu.edu.cn/eams/logout.action"
    res = await fetch(session, logout_url)
    return '请输入用户名' in res
        

# 通过html代码获取成绩表
def get_grade_table(html: str) -> list:
    grade_content_soup = bs(html, "html.parser")
    grid = grade_content_soup.find_all('div', 'grid')

    if len(grid): grid = grid[0]
    else: return {}

    grade_table = {}
    semisters = []

    for tr in grid.table.tbody:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            semister = tds[0].string
            if semister not in grade_table:
                semisters.append(semister)
                grade_table[semister] = []
            grade_table[semister].append({'name': tds[3].a.string, 'grade': tds[-2].string.strip(), 'score': tds[5].string})
    grades = []
    for s in semisters:
        grades.append(grade_table[s])
    return {'semister': semisters, 'grades': grades}


async def get_grade(stu_id, password):
    # 将asyncio的事件循环替换为uvloop
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    async with aiohttp.ClientSession() as session:
        if not await login(session, stu_id, password):
            return {'密码错误'}
        course_grade_url = 'http://us.nwpu.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR'
        grade_content = await fetch(session, course_grade_url)
        await logout(session)
        return get_grade_table(grade_content)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(get_grade('2016301777', 'mypassword'), get_grade('2016301777', 'mypassword')))