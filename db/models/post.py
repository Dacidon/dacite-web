from . import author_model
from db.db_init import connect
from datetime import datetime

async def fetch_posts():
    conn = await connect()    
    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM post")
        posts = await cur.fetchall()
    await conn.close()
    return posts

async def fetch_recent_posts():
    conn = await connect()    
    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM post")
        posts = await cur.fetchall()
    await conn.close()
    return posts

async def create_post(title: str, content: str):
    conn = await connect()
    data = (title, content)
    async with conn.cursor() as cur:
        await cur.execute("INSERT INTO post (title, content) VALUES (%s, %s)", data)
        await cur.commit()
    await conn.close()
    
async def delete_post(id: int):
    conn = await connect()
    async with conn.cursor() as cur:
        await cur.execute("DELETE FROM post WHERE id = %s", (id))
        await cur.commit()
    await conn.close()

async def delete_post(title: str, content: str, id: int):
    conn = await connect()
    async with conn.cursor() as cur:
        await cur.execute("UPDATE post SET title = %s, content = %s WHERE id = %s", (title, content, id))
        await cur.commit()
    await conn.close()