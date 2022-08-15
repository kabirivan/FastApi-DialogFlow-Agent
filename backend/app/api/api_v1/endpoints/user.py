from typing import Optional
from app.schemas.common import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
)
from fastapi_pagination import Page, Params
from app.schemas.user import IUserCreate, IUserRead, IUserReadWithoutGroups, IUserStatus
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from app import crud

router = APIRouter()


@router.get("/user/list", response_model=IGetResponseBase[Page[IUserReadWithoutGroups]])
async def read_users_list(    
    params: Params = Depends(),
    db_session: AsyncSession = Depends(deps.get_db),
):
    """
    Retrieve users.
    """    
    users = await crud.user.get_multi_paginated(db_session, params=params)
    return IGetResponseBase[Page[IUserReadWithoutGroups]](data=users)