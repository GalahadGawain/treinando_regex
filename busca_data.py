from extrator_base import ExtratorBase


class ExtratorDeData(ExtratorBase):
    def _processar_matches(self, matches) -> list:
        datas_unicas = {}
        for dia, mes, ano in matches:
            data_numerica = f"{dia.zfill(2)}{mes.zfill(2)}{ano}"
            datas_unicas[data_numerica] = (dia.zfill(2), mes.zfill(2), ano)

        resultados = []
        for data in sorted(datas_unicas.values(), key=lambda d: f"{d[2]}{d[1]}{d[0]}"):
            resultados.append(f"{data[0]}/{data[1]}/{data[2]}")
        return resultados

    def _get_regex(self) -> None:
        return r"\b(\d{2})[\/\-. ]?(\d{2})[\/\-. ]?(\d{4})\b"

    def _get_titulo(self) -> None:
        return "Datas de Nascimento"

    def procurar_data(self) -> None:
        self.executar()
