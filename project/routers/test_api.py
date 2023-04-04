from fastapi import APIRouter, Depends
from database.connection import get_db
from api import read_api
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api/test",
)


@router.get("/test1-info")
def test1_info(db: Session = Depends(get_db)):
    res = read_api.test1_info(db=db)
    
    return {
        "res" : res
    }
    

    
# @router.get("/{board_number}")
# def get_one_board(board_number: int, db: Session = Depends(get_db)):
#     res = board.get_one_board(db=db, board_number=board_number)
    
#     return {
#         "res" : res
#     }
    
# @router.post("/")
# def post_board(post_form: Board_post_pydantic, db: Session = Depends(get_db)):
#     res = board.post_board(db=db, post_form=post_form)
    
#     return {
#         "res": res
#     }