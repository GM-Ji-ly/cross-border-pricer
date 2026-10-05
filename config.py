from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# Neon PostgreSQL (Serverless)
DATABASE_URL = "postgresql+asyncpg://neondb_owner:npg_jwL84NdxiEaQ@ep-winter-dream-aot6lct0-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb"
DATABASE_CONNECT_ARGS = {"ssl": True}
