#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 17:30
@Author: 199312306017deg@gmail.com
@File:   test
"""
from injector import Injector, inject


class A:
    name = 'llmops'


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"class A的name：{self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
