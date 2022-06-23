#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 13:59
import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class TimeHTTPMiddleware(BaseHTTPMiddleware):
    # I want the `action` parameter from the route to be accessible in this middleware
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["x-server-time"] = str(process_time)
        return response


class InitHTTPMiddleware(BaseHTTPMiddleware):
    # I want the `action` parameter from the route to be accessible in this middleware
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # init parameters to request.state
        request.state.x_source = request.headers.get("x-source")
        request.state.x_trace_id = request.headers.get("x-trace-id")
        response = await call_next(request)
        response.headers["x-trace-id"] = request.state.x_trace_id

        return response
