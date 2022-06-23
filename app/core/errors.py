#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/18 9:47

# | `200` | 请求成功
# | `204` | 成功，但无响应内容
# | `400` | 客户端请求语法错误
# | `401` | 未授权
# | `403` | 请求正确，但拒绝执行
# | `404` | 无法找到资源
# | `409` | 更新冲突
# | `414` | URI 太长
# | `500` | 服务器内部错误
# | `501` | 方法未实现
# | `503` | 暂时无法处理，稍后可以重试
# | `504` | 未从远端服务器获取请求
from starlette.responses import JSONResponse


class GenericError(Exception):
    def __init__(self, code, msg, status_code=500, detail=None):
        self.code = code
        self.msg = msg
        self.status_code = status_code
        self.detail = detail

    def __str__(self):
        return f'{self.__class__}'

    def json(self):
        err = {
            "error_code": self.code,
            "error_msg": self.msg
        }
        if self.detail:
            err['error_detail'] = self.detail
        return JSONResponse(content=err, status_code=self.status_code)


# 400-499
class BadRequestError(GenericError):
    def __init__(self, code=400, msg='Bad Request', status_code=400, detail=None):
        super().__init__(code, msg, status_code, detail)


class UnauthorizedError(GenericError):
    def __init__(self, code=401, msg='Unauthorized', status_code=401, detail=None):
        super().__init__(code, msg, status_code, detail)


class ForbiddenError(GenericError):
    def __init__(self, code=403, msg='Forbidden', status_code=403, detail=None):
        super().__init__(code, msg, status_code, detail)


class NotFoundError(GenericError):
    def __init__(self, code=404, msg='Not Found', status_code=404, detail=None):
        super().__init__(code, msg, status_code, detail)


# Trying to overwrite a resource, ex. when creating a user with an email that already exists
class ConflictError(GenericError):
    def __init__(self, code=409, msg='Conflict', status_code=409, detail=None):
        super().__init__(code, msg, status_code, detail)


class URILongError(GenericError):
    def __init__(self, code=414, msg='Request-URI Too Long', status_code=414, detail=None):
        super().__init__(code, msg, status_code, detail)


class ManyRequestError(GenericError):
    def __init__(self, code=414, msg='Too Many Request', status_code=429, detail=None):
        super().__init__(code, msg, status_code, detail)


# 500-599
class InternalServerError(GenericError):
    def __init__(self, code=500, msg='Internal Server Error', status_code=500, detail=None):
        super().__init__(code, msg, status_code, detail)


class NotImplementError(GenericError):
    def __init__(self, code=501, msg='Not Implemented', status_code=501, detail=None):
        super().__init__(code, msg, status_code, detail)


class ServiceUnavailableError(GenericError):
    def __init__(self, code=503, msg='Service Unavailable', status_code=503, detail=None):
        super().__init__(code, msg, status_code, detail)


class RemoteServiceError(GenericError):
    def __init__(self, code=503, msg='Remote Service Unavailable', status_code=503, detail=None):
        super().__init__(code, msg, status_code, detail)
