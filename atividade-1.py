# 1 - Programa de Saudação
def greet() -> None:
    print("Hello, World!")

# 2 - Calculadora de Soma
def sum_calculator() -> None:
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        result = num1 + num2
        print(f"A soma de {num1} e {num2} é igual a {result}")
    except ValueError:
        print("Por favor, insira números válidos.")

# 3 - Calculadora de Volume
def volume_calculator() -> None:
    print("Cálculo do volume do paralelepípedo:")
    try:
        base = float(input("Base (em metros): "))
        height = float(input("Altura (em metros): "))
        width = float(input("Largura (em metros): "))
        volume = base * height * width
        print(f"O volume é {volume:.2f} m³")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# 4 - Calculadora de Preço Total
def total_price_calculator() -> None:
    try:
        quantity = int(input("Quantidade de itens: "))
        unit_price = float(input("Preço unitário (R$): "))
        total = quantity * unit_price
        print(f"O preço total é R$ {total:.2f}")
    except ValueError:
        print("Por favor, insira valores válidos.")

#
def main() -> None:
    while True:
        print("\nMenu Principal")
        print("1 - Programa de Saudação")
        print("2 - Calculadora de Soma")
        print("3 - Calculadora de Volume")
        print("4 - Calculadora de Preço Total")
        print("0 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            greet()
        elif choice == "2":
            sum_calculator()
        elif choice == "3":
            volume_calculator()
        elif choice == "4":
            total_price_calculator()
        elif choice == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()