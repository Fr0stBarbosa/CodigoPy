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
locadora2 = Automoveis('Renault','2007')
locadora3 = Automoveis('Fiat Uno','2004')

print(Automoveis.ano_marca(locadora1))
print(Automoveis.ano_marca(locadora2))
print(Automoveis.ano_marca(locadora3))

#Criar Classe
class Computador:
    def __init__(self,marca,memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    def ExibirInformacoes(self):
        print(self.marca,self.memoria_ram,self.placa_de_video)
    #Método
    def Desligar(self):
        print('Estou Desligando')

#Criar Objeto da Classe
computador1 = Computador('Asus', '16gb','Samsung')
#Exibindo os atributos do objeto
computador1.ExibirInformacoes()
#Usando metodos do objeto
computador1.Desligar()
'''

#Class / Construtores

'''
Velocidade Máxima, Cor, Ligado
'''

class Carro:
    def __init__(self,velMax,cor,ligado):
        self.velMax = velMax
        self.cor = cor
        self.ligado = ligado
    def Mostrar(self):
        print('Velocidade Máxima: ' + str(self.velMax))
        print('Cor..............: ' + self.cor)
        estado = 'Sim' if self.ligado else 'Não'
        print('Ligado...........: ' + estado)
        print('.................................')
    def ligar(self):
        self.ligado = True

c1 = Carro (200,'Preto',False)
c2 = Carro (120,'Azul',False)
c3 = Carro (300,'Vermelho',False)

c1.ligar()
c1.Mostrar()
c2.ligar()
c2.Mostrar()
c3.ligar()
c3.Mostrar()

print(Carro.ligar(c1))