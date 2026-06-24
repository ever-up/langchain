from langchain.agents import create_agent

from my_llm import deepseek_llm,tongyi_llm

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_community")
def get_weather(city: str) -> str:
    # 模拟天气查询
    """获取给定城市的天气。"""
    return f"{city} 天气暴雨！"

# 创建Agent
agent_deepseek = create_agent(
    model=deepseek_llm,
    tools=[get_weather],
    system_prompt="你是一个助手，你可以查询城市的天气。",
)
# 创建Agent
agent_tongyi = create_agent(
    model=tongyi_llm,
    tools=[get_weather],
    system_prompt="你是一个助手，你可以查询城市的天气。",
)

# 调用Agent
resp1 = agent_deepseek.invoke(
    {"messages": [{"role": "user", "content": "查询北京的天气"}]}
)
# 调用Agent
resp2 = agent_tongyi.invoke(
    {"messages": [{"role": "user", "content": "查询北京的天气"}]}
)

print(resp1)
print('*' * 50)
print(resp2)