#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/18 14:12
import asyncio

import httpx


async def request(x):
    headers = {"x-trace-id": str(x)}
    async with httpx.AsyncClient() as client:
        r = await client.post("http://localhost:8888/db/", headers=headers, data={"edb": 123})
        print(r.headers.get('x-trace-id'))

async def run():
    await asyncio.gather(*[request(z) for z in range(1000, 1004)])


if __name__ == "__main__":
    asyncio.run(run())
