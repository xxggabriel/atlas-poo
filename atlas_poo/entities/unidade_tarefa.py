from .tarefa import Tarefa
from .predecessao import Predecessao
from typing import List

class UnidadeTarefa:
    def __init__(self, tarefa: Tarefa, predecessoes: List[Predecessao] = []):
        self.__tarefa = tarefa
        self.__predecessoes = predecessoes

    @property
    def tarefa(self) -> List[Tarefa]:
        return self.__tarefa


    @property
    def predecessoes(self) -> List[Predecessao]:
        return self.__predecessoes

    def addPredecessao(self, predecessao: Predecessao):
        self.__predecessoes.append(predecessao)

    def removePredecessao(self, predecessao: Predecessao):
        if predecessao in self.__predecessoes:
            self.__predecessoes.remove(predecessao)