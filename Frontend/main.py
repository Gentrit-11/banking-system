from login import kyqu, ckyqu
from transactions import kryej_transaksione
from utils import lexo_llogarite_prej_fajllit


def fillo_sistemin():
    print("Mirë se vini në sistemin bankar")
    llogari = None
    tipi_seances = None
    transaksionet = []
    llogarite = {}

    while True:
        komanda = input("Shtyp komandën: ").strip().lower()

        if komanda == "login":
            if llogari:
                print("Jeni tashmë të kyçur. Fillimisht bëni logout.")
                continue
            tipi_seances, llogari = kyqu()
            llogarite = lexo_llogarite_prej_fajllit()

        elif komanda == "logout":
            if not llogari:
                print("Nuk jeni të kyçur.")
                continue
            ckyqu(llogari, transaksionet)
            llogari = None
            tipi_seances = None
            transaksionet = []

        elif komanda in ["withdrawal", "transfer", "paybill", "deposit", "create", "delete", "disable", "changeplan"]:
            if not llogari:
                print("Duhet të bëni login fillimisht.")
                continue
            transaksioni = kryej_transaksione(komanda, llogari, tipi_seances, llogarite)
            if transaksioni:
                transaksionet.append(transaksioni)

        elif komanda == "dal":
            print("Duke dalë nga sistemi...")
            break

        else:
            print("Komandë e panjohur.")

if __name__ == "__main__":
    fillo_sistemin()
