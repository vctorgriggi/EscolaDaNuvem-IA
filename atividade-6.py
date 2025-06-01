import random
import string
import requests

# 1 - Gerador de Senha Aleatória
def gerar_senha() -> None:
    try:
        tamanho = int(input("Digite a quantidade de caracteres da senha: "))
        if tamanho <= 0:
            print("Tamanho inválido. Digite um valor positivo.")
            return

        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print(f"Senha gerada: {senha}")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# 2 - Gerador de Perfil Aleatório (API Random User)
def gerar_usuario() -> None:
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            usuario = dados["results"][0]
            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario["email"]
            pais = usuario["location"]["country"]

            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"País: {pais}")
        else:
            print("Erro ao obter os dados da API.")
    except requests.RequestException:
        print("Erro de conexão. Verifique sua internet.")

# 3 - Consulta de Endereço por CEP (API ViaCEP)
def consultar_cep() -> None:
    cep = input("Digite um CEP para consulta: ").strip().replace("-", "")
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Deve conter 8 dígitos numéricos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" in dados:
                print("CEP não encontrado. Tente novamente.")
            else:
                print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
                print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
                print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
                print(f"Estado: {dados.get('uf', 'Não disponível')}")
        else:
            print("Erro ao acessar a API.")
    except requests.RequestException:
        print("Erro de conexão. Verifique sua internet.")

# 4 - Consulta de Cotação de Moeda (API AwesomeAPI)
def consultar_cotacao() -> None:
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            chave_moeda = f"{moeda}BRL"

            if chave_moeda in dados:
                cotacao = dados[chave_moeda]
                print(f"Moeda: {cotacao['name']}")
                print(f"Valor atual: R$ {cotacao['bid']}")
                print(f"Valor máximo: R$ {cotacao['high']}")
                print(f"Valor mínimo: R$ {cotacao['low']}")
                print(f"Última atualização: {cotacao['create_date']}")
            else:
                print("Código da moeda inválido. Tente novamente.")
        else:
            print("Erro ao acessar a API.")
    except requests.RequestException:
        print("Erro de conexão. Verifique sua internet.")

# Menu
def main() -> None:
    while True:
        print("Menu Principal")
        print("1 - Gerar Senha Aleatória")
        print("2 - Gerar Perfil Aleatório")
        print("3 - Consultar Endereço por CEP")
        print("4 - Consultar Cotação de Moeda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            gerar_senha()
        elif opcao == "2":
            gerar_usuario()
        elif opcao == "3":
            consultar_cep()
        elif opcao == "4":
            consultar_cotacao()
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
