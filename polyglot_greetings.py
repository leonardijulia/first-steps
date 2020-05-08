# Program pozdrawiający w obcych językach
# Autorka: Julia Leonardi

def tekstPowitania(kod_języka):
    if kod_języka == "it":
        return "Ciao!"  #włoski: Wiedza własna
    elif kod_języka == "en":
        return "Hello!" #angielski: Wiedza własna
    elif kod_języka == "swh":
        return "Habari!"   #suahili: https://www.17-minute-world-languages.com/pl/suahili/
    elif kod_języka == "jpn":
        return "こんにちは！" #japoński: Wiedza własna oraz http://www.rozmowki.slowka.pl/japonski_rozmowki.php
    elif kod_języka == "es":
        return "¡Hola!" #hiszpański: Wiedza własna oraz https://translate.google.pl/?hl=pl
    else:
        "Nie znam języka: " + "'" + kod_języka + "'" + ". Wpisz dokładny kod dostępnego języka."

def powitaj():
    print("Dostępne języki: \nit - włoski \nen - angielski \nswh - suahili \njpn - japoński \nes - hiszpański")
    kod = input("Podaj wybrany język: ")
    print(tekstPowitania(kod))

powitaj()
