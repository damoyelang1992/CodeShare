#-*- coding:utf-8 -*-
import pymongo
from pymongo import MongoClient

def test_mongo():
    ### 连接MongoDB服务
    ### 从管理控制台获取host, port, db_name, api_key, secret_key
    con = MongoClient("mongo.duapp.com", 8908)  
    db_name = "zUkozBEXjBFaBdIdyfQW" # 数据库名称
    db = con[db_name]
    api_key = "4aaf5ea18d7c476183d3e0936740d4a2" # 用户AK
    secret_key = "336148406f8f41dfbb0596fc7779d829" # 用户SK
    db.authenticate(api_key, secret_key)

    ### 插入数据到集合test
    collection_name = 'test'
    db[collection_name].insert({"id":10, 'value':"test test"})

    ### 查询集合test
    cursor = db[collection_name].find()
    con.close()
    return "select collection test %s"%str(cursor[0])

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    try:
        return test_mongo()
    except Exception as e:
        return "exception"

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)