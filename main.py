import asyncio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime as dt
from db.db_init import init_db
from db.models.post import fetch_post, fetch_recent_posts, create_post, delete_post, update_post

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
async def home_render():
    return FileResponse("ui/html/home.html")

@app.get("/blog")
async def blog_render():
    return FileResponse("ui/html/blog.html")

@app.get("/blog/create")
async def create_post_render():
    return FileResponse("ui/html/create_post.html")

@app.get("/blog/edit/{post_id}")
async def edit_post_render():
    return FileResponse("ui/html/edit_post.html")

@app.get("/blog/{post_id}")
async def post_render():
    return FileResponse("ui/html/post_template.html")

@app.get("/api/blog/recent")
async def recent_posts_handler():
    recent = await fetch_recent_posts()
    data = []
    for element in recent:
        json = {
            "id": element[0],
            "title": element[1],
            "content": element[2],
            "created_at": element[3],
            "updated_at": element[4]
        }
        data.append(json)
    return data
        
@app.get("/api/blog/{post_id}")
async def post_handler(post_id):
    post = await fetch_post(post_id)
    json = {
        "id": post[0],
        "title": post[1],
        "content": post[2],
        "created_at": post[3],
        "updated_at": post[4]
    }
    return json
    
@app.post("/api/blog/create")
async def create_post_handler(post: Post):
    await create_post(post.title, post.content)
    return {"message": "successfully created post"}

@app.post("/api/blog/edit/{post_id}")
async def edit_post_handler(post_id, post: Post):
    await update_post(post.title, post.content, post_id)
    return {"message": "successfully edited post"}

# @app.delete("/api/blog/delete")
# async def delete_post_handler(post: Post):
#     await delete_post(post.)

async def main():
   await init_db()

if __name__ == "__main__":
    asyncio.run(main())
    