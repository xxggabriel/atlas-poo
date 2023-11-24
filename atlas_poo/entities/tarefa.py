from datetime import date

class Tarefa:
    def __init__(self, nome: str, duracao: int, dataInicio: date):
        self.__nome = nome
        self.__duracao = duracao
        self.__dataInicio = dataInicio

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def duracao(self) -> int:
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: int):
        self.__duracao = duracao
    
    @property
    def dataInicio(self) -> date:
        return self.__dataInicio   

    @dataInicio.setter
    def dataInicio(self, dataInicio: date):
        self.__dataInicio = dataInicio