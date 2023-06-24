# -*- coding: UTF-8 -*-

from langchain import ConversationChain
from langchain.llms import OpenAI

from service.langchain_openai_interface import ILangChainOpenAI


class LangChainOpenAIConversations(ILangChainOpenAI):
    def __init__(self):
        llm = OpenAI(temperature=0)
        self.conversation = ConversationChain(llm=llm, verbose=True)

    def get_answer(self, question: str) -> str:
        return self.conversation.predict(input=question)
