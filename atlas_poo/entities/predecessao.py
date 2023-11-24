from .tarefa import Tarefa
from ..enum.tipo_predecessao import TipoPredecessao

class Predecessao:
    def __init__(self, tarefa: Tarefa, tipoPredecessao: TipoPredecessao, latencia: int):
        self.__tarefa = tarefa
        self.__tipoPredecessao = tipoPredecessao
        self.__latencia = latencia

    @property
    def tarefa(self) -> Tarefa:
        return self.__tarefa

    @property
    def tipoPredecessao(self) -> TipoPredecessao:
        return self.__tipoPredecessao
    
    @tipoPredecessao.setter
    def tipoPredecessao(self, tipoPredecessao: TipoPredecessao):
        self.__tipoPredecessao = tipoPredecessao

    @property
    def latencia(self) -> int:
        return self.__latencia

    @latencia.setter
    def latencia(self, latencia: int):
        self.__latencia = latencia