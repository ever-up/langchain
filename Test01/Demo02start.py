from my_llm import deepseek_llm, tongyi_llm

print(deepseek_llm.invoke('请介绍一下你自己'))
print('*' * 50)
print(tongyi_llm.invoke('请介绍一下你自己'))