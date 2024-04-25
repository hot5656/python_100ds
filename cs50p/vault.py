# operation overload
# vault.py
class Vault:
    def __init__(self, galleous=0, sickles=0, knuts=0):
        self.galleous = galleous
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleous} galleous, {self.sickles} sickles,{self.knuts} knuts"

    def __add__(self, other):
        galleous = self.galleous + other.galleous
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleous, sickles, knuts)

potter = Vault(100, 50,25)
print(potter)
ron = Vault(25, 50, 100)
print(ron)
total = potter + ron
print(total)
