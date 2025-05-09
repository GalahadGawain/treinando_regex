from extrator_base import ExtratorBase
import re


class ExtratorDeNome(ExtratorBase):
    def _processar_matches(self, matches) -> list:
        nomes_completos = []
        for linha in matches:
            nome_completo = linha.strip().split(",")[0]
            nomes_completos.append(nome_completo.strip())

        nomes_unicos = []
        visto = set()
        for nome in nomes_completos:
            if nome not in visto:
                visto.add(nome)
                nomes_unicos.append(nome)

        return sorted(nomes_unicos)

    def _get_regex(self) -> None:
        return r"^([A-Za-zÀ-ÿ]+)(?:\s([A-Za-zÀ-ÿ]+))+"

    def _get_titulo(self) -> None:
        return "Nomes completos"

    def buscar_e_agrupar(self) -> None:
        regex = self._get_regex()
        linhas = self.banco.split("\n")[1:]
        encontrados = []

        for linha in linhas:
            if not linha.strip():
                continue
            if re.match(regex, linha):
                encontrados.append(linha)

        print(f"{self._get_titulo()}:\n")

        if encontrados:
            nomes_processados = self._processar_matches(encontrados)
            for nome in nomes_processados:
                print(nome)
        else:
            print("Nenhum nome encontrado.\n")

    def procurar_nome(self) -> None:
        self.buscar_e_agrupar()
