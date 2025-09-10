name=input('Enter your name:')
print('Your name is:', name)
print('and it has\t', len(name), '\t charachter');
m=1

#\t é um caracter especial chamado tabulação horizontal(TAB)
#exercicio implementar um programa em Python que solicite ao utilizador dois numeros e efectue: diferneça entre esses dois numero, some, subtração e divisão
numero1=int(input('indicar o numero: '))
numero2=int(input('indique o numero: '))
#2colocar int antes cada input pedido vem em método string e não inteiro
soma=numero1+numero2
diferença=numero1-numero2
divisao=numero1/numero2
print('soma:', soma)
print('diferença:', diferença)
print('divisao:', divisao)
#3desenvolver um programa que solicte uma mensagem ao utilizador e exiba essa mensagem com as seguintes formatações: escrever a mensagem repetida 3 vezes; 
# dividir a mensagem em vários textos: sempre que é encontra um espaço começa nova mensagem
mensagem=input("introduza um text:")
mensagem=mensagem + "\n"
print(3*mensagem)
'''dividir a mensagem em vários textos: sempre que é encontra um espaço começa 
nova mensagem '''
mensagem3=mensagem.replace(' ', '\n')
print('mensagem3:')
print(mensagem3)

#Implementar o seguinte programa e verificar o resultado final.
name=input('enter name:')
ID=input('enter your student ID number:')
course=input('Enter your course number:')
print(name+"'sID is"+ID+'\n and is enrolled in'+course)

#3.5byte=int(input('dé me um valor da memoria ram que usa'))
byte=int(input('dé me um valor da memoria ram que usa'))
print (byte*1024**3)
'''ou byte1=byte*1024*1024*1024
print(byte, ' =', byte1, "bytes." '''
#3.6 
v_inicial=int(input('introduza a valocidade inicial:'))
v_aceleracao=int(input('introduza a aceleracao:'))
v_tempo=int(input('introduza o tempo:'))
v_final=v_inicial+v_aceleracao*v_tempo
print('velocidade final:', v_inicial)
print('aceleracao:', v_aceleracao)
print('tempo:', v_tempo)
print('velocidade final:', v_final)

