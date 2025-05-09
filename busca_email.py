from extrator_base import ExtratorBase
import re


class ExtratorDeEmail(ExtratorBase):
    def _processar_matches(self, matches):
        emails_unicos = {}
        for email in matches:
            email_lower = email.lower()
            if email_lower not in emails_unicos:
                emails_unicos[email_lower] = email
        return sorted(emails_unicos.values())

    def _get_regex(self):
        return r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    def _get_titulo(self):
        return "E-mails encontrados"

    def procurar_email(self):
        self.executar()
