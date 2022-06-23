#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 11:02
from typing import Optional, Union
from pydantic import BaseModel


class EntityClsBase(BaseModel):
    db: str
    description: Union[str, None] = None


class EntityClsCreate(EntityClsBase):
    dataPath: Union[str, None] = None
    logDB: Union[str, None] = None
    indexDB: Union[str, None] = None
    mqExchange: Union[str, None] = None


class EntityClsUpdate(EntityClsBase):
    flog: Union[dict, None] = None
    logApis: Union[dict, None] = None


class EntityClsInDBBase(BaseModel):
    id: str
    indexDB: str
    dataPath: str
    logDB: str
    mqExchange: str
    flog: dict
    apis: dict
    views: dict


class EntityCls(EntityClsInDBBase):
    # return to client
    pass


class EntityClsInDB(EntityClsInDBBase):
    # store to es edb
    pass

