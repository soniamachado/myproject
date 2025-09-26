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
    def escrever_dados(self):
        print('*** Números:', self.numero_conta)
        print('*** Saldo:', self.saldo)

    def levantamento(self,valor_debito):
        if(self.saldo>valor_debito):
            self.saldo=self.saldo-valor_debito
        else:
            print('saldo insufeciente')
    
    def obter_nome_cliente(self):
        return self.nome_cliente
    
    def obter_saldo(self):
        return self.saldo

    def deposito(self,valor):
        if(valor>0):
            self.saldo=self.saldo+valor
        else:
            print('saldo insufeciente')



contaRui=ContaBancaria('Rui',123) #uma variável criada a partir de uma classe é um objeto
contaAna=ContaBancaria('Ana',7777)

contaRui.numero_conta =123;
contaRui.saldo= 250;
contaRui.escrever_dados()
contaRui.levantamento(5000)

contaAna.numero_conta=7777;
contaAna.saldo=550;
contaAna.levantamento(50)
contaAna.escrever_dados()

print(contaAna)