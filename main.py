from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
# from db.db_init import Base

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.mount("/static", StaticFiles(directory="ui/static"), name="static")

@app.get("/")
async def home():
    return FileResponse("ui/html/home.html")

@app.get("/blog")
async def blog_handler():
    return FileResponse("ui/html/blog.html")

@app.get("/blog/data")
async def blog_data_handler():
    return {"articles": [
        {
            "title": "First post",
            "content": "Skibidi dop dop dop dop yes yes yes..."
        }, 
        {
            "title": "Second post",
            "content": "Skibidi dop dop dop dop yes yes yes..."
        }, 
        {
            "title": "Third post",
            "content": "Skibidi dop dop dop dop yes yes yes..."
        }
    ]}




# if __name__ == "main":
#     Base.metadata.create_all(db_engine)
    