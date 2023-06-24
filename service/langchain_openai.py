# -*- coding: UTF-8 -*-

import os

from service.langchain_openai_agent import LangChainOpenAIAgent
from service.langchain_openai_coversations import LangChainOpenAIConversations
from service.langchain_openai_documents import LangChainOpenAIDocuments
from service.langchain_openai_interface import ILangChainOpenAI
from service.langchain_type import ChainType


class LangChainOpenAI:
    def __init__(self):
        if "OPENAI_API_KEY" not in os.environ:
            print("Please set OPENAI_API_KEY in your environment variables.")
            return

    def get_langchain_openai(self, chainType: ChainType) -> ILangChainOpenAI:
        if chainType == ChainType.AGENT:
            return LangChainOpenAIAgent()
        elif chainType == ChainType.CONVERSATION:
            return LangChainOpenAIConversations()
        elif chainType == ChainType.DOCUMENT:
            return LangChainOpenAIDocuments()
        else:
            return LangChainOpenAIAgent()
