from typing import TypedDict, Annotated, List

from Test01.Demo03init_llm import deepseek_init_llm

# class Movie(TypedDict):
#     title: Annotated[str,'电影标题']
#     year: Annotated[int,'上映年份']
#     director: Annotated[str,'导演']
#     rating: Annotated[float,'评分（10分制）']
#
#
# output = deepseek_init_llm.with_structured_output(Movie)
# invoke = output.invoke("""
# 请严格按照JSON格式输出，不要省略任何字段：
# {
#   "title": "",
#   "year": 0,
#   "director": "",
#   "cast": [{"name": "", "role": ""}],
#   "rating": 0.0
# }
#
# 电影：《盗梦空间》
# """)
# print(type(invoke))
# print(invoke)
# from typing import TypedDict, List, Annotated
#

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

