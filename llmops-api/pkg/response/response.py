#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2026/1/15 - 17:30
@Author: 199312306017deg@gmail.com
@File:   response.py
"""
from dataclasses import dataclass, field
from typing import Any

from flask import jsonify

from pkg.response.http_code import HttpCode


@dataclass
class Response:
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    return jsonify(data)


def success_json(data: Any = None):
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    return json(Response(code=HttpCode.FAIL, message="", data=data))
