from typing import Dict, List, Union
from sqlmodel.ext.asyncio.session import AsyncSession
from app import crud
from app.core.config import settings
from app.schemas.user import IUserCreate


users: List[Dict[str, Union[str, IUserCreate]]] = [
    {
        "data": IUserCreate(
            first_name="Admin",
            last_name="FastAPI",
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email=settings.FIRST_SUPERUSER_EMAIL,
            is_superuser=True,
        ),
        "role": "admin",
    },
    {
        "data": IUserCreate(
            first_name="Manager",
            last_name="FastAPI",
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email="manager@example.com",
            is_superuser=False,
        ),
        "role": "manager",
    },
    {
        "data": IUserCreate(
            first_name="User",
            last_name="FastAPI",
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email="user@example.com",
            is_superuser=False,
        ),
        "role": "user",
    },
]
,
]


async def init_db(db_session: AsyncSession) -> None:

    for user in users:
        current_user = await crud.user.get_by_email(
            db_session, email=user["data"].email
        )
        role = await crud.role.get_role_by_name(db_session, name=user["role"])
        if not current_user:
            user["data"].role_id = role.id
            await crud.user.create_with_role(db_session, obj_in=user["data"])
