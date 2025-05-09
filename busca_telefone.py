from extrator_base import ExtratorBase
from collections import defaultdict
import re


class ExtratorDeContatos(ExtratorBase):
    def _processar_matches(self, matches):
        agrupado = defaultdict(list)
        for codigo_area, numero in matches:
            numero_completo = f"({codigo_area}) {numero}"
            agrupado[codigo_area].append(numero_completo)
        return [item for sublist in agrupado.values() for item in sublist]

    def _get_regex(self):
        return ""

    def _get_titulo(self):
        return ""

    def procura_telefone(self):
        regex_telefone = r"\((\d{2})\)\s(\d{4}-\d{4})"
        encontrados = re.findall(regex_telefone, self.banco)

        print("Telefones: \n")

        if encontrados:
            for telefone in self._processar_matches(encontrados):
                print(telefone)
        else:
            print("Não Encontrado\n")

    def procura_celular(self):
        regex_celular = r"\((\d{2})\)\s(\d{5}-\d{4})"
        encontrados = re.findall(regex_celular, self.banco)

        print("Celulares: \n")

        if encontrados:
            for celular in self._processar_matches(encontrados):
                print(celular)
        else:
            print("Não Encontrado\n")

    def executar(self):
        pass
