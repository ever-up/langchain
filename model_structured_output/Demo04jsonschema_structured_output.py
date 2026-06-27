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

model_with_structure = qwen_init_llm.with_structured_output(json_schema, method="json_mode",)
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
