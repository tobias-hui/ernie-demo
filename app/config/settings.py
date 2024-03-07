from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())


class Config():
    def __init__(self):
        self.EB_AGENT_ACCESS_TOKEN=os.getenv("EB_AGENT_ACCESS_TOKEN")
        self.TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")



Config = Config()