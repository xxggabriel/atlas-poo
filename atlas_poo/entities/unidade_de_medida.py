from .unidade_tarefa import UnidadeTarefa
from typing import List

class UnidadeDeMedida:
    def __init__(self, name: str, unidadeTarefas: List[UnidadeTarefa] = []):
        self.__identificador = name
        self.__unidadeTarefas = unidadeTarefas

    @property
    def identificador(self) -> str:
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador: str):
        self.__identificador = identificador

    @property
    def unidadeTarefas(self) -> List[UnidadeTarefa]:
        return self.__unidadeTarefas

    def addUnidadeTarefa(self, unidade: UnidadeTarefa):
        self.__unidadeTarefas.append(unidade)

    def removeUnidadeTarefa(self, unidade: UnidadeTarefa):
        if unidade in self.__unidadeTarefas:
            self.__unidadeTarefas.remove(unidade)