#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 11:01
from fastapi import APIRouter

from serv.api.api_v1.endpoints import db_service

api_router = APIRouter()
api_router.include_router(db_service.router, prefix="/edb", tags=["edb"])
