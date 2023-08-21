#03/08/2023
#calculando a idade com input 
# variaveis guardam valores e podem 
'''
ano_nascimento = input("Em que você nasceu?")
idade = 2023 - int(ano_nascimento)

print (idade)
'''
#A slice() função retorna um objeto de fatia.

#Um objeto de fatia é usado para especificar como fatiar uma sequência.
#Você pode especificar onde começar a fatiar e onde terminar. Você também 
#pode especificar a etapa, que permite, por exemplo, fatiar apenas itens alternados 
'''
fruta = 'Abacate'

#index 0123456

print(fruta[-7])

'''
# o marcos silva e um execelente [programador]

#formated string

#Para usar string literais formatadas, comece uma string com f ou F 
# antes das aspas de abertura ou aspas triplas.Dentro dessa string, você
#  pode escrever uma expressão Python entre os caracteres { e } que podem se 
# referir a variáveis ou valores literais 
'''
nome = 'marcos' 
sobrenome = 'silva'
profissao = 'programador'

texto = 'O ' + nome+ ' ' + sobrenome + ' e um excelente '+'[' + profissao +']'

texto2 = f'O {nome} {sobrenome} e um excelente [{profissao}] '

print (texto)
print(texto2)
'''
'''
#calculo = 2 +2 * 3 /2

calculodois = 2 ** (3 + 4)


print(calculodois)
'''
'''
num_1 = 5
num_2 = 2

soma = num_1 + num_2
subtracao = num_1 - num_2
multiplicacao = num_1 * num_2
divisao = num_1 / num_2
divisao_inteira = num_1 // num_2
modulo = num_1 % num_2
expo = num_1 ** num_2


print (soma) #7
print(subtracao) #3
print(multiplicacao) #10
print(divisao) #2.5
print(divisao_inteira) #2
print(modulo) #1
print(expo) #25

'''
#print ((2+5)*3) resul=21 ()

#print(1+5**2) resul = 26 **

#print (5*3+8) # result 23 * /
'''
s = 2 + 2 
s2 = 2 + 2 

if s == s2:
    print("os resultados são iguais")
else:
    print ("os resultados são diferentes")
'''