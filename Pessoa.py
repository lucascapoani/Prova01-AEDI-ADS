from abc import ABC, abstractmethod

# a) A classe Pessoa é abstrata
class Pessoa(ABC):
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        # c) O atributo cpf é fracamente privado
        self._cpf = cpf
    
    # b) O método marcarPresença da classe Pessoa é abstrato.
    @abstractmethod
    def marcarPresenca(self):
        print("Marcando presença.")

    def matricular(self):
        return None

    