from typing import Optional
from routers import test_api
import uvicorn
from fastapi import FastAPI
import subprocess

def create_app():

    app = FastAPI()
    app.include_router(test_api.router)

    return app

app = create_app()


if __name__=="__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    gunicorn_command = [
        'gunicorn',
        '-b', '0.0.0.0:8080',
        '-w', '3',
        '-k', 'uvicorn.workers.UvicornWorker',
        'main:app'
    ]

    gunicorn_process = subprocess.Popen(gunicorn_command)
