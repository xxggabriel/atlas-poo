from typing import List
from .projeto import Projeto
from .funcionario import Funcionario
from pycpfcnpj import cnpj as ValidarCNPJ

class Empresa:
    def __init__(self, nome: str, cnpj: str):
        self.__cnpj = None
        self.__nome: str = nome
        
        
        self.cnpj = cnpj
        self.__projetos: List[Projeto] = []
        self.__funcionarios: List[Funcionario] = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cnpj(self) -> str:
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: str):
        if ValidarCNPJ.validate(cnpj) == False:
            raise ValueError("CNPJ inválido!")
        self.__cnpj = cnpj

    @property
    def funcionarios(self) -> List[Funcionario]:
        return self.__funcionarios
    
    @property
    def projetos(self) -> List[Projeto]:
        return self.__projetos
    
    def addProjeto(self, projeto: Projeto):
        self.__projetos.append(projeto)

    def removeProjeto(self, projeto: Projeto):
        if projeto in self.__projetos:
            self.__projetos.remove(projeto)

    
