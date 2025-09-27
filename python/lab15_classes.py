#variáveis são os nossos objetos

#classe é um agrupamento de variaveis e funções.
#e depois posso colocar variaveis a partir de classes
class ContaBancaria:
    
    #Método construtor
    def __init__(self,nome, numero, valor):
        self.nome_cliente=nome
        self.numero_conta=numero
        self.saldo=valor
        print('Benvindo,', nome)
#self corresponde à variável global, todos os atributos tem de ter self em primeiro lugar
#self indica a própria classe
    #método especial para imprimir objetos de forma legível
    def __str__(self):
        return f"conta de {self.nome_cliente},nº{self.numero_conta}, saldo {self.saldo}"
    
    #Mostrar dados da conta
    def escrever_dados(self):
        print('*** Números:', self.numero_conta)
        print('*** Saldo:', self.saldo)

    #levantamento de dinheiro
    def levantamento(self,valor_debito):
        if(self.saldo>valor_debito):
            self.saldo=self.saldo-valor_debito
        else:
            print('saldo insufeciente')
    
    #obter nome do cliente
    def obter_nome_cliente(self):
        return self.nome_cliente
    
    #onter nome do cliente
    def obter_saldo(self):
        return self.saldo

    #depositar dinheiro
    def deposito(self,valor):
        if(valor>0):
            self.saldo=self.saldo+valor
        else:
            print('saldo insufeciente')


#criar contas(com saldo inicial)
contaRui=ContaBancaria('Rui',123,250) #uma variável criada a partir de uma classe é um objeto
contaAna=ContaBancaria('Ana',7777,550)#O construtor espera 3 parâmetros:(nome, numero, valor)

# Testar operações
contaRui.escrever_dados()
contaRui.levantamento(50)
print("Saldo do Rui:", contaRui.obter_saldo())

print()  # linha em branco

contaAna.escrever_dados()
contaAna.deposito(100)
print("Saldo da Ana:", contaAna.obter_saldo())

# Teste do __str__
print(contaAna)  # imprime de forma legível por causa do __str__

'''explicação do ___str___
por padrão mostra como <__main__.contabancaria object at 0x7f...>
ou seja : o tipo do objeto+a posição de memória. Isso não é muito útil. Para mudar esse comportamento, definimos o método especial __str__ dentro da classe
def __str__(self):
    return f"Conta de {self.nome_client},nº{self.numero_conta}, saldo {self.saldo}€
Desta forma ele devolve, quando acionas print(contaAna), ele devolve a string formatada
R: Conta de Ana, nº 7777, saldo 650€, ou seja, __str__=como o objetivo deve ser apresentado como texto


explicação self
O self representa o próprio objeto que está a ser usado. É um cartão de identidade do objeto atual
exemplo
contaRui=contaBancaria('rui',123,250)
contaAna=contaBancaria('Ana,7777,550)

Quando chamas contaRui.escrever_dados(), python executa:
    contaBancaria.escrever_dados(contaRui)
ou seja, passa o objeto contaRui como argumento para self. Quando chamas contaAna.escrever_dados(), faz o mesmo mas passa contaAna.
Isso garante que cada objeto usa os seus próprios atributos(nome_cliente, saldo,etc.).
Senão tivessemos self, as funções não saberiam a que objeto se referem,


Resumindo

__str__ → define como o objeto deve ser impresso (em vez de mostrar só a posição na memória).
self → é sempre o primeiro argumento dos métodos, e representa o objeto atual (cada conta guarda e usa os seus próprios dados).'''
