import random

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
            print(ansikte, end="")
        print()

def skriv_ut_slumpkluster(bredd, hojd):
    for rad in range(hojd):
        for kolumn in range(bredd):
            print(slumpa_ansikte(), end=" ")
        print()


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

    print("Slumpat ansikte:", slumpa_ansikte())


def visa_slumpkluster():
    """
    Låter användaren skapa ett kluster med slumpade ansikten.
    """

    bredd = int(input("Bredd: "))
    hojd = int(input("Höjd: "))

    skriv_ut_slumpkluster(bredd, hojd)

# === HUVUDPROGRAM ===

def huvudprogram():
    """Huvudprogrammet som styr menyn och programflödet."""
    while True:
        print("\n--- ASCII-ANSIKTEN ---")
        print("1. Skapa eget ansikte")
        print("2. Skapa kluster (samma ansikte)")
        print("3. Slumpa ett ansikte")
        print("4. Slumpa kluster (blandade ansikten)")
        print("5. Avsluta")

        val = input("Välj: ")

        if val == "1":
            skapa_eget_ansikte()
        elif val == "2":
            skapa_kluster()
        elif val == "3":
            visa_slump_ansikte()
        elif val == "4":
            visa_slumpkluster()
        elif val == "5":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.")


# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def farglagg_ansikte(ansikte, farg_kod):
    """
    Lägger till ANSI-färgkoder runt ett ansikte.

    Parametrar:
        ansikte (str): Ansiktet som ska färgläggas
        farg_kod (str): ANSI-färgkod (t.ex. "\033[91m")

    Returnerar:
        str: Ansikte med färgkoder
    """
    # TODO: return farg_kod + ansikte + "\033[0m"
    pass


def spara_ansikte_till_json(ansikte, filnamn="sparade_ansikten.json"):
    """Sparar ett ansikte till en JSON-fil."""
    # TODO: Importera json
    # TODO: Ladda befintlig lista, lägg till nytt ansikte, spara
    pass


def ladda_ansikten_fran_json(filnamn="sparade_ansikten.json"):
    """Laddar sparade ansikten från en JSON-fil."""
    # TODO: Använd json.load() och returnera listan
    pass


# === TURTLE-UTMANING (FÖR DIG MED TURTLE) ===

def rita_ansikte_med_turtle(ogon, mun, ram):
    """
    EXTRA UTMANING: Ritar ett ansikte med Turtle-grafik istället för ASCII.
    Detta är för de som har tillgång till Turtle-biblioteket.
    """
    # TODO: Importera turtle
    # TODO: Skapa en turtle
    # TODO: Rita två cirklar som ögon
    # TODO: Rita en båge som mun
    # TODO: Rita en cirkel som huvud (ram)
    # TODO: turtle.done()
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()