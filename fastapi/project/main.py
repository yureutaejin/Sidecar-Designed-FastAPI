from typing import Optional
from routers import master_access, dataset_api_query
import uvicorn
from fastapi import FastAPI, HTTPException
import subprocess
import os

# Setting object
from pydantic_settings import BaseSettings
## load .env file
from dotenv import load_dotenv
import json
import ast

# api token authorization
from apiKey import api_key_auth
from fastapi.security import APIKeyHeader

# logger
from logger.custom_logger import CustomLogger
from datetime import datetime
current_time = datetime.now()
# add logger
denied_logger = CustomLogger(f"logs/gunicorn/denied-{current_time.strftime('%Y-%m')}.log", "INFO").logger


# class for setting object
class Base_Settings(BaseSettings):
    MASTER_API_KEY: str = "master-api-key"
    TEST_MODE: bool = False
    API_KEY_DIRECTORY: str = "api_key.json"

    class Config:
        env_file = ".env"

def create_app():
    
    if settings.TEST_MODE==True:
        app = FastAPI()
    else:
        app = FastAPI(docs_url=None, redoc_url=None)
    # include routers
    app.include_router(master_access.router)
    app.include_router(dataset_api_query.router)

    return app

# create fastapi app
load_dotenv()
settings = Base_Settings()
api_keys = (json.load(open(os.path.join(os.getcwd(), settings.API_KEY_DIRECTORY), 'r')))['api-key-list']
app = create_app()

@app.middleware("http")
async def check_origin_header(request, call_next):
    
    origin = request.headers.get("Origin")
    authorization = request.headers.get("Authorization")
    
    if settings.TEST_MODE:
        return await(call_next(request))
    
    # filtering master access
    try:
        if request.query_params['api-key']==settings.MASTER_API_KEY:
            print("master access")
            response = await call_next(request)
            global api_keys
            api_keys = (json.load(open(os.path.join(os.getcwd(), settings.API_KEY_DIRECTORY), 'r')))['api-key-list']
            return response
    except:
        pass
    
    # validation
    origin_validation = api_key_auth.validate_origin(origin, api_keys)
    authorization_validation = api_key_auth.validate_api_key(authorization, api_keys)
    # blocked_ip = request.client.host in settings.BLOCKED_IP

    if origin_validation==False or authorization_validation==False:
        ## exception by incorrect origin
        denied_logger.info(msg={"origin": origin, "req_url": str(request.url), "usr_agent": request.headers["User-Agent"], "ip": request.client.host, "apikey": authorization, "result": {"origin_valid": origin_validation, "apikey_valid": authorization_validation, "result": "error"}})
        raise HTTPException(status_code=403, detail="Invalid or missing Origin header or Authorization")
    ## for client access 
    response = await call_next(request)
    return response



if __name__=="__main__":
    # test command
    # uvicorn.run("main:app", host="0.0.0.0", port=22222, reload=True)
    
    #deploy command
    gunicorn_command = [
        'gunicorn',
        '-c', './gunicorn.conf.py',
        'main:app',
        '--reload'
    ]
    gunicorn_process = subprocess.Popen(gunicorn_command)