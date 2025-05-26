# 1 - Classificador de Idade
def age_classifier() -> None:
    try:
        age = int(input("Insira sua idade: "))
        if age < 0:
            print("Insira uma idade válida (não negativa).")
        elif age <= 12:
            print("Você é classificado como uma criança.")
        elif age <= 17:
            print("Você é classificado como um adolescente.")
        elif age <= 59:
            print("Você é classificado como um adulto.")
        else:
            print("Você é classificado como idoso.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro para a idade.")

# 2 - Calculadora de IMC
def imc_calculator() -> None:
    try:
        weight = float(input("Digite seu peso (kg): "))
        height = float(input("Digite sua altura (m): "))
        imc = weight / (height ** 2)

        if imc < 18.5:
            classification = "Abaixo do peso"
        elif imc < 25:
            classification = "Peso normal"
        elif imc < 30:
            classification = "Sobrepeso"
        else:
            classification = "Obeso"

        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classification}")
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números corretamente.")

# 3 - Conversor de Temperatura
def temperature_converter() -> None:
    try:
        temperature = float(input("Insira a temperatura: "))
    except ValueError:
        print("Entrada inválida! Digite um número para a temperatura.")
        return

    origin = input("Unidade de origem (Celsius, Fahrenheit, Kelvin): ").strip().title()
    target = input("Unidade de destino (Celsius, Fahrenheit, Kelvin): ").strip().title()

    valid_units = {"Celsius", "Fahrenheit", "Kelvin"}
    if origin not in valid_units or target not in valid_units:
        print("Unidade inválida. Escolha entre Celsius, Fahrenheit e Kelvin.")
        return

    if origin == target:
        result = temperature
    elif origin == "Celsius":
        result = (temperature * 9 / 5 + 32) if target == "Fahrenheit" else temperature + 273.15
    elif origin == "Fahrenheit":
        result = (temperature - 32) * 5 / 9 if target == "Celsius" else ((temperature - 32) * 5 / 9) + 273.15
    elif origin == "Kelvin":
        result = temperature - 273.15 if target == "Celsius" else (temperature - 273.15) * 9 / 5 + 32

    print(f"\nA temperatura convertida é: {result:.2f} {target}")

# 4 - Verificador de Ano Bissexto
def leap_year_checker() -> None:
    try:
        year = int(input("Digite um ano: "))
    except ValueError:
        print("Entrada inválida! Digite um número inteiro para o ano.")
        return

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} é um ano bissexto.")
    else:
        print(f"{year} não é um ano bissexto.")

#
def main() -> None:
    while True:
        print("Menu Principal")
        print("1 - Classificador de Idade")
        print("2 - Calculadora de IMC")
        print("3 - Conversor de Temperatura")
        print("4 - Verificador de Ano Bissexto")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            age_classifier()
        elif option == "2":
            imc_calculator()
        elif option == "3":
            temperature_converter()
        elif option == "4":
            leap_year_checker()
        elif option == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()