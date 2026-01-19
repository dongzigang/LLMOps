#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2026/1/16 - 15:30
@Author: 199312306017deg@gmail.com
@File:   conftest.py
"""
import pytest

from app.http.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
