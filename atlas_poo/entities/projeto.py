from typing import List
from .unidade_de_medida import UnidadeDeMedida
from datetime import date

class Projeto:
    
    def __init__(self, nome: str, dataInicio: date = None, previsaoTermino: date = None, unidadesDeMedida: List[UnidadeDeMedida] = []):
        self.__nome = nome
        self.__dataInicio = dataInicio
        self.__previsaoTermino = previsaoTermino
        self.__unidadesDeMedida = unidadesDeMedida

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def dataInicio(self) -> date:
        return self.__dataInicio

    @dataInicio.setter
    def dataInicio(self, dataInicio: date):
        self.__dataInicio = dataInicio

    @property
    def previsaoTermino(self) -> date:
        return self.__previsaoTermino

    @previsaoTermino.setter
    def previsaoTermino(self, previsaoTermino: date):
        self.__previsaoTermino = previsaoTermino

    @property
    def unidadesDeMedida(self) -> List[UnidadeDeMedida]:
        return self.__unidadesDeMedida

    @unidadesDeMedida.setter
    def unidadesDeMedida(self, unidadeDeMedida: UnidadeDeMedida):
        self.__unidadesDeMedida = unidadeDeMedida
        
    def addUnidadeDeMedida(self, unidade: UnidadeDeMedida):
        self.__unidadesDeMedida.append(unidade)

    def removeUnidadeDeMedida(self, unidade: UnidadeDeMedida):
        if unidade in self.__unidadesDeMedida:
            self.__unidadesDeMedida.remove(unidade)
