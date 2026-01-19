#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 21:07
@Author: 199312306017deg@gmail.com
@File:   app
"""
import dotenv
from pkg.sqlalchemy import SQLAlchemy
from injector import Injector
from flask_migrate import Migrate
from config import Config
from internal.module.module import ExtensionModule
from internal.router import Router
from internal.server import Http

dotenv.load_dotenv()

conf = Config()

injector = Injector([ExtensionModule])

app = Http(
    __name__,
    conf=conf,
    db=injector.get(SQLAlchemy),
    migrate=injector.get(Migrate),
    router=injector.get(Router)
)

if __name__ == "__main__":
    app.run(debug=True)
