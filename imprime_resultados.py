from busca_nome import ExtratorDeNome
from busca_email import ExtratorDeEmail
from busca_telefone import ExtratorDeContatos
from busca_cpf import ExtratorDeCPF
from busca_data import ExtratorDeData


class ImprimeResultados:
    def __init__(self, banco_csv="database.csv") -> None:
        self.banco_csv = banco_csv

    def imprime_resultados(self):
        print("\n")
        ExtratorDeNome(self.banco_csv).executar()

        print("\n")
        ExtratorDeEmail(self.banco_csv).executar()

        print("\n")
        extrator_contato = ExtratorDeContatos(self.banco_csv)
        extrator_contato.procura_telefone()
        print("\n")
        extrator_contato.procura_celular()

        print("\n")
        ExtratorDeCPF(self.banco_csv).executar()

        print("\n")
        ExtratorDeData(self.banco_csv).executar()
