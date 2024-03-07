from fastapi import FastAPI
from typing import Dict
import uvicorn

from services.plan_excute import PlanExcute

app = FastAPI()

@app.get("/plan_execute")
async def plan_execute(userMessage: str):
    result = await PlanExcute(userMessage)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)







# from tavily import TavilyClient
# tavily = TavilyClient(api_key="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")
# # For basic search:
# response = tavily.search(query="百度2023年在人工智能领域取得的领域以及峰会照片", include_images=True)
# context = [{"url": obj["url"], "content": obj["content"]} for obj in response["results"]]
# images = response["images"]
# result = {"context": context, "images": images}
# print(result)