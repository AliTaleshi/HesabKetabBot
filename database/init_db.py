from database.models import Base
from utils.logger import logger

async def init_models():
    from database.db import engine

    if engine is None:
        raise RuntimeError("❌ Database engine has not been initialized. Call init_engine() before init_models().")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ Database models initialized successfully")
