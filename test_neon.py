import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def test_neon():
    url = "postgresql+asyncpg://neondb_owner:npg_jwL84NdxiEaQ@ep-winter-dream-aot6lct0-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb"
    engine = create_async_engine(url, connect_args={"ssl": True})
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1 AS test"))
            print("Neon OK:", result.fetchall())
    except Exception as e:
        print("Neon FAIL:", e)
    finally:
        await engine.dispose()

asyncio.run(test_neon())
