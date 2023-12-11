from sqlalchemy.orm import Session
from sqlalchemy import text
import math
from model.custom_orm import TestModel
from model.db_query import DqTest

def testapi(user_form: TestModel, db: Session):
    query, pagination_query = DqTest(time_set=user_form.time_set)
    results = db.execute(text(query)).all()
    return results
    
    