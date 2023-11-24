from funcionario import Funcionario

class Usuario(Funcionario):
    def __init__(self, login: str, email: str):
        self.__login = login
        self.__email = email

    @property
    def login(self) -> str:
        return self.__login

    @property
    def email(self) -> str:
        return self.__email


    def logar(self, login: str, senha: str) -> bool:
        # TODO: lógica de login
        pass

    def alterarSenha(self, senha: str) -> bool:
        # TODO: lógica de alteração de senha
        pass

    def alterarEmail(self, novo_email: str) -> bool:
        # TODO: lógica de alteração de email
        pass


    