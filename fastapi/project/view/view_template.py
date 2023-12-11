from fastapi import Request
from typing import List
from model.custom_orm import TestModel
from datetime import datetime

def TemplateTest(request: Request, user_form: TestModel, value: list):
    result = {
        "origin": request.headers.get("Origin"),
        "req_url": str(request.url),
        "usr_agent": request.headers["User-Agent"],
        "ip" : request.client.host,
        "user" : user_form.user_info,
        "res_time" : (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    }
    return result