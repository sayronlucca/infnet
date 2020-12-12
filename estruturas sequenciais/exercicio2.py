#Recrie o algoritmo de cálculo de média das notas, mas, desta vez, calcule a média ponderada
# Sabendo que a primeira nota possui peso 1, a segunda nota possui peso 2 e a terceira nota possui peso 3.


n1=int(input('Informe a primeira nota:'))
p1=int(input('Informe o peso1:'))


n2=int(input('Informe a segunda nota:'))
p2=int(input('Informe o peso2:'))


n3=int(input('Informe a terceira nota:'))
p3=int(input('Informe o peso3:'))

print(f"a média ponderada é: {(n1*p1+n2*p2+n3*p3)/(p1+p2+p3)}")
