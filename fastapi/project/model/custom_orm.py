from pydantic import BaseModel, validator
    
class TestModel(BaseModel):
    user_info: str