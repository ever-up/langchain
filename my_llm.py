from langchain_community.chat_models import ChatTongyi
from langchain_deepseek import ChatDeepSeek

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DASHSCOPE_API_KEY, DASHSCOPE_BASE_URL

# 创建DeepSeek LLM
tongyi_llm  = ChatTongyi(
    api_key=DASHSCOPE_API_KEY,
    # base_url = DASHSCOPE_BASE_URL,
    model="qwen-plus",
)

# 创建DeepSeek LLM
deepseek_llm = ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,  # 注意：这里是api_base，不是base_url
    model="deepseek-chat",
)
