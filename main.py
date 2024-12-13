from fastapi import FastAPI
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
# from db.db_init import Base

app = FastAPI()

app.mount("/static", StaticFiles(directory="ui/static"), name="static")

@app.get("/")
async def home():
    return FileResponse("ui/html/home.html")

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("ui/static/favicon.ico")


# if __name__ == "main":
#     Base.metadata.create_all(db_engine)
    