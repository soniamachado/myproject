def primo(n):
    if n<2:
        return False
    p=True
    for i in range(2,n):
        if (n%i ==0 ):
            p=False
        break

    return p

def paridade(a,b):
    par=[]
    impar=[]
    primos=[]
    não_primos=[]
    for i in range(a,b+1):
        
        if i%2==0:
            par.append(i)
                       
        elif i%2==1:
            
            impar.append(i)
            
            
        if primo(i):
            primos.append(i)
        else:
             não_primos.append(i)

    contagem_par=int(len(par))
    print('quantidade de números pares:',contagem_par)
    
    maior_par=0
    for k in par:
        if k>maior_par:
            maior_par=k     
    print('maior búmero par é:', maior_par)
            
    menor_impar=0
    for k in impar:
        if menor_impar<k:
            menor_impar=k
    print('menor número impar:', menor_impar)

    somatorio_pares=0
    for k in par:
        somatorio_pares +=k
    print('somatório dos números pares',somatorio_pares)

    contagem_primos=int(len(primos))
    print('quantidade de números primos:',contagem_primos)

    media_impares=0
    for k in impar:
        media_impares +=k
    solucao_media_impares=media_impares/int(len(impar))   
    print('média dos números ímpares',solucao_media_impares)

    maior_não_primos=0
    for k in não_primos:
        if k>maior_não_primos:
            maior_não_primos=k     
    print('maior número não primo:', maior_não_primos)

    menor_primos=0
    for k in primos:
        if menor_primos<k:
            menor_primos=k
    print('menor número primo:',menor_primos)
    
    somatorio_dos_Ninteiros=0
    for i in range(a,b+1):
        somatorio_dos_Ninteiros +=i
    print('somatório de todos os números inteiros:', somatorio_dos_Ninteiros) 

    lista_todos_numeros=[]
    for i in range(a,b+1):
        lista_todos_numeros.append(i)
    contagem_todos_numeros=len(lista_todos_numeros)
    media_todos_valores=somatorio_dos_Ninteiros/contagem_todos_numeros
    print('média de todos os números inteiros:', media_todos_valores)