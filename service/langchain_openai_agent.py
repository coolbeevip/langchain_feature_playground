# -*- coding: UTF-8 -*-

from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

from service.langchain_openai_interface import ILangChainOpenAI


class LangChainOpenAIAgent(ILangChainOpenAI):
    def __init__(self):
        llm = OpenAI(temperature=0)
        tools = load_tools(["wikipedia", "llm-math"], llm=llm)
        self.agent = initialize_agent(tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    def get_answer(self, question: str) -> str:
        return self.agent.run(question)
