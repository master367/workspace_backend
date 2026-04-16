import asyncio
import asyncpg

async def test():
    try:
        conn = await asyncpg.connect(user='postgres', password='postgres',
                                     database='workspace_db', host='127.0.0.1', port=5433)
        print("Connected successfully!")
        await conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(test())
