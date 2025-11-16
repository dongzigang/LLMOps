#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 21:01
@Author: 199312306017deg@gmail.com
@File:   http
"""
from flask import Flask

from internal.router import Router


class Http(Flask):
    """Http引擎"""

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
