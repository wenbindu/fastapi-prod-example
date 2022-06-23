#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 10:59
from typing import Generator

from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
