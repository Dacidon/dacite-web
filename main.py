import asyncio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime as dt
from db.db_init import init_db

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Post(BaseModel):
    title: str
    content: str
    
class PostUpdate(BaseModel):
    title: str
    content: str

app.mount("/static", StaticFiles(directory="ui/static"), name="static")

@app.get("/")
async def home():
    return FileResponse("ui/html/home.html")

@app.get("/blog")
async def blog_handler():
    return FileResponse("ui/html/blog.html")

@app.get("/blog/data")
async def blog_data_handler():
    return

async def main():
   await init_db()

if __name__ == "main":
    asyncio.run(main())
    