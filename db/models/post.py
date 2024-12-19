from db.db_init import connect
from datetime import datetime, timezone, timedelta

async def fetch_post(post_id: int):
    conn = await connect()    
    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM post WHERE id = %s", post_id)
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
    data = (title, content, datetime.now(timezone(timedelta(hours=3))), datetime.now(timezone(timedelta(hours=3))))
    async with conn.cursor() as cur:
        await cur.execute("INSERT INTO post (title, content, created_at, updated_at) VALUES (%s, %s, %s, %s)", data)
        await conn.commit()
    await conn.close()
    
async def delete_post(id: int):
    conn = await connect()
    async with conn.cursor() as cur:
        await cur.execute("DELETE FROM post WHERE id = %s", (id))
        await conn.commit()
    await conn.close()

async def update_post(title: str, content: str, id: int):
    conn = await connect()
    async with conn.cursor() as cur:
        await cur.execute("UPDATE post SET title = %s, content = %s WHERE id = %s", (title, content, id))
        await conn.commit()
    await conn.close()