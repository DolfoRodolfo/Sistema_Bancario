class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo = 0):
        self.numero_conta = numero_conta
        self.titulas = titular
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor}. Novo saldo é {self.saldo}.")
        else:
            print("O valor do depósito deve ser positivo")
        
    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de {valor}. Novo saldo é {self.saldo}.")
            else:
                print ("Fundos insuficientes.")
        else:
            print("O Valor do saque deve ser positivo")
    
    def consultar_saldo(self):

        print (f"O saldo da conta é {self.saldo}.")
        

class Banco:
    def __init__(self):
        self.contas = {}
    def criar_conta(self, numero_conta, titular):
    
        if numero_conta not in self.contas:
            self.contas[numero_conta] = ContaBancaria(numero_conta, titular)
            print(f"Conta para {titular} criada com o numero {numero_conta}.")
        
        else:
            print("Conta já existe.")
    
    def obter_conta(self, numero_conta):

        return self.contas.get(numero_conta, None)
    

def main():
    banco = Banco()


    while True:
        print("\nSistema Bancário")
        print("1. Criar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Consultar Saldo")
        print("5. Sair")
    

        escolha = input("Digite sua escolha: ")

        if escolha == '1':

            numero_conta = input("Digite numero da conta: ")
            titular = input("Digite o nome do titular: ")
            banco.criar_conta(numero_conta, titular)
        
        elif escolha == '2':
            numero_conta = input("Digite o numero da conta: ")
            valor = float(input("Digite o valor do deposito: "))
            conta = banco.obter_conta(numero_conta)
    
            if conta:
                conta.deposito(valor)
            else:
                print("Conta não encontrada.")
        
        elif escolha == '3':
        
            numero_conta = input("Digite o numero da conta: ")
            valor = float(input("Digite o valor do Saque: "))
            conta = banco.obter_conta(numero_conta)

            if conta:
                conta.saque(valor)
            else:
                print("Conta não encontrada.")
        
        elif escolha == '4':
            numero_conta = input("Digite o numero da conta: ")
            conta = banco.obter_conta(numero_conta)
            if conta:
                conta.consultar_saldo()
            else:
                print("Conta não encontrada.")
        
        elif escolha == '5':

            print("Saindo do sistema.")
            break
        else:
            print("Escolha invalida. Por favor, rebole de ladinho novamente.")

if __name__ == "__main__":
    main()


