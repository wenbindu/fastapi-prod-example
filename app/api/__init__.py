#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/9 11:05

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.api_v1.api import api_router
from app.api.exception_handler import handler_for_validate_error, handler_for_generic_error
from app.api.middleware import TimeHTTPMiddleware, InitHTTPMiddleware
from app.core.config import settings
from app.core.errors import GenericError

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
# add middleware
app.add_middleware(TimeHTTPMiddleware)
app.add_middleware(InitHTTPMiddleware)
# include router
app.include_router(api_router)
# add exception handler
app.add_exception_handler(RequestValidationError, handler_for_validate_error)
app.add_exception_handler(GenericError, handler_for_generic_error)
