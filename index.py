# Lista global para armazenar todas as transações
transacoes = []

def exibir_menu():
    print("\n--- Sistema de Gestão de Finanças Pessoais ---")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Ver Extrato Detalhado")
    print("4. Gerar Resumo Financeiro")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def validar_float(prompt):
    while True:
        try:
            valor = float(input(prompt).replace(',', '.')) # Permite vírgula ou ponto
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def adicionar_transacao(tipo, transacoes_list):
    print(f"\n--- Adicionar {tipo.capitalize()} ---")
    valor = validar_float(f"Digite o valor da {tipo}: ")
    descricao = input(f"Digite a descrição da {tipo}: ")
    categoria = input(f"Digite a categoria da {tipo} (ex: Salário, Alimentação, Transporte): ")
    data = input("Digite a data da transação (AAAA-MM-DD): ") # Simplificado por enquanto, validação mais robusta depois

    nova_transacao = {
        'tipo': tipo,
        'valor': valor,
        'descricao': descricao,
        'categoria': categoria,
        'data': data
    }
    transacoes_list.append(nova_transacao)
    print(f"{tipo.capitalize()} adicionada com sucesso!")

def ver_extrato(transacoes_list):
    if not transacoes_list:
        print("\nNenhuma transação registrada ainda.")
        return

    print("\n--- Extrato Detalhado ---")
    print(f"{'Data':<12} {'Tipo':<8} {'Categoria':<15} {'Valor (R$)':<15} {'Descrição':<30}")
    print("-" * 80)
    for t in transacoes_list:
        valor_str = f"{t['valor']:.2f}".replace('.', ',')
        print(f"{t['data']:<12} {t['tipo'].capitalize():<8} {t['categoria']:<15} {valor_str:<15} {t['descricao']:<30}")

def gerar_resumo(transacoes_list):
    total_receitas = 0
    total_despesas = 0

    for t in transacoes_list:
        if t['tipo'] == 'receita':
            total_receitas += t['valor']
        elif t['tipo'] == 'despesa':
            total_despesas += t['valor']

    saldo_atual = total_receitas - total_despesas

    print("\n--- Resumo Financeiro ---")
    print(f"Total de Receitas: R$ {total_receitas:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ','))
    print(f"Total de Despesas: R$ {total_despesas:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ','))
    print(f"Saldo Atual: R$ {saldo_atual:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ','))

    if saldo_atual >= 0:
        print("Sua situação financeira está positiva. Continue assim!")
    else:
        print("Atenção: Seu saldo está negativo. Considere revisar seus gastos.")

def main():
    while True:
        escolha = exibir_menu()

        if escolha == '1':
            adicionar_transacao('receita', transacoes)
        elif escolha == '2':
            adicionar_transacao('despesa', transacoes)
        elif escolha == '3':
            ver_extrato(transacoes)
        elif escolha == '4':
            gerar_resumo(transacoes)
        elif escolha == '5':
            print("Saindo do Sistema. Obrigado por usar!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()
