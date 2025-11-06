from pathlib import Path
import json
import csv
from lead import Lead

class LeadRepository:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load(self):
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads_data):
        self.db_path.write_text(json.dumps(leads_data, ensure_ascii=False, indent=2), encoding="utf-8")

    def get_all(self):
        return [Lead.from_dict(d) for d in self._load()]

    def add(self, lead: Lead):
        leads_data = self._load()
        leads_data.append(lead.to_dict())
        self._save(leads_data)

    def export_csv(self, path=None):
        path = Path(path) if path else (self.data_dir / "leads.csv")
        leads = self._load()
        try:
            with path.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["name", "company", "email", "stage", "created"])
                w.writeheader()
                for row in leads:
                    w.writerow(row)
            return path
        except PermissionError:
            return None
