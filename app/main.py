#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/17 12:06
import uvicorn

from app.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888, debug=True, access_log=True)
