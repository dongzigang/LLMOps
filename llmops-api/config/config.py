#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2026/1/15 - 16:40
@Author: 199312306017deg@gmail.com
@File:   config.py
"""
import os

from .default_config import DEFAULT_CONFIG


def _get_env(key):
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key):
    value: str = _get_env(key)
    return value.lower() == "true" if value is not None else False


class Config:
    def __init__(self):
        # 关闭wtf 的csrf保护
        self.WTF_CSRF_ENABLED = _get_bool_env("WTF_CSRF_ENABLED")

        # 配置数据库
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
