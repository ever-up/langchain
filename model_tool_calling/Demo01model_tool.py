"""
模型工具调用
"""
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from Test01.Demo03init_llm import deepseek_init_llm, qwen_init_llm

# 创建一个模型工具
@tool
def get_weather(location: str) -> str:
    """获取天气信息"""
    return f"{location} 天气是晴天。"

# 工具告诉给模型 模型绑定工具
model_with_tools  = deepseek_init_llm.bind_tools([get_weather])
messages = []
human_message = HumanMessage(content="北京的天气")
# human_message = HumanMessage(content="海水为什么是咸的？")
messages.append(human_message)
# 模型返回调用工具返回工具结果
resp = model_with_tools.invoke(messages)

messages.append(resp)
## 获取工具调用信息
if resp.tool_calls:
    for tool_call in resp.tool_calls:
        print(f"工具调用ID：{tool_call}")
        if tool_call['name'] == 'get_weather':
            tool_result = get_weather.invoke(tool_call)
            messages.append(tool_result)
# 模型返回结果
final_response = model_with_tools.invoke(messages)
print('final_response', final_response)
print('final_response.content', final_response.content)
