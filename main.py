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

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("ui/static/favicon.ico")

@app.get("blog")
async def blog_handler():
    return {"articles": ["some", "strange", "bullshit"]}


# if __name__ == "main":
#     Base.metadata.create_all(db_engine)
    