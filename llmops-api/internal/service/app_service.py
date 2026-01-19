#!/usr/bin/env python
# coding: utf-8
""" 
@Tíme:   2026/1/19 - 10:14
@Author: 199312306017deg@gmail.com
@File:   app_service.py
"""
import uuid
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from injector import inject
from internal.model import App

@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        # 1. 创建模型的实体类
        app = App()
        app.name = "测试机器人"
        app.account_id = uuid.uuid4()
        app.icon = ""
        app.description = "这是一个简单的聊天机器人"
        # 2. 将实体类添加到session会话中
        self.db.session.add(app)
        # 3. 提交session会话
        self.db.session.commit()
        return app
