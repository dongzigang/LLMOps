#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 20:40
@Author: 199312306017deg@gmail.com
@File:   app_handler
"""
import os
import uuid
from flask import request
from openai import OpenAI

from internal.exception import NotFoundException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message
from dataclasses import dataclass
from injector import inject

@inject
@dataclass
class AppHandler:
    """" 应用控制器 """
    app_service:AppService
    def create_app(self):
        app = self.app_service.create_app()
        return success_message(f"应用创建成功，id={app.id}")

    def get_app(self, id:uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用成功获取，name={app.name}")

    def update_app(self, id:uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用成功修改，name={app.name}")

    def delete_app(self, id:uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用成功删除，name={app.name}")


    def ping(self):
        raise NotFoundException('no data')
        # return {"ping": "pong"}

    def completion(self):
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

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

        return success_json(data={"content": content})
