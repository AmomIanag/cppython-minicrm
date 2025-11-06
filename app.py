from lead import Lead
from repository import LeadRepository

class CRMApp:
    def __init__(self):
        self.repo = LeadRepository()

    def add_lead(self):
        name = input("Nome: ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()

        if not name or not email or "@" not in email:
            print("⚠ Nome e e-mail válido são obrigatórios.")
            return

        lead = Lead(name, company, email)
        self.repo.add(lead)
        print("✔ Lead adicionado!")

    def list_leads(self):
        leads = self.repo.get_all()
        if not leads:
            print("Nenhum lead ainda.")
            return

        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, lead in enumerate(leads):
            print(f"{i:02d}| {lead.name:<20} | {lead.company:<17} | {lead.email:<21}")

    def search_leads(self):
        query = input("Buscar por: ").strip().lower()
        if not query:
            print("Consulta vazia.")
            return

        leads = self.repo.get_all()
        results = [
            (i, lead)
            for i, lead in enumerate(leads)
            if query in f"{lead.name} {lead.company} {lead.email}".lower()
        ]

        if not results:
            print("Nada encontrado.")
            return

        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, lead in results:
            print(f"{i:02d}| {lead.name:<20} | {lead.company:<17} | {lead.email:<21}")

    def export_leads(self):
        path = self.repo.export_csv()
        if path is None:
            print("⚠ Não consegui escrever o CSV. Feche o arquivo se estiver aberto e tente novamente.")
        else:
            print(f"✔ Exportado para: {path}")

    def print_menu(self):
        print("\nMini CRM de Leads — Versão POO")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/empresa/e-mail)")
        print("[4] Exportar CSV")
        print("[0] Sair")

    def run(self):
        while True:
            self.print_menu()
            op = input("Escolha: ").strip()
            if op == "1":
                self.add_lead()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_leads()
            elif op == "4":
                self.export_leads()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    CRMApp().run()
