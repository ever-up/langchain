from pydantic import BaseModel, Field
from typing import List, Optional, Union
from Test01.Demo03init_llm import qwen_init_llm


# 定义一个表示评分的嵌套模型
class Rating(BaseModel):
    imdb_rating: Optional[float] = Field(default=None, description='IMDB评分')
    douban_rating: Optional[float] = Field(default=None, description='豆瓣评分')
class  Actor(BaseModel):
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
output = qwen_init_llm.with_structured_output(Drama)
res: Drama = output.invoke('介绍电视剧《甄嬛传》，我想请求的数据都要做返回并且严格按照我定义的json格式进行返回数据')

print(type(res))
print(res)