import psycopg

async def connect():
    conn = psycopg.AsyncConnection.connect("dbname=daciteWeb user=daciteweb password=1952 host=localhost", min_size=1, max_size=10)

async def init_db():
    conn = await connect()    
    async with conn.cursor() as cur:
        await cur.execute("SET TIMEZONE to 'Europe/Moscow'")
    await conn.close()
            