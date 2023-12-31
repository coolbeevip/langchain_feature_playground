import unittest

from service.langchain_openai import LangChainOpenAI
from service.langchain_type import ChainType


class TestLangChainAgent(unittest.TestCase):

    def setUp(self):
        self.langchain_openai = LangChainOpenAI()

    def test_agent(self):
        langchain_openai = self.langchain_openai.get_langchain_openai(ChainType.AGENT)
        answer = langchain_openai.get_answer("哪个国家获得了2002年足球世界杯冠军")
        self.assertIn('Brazil', answer)

    def test_conversation(self):
        langchain_openai = self.langchain_openai.get_langchain_openai(ChainType.CONVERSATION)
        answer = langchain_openai.get_answer("哪个国家获得了2002年足球世界杯冠军")
        self.assertIn('西班牙', answer)
        answer = langchain_openai.get_answer("这届足球世界杯的最佳射手是谁")
        self.assertIn('路易斯', answer)

    def test_document(self):
        langchain_openai = self.langchain_openai.get_langchain_openai(ChainType.DOCUMENT)
        answer = langchain_openai.get_answer("现在的美国总统是谁?")
        self.assertIn('Biden', answer)


if __name__ == '__main__':
    unittest.main()
