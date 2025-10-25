from sqlalchemy.future import select
from database.models import User

async def get_user_by_telegram_id(telegram_id: int):
    from database.db import async_session  # ✅ import AFTER init_engine()
    async with async_session() as session:
        result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
        return result.scalars().first()

async def register_user(telegram_id: int, username: str, first_name: str, last_name: str):
    from database.db import async_session  # ✅ same fix here
    async with async_session() as session:
        new_user = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        session.add(new_user)
        await session.commit()
        return new_user
