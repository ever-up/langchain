"""
流式调用Stream
"""
from Test01.Demo03init_llm import deepseek_init_llm

resp = deepseek_init_llm.stream('请介绍一下你自己')
print(type(resp))
for chunk in resp:
    # print(type(chunk)) # <class 'langchain_core.messages.ai.AIMessageChunk'>
    print(chunk.content,end='|',flush=True)