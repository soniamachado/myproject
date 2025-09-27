'''Neste exercício após ser efetuada a assignação de um valor decimal a uma variável do tipo
float, devem ser efetuadas a seguintes operações com essa variável:'''

entrada = (input('inserir um número'))
entrada = entrada.replace(',', '.')  # Substituir vírgulas por ponto
entrada=float(entrada)
#1.2.a.Escrever o dobro
dobro=entrada*2
print(f' o dobro do valor é: {dobro}')

#1.2.b.Escrever a terça parte do valor
terca_parte=entrada/3
print(f'A parte decimal do valor é:{terca_parte}')

#1.2.c.Escrever a parte decimal
parte_decimal=entrada-int(entrada)
print(f'A parte decimal do valor é:{parte_decimal}')

#1.2.d Escrever o valor somente com duas casas decimais
valor_duas_casas=round(entrada,2)
print(f'O valor com duas casas decimais é: {valor_duas_casas}')

#1.2.e Apresentar a soma desse valor com 100
soma_com_100=entrada+100
print(f'A soma do valor com 100 é: {soma_com_100}')