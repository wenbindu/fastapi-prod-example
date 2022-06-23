#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 11:53
from typing import Optional

from pydantic import BaseModel


class View(BaseModel):
    db: str
    ruleId: str
    viewName: str
    subRoutingKey: Optional[str] = '#'
    description: Optional[str] = None
