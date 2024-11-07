class Kals:
    def __init__(self, nom, rang, yosh):
        self.nom = nom
        self.rang = rang
        self.yosh = yosh

    def malumot_berish(self):
        return f"Bu {self.nom}. Rang: {self.rang}, yosh: {self.yosh}."

    def yosh_tekshirish(self):
        if self.yosh >= 18:
            return f"{self.nom} katta."
        else:
            return f"{self.nom} hali kichik."

    def rangni_ozgartirish(self, yangi_rang):
        self.rang = yangi_rang
        return f"{self.nom}ning rangi endi {self.rang}."
