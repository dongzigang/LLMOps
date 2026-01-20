#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@Tíme:   2025/11/16 - 17:30
@Author: 199312306017deg@gmail.com
@File:   test
"""
import os
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是阿里千问开发的机器人，请回答用户提出的问题，现在的时间是{now}"),
    ("human", "{query}")
]).partial(now=datetime.now())

chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_API_BASE"),
    model="qwen-plus",
)

print("请输入内容（输入 '结束' 或 'exit' 退出）：")
print("-" * 30)

while True:
    user_input = input("> ")

    if user_input.lower() in ['结束', 'exit', 'quit', 'q']:
        print("输入结束！")
        break
    response = chatLLM.stream(prompt.invoke({"query": user_input}))

    for chunk in response:
        print(chunk.content, flush=True, end='')
