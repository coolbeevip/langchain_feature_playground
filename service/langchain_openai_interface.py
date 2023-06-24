# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod


class ILangChainOpenAI(metaclass=ABCMeta):

    @abstractmethod
    def get_answer(self, question: str) -> str:
        pass
