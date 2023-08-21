#Armazenar mais de uma informação em variaveis
#manter a sequencia dos dados em uma variavel 
#O lowe() metodo retorna uma string onde todos os 
#caracteres sao minusculos
#Simbolos e numeros sao ignorados
'''
cor_cliente = input('Digite a cor desejada: ')
cores=('amarelo','verde','azul','vermelho')

if cor_cliente.lower() in cores:
    print('sim')
else:
    print('Não temos esta cor em estoque')
'''
#juntar listas

cores = ['amarelo','verde','azul','vernelho','roxo']
valores=[10,20,30,40,50]

duas_listas = zip(cores, valores)

print(list(duas_listas))