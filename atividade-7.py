import csv
import os
import json

# 1 - Análise de Tempos de Execução
def analisar_tempos_execucao() -> None:
    try:
        tempos = []
        with open('./data/logs_treinamento.csv', 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor)
            for linha in leitor:
                modelo, tempo = linha
                tempos.append(int(tempo))

        if not tempos:
            print("Não foram encontrados dados no arquivo 'logs_treinamento.csv'.")
            return

        media = sum(tempos) / len(tempos)
        variancia = sum((x - media) ** 2 for x in tempos) / (len(tempos) - 1)
        desvio_padrao = variancia ** 0.5

        print("\n--- Análise de Tempos de Execução ---")
        print(f"Tempo médio: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio_padrao:.2f} segundos\n")
    except FileNotFoundError:
        print("Arquivo 'logs_treinamento.csv' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar dados: {e}")

# 2 - Escrita em CSV
def escrever_csv_pessoas() -> None:
    caminho = './data/pessoas.csv'
    arquivo_existe = os.path.exists(caminho)

    try:
        with open(caminho, 'a', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)

            if not arquivo_existe:
                escritor.writerow(['Nome', 'Idade', 'Cidade'])

            while True:
                nome = input("Digite o nome (ou 'sair' para encerrar): ").strip()
                if nome.lower() == 'sair':
                    print("Encerrando...")
                    break

                try:
                    idade = int(input("Digite a idade: ").strip())
                except ValueError:
                    print("Idade inválida. Digite um número inteiro.")
                    continue

                cidade = input("Digite a cidade: ").strip()
                escritor.writerow([nome, idade, cidade])
                print(f"{nome} foi adicionado ao arquivo.\n")
    except Exception as e:
        print(f"Erro ao escrever no arquivo CSV: {e}")

# 3 - Leitura de CSV
def ler_csv_pessoas() -> None:
    caminho = './data/pessoas.csv'
    if not os.path.exists(caminho):
        print("Arquivo 'pessoas.csv' não encontrado.")
        return

    try:
        print("\n--- Lista de Pessoas (CSV) ---")
        with open(caminho, 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for i, linha in enumerate(leitor):
                if i == 0:
                    print(f"| {linha[0]:<10} | {linha[1]:^5} | {linha[2]:<20} |")
                    print("-" * 45)
                else:
                    print(f"| {linha[0]:<10} | {linha[1]:^5} | {linha[2]:<20} |")
        print("-" * 45 + "\n")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# 4 - Leitura e Escrita em JSON
def gerenciar_json_pessoas() -> None:
    caminho = './data/dados.json'
    dados = []

    if os.path.exists(caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo_json:
                dados = json.load(arquivo_json)
        except Exception as e:
            print(f"Erro ao carregar JSON existente: {e}")

    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ").strip()
        if nome.lower() == 'sair':
            print("Encerrando entrada de dados...")
            break

        try:
            idade = int(input("Digite a idade: ").strip())
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")
            continue

        cidade = input("Digite a cidade: ").strip()
        dados.append({"nome": nome, "idade": idade, "cidade": cidade})

    try:
        with open(caminho, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados salvos em '{caminho}'.\n")
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")

    # Leitura dos dados salvos
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo_json:
            dados_lidos = json.load(arquivo_json)
            print("--- Dados Salvos (JSON) ---")
            for pessoa in dados_lidos:
                print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
            print()
    except Exception as e:
        print(f"Erro ao ler o JSON salvo: {e}")

# Menu
def main() -> None:
    while True:
        print("Menu Principal")
        print("1 - Analisar Tempos de Execução (CSV)")
        print("2 - Escrever Dados em CSV (Pessoas)")
        print("3 - Ler Dados do CSV (Pessoas)")
        print("4 - Gerenciar Dados em JSON (Pessoas)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            analisar_tempos_execucao()
        elif opcao == "2":
            escrever_csv_pessoas()
        elif opcao == "3":
            ler_csv_pessoas()
        elif opcao == "4":
            gerenciar_json_pessoas()
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
