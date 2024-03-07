from __future__ import annotations

import os
from typing import Any, Dict, Type
from pydantic import Field
from dotenv import load_dotenv
from erniebot_agent.tools.base import Tool
from erniebot_agent.tools.schema import ToolParameterView
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

class SearchQuery(ToolParameterView):
    query: str = Field(description="等待搜索的关键词")

class SearchOutput(ToolParameterView):
    result: str = Field(description="搜索引擎返回的搜索结果")

class TavilySearchTool(Tool):
    description: str = "搜索引擎，快速提供实时、准确和真实的搜索结果"
    input_type: Type[ToolParameterView] = SearchQuery
    output_type: Type[ToolParameterView] = SearchOutput

    def __init__(self) -> None:
        super().__init__()

    async def __call__(self, query: str) -> Dict[str, Any]:
        tavily = TavilyClient(api_key=TAVILY_API_KEY)

        response = tavily.search(query=query, include_images=True, max_results=3)
        context = [{"url": obj["url"], "content": obj["content"]} for obj in response["results"]]
        images = response["images"]
        result = {"context": context, "images": images}
        print(result)
        return result