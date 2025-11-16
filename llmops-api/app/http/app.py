#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 21:07
@Author: 199312306017deg@gmail.com
@File:   app
"""
from injector import Injector

from internal.router import Router
from internal.server import Http

injector = Injector()
app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
