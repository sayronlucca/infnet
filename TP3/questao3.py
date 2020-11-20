#Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando de 0 até 10. 
# Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.
#Fluxo de exceção: 
#O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.
 #Exemplo de saída do programa:
#Informe nome do 1º participante: Zefrônio
#Informe nota do 1º participante: 8.5
#Informe nome do 2º participante: Oliúde
#Informe nota do 2º participante: 6.0
#Informe nome do 3º participante: Xonotrônfila
#Informe nota do 3º participante: 7.8
#Informe nome do 4º participante: Carbúncleo
#Informe nota do 4º participante: 8.6
#Informe nome do 5º participante: Zeugma
#Informe nota do 5º participante: 9.4
#O(a) vencedor(a) foi Zeugma com nota 9.4!






nomes = []
notas = []

def informar_dados():
    for contador in range (5):

        nome = input("Digite o nome do candidato: ")
        nomes.append(nome)

        nota_valida = False 
        while not nota_valida:
            nota = float(input("Digite a nota do candidato: "))
            if nota >= 0 and nota <= 10:
                notas.append(nota)
                nota_valida = True 
            else:
             print("Idade inválida (deve ser maior ou igual a zero).")

informar_dados()

def nota_mais_alta():
    nota_mais_alta = max(notas)
    n = notas.index(nota_mais_alta)
    nome_maior_nota = nomes[n]
    print(f"O vencedor foi {nome_maior_nota} com nota {nota_mais_alta}")

nota_mais_alta()




  