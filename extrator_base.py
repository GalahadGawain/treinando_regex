import re
from abc import ABC, abstractmethod

class ExtratorBase(ABC):
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.banco = self._carregar_banco()
    
    def _carregar_banco(self):
        try:
            with open(self.arquivo_csv, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.arquivo_csv}' não foi encontrado.")
            exit()
    
    @abstractmethod
    def _processar_matches(self, matches):
        pass
    
    @abstractmethod
    def _get_regex(self):
        pass
    
    @abstractmethod
    def _get_titulo(self):
        pass
    
    def buscar_e_agrupar(self):
        regex = self._get_regex()
        encontrados = re.findall(regex, self.banco)
        
        print(f"{self._get_titulo()}:\n")
        
        if encontrados:
            resultados_processados = self._processar_matches(encontrados)
            for resultado in resultados_processados:
                print(resultado)
        else:
            print("Não Encontrado.\n")
    
    def executar(self):
        self.buscar_e_agrupar()