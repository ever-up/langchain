"""
批量调用模型
"""
from Test01.Demo03init_llm import deepseek_init_llm, qwen_init_llm

# res = qwen_init_llm.batch(['什么是Python', '什么是机器学习', '什么是大模型'])
# print(type(res)) # <class 'list'>
# for re in res:
#     # print(type(re)) #<class 'langchain_core.messages.ai.AIMessage'>
#     print(re.content)
res = qwen_init_llm.batch_as_completed(
    ['什么是Python', '什么是机器学习', '什么是大模型'],
    config={
        'max_concurrency': 5,
        'timeout': 10
    }
)
for re in res:
    # print(type(re)) #<class 'tuple'>
    print(re)
