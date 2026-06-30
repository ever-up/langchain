# 一、LangChain简介

## 1.1 LangChain由来

**其名称来源于"Language"（语言模型）和"Chain"（链式连接）的组合**，体现了其核心设计理念——**将大语言模型与其他计算资源和数据源以链式方式连接，构建出功能更加强大的AI应用**。

LangChain&LangGraph文档地址如下：

英文文档地址：https://docs.langchain.com/oss/python/langchain/overview（较全）

中文文档地址：https://docs.langchain.org.cn/oss/python/langchain/overview

## 1.2 LangChain**核心特点**

1. **统一的模型接口**

LangChain通过统一的API抽象层，解决了不同模型提供商接口各异的问题。各大模型提供商（如OpenAI、Anthropic、Google等）都有独特的API接口、参数规范和响应格式。LangChain通过标准化模型交互接口，使开发者可以无缝切换不同模型而无需重写大量代码。这一特性不仅降低了技术锁定风险，还使得开发者能够轻松利用最新最先进的模型，加速实验和创新周期。

1. **模块化架构**

LangChain采用高度模块化架构，将复杂的大模型应用分解为可复用的构建块。核心组件包括模型（Models）、提示模板（Prompts）、记忆（Memory）、链（Chains）、智能体（Agents）和工具（Tools）等。这种设计使开发者可以像搭积木一样组合各种功能，快速构建符合特定需求的AI应用。

组件的可组合性体现在LangChain表达式语言（LCEL）中，它允许开发者通过管道操作符（|）将多个组件连接成复杂的工作流。例如，一个简单的检索增强生成流程可以通过组合检索器、提示模板和LLM来实现。这种声明式的工作流定义方式不仅代码简洁，而且天然支持流式输出、异步调用和并行执行等高级特性，显著提升了开发效率和运行时性能。

1. **智能体与工具调用**

智能体是LangChain最强大的特性之一，它将大语言模型从被动的文本生成器转变为能够主动决策和执行任务的智能系统。智能体的核心思想是使用LLM作为"大脑"，通过观察-思考-行动的循环来动态决定如何解决用户问题。

LangChain智能体支持丰富的外部工具集成，包括搜索引擎、数据库、API接口等。工具是标准的函数接口，包含名称、描述和执行函数三个基本要素。智能体通过分析用户查询，自动选择适当的工具，执行后根据结果决定下一步行动，直至问题解决。这种机制极大地扩展了大模型的能力边界，使其能够处理需要实时数据或具体操作的任务。

1. **记忆管理机制**

LangChain的记忆系统使大模型应用能够保持对话状态和历史上下文，实现了真正有意义的多轮交互。记忆机制解决了纯LLM应用的无状态性问题，通过维护短期和长期记忆，使AI应用能够参考之前的对话内容，提供更加连贯和个性化的体验。

记忆系统的分层架构支持不同存储后端（内存、文件、数据库）和检索策略。开发者可以根据应用需求选择适当的记忆类型，如客服系统可能需要长期记忆用户偏好，而数据查询应用可能只需短期记忆当前会话上下文。这种灵活的记忆管理是构建高质量对话应用的关键。

## 1.3 LangChain使用场景

1. **检索增强生成（RAG）**

检索增强生成是LangChain最经典的应用场景，解决了大模型知识滞后和幻觉问题。RAG系统通过将外部知识源（文档、数据库等）向量化存储，在生成答案前先检索相关信息，使模型能够基于最新、最相关的数据生成回答。

1. **Agent智能体构建**

智能体应用将大语言模型作为推理引擎，使其能够自主规划并执行复杂任务。智能体通过分析用户目标，动态选择和执行适当的工具，逐步推进任务完成。

典型应用包括智能旅行规划，智能体可以依次调用航班查询、酒店预订、景点推荐等工具，生成完整行程；市场调研智能体可以自动搜索行业报告、分析数据并生成简报；数据分析智能体可以连接数据库，根据自然语言查询生成SQL并执行分析。

1. **对话系统与聊天机器人**

LangChain为构建上下文感知的对话系统提供了完整支持。通过记忆管理系统，对话应用能够保持多轮对话的连贯性，记住用户偏好和历史交互。

对话系统可以集成外部工具和知识源，提供超越通用聊天机器人的专业服务。例如，电商客服机器人可以连接订单数据库，提供个性化推荐和售后支持；教育助手可以结合教材内容，解答学生的学习问题。

1. **数据连接与处理**

LangChain强大的数据连接能力使大模型能够与各种数据源和结构化数据交互。这包括从非结构化文档中提取信息、查询数据库、分析数据等任务。

例如：从PDF合同中自动提取关键信息（各方、金额、条款）；将自然语言转换为SQL查询数据库；基于Excel数据生成趋势分析和报告。

1. **内容生成与自动化写作**

LangChain优化了结构化内容生成流程，通过提示模板和输出解析器确保生成内容符合特定格式和质量要求。应用场景包括自动生成报告、邮件、合同等结构化文档。例如，周报生成工具可以从业务系统提取数据，按固定格式生成报告；法律文书生成可以基于模板和用户输入，产出符合规范的法律文件。

1. **多模态应用开发**

随着多模态模型的发展，LangChain也扩展了对多种媒体类型的支持。多模态应用可以处理图像、音频、视频等非文本数据，结合语言模型的推理能力，实现更丰富的交互体验。典型应用包括图像分析系统，用户上传图片，LangChain调用图像识别API生成描述，再让LLM基于描述回答问题；语音交互系统将用户语音转换为文本，处理后再将答案转换为语音输出。

##  1.4 LangChain快速上手

### 1.4.1 python环境准备

LangChain 1.2版本要求Python版本为3.10+以上。我使用的是anconda 来 来创建和管理python环境。

```python
#创建一个名为langchain_v1.2的环境，指定Python版本是3.12.4
conda create --name langchain python=3.12.4

#查看anconda安装好的python环境
conda env list
langchain          D:\ProgramData\miniconda3\envs\langchain_v1.2

#在命令行窗口切换到某python环境
conda activate langchain
(langchain) C:\Users\22438>python -V
Python 3.12.4

#在命令行退出当前python环境
conda deactivate langchain

#删除一个已有的anconda管理的python环境
conda remove --name langchain --all
```

### 1.4.2 创建项目及配置

创建好Python环境后，创建python项目并指定python环境，同时把基本的配置文件配置好。按照如下步骤进行设置。

1、在IDEA中创建Langchainv12Project项目并指定python环境为“langchain_v1.2”。

2、**安装必要依赖**

想要正常使用LangChain还需要在该环境中安装如下依赖。

```python
# 切换conda环境
conda activate langchain_v1.2

#安装依赖
python -m pip install langchain==1.2.0  langchain-deepseek==1.0.1  dotenv==0.9.9 -i https://pypi.tuna.tsinghua.edu.cn/simple
#安装 ChatHunyuan、ChatTongyi、ChatZhipuAI依赖包
pip install langchain-community
#安装 ChatTongyi依赖包
pip install dashscope
```

注意：langchain-deepseek 是使用deepseek 大模型必要依赖，dotenv是从项目根目录.env文件中加载自定义环境变量必要依赖。

使用通义千问的话，2026.6.20的时候官方停止更新官方社区包了，可以先用langchain-community社区包来测试，我安装了一下langchain-dashscope包，但是有报错（不成熟）

忽略旧社区包的警告

```python
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_community")
```

使用langchain-dashscope报错：

这个错误是因为 `langchain_dashscope` 包依赖旧版 LangChain 的 Pydantic v1 API，但您安装的 `langchain_core` 版本可能已经升级到 v2，不再包含 `pydantic_v1` 模块。(AI分析)

```python
Traceback (most recent call last):
  File "D:\project\langchain\my_llm.py", line 1, in <module>
    from langchain_dashscope import ChatDashScope
  File "D:\conda\envs\langchain\Lib\site-packages\langchain_dashscope\__init__.py", line 1, in <module>
    from .aigc_generation import ChatDashScope
  File "D:\conda\envs\langchain\Lib\site-packages\langchain_dashscope\aigc_generation.py", line 11, in <module>
    from langchain_core.pydantic_v1 import BaseModel, Field, root_validator
ModuleNotFoundError: No module named 'langchain_core.pydantic_v1'
```

3、创建.env文件

在项目根目录下创建“.env”文件并写入如下内容，该文件中后续配置一些大模型的API_KEY和BASE_URL。

```python
DASHSCOPE_API_KEY=sk-2c3************************c35
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1

DEEPSEEK_API_KEY=sk-85*********************3d4
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

4、创建 env_utils.py 包

该文件中通过dotenv加载并获取.env文件中配置的环境变量，后续方便在项目中使用这些环境变量配置的值。

```python
import os

from dotenv import load_dotenv

# override=True 确保.env文件优先
load_dotenv(override=True)

# 从环境变量读取配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
```

5、创建my_llm.py文件

该文件后续会创建各种大模型，方便在项目中使用。如下：

```
from langchain_community.chat_models import ChatTongyi
from langchain_deepseek import ChatDeepSeek

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DASHSCOPE_API_KEY, DASHSCOPE_BASE_URL

# 创建DeepSeek LLM
tongyi_llm  = ChatTongyi(
    api_key=DASHSCOPE_API_KEY,
    # base_url = DASHSCOPE_BASE_URL,# 需要导入 dashscope包，里面有地址，不需要配了
    model="qwen-plus",
)

# 创建DeepSeek LLM
deepseek_llm = ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,  # 注意：这里是api_base，不是base_url
    model="deepseek-chat",
)
```

### 1.4.3 快速上手案例-Agent查询天气

该案例中使用langchain创建agent，该agent可以调用查询天气工具进行天气查询，天气查询工具通过代码模拟生成。

Demo01快速上手：

```py
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
```

```py
{'messages': [HumanMessage(content='查询北京的天气', additional_kwargs={}, response_metadata={}, id='ada91454-6df3-404f-a18c-6bd41f79f678'), AIMessage(content='好的，我来查询北京的天气。', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 51, 'prompt_tokens': 284, 'total_tokens': 335, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 256}, 'prompt_cache_hit_tokens': 256, 'prompt_cache_miss_tokens': 28}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402', 'id': 'd521e237-7db6-4c90-a63c-da85041524c2', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019ef7b8-dd83-7c70-8a9a-52b381e94fa5-0', tool_calls=[{'name': 'get_weather', 'args': {'city': '北京'}, 'id': 'call_00_54ZWJoNsEklnLzeSmK8d3439', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 284, 'output_tokens': 51, 'total_tokens': 335, 'input_token_details': {'cache_read': 256}, 'output_token_details': {}}), ToolMessage(content='北京 天气暴雨！', name='get_weather', id='ff30eb95-7975-498c-980d-0519c2d401be', tool_call_id='call_00_54ZWJoNsEklnLzeSmK8d3439'), AIMessage(content='北京当前的天气是 **暴雨** 🌧️，请注意出行安全，带好雨具，尽量避免在户外逗留。', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 26, 'prompt_tokens': 351, 'total_tokens': 377, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 256}, 'prompt_cache_hit_tokens': 256, 'prompt_cache_miss_tokens': 95}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402', 'id': 'df0bc87f-29dd-4243-924a-d9259c2a6063', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--019ef7b8-e277-7261-b225-cc609d3bf530-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 351, 'output_tokens': 26, 'total_tokens': 377, 'input_token_details': {'cache_read': 256}, 'output_token_details': {}})]}
**************************************************
{'messages': [HumanMessage(content='查询北京的天气', additional_kwargs={}, response_metadata={}, id='026fb39b-c396-4137-9bea-3b7173cf0853'), AIMessage(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_9d6d2ebc014740d6a7ad7b', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': '{"city": "北京"}'}}]}, response_metadata={'model_name': 'qwen-plus', 'finish_reason': 'tool_calls', 'request_id': 'b6cedf4d-b527-94aa-a635-3349f6abdd60', 'token_usage': {'input_tokens': 159, 'output_tokens': 19, 'total_tokens': 178, 'prompt_tokens_details': {'cached_tokens': 0}}}, id='lc_run--019ef7b8-e685-7470-9953-5a07ce78ea34-0', tool_calls=[{'name': 'get_weather', 'args': {'city': '北京'}, 'id': 'call_9d6d2ebc014740d6a7ad7b', 'type': 'tool_call'}], invalid_tool_calls=[]), ToolMessage(content='北京 天气暴雨！', name='get_weather', id='e524656d-3330-486a-a582-4c4848ee82e7', tool_call_id='call_9d6d2ebc014740d6a7ad7b'), AIMessage(content='北京当前天气为暴雨，请注意防范！', additional_kwargs={}, response_metadata={'model_name': 'qwen-plus', 'finish_reason': 'stop', 'request_id': '2c9c0f06-9d48-9d72-8e50-22d4ab38c1b9', 'token_usage': {'input_tokens': 198, 'output_tokens': 9, 'total_tokens': 207, 'prompt_tokens_details': {'cached_tokens': 128}}}, id='lc_run--019ef7b8-e9b3-7cb2-b767-2cd6ef7ef304-0', tool_calls=[], invalid_tool_calls=[])]}
```

# 二、模型

## 2.1 模型初始化

LangChain 支持所有主流模型提供商，包括 OpenAI、Anthropic、Google、Azure、AWS Bedrock 等，每个提供商都提供多种具有不同功能的模型(Chat、Embedding、图像、多模态等)，有关 LangChain 支持模型的完整列表，请参阅：https://docs.langchain.com/oss/python/integrations/providers/all_providers

- **关于各个聊天模型LangChain使用方式可以参考如下官网**

| 模型供应商 | 相关链接                                                     |
| ---------- | ------------------------------------------------------------ |
| OpenAI     | api_key地址：https://platform.openai.com/api-keysbase_ url地址：https://api.openai.com/v1 模型地址：https://platform.openai.com/docs/models 模型价格：https://platform.openai.com/docs/pricing |
| Anthropic  | api_key地址：https://console.anthropic.com/settings/keysbase_ url地址：https://console.anthropic.com/docs/zh-CN/get-started 模型地址：https://console.anthropic.com/docs/zh-CN/about-claude/models/overview 模型价格：https://console.anthropic.com/docs/zh-CN/about-claude/pricing |
| DeepSeek   | api_key地址：https://platform.deepseek.com/api_keysbase_ url地址:https://api-docs.deepseek.com/zh-cn/ 模型地址：https://api-docs.deepseek.com/zh-cn/quick_start/pricing 模型价格：https://api-docs.deepseek.com/zh-cn/quick_start/pricing |
| 腾讯混元   | api_key地址：https://console.cloud.tencent.com/cam/capibase_ url地址：https://cloud.tencent.com/document/api/1729/105701 模型地址：https://cloud.tencent.com/document/product/1729/104753 模型价格：https://cloud.tencent.com/document/product/1729/97731 |
| 通义千问   | api_key地址：https://bailian.console.aliyun.com/?tab=model#/api-keybase_ url地址：https://bailian.console.aliyun.com/?tab=api#/api 模型地址：https://bailian.console.aliyun.com/?tab=model#/model-market/all 模型价格：https://bailian.console.aliyun.com/?tab=doc#/doc/?type=model&url=2987148 |
| 智普AI     | api_key地址：https://bigmodel.cn/usercenter/proj-mgmt/apikeysbase_ url地址：https://docs.bigmodel.cn/cn/api/introduction 模型地址：https://docs.bigmodel.cn/cn/guide/start/model-overview 模型价格：https://open.bigmodel.cn/pricing |

### 2.1.1**Model Class方式初始化模型**

Model Class方式初始化模型最为直接，需要根据要使用的模型提供商，导入对应的具体类（如 ChatOpenAI, ChatAnthropic）并进行实例化。

```py
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
if __name__ == '__main__':
    print(resp1)
    print('*' * 50)
    print(resp2)
```

### 2.1.2 **init_chat_model初始化模型**

init_chat_model 初始化模型是LangChain v1.0版本后推出的模型统一初始化方法，该方法像一个智能工厂，需要传入“model”（模型）、“model_provider”（模型提供商）、“api_key”、“base_url”参数自动创建出对应的模型实例。初始化模型后，调用模型方式与ModelClass 方式完全一致。

model_provider支持的常见参数:openai、anthropic、deepseek、ollama同样，如果使用的模型供应商没有对应的provider，但是该模型供应商支持标准OpenAI访问，那么可以设置“model_provider”为“openai”。

```py
from langchain.chat_models import init_chat_model

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DASHSCOPE_API_KEY, DASHSCOPE_BASE_URL

deepseek_init_llm = init_chat_model(
    model= 'deepseek-v4-flash',
    api_key = DEEPSEEK_API_KEY,
    base_url = DEEPSEEK_BASE_URL
)
qwen_init_llm = init_chat_model(
    model= 'qwen3.6-plus',
    model_provider= 'openai',# init_chat_model中没有qwen，但是符合openai
    api_key = DASHSCOPE_API_KEY,
    base_url = DASHSCOPE_BASE_URL
)
if __name__ == '__main__':
    print(deepseek_init_llm.invoke('请介绍一下自己'))
    print('*' * 50)
    print(qwen_init_llm.invoke('请介绍一下自己'))
```



### 2.1.3 模型初始化参数解释

在LangChain中，Model Class 和init_chat_model初始化模型共同的参数及解释：

| 参数        | 类型   | 参数描述                                                     |
| ----------- | ------ | ------------------------------------------------------------ |
| model       | string | 指定要使用的模型标识符。                                     |
| api_key     | string | 用于身份验证的API密钥。建议通过环境变量设置，避免硬编码。    |
| base_url    | string | 指定API端点。                                                |
| temperature | number | 控制输出的随机性，值越低，结果越确定、保守；值越高，结果越多样、有创意。 |
| max_tokens  | number | 限制模型响应生成的最大令牌数，有效控制回复长度。             |
| timeout     | number | 设置等待模型响应的最大时间（秒），超时则取消请求。           |
| max_retries | number | 定义请求失败（如网络问题、速率限制）时的最大重试次数，提高鲁棒性。 |

特别提示：

- Model Class初始化模型中每个聊天模型可能有额外的参数，可以参考对应的LangChain集成页面查看；model_provider是init_chat_model方法中指定模型供应商的参数。
- Token并非简单的“字”或“词”，而是大模型通过分词器（Tokenizer）将输入文本拆分后的最小语义单元。不同的模型采用不同的分词算法（如BPE、WordPiece），因此同一段文本在不同模型中的Token数量可能不同。
  - 英文Token估算：1个Token约对应0.75个英文单词或4个字符；
  - 中文Token估算：1个汉字通常对应1~2个Token，但优化较好的模型（如通义千问、文心一言）约1:1的映射。

## 2.2 模型调用

在 LangChain 中，模型调用（Invocation）是指通过特定方法触发大语言模型生成输出的过程。根据不同的应用场景和需求，LangChain 提供了几种核心的调用方式，主要是 invoke(), stream()和 batch()方法，以及它们的异步版本 ainvoke(), astream(), 和 abatch(),下面将系统地介绍这些方法。

| 核心方法  | 主要特点                    | 适用场景                                             |
| --------- | --------------------------- | ---------------------------------------------------- |
| invoke()  | 阻塞式，一次性返回完整结果  | 简单问答、批处理任务、无需实时反馈的场景。           |
| ainvoke() | 非阻塞，提高系统吞吐量      | 高并发Web应用、IO密集型任务。                        |
| stream()  | 流式输出，实时返回每个token | 聊天机器人、长文本生成、需要提升用户体验的交互应用。 |
| asteam()  | 非阻塞，提高系统吞吐量      | 高并发Web应用、IO密集型任务。                        |
| batch()   | 批量处理多个输入            | 高并发场景，需要同时处理大量请求。                   |
| abatch()  | 非阻塞，提高系统吞吐量      | 高并发Web应用、IO密集型任务。                        |

### 2.2.1 invoke()方法调用模型

1、**单条消息**

该方式是最简单的方式，直接传入一个问题或指令，适用于不需要保留对话历史的简单生成任务

2、**消息列表（字典格式）**

该方式用于表达多轮对话历史，每条消息都需要通过 role字段指定其角色（如 system, user, assistant）

3、**消息列表（消息对象格式）**

这是LangChain推荐的方式，使用内置的消息类（如 SystemMessage, HumanMessage, AIMessage），类型更安全，功能也更丰富

```py
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
  {'role': 'system', 'content': '你是一个翻译助手，可以将汉语翻译成英语'},
  {"role": "assistant", "content": "I like programming"},
  {'role': 'user', 'content': '翻译：你今晚吃什么'},
  {'role': 'user', 'content': '翻译：大模型时代'}]
# resp1 = qwen_init_llm.invoke(conversations)
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
```

### 2.2.2 **流式调用模型**

流式传输调用大模型允许大语言模型（LLM）在生成内容的过程中，逐块（Chunk）地实时输出结果，而不是等待整个响应完全生成后再一次性返回。流式调用大模型使用方式是通过调用 [model.stream](http://model.stream/)()方法会返回一个迭代器（Iterator），你可以通过循环来实时处理每一个新生成的内容块。

```py
"""
流式调用Stream
"""
from Test01.Demo03init_llm import deepseek_init_llm

resp = deepseek_init_llm.stream('请介绍一下你自己')
print(type(resp))
for chunk in resp:
  # print(type(chunk)) # <class 'langchain_core.messages.ai.AIMessageChunk'>
  print(chunk.content, end='|', flush=True)
```

### **2.2.3. 批量调用模型**

LangChain 中的批处理功能是一种通过并行处理多个独立请求来显著提升性能、降低成本的强大机制。批处理的核心思想是将多个独立的请求集合成一个批次，并行发送给模型处理。这与逐个顺序调用（invoke）相比，能大幅减少网络往返开销和等待时间，尤其适合处理问答、文本分类、情感分析等独立任务。

batch()特点是等待所有请求处理完毕，按原始输入顺序返回结果列表。当输入列表很大或单个模型调用耗时差异显著时，batch_as_completed()允许应用在收到第一个结果后立即开始后续处理，而不必等待最慢的那个请求，也就是说

batch_as_completed() 每个请求完成后立即 yield 结果，结果可能乱序，但包含索引信息。

使用示例如下：

```py
"""
批量调用模型
"""
# 此外，当需要处理大量输入时，为了避免对模型服务造成过大压力或触发速率限制，可以通过 RunnableConfig字典中的 max_concurrency参数来控制最大并行数。
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
```

### 2.2.4 异步调用模型

在LangChain框架中，异步方法（ainvoke、astream、abatch）与它们的同步版本（invoke、stream、batch）相比，具备如下特点：

- 避免阻塞主线程：同步调用会阻塞程序执行，而异步方法让应用程序在等待API响应时保持响应性。
- 优化资源利用：异步操作可以更高效地利用系统资源，减少空闲等待时间

下面通过一个完整的示例展示如何在LangChain中使用异步方法调用模型。

```PY
"""
异步调用大模型
"""
import asyncio
import time

from langchain.chat_models import init_chat_model

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

llm = init_chat_model(
    model="deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

async def demo_async_invoke():
    """演示单个异步调用的非阻塞特性"""
    print("=== 演示：ainvoke 的异步（非阻塞）效果 ===")

    print("程序开始...")

    # 1. 发起一个异步请求，但不等待它完成
    print(">>> 发起异步模型调用 (ainvoke)...")
    async_task = llm.ainvoke("用一句话解释人工智能。")

    # 2. 在等待模型响应的同时，主程序可以继续执行其他任务
    print(">>> 模型请求已发送，程序无需等待，继续执行...")
    for i in range(3):
        # 等待1s
        time.sleep(1)
        print(f">>> 正在执行第{i + 1}个任务... ")

    # 3. 现在，我们需要模型的结果了，所以用 await 等待它完成
    print(">>> 其他任务已完成，现在等待模型返回结果...")
    response = await async_task  # 此时才开始等待

    print(f">>> 模型返回: {response.content}")


async def demo_async_stream():
    """演示异步调用的非阻塞特性"""
    print("=== 演示：astream 的异步（非阻塞）效果 ===")

    print("程序开始...")

    # 1. 发起异步流式请求，但不立即处理结果
    print(">>> 发起异步流式调用 (astream)...")
    stream_resp = llm.astream("请一句话解释机器学习的基本概念。")

    # 2. 在等待流式响应的同时，执行其他任务
    print(">>> 流式请求已发送，程序无需等待，继续执行...")
    for i in range(3):
        # 等待1s
        time.sleep(1)
        print(f">>> 正在执行第{i + 1}个任务... ")

    # 3. 现在开始处理流式结果
    print(">>> 其他任务已完成，开始处理流式结果...")

    print(">>> 流式输出: ", end="", flush=True)
    async for chunk in stream_resp:
        if hasattr(chunk, 'content'):
            print(chunk.content, end="", flush=True)
    print(">>> 流式输出结束\n")

async def demo_async_batch():
    """演示单个异步调用的非阻塞特性"""
    print("=== 演示：abatch 的异步（非阻塞）效果 ===")

    print("程序开始...")

    # 准备批量输入（即使是单个输入，也用列表形式）
    questions = ["用一句话说明深度学习与传统机器学习的区别"]

    # 1. 发起异步批量请求
    print(">>> 发起异步批量调用 (abatch)...")
    batch_resp = llm.abatch(questions)

    # 2. 在等待批量处理的同时，执行其他任务
    print(">>> 批量请求已发送，程序无需等待，继续执行...")
    for i in range(3):
        # 等待1s
        time.sleep(1)
        print(f">>> 正在执行第{i + 1}个任务... ")

    # 3. 等待批量处理结果
    print(">>> 其他任务已完成，现在等待批量处理结果...")
    responses = await batch_resp

    for response in responses:
        print(f">>> 批量响应: {response.content}")

async def main():
    """主函数"""
    await demo_async_invoke()
    await demo_async_stream()
    await demo_async_batch()


if __name__ == "__main__":
    asyncio.run(main())
```

## 2.3 模型结构化输出

**问题！！！**

```
如果调用的思考类模型，结构化输出就不适合
研究了一下，如果还想用结构化输出并且用思考大模型，prompt就需要要求的格外严格，并且最好添加method参数
output = qwen_init_llm.with_structured_output(Drama, method="json_mode",include_raw=True)
```



调用模型时，我们可以设置结构化输出来约束大模型输出结果，使其符合预定义的数据结构（如 JSON、Pydantic 模型或字典），而不是任意的自然文本。确保模型生成的结果能够被程序精准解析，并无缝集成到下游系统（如数据库、API 或前端展示逻辑）中，从而显著提升应用的可靠性和自动化程度。

### 2.3.1 **定义输出结构的模式**

在 LangChain 中，可以使用如下三种方式定义期望的输出结构：Pydantic 模型、TypedDict、JSON Schema，调用大模型时，三种方式都可通过“with_structured_output”方法来返回结构化结果。

#### **2.3.1.1. Pydantic 模型（推荐）**

Pydantic 模型是使用 Python 的 Pydantic 库定义强类型数据模型,支持复杂嵌套结构。适合需要严格数据验证和复杂结构的场景，如生成 API 响应。

Pydanitc是一个基于 Python 类型注解的库，它通过在运行时强制执行类型提示，确保数据的正确性和一致性，定义这种类型时需要创建一个继承自BaseModel的类，使用类型提示（如 str, int）和 Field函数来声明每个字段的名称、类型、默认值和描述。使用方式参考：https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage

**我尝试的，很多时候有些字段不返回或者返回的不符合预期定义的**

```py
from pydantic import BaseModel, Field
from typing import List, Optional, Union
from Test01.Demo03init_llm import qwen_init_llm


# 定义一个表示评分的嵌套模型
class Rating(BaseModel):
  imdb_rating: Optional[float] = Field(default=None, description='IMDB评分')
  douban_rating: Optional[float] = Field(default=None, description='豆瓣评分')


class Actor(BaseModel):
  name: str = Field(description='演员在现实中的名称')
  role: str = Field(description='角色在剧中的名称')


class Drama(BaseModel):
  title: str = Field(default=None, description='电视剧标题')
  year: int = Field(default=None, description='上映年份')
  director: str = Field(default=None, description='导演')
  # 使用嵌套的 Rating 模型来匹配大模型返回的评分对象 default= None 可能不返回
  # 兼容两种格式：浮点数或 Rating 对象
  rating: Optional[Union[float, Rating]] = Field(default=None, description='评分信息')
  # 注意：如果大模型返回的是 'cast'，您可能需要这里定义为 'cast' 并设置别名
  cast: List[Actor] = Field(default=[], description='主要参演人员列表')

  # 为兼容旧代码，可以添加一个计算属性来获取豆瓣评分
  @property
  def douban_score(self) -> Optional[float]:
    if isinstance(self.rating, Rating):
      return self.rating.douban_rating
    return self.rating


# 使用
# include_raw=True 会返回原始的 JSON 字符串，False 会返回解析后规定的结构化数据  json_mode模式
# output = qwen_init_llm.with_structured_output(Drama, method="json_mode",include_raw=True)
output = qwen_init_llm.with_structured_output(Drama)
res: Drama = output.invoke('介绍电视剧《甄嬛传》，我想请求的数据都要做返回并且严格按照我定义的json格式进行返回数据')


print(type(res))
print(res)
```

```py
<class '__main__.Drama'>
title='甄嬛传' year=2011 director='郑晓龙' rating=9.4 cast=[]
```



#### 2.3.1.2  **TypedDict**

TypedDict 是 Python 3.8+ 引入的一种类型提示工具，它允许为字典对象定义固定的键名和对应的值类型。TypeDict是使用 Python 的 TypedDict来定义带有类型提示的字典结构，无需额外依赖，适合需要快速定义字典结构且无需 Pydantic 重量级功能的场景。

```py
from typing import TypedDict, Annotated

from Test01.Demo03init_llm import deepseek_init_llm

class Movie(TypedDict):
    title: Annotated[str,'电影标题']
    year: Annotated[int,'上映年份']
    director: Annotated[str,'导演']
    rating: Annotated[float,'评分（10分制）']


output = deepseek_init_llm.with_structured_output(Movie)
invoke = output.invoke("""
请严格按照JSON格式输出，不要省略任何字段：
{
  "title": "",
  "year": 0,
  "director": "",
  "cast": [{"name": "", "role": ""}],
  "rating": 0.0
}

电影：《盗梦空间》
""")
print(type(invoke))
print(invoke)
from typing import TypedDict, List, Annotated


# 使用TypedDict定义嵌套结构
class Actor(TypedDict):
    name: Annotated[str, "演员姓名"]
    role: Annotated[str, "饰演的角色"]

class Movie(TypedDict):
    title: Annotated[str, "电影标题"]
    year: Annotated[int, "上映年份"]
    director: Annotated[str, "导演"]
    cast: Annotated[List[Actor], "演员列表"]  # 嵌套列表定义
    rating: Annotated[float, "评分"]

# 设置模型结构化输出
model_with_structure  = deepseek_init_llm.with_structured_output(Movie,method="json_mode")

# 调用模型并获取结构化输出
resp:Movie = model_with_structure.invoke("""
请严格按照JSON格式输出，不要省略任何字段：
{
  "title": "",
  "year": 0,
  "director": "",
  "cast": [{"name": "", "role": ""}],
  "rating": 0.0
}

电影：《盗梦空间》
""")
print(resp)
```

```
D:\python\python.exe D:\pythonProject\langchain\model_structured_output\Demo03typeddict_structured_output.py 
{'title': '盗梦空间', 'year': 2010, 'director': '克里斯托弗·诺兰', 'cast': [{'name': '莱昂纳多·迪卡普里奥', 'role': '柯布'}, {'name': '约瑟夫·戈登-莱维特', 'role': '亚瑟'}, {'name': '艾伦·佩吉', 'role': '阿德里安娜'}, {'name': '渡边谦', 'role': '斋藤'}, {'name': '汤姆·哈迪', 'role': '伊姆斯'}, {'name': '玛丽昂·歌迪亚', 'role': '梅尔'}, {'name': '基里安·墨菲', 'role': '罗伯特·费希尔'}], 'rating': 9.3}

```



#### 2.3.1.3 jsonschema

JSON Schema是提供一个标准的 JSON Schema 字典来定义结构。适合需要与多种编程语言交互或进行复杂数据约束定义的场景。

```py
import jsonschema

from Test01.Demo03init_llm import deepseek_init_llm, qwen_init_llm

json_schema = {
    "title": "MovieInfo", # 不能是中文
    "description": "电影信息",
    "type": "object",
    "properties": {
        "id": {"type": "string"    , "description": "电影ID"},
        "title": {"type": "string" , "description": "电影标题"},
        "year": {"type": "integer"  , "description": "上映年份"},
        "director": {"type": "string"    , "description": "导演"},
        "actors": {"type": "array", "items": {"type": "string", "description": "演员姓名"}},
        "genres": {"type": "array", "items": {"type": "string", "description": "电影类型"}},
        "rating": {"type": "number", "description": "评分（10分制）"},
    },
    # "required": ["title", "year", "director", "actors", "genres", "rating"] # 必须包含的字段，默认所有字段都必须包含，实际结果中可能缺少信息
}

model_with_structure = qwen_init_llm.with_structured_output(json_schema, method="json_mode")
invoke = model_with_structure.invoke("""
请以json格式输出：电影：《盗梦空间》
""")
print(type(invoke))
print(invoke)
# 验证返回的对象是否符合json_schema
try:
    error = jsonschema.validate(instance=invoke, schema=json_schema)
    # 验证成功，不抛出异常 ，返回 None
    print('验证成功')
except jsonschema.exceptions.ValidationError as e:
    print(e)
```

```py
{'title': '盗梦空间', 'original_title': 'Inception', 'year': 2010, 'director': '克里斯托弗·诺兰', 'genre': ['科幻', '动作', '悬疑', '惊悚'], 'rating': 9.3, 'description': '一名经验丰富的窃贼利用共享梦境技术，从目标潜意识中窃取商业机密。为了完成一次看似不可能的任务并洗清自己的罪名，他组建了一支团队，试图在目标的深层潜意识中植入一个想法。'}
验证成功
```

### **2.3.2. 获取结构化结果方式**

以上定义输出结构的三种模式中，我们都是通过调用“with_structured_output”来获取结构化输出结果，除了这种方式外，还可以通过使用输出解释器来获取结构化输出结果。下面介绍这两种获取结构化结果的方式。

#### **2.3.2.1. 使用with_structured_output**

这种方式是最新、最简洁的API，直接让模型“理解”你需要的数据结构，并返回解析好的对象。但是一些国内大模型不支持这种方式，例如：deepseek-reasoner不支持该方式，那么就考虑其他两种方式。

此外，我们可以在with_structured_output方法中传入include_raw=True参数同时获取原始的 AI 消息对象,从而访问令牌用量等元数据，操作如下：

```py
from pydantic import BaseModel, Field
from typing import List, Optional, Union
from Test01.Demo03init_llm import qwen_init_llm,deepseek_init_llm
# 定义一个表示评分的嵌套模型
class  Actor(BaseModel):
    name: str = Field(description='演员在现实中的名称')
    role: str = Field(description='角色在剧中的名称')

class Drama(BaseModel):
    title: str = Field(default=None, description='电视剧标题')
    year: int = Field(default=None, description='上映年份')
    director: str = Field(default=None, description='导演')
    # 使用嵌套的 Rating 模型来匹配大模型返回的评分对象 default= None 可能不返回
    # 兼容两种格式：浮点数或 Rating 对象
    rating:float = Field(default=None, description='评分信息')
    # 注意：如果大模型返回的是 'cast'，您可能需要这里定义为 'cast' 并设置别名
    cast: List[Actor] = Field(default=[], description='主要参演人员列表')

# include_raw=True 会返回原始的 JSON 字符串，False 会返回解析后规定的结构化数据  json_mode模式
output = qwen_init_llm.with_structured_output(Drama, method="json_mode",include_raw=True)
res = output.invoke('请介绍一下电影《盗梦空间》，评分字段只输出一个10分制的总评分数字，不要输出多个平台的评分。请以 JSON 格式返回结果。')
print(type(res))
print(res)
```

```py
<class 'dict'>
{'raw': AIMessage(content='{\n  "title": "盗梦空间",\n  "rating": 9.3\n}', additional_kwargs={'parsed': None, 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 48, 'total_tokens': 70, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': None, 'rejected_prediction_tokens': None, 'text_tokens': 22}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': None, 'text_tokens': 48}}, 'model_provider': 'openai', 'model_name': 'qwen3.6-plus', 'system_fingerprint': None, 'id': 'chatcmpl-f7f5712d-e2f1-97a6-b651-55b30ac9acdc', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--019f06d9-f357-74e2-8362-f55327e2d532-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 48, 'output_tokens': 22, 'total_tokens': 70, 'input_token_details': {}, 'output_token_details': {}}), 'parsed': Drama(title='盗梦空间', year=None, director=None, rating=9.3, cast=[]), 'parsing_error': None}
```

#### **2.3.2.2. 使用输出解析器**_支持推理模型

（上面说的思考模式无法正常返回甚至会报错的问题）

这种方法更传统，依赖于在提示词中明确指示模型输出特定格式的文本，然后使用解析器进行转换。其流程是：提示词指导 (引导生成指定类型）→ 模型生成文本 → 解析器转换。

```
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

init_deepseek_v4 = init_chat_model(
    model="deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    model_provider="deepseek",
)

# 1. 定义结构
class Movie(BaseModel):
    title: str = Field(description="电影标题")
    year: int = Field(description="上映年份")

# 2. 创建解析器和提示模板
parser = JsonOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_template("""
回答用户问题。
问题：{question}
你必须始终输出一个包含title(电影标题)和year(上映年份)的 JSON 对象。
""")

# 3. 创建链
chain = prompt | init_deepseek_v4 | parser

# 4. 调用（返回字典）
response = chain.invoke({"question": "介绍电影《盗梦空间》"})
print(response)
```

```py
{'title': '盗梦空间', 'year': 2010}  
```

## 2.4. **模型工具调用（了解）**

大模型工具调用（Tool Calling）可以扩展模型能力，使模型能够突破纯文本生成的限制，与外部系统和功能进行交互。在LangChain框架中，这一功能也被称为函数调用（Function Calling），两种术语可以互换使用。

### **2.4.1. 模型调用工具步骤**

如下是定义一个查询天气工具，工具名称为get_weather，具体工具创建可以参考Agent章节部分工具创建方式

```py
"""
模型工具调用
"""
from langchain_core.tools import tool

from Test01.Demo03init_llm import deepseek_init_llm, qwen_init_llm

# 创建一个模型工具
@tool
def get_weather(location: str) -> str:
    """获取天气信息"""
    return f"{location} 天气是晴天。"

# 工具告诉给模型 模型绑定工具(必须要返回结果，用返回的结果去调用，不然不会调用工具)
model_with_tools  = deepseek_init_llm.bind_tools([get_weather])

# 模型返回调用工具返回工具结果
resp = model_with_tools.invoke('获取北京天气')

## 获取工具调用信息
if resp.tool_calls:
    for tool_call in resp.tool_calls:

        print(f"工具调用ID：{tool_call}")

# 模型返回结果
print(type(resp))
print(resp)
```

以上代码运行后response对象是一个AIMessage，大模型根据用户提问如果调用了工具，该对象输出内容中只有调用工具的参数请求信息，并不会主动调用工具，所以如果真正要大模型根据工具调用结果进行回复，完整的调用流程包括如下四个步骤：

1. 模型绑定工具：通过model.bind_tools([...])绑定一个或者多个工具。
2. 模型生成工具调用请求：用户输入问题，如果调用工具，模型返回工具调用信息（如工具名称和参数）。
3. 开发者手动执行工具：用户从响应中提取工具调用信息并手动调用对应的工具。
4. 将工具执行结果传递给模型生成最终结果：将之前用户提问内容和手动执行工具结果返回模型，模型最终生成回复。

```py
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
print('final_response', final_response) # 也是AIMessage
print('final_response.content', final_response.content)
```

```py
工具调用ID：{'name': 'get_weather', 'args': {'location': '北京'}, 'id': 'call_00_gploLiDIiteVtYiuiZpv8737', 'type': 'tool_call'}
final_response content='北京的天气目前是**晴天** ☀️。' additional_kwargs={'refusal': None, 'reasoning_content': '北京的天气是晴天。我可以用中文回答用户。'} response_metadata={'token_usage': {'completion_tokens': 23, 'prompt_tokens': 352, 'total_tokens': 375, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 11, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 256}, 'prompt_cache_hit_tokens': 256, 'prompt_cache_miss_tokens': 96}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402', 'id': '55040437-20d1-4f1e-bb87-a79d28bcae84', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019f085f-8b05-78e3-9ad4-32d29be7293a-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 352, 'output_tokens': 23, 'total_tokens': 375, 'input_token_details': {'cache_read': 256}, 'output_token_details': {'reasoning': 11}}
final_response.content 北京的天气目前是**晴天** ☀️。
```

总结：大模型没有执行工具的能力

1、创建工具

2、给模型绑定工具

3、LL返回调用工具信息，手动调用工具

4、将所有消息(HumanMessage + AImessage + ToolMessage 传递给LLM，LLM出最后结果)

5、最后返回的也是AImessage

### **2.4.2. 模型多工具调用**

大模型调用工具是单次推理，即每次运行调用一个工具，当调用多个工具时，需要用户自己管理多次调用循环。

有两个工具get_stock_price（获取公司股票价格）、search_news（获取新闻），当用户提问“苹果公司今天的股价是多少？最近有什么新闻？”显然需要调用两个工具，那么第一次“model_with_tools.invoke(message)”调用执行会调用到“get_stock_price”工具（AIMessage对象中的tool_calls有工具调用），第二次“model_with_tools.invoke(message)”会调用到“search_news”工具（AIMessage对象中的tool_calls有工具调用），当不再调用工具时，返回的AIMessage对象中的tool_calls为空，所以我们使用一个While循环来自己管理工具多次调用循环，这样最终将所有消息交个大模型后，得到最终结果。

## 2.5. **模型其他使用**

### **2.5.1. Reasoning-模型推理**

大模型的“推理”能力，指的是其处理复杂问题时，模拟人类思维过程，进行逻辑链式思考和多步骤分析，而不仅仅是依赖模式匹配或简单检索来给出答案。

如果底层模型支持推理（一般是“深度思考模型”或“推理模型”，例如：deepseek-r1、openai o1/o3、qwen3-max等），我们可以在输出结果中显示推理过程。



# 三、Agent智能体

## 3.1 Agent介绍

### **3.1.1. 什么是Agent**

在LangChain框架中，Agent（智能体）是一个高级组件，它通过将大型语言模型（LLM）与一系列外部工具（Tools）相结合，构建了一个能够自主推理并执行复杂任务的智能系统。其核心思想是利用LLM作为推理引擎（Reasoning Engine），让模型能够动态地决定为解决用户问题所需采取的行动序列，包括选择何种工具、以何种顺序调用，并迭代地处理工具返回的结果，直至任务完成。

简单来说，一个Agent不再仅仅是生成文本的模型，而是一个具备“思考-行动-观察”循环的自主工作者。当用户提出一个复杂需求时，Agent会像人类一样，先理解任务、规划步骤、使用合适的工具（如搜索网络、查询数据库、执行计算）获取信息，最后综合所有信息给出最终答案。

### **3.1.2. Agent原理与执行流程**

Agent的核心工作原理遵循ReAct（Reasoning + Acting，推理+行动）框架，即在一个循环中交替进行推理和行动，这个过程会涉及到模型、工具、记忆、中间件等核心组件。

以下是一个具体的ReAct循环示例，演示Agent如何解决“找出当前最流行的无线耳机并检查库存”的任务。

用户输入---->  LLM推理 ----> 决定调用工具 ----> 执行工具 ---> 返回观察结果 ---> LLM推理 --->决定完成并生成答案 ---> 最终输出

1. **输入解析与初始推理**

**输入**：用户查询：“找出当前最流行的无线耳机并检查库存”。

**推理**：LLM分析任务后认为：“要找出‘最流行’的产品，需要最新的市场信息，我应该先使用搜索工具。”

1.   **第一次行动与观察**

**行动**：Agent调用search_products工具，参数为“wireless headphones”。

**观察**：工具返回结果：“找到5款匹配产品。Top结果：WH-1000XM5, ...”

1. **迭代推理**

**推理**：LLM根据搜索结果分析：“WH-1000XM5是排名第一的型号。现在需要确认其库存状态才能回答用户问题。”

1. **第二次行动与观察**

**行动**：Agent调用check_inventory工具，参数为“WH-1000XM5”。

**观察**：工具返回：“产品WH-1000XM5：库存10件。”

1. **最终输出**

**推理**：LLM综合所有信息后认为：“已获得所需信息，可以生成最终答案。”

**行动**：模型生成最终答案，不再调用工具。

### **3.1.3. LLM、LLM工具调用与Agent区别**

如下对比LLM、LLM工具调用和Agent工具调用三者的区别：

| 对比角度 | LLM                                  |               LLM+工具调用               | Agent工具调用                                      |
| :------: | :----------------------------------- | :--------------------------------------: | :------------------------------------------------- |
| 本质定位 | 文本生成器，基于训练数据生成连贯文本 |   增强型LLM，通过函数调用扩展能力边界    | 一个具备规划和执行能力的智能系统，以任务闭环为目标 |
| 核心功能 | 语言理解、文本生成、知识问答         | 基础工具调用、实时数据获取、简单操作执行 | 多步规划、工具编排、状态管理、错误恢复             |
| 工作模式 | 单次交互，静态响应                   |           单轮“请求-调用-响应”           | 多轮“感知-规划-执行-反馈”循环（ReAct框架）         |
| 系统架构 | 单一模型接口                         |        模型+工具绑定+手动执行循环        | LLM+规划+记忆+工具使用+防护措施                    |
| 状态管理 | 需外部维护状态                       |              需外部维护状态              | 内置记忆系统，支持短期/长期状态管理                |
| 错误处理 | 失败即终止，无自动恢复               |          失败即终止，无自动恢复          | 支持重试、回滚等恢复机制                           |































