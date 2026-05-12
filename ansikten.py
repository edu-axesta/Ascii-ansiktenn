import random
farger = {
    "1": "\033[91m",  # röd
    "2": "\033[92m",  # grön
    "3": "\033[93m",  # gul
    "4": "\033[94m",  # blå
    "5": "\033[95m",  # magenta
    "6": "\033[96m",  # cyan
    "7": "\033[0m"    # ingen färg
}
vald_farg = ""

farg_lista = [
    "\033[91m",  # röd
    "\033[92m",  # grön
    "\033[93m",  # gul
    "\033[94m",  # blå
    "\033[95m",  # magenta
    "\033[96m"   # cyan
]
def slumpa_farg():
    return random.choice(farg_lista)

def farglagg_ansikte(ansikte):
    return vald_farg + ansikte + "\033[0m"

# === FUNKTIONER FÖR ANSIKTEN ===

def skapa_ansikte(ogon, mun, ram):
    """
    Parametrar:
        ogon(str): Tecken för ögon (tex, "O", "o", "0", "-", "@", "¤", "*", "U", "u", "n", "T", "t", "^")
        mun(str): Tecken för mun (tex, "_", "-", "M", "w", "W", "v", "V", "U", "u", "~")
        ram(str): Tecken för ram (tex, "()", "{}", "[]", "ll")
    """
    return ram[0] + ogon + mun + ogon + ram[1]

def slumpa_ansikte():
    ogon_alternativ=["O", "o", "0", "-", "@", "¤", "*", "U", "u", "n", "T", "t", "^"]
    mun_alternativ=["_", "-", "M", "w", "W", "v", "V", "U", "u", "~"]
    ram_alternativ= ["()", "{}", "[]",]

    ogon= random.choice(ogon_alternativ)
    mun= random.choice(mun_alternativ)
    ram= random.choice(ram_alternativ)

    return skapa_ansikte(ogon, mun, ram)

# === FUNKTIONER FÖR KLUSTER ===

def skriv_ut_kluster(bredd, hojd, ansikte):
    for rad in range(hojd):
        for kolumn in range(bredd):
            print(farglagg_ansikte(ansikte), end="")
        print()

def skriv_ut_slumpkluster(bredd, hojd):
    for rad in range(hojd):
        rad_text = ""
        for kolumn in range(bredd):
            ansikte = slumpa_ansikte()
            farg = slumpa_farg()
            rad_text += farg + ansikte + "\033[0m" + " "
        print(rad_text)


# === MENYFUNKTIONER ===

# Listor för användarval (används i menyval 1)
ogon_alternativ = ["O", "o", "0", "-", "@", "¤", "*", "U", "u", "n", "T", "t", "^"]
mun_alternativ = ["_", "-", "M", "w", "W", "v", "V", "U", "u", "~"]
ram_alternativ = ["()", "{}", "[]"]

def skapa_eget_ansikte():
    """
    Låter användaren designa ett eget ansikte genom menyval.
    """

    print("\nVälj ögon:")
    for i in range(len(ogon_alternativ)):
        print(i + 1, "-", ogon_alternativ[i])

    val_ogon = int(input("Val: "))
    ogon = ogon_alternativ[val_ogon - 1]

    print("\nVälj mun:")
    for i in range(len(mun_alternativ)):
        print(i + 1, "-", mun_alternativ[i])

    val_mun = int(input("Val: "))
    mun = mun_alternativ[val_mun - 1]

    print("\nVälj ram:")
    for i in range(len(ram_alternativ)):
        print(i + 1, "-", ram_alternativ[i])

    val_ram = int(input("Val: "))
    ram = ram_alternativ[val_ram - 1]

    ansikte = skapa_ansikte(ogon, mun, ram)

    print("Ditt ansikte:", ansikte)

    return ansikte


def skapa_kluster():
    """
    Låter användaren skapa ett kluster med samma ansikte.
    """

    print("\n1. Skapa eget ansikte")
    print("2. Använd slumpat ansikte")

    val = input("Välj: ")

    if val == "1":
        ansikte = skapa_eget_ansikte()

    elif val == "2":
        ansikte = slumpa_ansikte()

    else:
        print("Ogiltigt val.")
        return

    bredd = int(input("Bredd: "))
    hojd = int(input("Höjd: "))

    skriv_ut_kluster(bredd, hojd, ansikte)


def visa_slump_ansikte():
    """Visar ett slumpmässigt ansikte."""

    print("Slumpat ansikte:", farglagg_ansikte(slumpa_ansikte()))


def visa_slumpkluster():
    """
    Låter användaren skapa ett kluster med slumpade ansikten.
    """

    bredd = int(input("Bredd: "))
    hojd = int(input("Höjd: "))

    skriv_ut_slumpkluster(bredd, hojd)

# === HUVUDPROGRAM ===

def valj_farg():
    global vald_farg

    print("\n--- VÄLJ FÄRG ---")
    print("1. Röd")
    print("2. Grön")
    print("3. Gul")
    print("4. Blå")
    print("5. Magenta")
    print("6. Cyan")
    print("7. Ingen färg")

    val = input("Välj färg: ")

    if val in farger:
        vald_farg = farger[val]
    else:
        print("Ogiltigt val, ingen färg används.")
        vald_farg = "\033[0m"


def huvudprogram():
    while True:
        print("\n--- ASCII-ANSIKTEN ---")
        print("0. Välj färg")   # 👈 NY
        print("1. Skapa eget ansikte")
        print("2. Skapa kluster (samma ansikte)")
        print("3. Slumpa ett ansikte")
        print("4. Slumpa kluster (blandade ansikten)")
        print("5. Avsluta")

        val = input("Välj: ")

        if val == "0":
            valj_farg()
        elif val == "1":
            skapa_eget_ansikte()
        elif val == "2":
            skapa_kluster()
        elif val == "3":
            print("Slumpat ansikte:", farglagg_ansikte(slumpa_ansikte()))
        elif val == "4":
            visa_slumpkluster()
        elif val == "5":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.")


# === EXTRA FUNKTIONER FÖR UTMANINGAR ===
huvudprogram()

# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()