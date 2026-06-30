"""
推理模型
"""
from langchain.chat_models import init_chat_model  # 新路径
from env_utils import DEEPSEEK_BASE_URL, DEEPSEEK_API_KEY

deepseek_chat_init_llm = init_chat_model(
    model="deepseek-chat",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    model_provider="deepseek",
)
response = deepseek_chat_init_llm.invoke("我有5个苹果，吃了一个还有几个？")
print(response)

deepseek_v4_init_llm = init_chat_model(
    model="deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    model_provider="deepseek",
)
response = deepseek_v4_init_llm.invoke('我有5个苹果，吃了一个还有几个？')
print(response)

"""
content='这个问题看似简单，但需要明确一点：苹果的总数是否发生了变化，或者“吃了一个”是否意味着苹果被消耗掉了。\n\n通常的理解是：你有5个苹果，吃掉了1个，那么剩下的苹果数量就是 **5 - 1 = 4个**。\n\n所以答案是：**还有4个苹果**。' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 67, 'prompt_tokens': 14, 'total_tokens': 81, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 14}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402', 'id': '8dd0959c-fe26-4c3d-aeb0-8b4b5eaee517', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019f17e7-2bc2-73d3-b0b4-5248b7dfebb3-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 14, 'output_tokens': 67, 'total_tokens': 81, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}}
content='吃了1个苹果后，还剩下4个苹果。' additional_kwargs={'refusal': None, 'reasoning_content': '我们被问到："我有5个苹果，吃了一个还有几个？" 这是一个简单的问题。初始有5个苹果，吃掉1个，剩余5-1=4个。所以答案是4。但要注意，问题是用中文问的，所以回答应该用中文或数字。通常，这样的问题期望一个数字答案。所以回答：4。'} response_metadata={'token_usage': {'completion_tokens': 86, 'prompt_tokens': 14, 'total_tokens': 100, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 73, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 14}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402', 'id': 'a264c688-8488-4752-803b-25a7784f60c9', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019f17e7-3756-7d72-a067-c959ebbaad0d-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 14, 'output_tokens': 86, 'total_tokens': 100, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 73}}
"""
