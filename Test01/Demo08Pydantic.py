from pydantic import BaseModel, Field


from Test01.Demo03init_llm import deepseek_init_llm


class Movie(BaseModel):
    title: str = Field(description="电影标题")
    year: int = Field(description="上映年份")
    director: str = Field(description="导演")
    rating: float = Field(description="评分（10分制）")

# 设置模型结构化输出
model_with_structure  = deepseek_init_llm.with_structured_output(Movie)

# 调用模型并获取结构化输出
resp:Movie = model_with_structure.invoke("给我介绍下电影《星际穿越》")

print(type(resp))
print(resp)