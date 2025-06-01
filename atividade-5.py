from datetime import date

# 1 - Calcular Idade em Dias
def calcula_idade_em_dias() -> None:
    try:
        ano_nascimento = int(input("Qual é seu ano de nascimento? "))
        data_atual = date.today()
        data_nascimento = date(ano_nascimento, 1, 1)
        diferenca = data_atual - data_nascimento
        print(f"Sua idade em dias: {diferenca.days}")
    except ValueError:
        print("Ano inválido. Digite um número inteiro válido.")

# 2 - Cálculo de Gorjeta
def calcula_gorjeta() -> None:
    try:
        valor = float(input("Qual o valor total da compra: "))
        percentual = float(input("Qual o % da gorjeta: "))
        gorjeta = valor * (percentual / 100)
        print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")

# 3 - Verificador de Palíndromo
def verifica_palindromo() -> None:
    texto = input("Digite uma palavra ou frase: ").lower()
    texto_limpo = ''.join(c for c in texto if c.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        print("É palíndromo!")
    else:
        print("Não é palíndromo.")

# Menu
def main() -> None:
    while True:
        print("Menu Principal")
        print("1 - Calcular Idade em Dias")
        print("2 - Calcular Gorjeta")
        print("3 - Verificar Palíndromo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            calcula_idade_em_dias()
        elif opcao == "2":
            calcula_gorjeta()
        elif opcao == "3":
            verifica_palindromo()
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
