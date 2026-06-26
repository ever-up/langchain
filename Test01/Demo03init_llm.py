from langchain.chat_models import init_chat_model
from langchain_deepseek import ChatDeepSeek
from openai import OpenAI

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DASHSCOPE_API_KEY, DASHSCOPE_BASE_URL

deepseek_init_llm = init_chat_model(
    model='deepseek-v4-flash',
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    extra_body={"enable_thinking": False}  # 改成这样
)
qwen_init_llm = init_chat_model(
    model='qwen3.6-plus',
    model_provider='openai',
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL,
    extra_body={
        'enable_thinking': False
    }
)
if __name__ == '__main__':
    print(deepseek_init_llm.invoke('请介绍一下自己'))
    print('*' * 50)
    print(qwen_init_llm.invoke('请介绍一下自己'))
