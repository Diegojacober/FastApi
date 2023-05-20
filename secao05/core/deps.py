from typing import Generator

from sqlalchemy.ext.asyncio import AsyncConnection

from core.database import Session

async def get_session() -> Generator:
    session: AsyncConnection = Session()
    
    try:
        yield session
    finally:
        await session.close()