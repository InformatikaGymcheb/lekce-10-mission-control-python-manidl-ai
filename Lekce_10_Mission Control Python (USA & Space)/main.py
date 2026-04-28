def vypocet_vahy(vaha_na_zemi, teleso="mesic"):
    if vaha_na_zemi < 0:
        return 0

    if teleso == "mesic":
        return vaha_na_zemi * 0.165
    elif teleso == "mars":
        return vaha_na_zemi * 0.38
    else:
        return 0


def simulator_pristani():
    vyska = 100
    rychlost = 10
    palivo = 50
    gravitace = 2

    print("\n--- ZAČÍNÁ PŘISTÁVACÍ MANÉVR ---")

    while vyska > 0:
        print(f"Výška: {vyska}m | Rychlost: {rychlost}m/s | Palivo: {palivo}j")

        zazeh = int(input("Zadej sílu zážehu (0–10): "))

        if zazeh < 0:
            zazeh = 0
        if zazeh > 10:
            zazeh = 10

        if zazeh > palivo:
            zazeh = palivo

        palivo -= zazeh

        rychlost = rychlost + gravitace - zazeh
        vyska = vyska - rychlost

        print("-" * 20)

    print(f"\nDopadová rychlost: {rychlost} m/s")

    if rychlost < 5:
        print("Výsledek mise: Úspěšné přistání!")
    else:
        print("Výsledek mise: Havárie!")


moje_vaha = 80
print(f"Moje váha na Měsíci: {vypocet_vahy(moje_vaha, 'mesic')} kg")

simulator_pristani()
