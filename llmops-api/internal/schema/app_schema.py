#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2026/1/15 - 16:20
@Author: 199312306017deg@gmail.com
@File:   app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    query = StringField("Query", validators=[
        DataRequired(message="Query is required"),
        Length(max=2000, message="Query is too long")
    ])
