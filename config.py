#!/usr/bin/env python
# -*- coding: utf-8 -*-

CSRF_ENABLED = True
SECRET_KEY = 'secret_key'

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DBNAME = 'magus'
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'password'
MONGO_CONNECT = False
AUTH_MECHANISM = 'SCRAM-SHA-1'
MONGO_COLLECTION_STRUCTURE_VERSION = 20170503190855

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 1

LOG_FILE_NAME = '../var/log/magus/access.log'

LOCAL_ENCRYPT_KEY = 'encrypt_key'
RED_ENCRYPT_KEY = 'encrypt_key'

RED_UPLOAD_GROUP_QRCODE_PATH = '/var/log/magus/red/group-qrcode/'

PARAMETER_LOST = 10000

UPLOADED_IMAGE_DEST = '/data/file_upload/image/'
UPLOADED_MODULE_DEST = '/data/file_upload/module/'

OTHERS_NOVEL_PATH = '/home/magus-server/data/huanlesong.txt'
OTHERS_NOVEL_LINES = 53031

WECHAT_DATA_PATH = '/home/data/wechat-data/'
