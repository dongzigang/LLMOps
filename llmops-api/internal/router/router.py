#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 20:43
@Author: 199312306017deg@gmail.com
@File:   router
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1.创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url与对应的控制器做绑定
        app_handler = AppHandler()
        bp.add_url_rule("/ping", view_func=self.app_handler.ping, methods=["GET"])

        # 3.在应用上注册蓝图
        app.register_blueprint(bp)
