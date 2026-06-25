from pydantic import BaseModel, Field

from Test01.Demo03init_llm import qwen_init_llm


class drama(BaseModel):
    title:str = Field(description='电视剧标题')
    year:int = Field(description='上映年份')
    director:str = Field(description='导演')
    range:float = Field(description='评分（10分制）')
    zhuyan:list[str] = Field(description='主要参演人员列表')


output = qwen_init_llm.with_structured_output(drama)
res:drama = output.invoke('请以json格式介绍电视剧《甄嬛传》，必须包含以下字段：title(标题)、year(年份)、director(导演)、range(评分)、zhuyan(主演)')
print(type(res))
print(res)
