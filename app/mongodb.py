#-*- coding:utf-8 -*-
import pymongo
from pymongo import MongoClient

### 连接MongoDB服务
### 从管理控制台获取host, port, db_name, api_key, secret_key
con = MongoClient("db server address", port)  
db_name = "your mongo database name" # 数据库名称
db = con[db_name]
########################################################
##############if you test it local######################
###############you may not be use this##################
########################################################
api_key = "auth username" # 用户AK
secret_key = "auth passwd " # 用户SK
db.authenticate(api_key, secret_key)