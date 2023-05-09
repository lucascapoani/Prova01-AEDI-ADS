from Pessoa import Pessoa
from abc import ABC, abstractmethod

class Aluno(Pessoa):
    def __init__(self, id, nome, cpf, matricula):
        super().__init__(id, nome, cpf)
        # d) O atributo matrícula é fortemente privado.
        self.__matricula = matricula

    # e) Construa um método assessor e um método modificador para o atributo matrícula.
    # Método assessor (getter).
    def getMatricula(self):
        if self.__matricula != None:
            return self.__matricula
        else:
            print("Sem matricula")
    		
	# Método Modificador (setter).
    def setMatricula(self, setado):
        if self.__matricula and setado != None:
            self.__matricula = setado
        else:
            print("Acesso Negado ou valor não permitido")

    def matricularAluno(self):
        super().matricular()
        print("Método matricular Aluno...")
    
    def marcarPresenca(self):
        print("Marcando presença.")
		