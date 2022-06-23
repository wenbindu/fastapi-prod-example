#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 10:58
from typing import Any

import httpx
from fastapi import APIRouter

from serv import schemas
from serv.core.config import settings
from serv.core.errors import BadRequestError

router = APIRouter()


async def request(client, url):
    response = await client.get(url)
    return response.json()


@router.post("/")
async def create_entity_db(
        *,
        item_in: schemas.EntityClsCreate
) -> Any:
    """
    Create new entity edb.
    """

    # return {"success": 1}
    raise BadRequestError(msg="te", detail="none")


@router.get("/{edb}")
async def get_entity_db(
        *,
        db: str,
        response_model=schemas.EntityCls
) -> Any:
    """
    Create new entity edb.
    """
    url = f"{settings.BASICEG_URI}/aldb/cnd_system/{db}"
    async with httpx.AsyncClient() as client:
        result = await request(client, url)
        print(result)

    return result
