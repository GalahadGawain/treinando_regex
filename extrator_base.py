import re
from abc import ABC, abstractmethod


class ExtratorBase(ABC):
    def __init__(self, arquivo_csv) -> None:
        self.arquivo_csv = arquivo_csv
        self.banco = self._carregar_banco()

    def _carregar_banco(self) -> str:
        try:
            with open(self.arquivo_csv, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.arquivo_csv}' não foi encontrado.")
            exit()

    @abstractmethod
    def _processar_matches(self, matches) -> None:
        pass

    @abstractmethod
    def _get_regex(self) -> None:
        pass

    @abstractmethod
    def _get_titulo(self) -> None:
        pass

    def buscar_e_agrupar(self) -> None:
        regex = self._get_regex()
        encontrados = re.findall(regex, self.banco)

        print(f"{self._get_titulo()}:\n")

        if encontrados:
            resultados_processados = self._processar_matches(encontrados)
            for resultado in resultados_processados:
                print(resultado)
        else:
            print("Não Encontrado.\n")

    def executar(self) -> None:
        self.buscar_e_agrupar()
