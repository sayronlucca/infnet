#Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o 
#número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas e o percentual do serviço prestado, entre 0 e 100.

#Fluxo de exceção: 

#O programa deve verificar se o número total de pessoas é maior do que zero.
#O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
#Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.
 #Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como separador de casa decimal, em vez de pontos.

#Para isso, converta o valor final da conta em uma string, usando a função str() e, em seguida, substitua os pontos por vírgulas com replace('.',','). Exemplo:

#valor = 1.99 # Valor numérico 
#valor = str(valor) # Converte o valor para uma string
#valor.replace('.', ',') # Substitui pontos por vírgulas
#print(valor) # Imprimirá 1,99


def divideconta (valor,pessoas,taxa):
    taxa = taxa/100
    conta = (valor*taxa)/pessoas
    return conta

conta = float(input("Informe o valor da conta"))

pessoas = int(input("Informe a quantidade de pessoas"))

if pessoas == 0:
    print("Valor inválido ")
else:
    
    
taxa = int(input("Informe a taxa de serviço do garçom"))

if taxa < 0 and taxa > 100:
    print("Valor inválido")
else:
    
    


    








