import re
from extrator_base import ExtratorBase


class ExtratorDeCPF(ExtratorBase):

    def _processar_matches(self, matches):
        cpfs_unicos = {}
        for cpf in matches:
            somente_numeros = re.sub(r"\D", "", cpf)
            if len(somente_numeros) == 11:
                cpfs_unicos[somente_numeros] = somente_numeros

        resultados = []
        for cpf_num in sorted(cpfs_unicos.values()):
            cpf_formatado = f"{cpf_num[:3]}.{cpf_num[3:6]}.{cpf_num[6:9]}-{cpf_num[9:]}"
            resultados.append(cpf_formatado)
        return resultados

    def _get_regex(self):
        return r"\d{3}[.-]?\d{3}[.-]?\d{3}[.-]?\d{2}"

    def _get_titulo(self):
        return "CPFs"

    def procurar_cpf(self):
        self.executar()
