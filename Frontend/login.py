def kyqu():
    tipi = input("Tipi i seancës (standard/admin): ").strip().lower()
    if tipi not in ["standard", "admin"]:
        print("Tip i pavlefshëm.")
        return None, None

    emri = ""
    if tipi == "standard":
        emri = input("Emri i llogarisë: ").strip()
    elif tipi == "admin":
        emri = "admin"

    print(f"U kyçët si {tipi}.")
    return tipi, {"emri": emri, "kyqur": True}


def ckyqu(llogari, transaksionet):
    print("Duke ruajtur transaksionet në fajll...")
    with open("data/transaction_log.txt", "w") as fajlli:
        for rreshti in transaksionet:
            fajlli.write(rreshti + "\n")
        fajlli.write("00 END_OF_SESSION        00000 00000000  \n")
    print(f"Llogaria e {llogari['emri']} u çkyç me sukses.")
