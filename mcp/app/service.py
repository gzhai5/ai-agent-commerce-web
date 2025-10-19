from collections import defaultdict
from loguru import logger
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.graph import CompiledGraph
from app.prompt import build_agent_prompt
from app.mcpclient.config import mcpclient_config


class Service:
    def __init__(self):
        self.session_agent_map = defaultdict(CompiledGraph) # session_id -> agent

    async def ai_query(self, session_id: str, query: str, image_url: str = ""):
        if session_id in self.session_agent_map:
            agent = self.session_agent_map[session_id]
        else:
            agent = await self._setup_ai_agent()
        response = await agent.ainvoke({"messages": query, "image_url": image_url}, config={"configurable": {"thread_id": session_id}})
        self.session_agent_map[session_id] = agent
        return response

    @staticmethod
    async def _setup_ai_agent(model_name: str = "openai:gpt-4.1-mini"):
        client = MultiServerMCPClient(mcpclient_config)
        tools = await client.get_tools()
        checkpointer = InMemorySaver()
        agent = create_react_agent(
            model=model_name, 
            tools=tools, 
            prompt=build_agent_prompt(),
            checkpointer=checkpointer,
        )
        return agent
    
    async def get_tools(self):
        client = MultiServerMCPClient(mcpclient_config)
        tools = await client.get_tools()
        return [
            {"name": tool.name, "description": tool.description.strip()}
            for tool in tools
        ]

service = Service()