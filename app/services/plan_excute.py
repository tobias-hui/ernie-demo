from config import Config
from services.tools import TavilySearchTool

import asyncio
from erniebot_agent.agents.function_agent import FunctionAgent
from erniebot_agent.chat_models import ERNIEBot
from erniebot_agent.memory import WholeMemory
from erniebot_agent.memory import HumanMessage, AIMessage

EB_AGENT_ACCESS_TOKEN = Config.EB_AGENT_ACCESS_TOKEN


async def PlanExcute(userMessage):
    chat_model = ERNIEBot(access_token=EB_AGENT_ACCESS_TOKEN, model='ernie-4.0')
    tools = []
    tools.append(TavilySearchTool())
    message = [
        HumanMessage("记住你的角色,你是百度的代言人:小度,你的职责维护百度的企业形象,服务客户,根据客户的问题使用Tavily搜索引擎来查找回答,然后记住查找的回答里有url或者图片链接的话也需要给到客户,方便他们查看，你要组织梳理你的回复"),
        AIMessage("你好，我是小度，有什么可以帮到你的吗？"),
        HumanMessage(userMessage)
    ]

    agent = FunctionAgent(llm=chat_model, tools=tools, memory=WholeMemory())
    result = await agent.run_llm(messages=message)
    print(result)
    return result.message.content

async def SEOpt(userMessage):
    chat_model = ERNIEBot(access_token=EB_AGENT_ACCESS_TOKEN, model='ernie-4.0')
    tools = []
    tools.append(TavilySearchTool())
    message = [
        HumanMessage("你负责帮助用户优化他们的商品描述，满足这样的商品描述上传到独立站之后可以被搜索引擎识别到，尽量准确的描述商品外观功能同时还能保证SEO的优化保持在40-60字即可"),
        AIMessage("你好我是小度，你需要优化什么？"),
        HumanMessage(userMessage)
    ]

    agent = FunctionAgent(llm=chat_model, tools=tools, memory=WholeMemory())
    result = await agent.run_llm(messages=message)
    print(result)
    return result.message.content

if __name__ == "__main__":
    asyncio.run(PlanExcute())
