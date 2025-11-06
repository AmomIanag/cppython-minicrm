from datetime import date

class Lead:
    def __init__(self, name: str, company: str, email: str, stage: str = "novo", created=None):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = created or date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", ""),
            company=data.get("company", ""),
            email=data.get("email", ""),
            stage=data.get("stage", "novo"),
            created=data.get("created"),
        )
