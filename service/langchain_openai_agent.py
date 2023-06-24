# -*- coding: UTF-8 -*-

from typing import List

from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

from service.langchain_openai_interface import ILangChainOpenAI


class LangChainOpenAIAgent(ILangChainOpenAI):
    def __init__(self):
        self.llm = OpenAI(temperature=0)
        self.tools = load_tools(["wikipedia", "llm-math"], llm=self.llm)
        self.agent = initialize_agent(self.tools, self.llm, agent="zero-shot-react-description", verbose=True)

    def get_answer(self, question: str) -> str:
        return self.agent.run(question)
