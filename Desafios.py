
'''
#Desafio1

print("Olá Mundo, Jade Python")

#Desafio2

nome = str(input("Digite seu nome: "))
idade = int(input("Insira sua idade: "))
#print("Olá meu nome é ",nome," e eu tenho ", idade, " anos.")

#texto = f'Olá meu nome é {nome} e eu tenho  {idade}  anos.'

print("Meu nome e {} e eu tenho {} anos.".format(nome,idade))
'''
'''
#desafio3
#variaveis com valores
n1 = 10 
n2 = 3.5
#divisao com resultado float
print (n1//n2)


#desafio4
#capturando o nome e idade do usuario
nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))
#imprimindo as variaveis para o usuario
print("Olá, {}! Você tem {} anos .".format(nome,idade))


#desafio5
#capturando os numeros
n1 = int(input("Insira o 1° número: "))
n2 = int(input("Insira o 2° número: "))
#fazendo as operações matematicas 
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
expo = n1 ** n2

print (soma) 
print(subtracao) 
print(multiplicacao) 
print(divisao) 
print(expo) 

#desafio6
frutas = ['Maçã','Banana','Manga','Uva']

for i in frutas:
    print(i)
    print('Frutas')

#desafio7
#imprimindo apenas a primeira e ultima fruta

frutas = ['Maçã','Banana','Manga','Uva']

for i in range (0,4,3):
    print (frutas[i])

#desafio10

frutas = ['Maçã','Banana','Manga','Uva']


for l in frutas:
    print ('Eu gosto de {}'.format(l) )



#desafio11 

for n in range (1,11):
    print('Numero {}'.format(n)) 

#desafio12

frutas = ['Maça','Banana','Manga','Uva']
vegetais = ['Tomate','Pimentão','Cebola','Cenoura'] 

for n1 in frutas:
    for n2 in vegetais:
        print (n1,[n2])

#desafio13

n = 1
while n <= 9:
    n += 1
    print(n)

#desafio14

n = 0
while n <= 9:
    n += 1
    print('Loop ate 5: ',n)
    if (n==5):
        break # parando de contar ao chegar em 5
n = 0
while n <=  9:
    n += 1
    if (n==5):
        continue #fazendo continuar sem contar com o 5
    print('Loop sem o 5: ',n)


#desafio15
#definindo uma funçao
def contar_palavra(sequencia, palavra):
    cont = 0 # Inicializa o contador para contar quantas vezes a palavra aparece
    for i in sequencia: # Itera sobre cada elemento (fruta) na sequência (lista de frutas)
        if i == palavra: # Verifica se o elemento atual é igual à palavra-chave
            cont += 1 # Incrementa o contador se o elemento atual for igual à palavra-chave
    return cont  # Retorna o total de vezes que a palavra apareceu na sequência

frutas = ['maçã','maçã','maçã','abacate','uva','melancia'] #Criando a lista de frutas
palavra_chave = "maçã" # Define a palavra que queremos contar

# Chama a função contar_palavra com a lista de frutas e a palavra-alvo, armazena o resultado em 'quantidade'
quant = contar_palavra(frutas, palavra_chave)
# Imprime a mensagem que informa quantas vezes a palavra-alvo aparece na lista de frutas
print(f"A palavra '{palavra_chave}' aparece {quant} vezes na lista.") 


#desafio16 

n = int(input('insira um número: '))

if n > 10:
    print ('O número é maior que 10')
else:
    print('O número é menor que 10')

#desafio17

id = int(input('Insira sua idade: '))

if id < 13:
    print('Você é uma criança')
elif id > 13 and id <19:
    print('Você é um adolecente')
else:
    print('Você é um adulto')


#desafio18

carros = ['BMW X6','BMW i5','BMW i8']

car = input('Insira um carro que deseja comprar: ').upper()

if car in carros:
    print('Este carro está disponível')
else:
    print('Desculpe, este carro não está disponível')


#desafio24

#função para saber o quadrado de um numero
def quadrado(n):
    c=2
    resultado = n ** c
    return resultado
#pedindo um numero do usuario para ver o seu valor em quadrado
numero1 = int(input('Insira um numero: '))
calculo = quadrado(numero1)
print(calculo)  # Saída

#desafio25
#função para somar dois numeros
def somar(a, b):
    resultado = a + b
    return resultado
#solicitando os numeros do usuario para somar
n1 = int(input('Insira um numero: '))
n2 = int(input('Insira outro numero: '))
soma = somar(n1, n2)
print(soma)  # Saída: 8

#desafio26
#função para calcular a potencia de um numero
def potencia(n,c):
    if c == 0:
        c = 2
    resultado = n ** c
    return resultado

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira o numero para ser o expoente: '))
calculo = potencia(n1,n2)
print(calculo)


#desafio27

def fatorial(n):
    if n == 0:
        return 1  # Caso base
    else:
        return n * fatorial(n - 1)  # Chamada recursiva

numero = int(input('Digite um número para calcular o fatorial: '))
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')
'''
#desafio28

def dobro(n):
    if n == 0:
        return 1
    else:
        return (n * 2)

#Este codigo esta incompleto
#Responda agora

numero = int(input('Insira um numero para saber seu dobro: '))
dobro(numero)
print(numero)
