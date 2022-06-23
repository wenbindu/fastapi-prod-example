#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 17:32
from collections import defaultdict

from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.core.errors import GenericError


async def handler_for_validate_error(
        request: Request,
        exc: RequestValidationError
) -> JSONResponse:
    refmt_msg = defaultdict(list)
    for pydantic_err in exc.errors():
        loc, msg = pydantic_err['loc'], pydantic_err['msg']
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)
        refmt_msg[field_string].append(msg)
    return JSONResponse(content={"error_code": 400,
                                 "error_msg": "Invalid request",
                                 "error_detail": refmt_msg},
                        status_code=400)


async def handler_for_generic_error(
        request: Request,
        exc: GenericError
) -> JSONResponse:
    return exc.json()
