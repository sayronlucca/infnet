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
#print(valor.replace('.', ',')) # Substitui pontos por vírgulas
# Imprimirá 1,99


def divideconta (valor,pessoas,taxa):
    n = taxa/100
    totaltaxa = (valor*n)
    total = valor + totaltaxa
    return total

conta = float(input("Informe o valor da conta: "))

npessoas = False 
while not npessoas:
    pessoas = int(input("Digite o número de pessoas: "))
    if pessoas > 0:
        npessoas = True 
    else:
        print("Valor inválido")
    


taxa_garcom = False
while not taxa_garcom:
    taxa = int(input("Informe a taxa de serviço do garçom: "))
    if taxa > 0 and taxa <= 100:
        taxa_garcom = True
    else:    
        print("Valor inválido")


valortotal = divideconta(conta,pessoas,taxa)
valortotal = str(valortotal)
print(valortotal.replace('.',','))

print("O valor total é R$: ", valortotal.replace('.',','))