from imprime_resultados import ImprimeResultados
import sys


def main() -> None:
    if len(sys.argv) > 1:
        arquivo_csv = sys.argv[1]
        print(f"Processando arquivo: {arquivo_csv}")
    else:
        arquivo_csv = "database.csv"
        print("Usando arquivo padrão database.csv")

    try:
        impressor = ImprimeResultados(arquivo_csv)
        impressor.imprime_resultados()
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
