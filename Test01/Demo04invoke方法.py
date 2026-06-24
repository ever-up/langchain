"""
模型调用
"""

from Test01.Demo03init_llm import deepseek_init_llm, qwen_init_llm

# 1、 invoke方法
# resp = qwen_init_llm.invoke('请介绍一下你自己')
# print(type(resp))
# print(resp.content)
# 2、字典格式的消息列表
conversations = [
    {'role':'system', 'content': '你是一个翻译助手，可以将汉语翻译成英语'},
    {'role':'user', 'content': '翻译:你今晚吃什么'},
    {"role": "assistant", "content": "I like programming"},
    {'role':'user', 'content': '翻译：大模型时代'}]
resp1 = qwen_init_llm.invoke(conversations)
print(type(resp1))
print(resp1.content)