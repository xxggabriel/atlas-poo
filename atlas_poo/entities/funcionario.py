from ..enum.cargo import Cargo
from pycpfcnpj import cnpj as ValidarCNPJ

class Funcionario:
    def __init__(self, nome: str, cpf_cnpj: str, cargo: Cargo, salario: float):
        self.__nome: str = nome
        self.__cpf_cnpj: str = cpf_cnpj
        self.__cargo: Cargo = cargo
        self.__salario: float = salario

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def cpf_cnpj(self) -> str:
        return self.__cpf_cnpj
    
    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj: str):
        
        if ValidarCNPJ.validate(cnpj) == False:
            raise ValueError("CPF ou CNPJ inválido!")
            
        self.__cpf_cnpj = cpf_cnpj

    @property
    def cargo(self) -> Cargo:
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo: Cargo):
        self.__cargo = cargo

    @property
    def salario(self) -> float:
        return self.__salario
    
    @salario.setter
    def salario(self) -> float:
        return self.__salario
