#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 21:01
@Author: 199312306017deg@gmail.com
@File:   http
"""
import os

from flask import Flask
from flask_migrate import Migrate

from config import Config
from internal.exception import CustomException
from internal.model import App
from internal.router import Router
from pkg.response import Response, json, HttpCode
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):
    """Http引擎"""

    def __init__(
            self,
            *args,
            conf: Config,
            db: SQLAlchemy,
            migrate: Migrate,
            router: Router,
            **kwargs
    ):
        # 调用父类构造函数初始化
        super().__init__(*args, **kwargs)

        # 初始化应用配置
        self.config.from_object(conf)

        # 注册绑定异常错误处理
        self.register_error_handler(Exception, self.handle_exception)

        # 初始化flask 扩展
        db.init_app(self)
        with self.app_context():
            _ = App()
            # db.create_all()
            migrate.init_app(self, db, directory="internal/migration")

        # 注册应用路由
        router.register_router(self)

    def handle_exception(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))
        if self.debug or os.getenv("FLASK_ENV") == 'development':
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
