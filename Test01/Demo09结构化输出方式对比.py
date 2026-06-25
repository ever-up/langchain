"""
结构化输出的几种实现方式演示
"""
from pydantic import BaseModel, Field
import json

from Test01.Demo03init_llm import qwen_init_llm


class Drama(BaseModel):
    title: str = Field(description='电视剧标题')
    year: int = Field(description='上映年份')
    director: str = Field(description='导演')
    rating: float = Field(description='评分（10分制）')
    cast: list[str] = Field(description='主要参演人员列表')


# ============================================
# 方式1: with_structured_output() + 明确提示词
# ============================================
# 注意：某些 API 使用 response_format 而非 tool_choice
# 需要在提示词中明确指定所有字段
print("=== 方式1: with_structured_output() ===")
structured_model = qwen_init_llm.with_structured_output(Drama)
prompt1 = '''请以json格式介绍电视剧《甄嬛传》，必须包含以下字段：
- title: 电视剧标题
- year: 上映年份（整数）
- director: 导演名字
- rating: 评分（浮点数，10分制）
- cast: 主演列表（数组）

示例格式：{"title": "剧名", "year": 2011, "director": "导演", "rating": 9.0, "cast": ["演员1", "演员2"]}'''
result1 = structured_model.invoke(prompt1)
print(f"类型: {type(result1)}")
print(f"结果: {result1}")
print()


# ============================================
# 方式2: response_format={"type": "json_object"} + 手动解析
# ============================================
# 强制 JSON 输出，需要提示词包含 "json" 并指定完整结构
print("=== 方式2: response_format json_object ===")
json_model = qwen_init_llm.bind(response_format={"type": "json_object"})
prompt2 = '''请以json格式返回电视剧《琅琊榜》的信息，严格按照此格式：
{"title": "琅琊榜", "year": 2015, "director": "孔笙", "rating": 9.1, "cast": ["胡歌", "刘涛", "王凯"]}'''
response2 = json_model.invoke(prompt2)
result2 = Drama.model_validate_json(response2.content)
print(f"类型: {type(result2)}")
print(f"结果: {result2}")
print()


# ============================================
# 方式3: 纯提示词方式 - 手动解析
# ============================================
# 不使用任何 response_format，完全靠提示词控制
print("=== 方式3: 纯提示词方式 ===")
prompt3 = '''请返回电视剧《庆余年》的信息，严格按照以下JSON格式，不要添加任何其他内容：
{"title": "庆余年", "year": 2019, "director": "孙皓", "rating": 8.0, "cast": ["张若昀", "李沁", "陈道明"]}'''
response3 = qwen_init_llm.invoke(prompt3)
# 手动解析 JSON
json_str = response3.content
result3 = Drama.model_validate_json(json_str)
print(f"类型: {type(result3)}")
print(f"结果: {result3}")
print()


# ============================================
# 方式4: 使用 json_schema（OpenAI 原生 API 支持）
# ============================================
# 注意：阿里云 DashScope 不支持此方式，会当作 json_object 处理
# 仍需要提示词包含 "json"
print("=== 方式4: json_schema 方式 ===")
schema = Drama.model_json_schema()
try:
    schema_model = qwen_init_llm.bind(
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "Drama",
                "schema": schema,
                "strict": True
            }
        }
    )
    # DashScope 不支持 json_schema，仍需要提示词含 "json"
    response4 = schema_model.invoke('请以json格式介绍电视剧《西游记》，包含title、year、director、rating、cast字段')
    result4 = Drama.model_validate_json(response4.content)
    print(f"类型: {type(result4)}")
    print(f"结果: {result4}")
except Exception as e:
    print(f"错误: {e}")
    print("说明：阿里云 DashScope 不支持 json_schema，会当作 json_object 处理")