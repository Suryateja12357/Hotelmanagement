from pydantic import BaseModel,Field
class UserRequest(BaseModel):
    username:str=Field(min_length=4,max_length=100)
    name:str=Field(min_length=3,max_length=15)
    email:str=Field(min_length=4,max_length=25)
    password:str=Field(min_length=4,max_length=20)