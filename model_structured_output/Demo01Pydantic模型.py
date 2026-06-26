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

# 使用
output = qwen_init_llm.with_structured_output(Drama, method="json_mode")
res = output.invoke('请以json格式介绍电视剧《甄嬛传》')

print(type(res))
print(res)