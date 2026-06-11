from pydantic import BaseModel

# class PostResponse(BaseModel):
    
class PostRequest(BaseModel):
    title: str
    content: str
