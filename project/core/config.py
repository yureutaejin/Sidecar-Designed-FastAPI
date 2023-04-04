
# DB 연결 configuration

import os
import json
import urllib.parse

try:
    DB = (json.load(open("./core/DB_info.json", 'r')))['DB']
except:
    DB = (json.load(open("/app/project/core/DB_info.json", 'r')))['DB']

class Settings:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB['user']}:{urllib.parse.quote(DB['password'], safe='')}@{DB['host']}:{DB['port']}/{DB['database']}"

settings = Settings()    
