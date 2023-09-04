#Classe / Construtores - 04-09-23
'''
class Funcionarios:
    nome = 'elena'
    sobrenome = 'cabra'
    
usuario = Funcionarios()

print(usuario.nome,usuario.sobrenome)


#Modulo 
from datetime import datetime 

#Criar classe

class Funcionarios:
    def __init__(self,nome,sobrenome,ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome +' '+ self.sobrenome
    
    def idade_funcionarios(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
#Criar objeto

usuario1 = Funcionarios('elena','cabra',2009)
usuario2 = Funcionarios('elenco','cata',2007)
usuario3 = Funcionarios('lucas','katiau',2004)
#Criar Parametros
#usuario1.nome = 'elena'
#usuario1.sobrenome = 'cabra'
#usuario1.data_nascimento = '12/01/2009'

#usuario2.nome = 'elenco'
#usuario2.sobrenome = 'cata'
#usuario2.data_nascimento = '02/05/2007'

#print

print(usuario1.nome,usuario1.sobrenome)
print(usuario1.nome_completo())
print(Funcionarios.idade_funcionarios(usuario1))
print(Funcionarios.nome_completo(usuario3))
print(usuario2.nome)
print(usuario3.nome)
'''

#Exercicio 
#criem uma class chamada Automoveis com parametros = marca,ano
#objetos locadora1,locadora2,locadora3 e imprima os valores marca,ano

class Automoveis:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano

    def ano_marca(self):
        return self.marca +' de '+ self.ano

locadora1 = Automoveis('Gol','2009')
locadora2 = Automoveis('Fiat','2007')
locadora3 = Automoveis('Fiat Uno','2004')

print(Automoveis.ano_marca(locadora1))
print(Automoveis.ano_marca(locadora2))
print(Automoveis.ano_marca(locadora3))
