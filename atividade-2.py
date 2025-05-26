# 1 - Conversor de Moeda
def currency_converter() -> None:
    try:
        value_brl = float(input("Insira o valor em reais (R$): "))
        usd_rate = 5.20
        eur_rate = 6.15

        value_usd = value_brl / usd_rate
        value_eur = value_brl / eur_rate

        print(f"Valor em dólares: ${value_usd:.2f}")
        print(f"Valor em euros: €{value_eur:.2f}")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

# 2 - Calculadora de Desconto
def discount_calculator() -> None:
    try:
        product_name = input("Insira o nome do produto: ")
        original_price = float(input("Insira o preço original (R$): "))
        discount_input = input("Insira a porcentagem de desconto (ex: 10%): ")

        discount_percent = float(discount_input.replace("%", "").strip())
        discount_value = original_price * (discount_percent / 100)
        final_price = original_price - discount_value

        print(f"\nProduto: {product_name}")
        print(f"Preço original: R$ {original_price:.2f}")
        print(f"Desconto aplicado ({discount_percent:.2f}%): R$ {discount_value:.2f}")
        print(f"Preço final: R$ {final_price:.2f}")
    except ValueError:
        print("Entrada inválida. Verifique os valores e tente novamente.")

# 3 - Calculadora de Média Escolar
def grade_average() -> None:
    grades = [7.5, 8.0, 6.5]
    average = sum(grades) / len(grades)

    for i, grade in enumerate(grades, start=1):
        print(f"Nota {i}: {grade:.2f}")
    print(f"Média final: {average:.2f}")

# 4 - Calculadora de Consumo de Combustível
def fuel_efficiency_calculator() -> None:
    distance_km = 300
    fuel_liters = 25
    consumption = distance_km / fuel_liters

    print(f"Distância percorrida: {distance_km:.2f} km")
    print(f"Combustível gasto: {fuel_liters:.2f} litros")
    print(f"Consumo médio: {consumption:.2f} km/l")

#
def main() -> None:
    while True:
        print("Menu Principal")
        print("1 - Conversor de Moeda")
        print("2 - Calculadora de Desconto")
        print("3 - Calculadora de Média Escolar")
        print("4 - Calculadora de Consumo de Combustível")
        print("0 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            currency_converter()
        elif choice == "2":
            discount_calculator()
        elif choice == "3":
            grade_average()
        elif choice == "4":
            fuel_efficiency_calculator()
        elif choice == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()