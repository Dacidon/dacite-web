import psycopg

async def connect():
    conn = await psycopg.AsyncConnection.connect("dbname=daciteWeb user=daciteweb password=1952 host=localhost")
    return conn

async def init_db():
    conn = await connect()    
    async with conn.cursor() as cur:
        await cur.execute("SET TIMEZONE to 'Europe/Moscow'")
    await conn.close()
            