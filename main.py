from program import Program




if __name__ == "__main__":
    program = Program()
    while True:
        volba = input("Vyberte možnost (1 - přidat pojištěného, 2 - výpis pojištěných, 3 - vyhledat pojištěného, 4 - konec programu): ")
        if volba == "1":
            program.pridat_pojisteneho()
        elif volba == "2":
            program.vypis_pojistenych()
        elif volba == "3":
            program.vyhledat_pojisteneho()
        elif volba == "4":
            break
        else:
            print("Neplatná volba.")