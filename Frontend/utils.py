def lexo_llogarite_prej_fajllit(path="data/current_accounts.txt"):
    llogarite = {}
    try:
        with open(path, "r") as f:
            for rreshti in f:
                if "END_OF_FILE" in rreshti:
                    break
                nr = rreshti[0:5]
                emri = rreshti[6:26].strip()
                statusi = rreshti[27]
                balanca = float(rreshti[29:37])
                llogarite[nr] = {
                    "emri": emri,
                    "statusi": statusi,
                    "balanca": balanca
                }
    except FileNotFoundError:
        print("Fajlli current_accounts.txt nuk u gjet!")
    return llogarite
