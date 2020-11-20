#Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:

#Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
#Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
#Não tem direito a voto (menor de 16 anos).
#Fluxo de exceção: 

#O programa deve verificar se a idade da pessoa é maior do que zero.
#Exemplos de saída do programa:

#Informe a idade: 25 

#Tem obrigação de votar.

#Informe a idade: 75

#Não tem obrigação de votar.

#Informe a idade: 12

#Não tem direito a voto.


def voto_obrigatorio(idade):
    if idade >= 18 and idade < 70:
        print("Voto obrigatório")
    elif idade >= 16 and idade < 18 or idade >= 70:
        print ("Voto facultativo")
    else:
        print ("não tem direito a voto")    
    return idade


idade = int(input("Idade: "))
print(voto_obrigatorio(idade))

