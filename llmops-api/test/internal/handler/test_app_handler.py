#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2026/1/16 - 15:12
@Author: 199312306017deg@gmail.com
@File:   test_app_handler.py
"""
import pytest

from pkg.response import HttpCode


@pytest.mark.parametrize("query", [None, "你好"])
class TestAppHandler:
    def test_completion(self, query, client):
        resp = client.post('/app/completion', json={"query": query})
        assert resp.status_code == 200
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
