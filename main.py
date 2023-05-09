from Pessoa import Pessoa
from Aluno import Aluno

m1 = Aluno(1,"Lucas","000.333.555-99","12345")
print(m1.getMatricula())
print(m1.id," - ",m1.nome," - ",m1._cpf," - ",m1.getMatricula())
print("------------")
m1.setMatricula("33333")
print("------------")
print(m1.id," - ",m1.nome," - ",m1._cpf," - ",m1.getMatricula())