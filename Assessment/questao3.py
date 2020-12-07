#Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, 
# gastos totais com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário,
# com base nos valores percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo. 
#Se o gasto estiver dentro do percentual recomendado, informe ainda que 
#Seus gastos estão dentro da margem recomendada.
#Caso contrário, informe:
#Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
#Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de gasto com esse tipo de custo.
#Exemplo de saída do programa:
#Renda mensal total: R$ 5000
#Gastos totais com moradia: R$ 1760
#Gastos totais com educação: R$ 800
#Gastos totais com transporte: R$ 300
#Diagnóstico:
#Seus gastos totais com moradia comprometem 35.2% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$1500.
#Seus gastos totais com educação comprometem 16% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.
#Seus gastos totais com transporte comprometem 6% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.



def diagnostico_gastos(renda_mensal, gasto_moradia, gasto_educacao, gasto_transporte):

  max_gasto_moradia = renda_mensal * 0.3
  max_gasto_educacao = renda_mensal * 0.2
  max_gasto_transporte = renda_mensal * 0.15

  perc_moradia = (gasto_moradia / renda_mensal) * 100
  perc_educacao = (gasto_educacao / renda_mensal) * 100
  perc_transporte = (gasto_transporte / renda_mensal) * 100


  diagnostico = ""

  if gasto_moradia <= max_gasto_moradia:
    diagnostico += f"Seus gastos totais com moradia comprometem {perc_moradia}%. O máxmo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.\n"
  else: 
    diagnostico += f"Os gastos totais com moradia comprometem {perc_moradia}%. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${max_gasto_moradia}.\n"

  if gasto_educacao <= max_gasto_educacao:
    diagnostico += f"Seus gastos totais com educação comprometem {perc_educacao}%. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.\n"
  else:
    diagnostico += f"Os gastos totais com educação comprometem {perc_educacao}%, O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R${max_gasto_educacao}.\n"

  if gasto_transporte <= max_gasto_transporte:
    diagnostico += f"Seus gastos totais com transporte comprometem {perc_transporte}%. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.\n"
  else:
    diagnostico += f"Os gastos totais com transporte comprometem {perc_transporte}%, O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R${max_gasto_transporte}.\n"

  return diagnostico

renda_mensal = float(input("Informe a renda mensal: R$ "))
gasto_moradia = float(input("Informe o gasto com moradia: R$ "))
gasto_educacao = float(input("Informe o gasto com educação: R$ "))
gasto_transporte = float(input("Informe o gasto com transporte: R$ "))
diagnostico = diagnostico_gastos(renda_mensal, gasto_moradia, gasto_educacao, gasto_transporte)
print(diagnostico)