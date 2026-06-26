"""
模型调用
"""

# 1、 invoke方法
# resp = qwen_init_llm.invoke('请介绍一下你自己')
# print(type(resp))
# print(resp.content)
# 2、字典格式的消息列表
conversations = [
    {'role':'system', 'content': '你是一个翻译助手，可以将汉语翻译成英语'},
    {"role": "assistant", "content": "I like programming"},
    {'role':'user', 'content': '翻译：你今晚吃什么'},
    {'role':'user', 'content': '翻译：大模型时代'}]
#resp1 = qwen_init_llm.invoke(conversations)
# print(type(resp1))
# print(resp1.content)
# 消息对象格式的消息列表[建议使用]
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
messages = [
    SystemMessage(content='你是一个翻译助手，可以将汉语翻译成英语'),
    AIMessage(content="I like programming"),
    HumanMessage(content='你今晚吃什么'),
    HumanMessage(content='大模型时代')]
# resp2 = qwen_init_llm.invoke(messages)
# print(type(resp2))
# print(resp2.content)
