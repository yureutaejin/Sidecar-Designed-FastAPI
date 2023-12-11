from fastapi import APIRouter, Depends, Request
from database.connection import get_db
from api import read_api_query as read_api
from sqlalchemy.orm import Session
from typing import List

from model.custom_orm import TestModel

from logger.custom_logger import CustomLogger
from datetime import datetime

from view.view_template import TemplateTest
from datetime import datetime

current_time = datetime.now()
# add logger
query_endpoint_access_logger = CustomLogger(f"./logs/gunicorn/access-query-endpoint-{current_time.strftime('%Y-%m')}.log", "INFO").logger

router = APIRouter(
    prefix="/api/dataset_api_query"
)


@router.post("/test/")
def test_function(user_form: TestModel, request: Request = Request, db: Session = Depends(get_db)):
    value = read_api.testapi(user_form=user_form, db=db)
    result = TemplateTest(request=request, user_form=user_form, value=value)
    query_endpoint_access_logger.info(msg=result)
    result["res"] = value
    return result
