def numero_primo(inteiro):
    if inteiro > 1:
        for i in range(2, inteiro):
            if (inteiro % i) == 0:
                return False
        return True
    else:
        return False        
    
valor1=int(input('indique o primeiro valor'))
valor2=int(input('indique o segundo valor'))

for i in range(valor1, valor2+1):
    if (i%5==0):
        print('termina o programa')
        break
    z=numero_primo(i)
    if(z==True):
        print (i,'é primo')
    else:
        print(i,'não é primo')  

