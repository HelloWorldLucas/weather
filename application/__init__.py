#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_pymongo import PyMongo
from flask_redis import Redis
from flask_uploads import UploadSet, configure_uploads, patch_request_class, ALL, IMAGES

import datetime
import logging
from logging.handlers import RotatingFileHandler

from application.studio import studio_blueprint
from application.dashboard import dashboard_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    register_log(app)
    init_mongo(app)
    init_redis(app)
    init_upload(app)

    app.register_blueprint(studio_blueprint)
    app.register_blueprint(dashboard_blueprint)

    return app

def register_log(app):
    #为app绑定logger。
    # backupCount=100 文件数量到达100个之后会覆盖最旧的一个，及时备份
    handler = RotatingFileHandler(app.config['LOG_FILE_NAME'], maxBytes = 1024 * 1024 * 512, backupCount = 30)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

def init_mongo(app):
    #连接mongo数据库
    app.mongo = PyMongo(app)

def init_redis(app):
    #redis所谓内存中存储键值对数据库?
    #redis是一个缓存服务器。
    app.redis = Redis(app)

def init_upload(app):
    # 文件上传集合名字为image
    app.image = UploadSet('image', IMAGES)
    configure_uploads(app, app.image)
    patch_request_class(app, 1 * 1024 * 1024)

    app.module = UploadSet('module', ALL)
    configure_uploads(app, app.module)
    patch_request_class(app, 16 * 1024 * 1024)
