from typing import Dict, List, Union
from sqlmodel.ext.asyncio.session import AsyncSession
from app import crud
from app.core.config import settings
from app.schemas.user import IUserCreate
from ..core.security import get_password_hash


users: List[Dict[str, Union[str, IUserCreate]]] = [
    {
        "data": IUserCreate(
            first_name="Admin",
            last_name="FastAPI",
            hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
            email=settings.FIRST_SUPERUSER_EMAIL,
            is_superuser=True,

        ),
    },
]


async def init_db(db_session: AsyncSession) -> None:

    for user in users:
        current_user = await crud.user.get_by_email(
            db_session, email=user["data"].email
        )
        if not current_user:
            await crud.user.create(db_session, obj_in=user["data"])
