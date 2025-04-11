def kryej_transaksione(komanda, llogari, tipi_seances, llogarite):
    emri = llogari['emri'].strip()[:20].ljust(20)

    if komanda == "withdrawal":
        shuma = float(input("Shuma për tërheqje: "))
        if tipi_seances == "standard" and shuma > 500.00:
            print("Maksimumi për tërheqje në seancë standarde është 500.00")
            return None
        nr_llogarie = input("Numri i llogarisë: ").zfill(5)
        shuma_formatuar = f"{shuma:08.2f}"
        return f"01 {emri}{nr_llogarie} {shuma_formatuar}  ".ljust(40)

    elif komanda == "transfer":
        nr_prej = input("Llogaria prej (nr): ").zfill(5)
        nr_tek = input("Llogaria tek (nr): ").zfill(5)
        shuma = float(input("Shuma për transfer: "))
        if tipi_seances == "standard" and shuma > 1000.00:
            print("Maksimumi për transfer në seancë standarde është 1000.00")
            return None
        shuma_formatuar = f"{shuma:08.2f}"
        return f"02 {emri}{nr_prej} {shuma_formatuar} {nr_tek}".ljust(40)

    elif komanda == "deposit":
        shuma = float(input("Shuma për depozitë: "))
        nr_llogarie = input("Numri i llogarisë: ").zfill(5)
        shuma_formatuar = f"{shuma:08.2f}"
        return f"04 {emri}{nr_llogarie} {shuma_formatuar}  ".ljust(40)

    elif komanda == "paybill":
        kompania = input("Kompania (EC, CQ, FI): ").upper()
        if kompania not in ["EC", "CQ", "FI"]:
            print("Kompania e papranueshme.")
            return None
        shuma = float(input("Shuma për pagesë: "))
        if tipi_seances == "standard" and shuma > 2000.00:
            print("Maksimumi për pagesë në seancë standarde është 2000.00")
            return None
        nr_llogarie = input("Numri i llogarisë: ").zfill(5)
        shuma_formatuar = f"{shuma:08.2f}"
        return f"03 {emri}{nr_llogarie} {shuma_formatuar} {kompania}".ljust(40)

    elif komanda == "create":
        if tipi_seances != "admin":
            print("Vetëm admin mund të krijojë llogari të re.")
            return None
        emri_ri = input("Emri i llogarisë së re: ").strip()[:20].ljust(20)
        nr_llogarie = input("Numri i ri i llogarisë: ").zfill(5)
        shuma = float(input("Shuma fillestare: "))
        if shuma > 99999.99:
            print("Shuma maksimale për llogari të re është 99999.99")
            return None
        shuma_formatuar = f"{shuma:08.2f}"
        return f"05 {emri_ri}{nr_llogarie} {shuma_formatuar}  ".ljust(40)

    elif komanda == "delete":
        if tipi_seances != "admin":
            print("Vetëm admin mund të fshijë llogari.")
            return None
        emri = input("Emri i llogarisë për fshirje: ").strip()[:20].ljust(20)
        nr_llogarie = input("Numri i llogarisë: ").zfill(5)
        return f"06 {emri}{nr_llogarie} 00000000  ".ljust(40)

    elif komanda == "disable":
        if tipi_seances != "admin":
            print("Vetëm admin mund të deaktivizojë llogari.")
            return None
        emri = input("Emri i llogarisë për deaktivizim: ").strip()[:20].ljust(20)
        nr_llogarie = input("Numri i llogarisë: ").zfill(5)
        return f"07 {emri}{nr_llogarie} 00000000  ".ljust(40)

    elif komanda == "changeplan":
        if tipi_seances != "admin":
            print("Vetëm admin mund të ndryshojë planin.")
            return None
        emri = input("Emri i llogarisë: ").strip()[:20].ljust(20)
        nr_llogarie = input("Numri i llogarisë: ").zfill(5)
        return f"08 {emri}{nr_llogarie} 00000000 NP".ljust(40)

    else:
        print("Komanda nuk është e implementuar ende.")
        return None
