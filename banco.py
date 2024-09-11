class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.limite_saque_diario = 3
        self.saques_realizados = 0
        self.movimentacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentacoes.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor para depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saque_diario:
            print("Limite diário de saques atingido.")
        elif valor > 500:
            print("O valor máximo para saque é de R$ 500.00.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.movimentacoes.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_extrato(self):
        if not self.movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            print("\nExtrato bancário:")
            for movimentacao in self.movimentacoes:
                print(movimentacao)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")


# Criar instância do banco
conta = Banco()

# Menu de operações
while True:
    print("\nSelecione a operação:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Extrato")
    print("4. Sair")
    
    opcao = input("Escolha a opção (1/2/3/4): ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        conta.depositar(valor_deposito)
    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: R$ "))
        conta.sacar(valor_saque)
    elif opcao == '3':
        conta.exibir_extrato()
    elif opcao == '4':
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
