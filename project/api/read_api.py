from sqlalchemy.orm import Session
from sqlalchemy import text


def test1_info(db: Session):
    query = ""
    results = db.execute(text(query)).all()
    templete = [" ", " "]
    results = list(map(lambda result: dict(zip(templete, result)), results))
    return results
