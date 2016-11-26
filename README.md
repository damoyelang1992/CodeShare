# CodeShare
一个完整的代码编写、分享模块  

代码的验证只支持Arduino IDE语法没有库支持  
CodeShare文件夹内除了app之外的所有文件适用于百度云bae基础版  
app内的代码可以本地运行，要在__init__里面添加Flask的本地启动文件  

It is built on the [Flask](http://flask.pocoo.org/) framework, using [MongoDB](https://www.mongodb.org/) for the database.

## Features
* Unique URL generation for sharing
* Workspace for editing sketches

## Run Locally

Currently configured to run on a local machine.

Set up MongoDB
```
  sudo mkdir -p /data/db
  sudo chown -R `id -u` /data/db
  mongod --dbpath /data/db
```
Install requirements
```
  pip install -r requirements.txt
```
Running MongoDB and the server
```
  mongod
  python /app/main.py
```
Open a browser and navigate to
```
  localhost:8080
```

