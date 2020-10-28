# Uma função que retorna o quadrado de um número:
def quadrado(n):
  q = n * n
  return q

# A função quadrado produz um retorno, e portanto pode ser usada como resultado de uma atribuição:
n = float(input("Informe um número: "))
q = quadrado(n) 
print(f"O quadrado de {n} é {q}.")