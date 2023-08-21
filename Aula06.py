#FOR LOOP - utilizando If e Else 
#Enviar um email com detalhes da compra online (máximo de 3 tentativas)
#para compras confirmadas
'''
compra_confirmada = True
dados_compra = 'Compra no valor de R$ 12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para seu email')
        break
    else:
        print('falha na compra')


#FOR LOOP - utilizando If e Else (Laços aninhados)

#outer loop (laço externo)
for numero1 in range(5):
    print (numero1)
    for numero2 in range(5):
        print (numero1,[numero2])

#inner loop(laço interno)

for numero1 in range(1,6):
    print ('Produto {}'.format(numero1))
    for numero2 in range(5):
        print (numero1,[numero2])


# modificar de FANTASTICO para F A N T A S T I C O

palavra = 'FANTASTICO'

for space in palavra:
    
    print(space, end='') #sem espaçamento de uma letra para outra ''
    print(space, end=' ') #espaçamento de uma letra para outra ' ' 
'''
# criar um retangulo de 6x6
'''
$$$$$$
$$$$$$
$$$$$$
$$$$$$
$$$$$$
$$$$$$
'''
'''
linha = 6
coluna = 6
simbolo = '$'

for l in range(linha):
    for c in range(coluna):
        print(simbolo, end='')
    print( )
'''
# == While loops == 

#excelente para loops dependentes de condição

# Eu preciso criar uma promoção para um produto no valor de 100 reais.

#Só que a promoção tem um porém ela começa com 100 reais e depois vai baixando 5 reais por dia
'''

valor = 100
dia = 0
while valor >20:
    dia += 1
    print ('{}º Dia da promoção'.format(dia))
    print('Está no valor R${},00 de desconto!!!'.format(valor) )
    valor -= 5

# Operador Ternário

idade = 20

#if idade >=16:
 #   resultado = print('voto permitdo')
#else:
 #   resultado = print ('voto não permitido')

resultado = 'voto permitdo' if idade >= 16 else 'voto não permitido'
print(resultado)

# Publicar um produto com comissão de 10% se for acima de R$: 20

valor = int(input('Digite o valor do seu produto em R$: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print('O valor final do produto será de R${}'.format(valor))
    break
    

#Functios(funções)
#Parâmetros e Argumentos

#default = aquele que você define o valor no parârametro

#no-default = aquele que você não define o valor no parâmetro

#criar uma função que soma varios numeros

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado+=num
    return numeros

x = soma(2,3,4,7)

print(x)


#define função 

def somador(v1,v2):
    soma = v1 * v2
    return soma 

#chama função 

res = somador(3,4)

print('Valor é {}'.format(res))


#declaração da função 

def imp_msg(np):
    print('O usuario {} escreveu uma mensagem'.format(np))

#chamando a função

n = input('Digite seu nome: ')
imp_msg(n)


#varios argumentos 

def agencia(*carro):
    return carro

print(agencia('gol','Branca','1.0'))

#varios argumentos e parametros

def agenc(**carros):
    return carros

print(agenc(marca='Fiat',cor='preto',motor='2.0'))


#qual é o numero fatorial de 4

# 4 * 3 * 2 * 1 = 24

import math

print(math.factorial(4))

fatorial = 4*3*2*1
print(fatorial)
'''

cidade1 = 'rio de janeiro'
cidade2 = 'são paulo'
cidade3 = 'salvador'

cidades = ['brasil', 'america','cuba']
#             0          1        2

#cidades.append('santa catarina')
#cidade.remove('salvador)
#cidade.insert(2,'manaus')
cidades.sort()

print(cidades)



numeros = [2,3,4,5]

letras = ['a','b','c','d']

#final = numeros + letras
numeros.extend(letras)
print(numeros)
             #lista 0            1
itens = [['item1','item2'],['item3','item4']]
    #    item0       1         0       1
print(itens[1] [0])
#     lista 0 item1