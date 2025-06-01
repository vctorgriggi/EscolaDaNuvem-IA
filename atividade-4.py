import string
import getpass

# 1 - Calculadora Simples
def simple_calculator() -> None:
    while True:
        try:
            numero1 = float(input("\nInsira o primeiro número: "))
            numero2 = float(input("Insira o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ").strip()

            if operacao == "+":
                resultado = numero1 + numero2
            elif operacao == "-":
                resultado = numero1 - numero2
            elif operacao == "*":
                resultado = numero1 * numero2
            elif operacao == "/":
                resultado = numero1 / numero2
            else:
                print("Erro: Operação inválida. Tente novamente.")
                continue

            print(f"\nResultado: {resultado:.2f}")

            sair = input("Deseja finalizar esta operação? (Y/N): ").strip().upper()
            if sair == "Y":
                break

        except ValueError:
            print("Erro: Insira um valor numérico válido.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")

# 2 - Calculadora de Média de Notas
def average_grade_calculator() -> None:
    notas = []

    while True:
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip().lower()
        if entrada == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia das notas: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida.")

# 3 - Verificador de Força de Senha
def password_checker() -> None:
    while True:
        senha = getpass.getpass("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue
        if not any(c.isdigit() for c in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue
        if not any(c.isupper() for c in senha):
            print("Senha fraca: deve conter pelo menos uma letra maiúscula.")
            continue
        if not any(c.islower() for c in senha):
            print("Senha fraca: deve conter pelo menos uma letra minúscula.")
            continue
        if not any(c in string.punctuation for c in senha):
            print("Senha fraca: deve conter pelo menos um caractere especial.")
            continue

        print("Senha forte!")
        break

# 4 - Analisador de Números Pares/Ímpares
def number_analyzer() -> None:
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros.")

    print("\nResultado final:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

# Menu
def main() -> None:
    while True:
        print("Menu Principal")
        print("1 - Calculadora Simples")
        print("2 - Calculadora de Média de Notas")
        print("3 - Verificador de Força de Senha")
        print("4 - Analisador de Números Pares/Ímpares")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            simple_calculator()
        elif opcao == "2":
            average_grade_calculator()
        elif opcao == "3":
            password_checker()
        elif opcao == "4":
            number_analyzer()
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
