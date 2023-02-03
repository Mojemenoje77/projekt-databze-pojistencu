from pojisteny import Pojisteny

class Pojistovna:
    def __init__(self):
        self.seznam_pojistenych = []
    
    def pridat_pojisteneho(self, pojisteny: Pojisteny):
        self.seznam_pojistenych.append(pojisteny)
        
    def vypis_pojistenych(self):
        for pojisteny in self.seznam_pojistenych:
            print(pojisteny)
            
    def vyhledat_pojisteneho(self, jmeno: str, prijmeni: str):
        for pojisteny in self.seznam_pojistenych:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None