#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2026/1/16 - 17:18
@Author: 199312306017deg@gmail.com
@File:   module.py
"""
from flask_sqlalchemy import SQLAlchemy
from injector import Binder, Module

from internal.extension.database_extension import db


class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
