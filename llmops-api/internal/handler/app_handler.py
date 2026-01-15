#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 20:40
@Author: 199312306017deg@gmail.com
@File:   app_handler
"""
import os

from flask import request, jsonify
from openai import OpenAI

from internal.schema.app_schema import CompletionReq
from pkg.response import Response, HttpCode


class AppHandler:
    """" 应用控制器 """

    def ping(self):
        return {"ping": "pong"}

    def completion(self):
        req = CompletionReq()
        if not req.validate():
            return req.errors

        query = request.json.get("query")
        client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"), base_url=os.getenv("DASHSCOPE_API_BASE"))
        completion = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {"role": "system", "content": "你是一个股票专家，请根据用户输入回复"},
                {"role": "user", "content": query}
            ],
        )
        content = completion.choices[0].message.content

        resp = Response(code=HttpCode.SUCCESS, message="", data={"content": content})

        return jsonify(resp), 200
