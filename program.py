from pojisteny import Pojisteny
from pojistovna import Pojistovna


class Program:
    def __init__(self):
        self.pojistovna = Pojistovna()
        
    def pridat_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")
        vek = input("Zadejte věk pojištěného: ")
        telefon = input("Zadejte telefon pojištěného: ")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojistovna.pridat_pojisteneho(pojisteny)
        
    def vypis_pojistenych(self):
        self.pojistovna.vypis_pojistenych()
        
    def vyhledat_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěného, kterého chcete vyhledat: ")
        prijmeni = input("Zadejte příjmení pojištěného, kterého chcete vyhledat: ")
        pojisteny = self.pojistovna.vyhledat_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print(pojisteny)
        else:
            print(f"Pojištěný s jménem {jmeno} {prijmeni} nebyl nalezen.")