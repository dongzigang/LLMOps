#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 17:02
@Author: 199312306017deg@gmail.com
@File:   __init__.py
公用异常信息
"""

from .exception import (
    CustomException,
    FailException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
    ValidateErrorException
)

__all__ = [
    "CustomException",
    "FailException",
    "UnauthorizedException",
    "ForbiddenException",
    "ValidateErrorException",
    "NotFoundException",
]
