"""Program rysuje spiżarnię z zapasami słoików, czekolad i kawiarek
Autorka: Julia Leonardi
"""

from turtle import *
from random import *
from math import *


def inicjuj_grafikę():
    """"Funkcja inicjuje grafikę żółwia"""

    mode("logo")
    speed(0)


def hop(y, x):
    """Funkcja przenosi żółwia o określoną liczbę 'y' w kierunku ustawienia żółwia i o 'x' w kierunku prostopadłym"""

    up()
    fd(y)
    rt(90)
    fd(x)
    lt(90)
    down()


def prostokąt(wysokość, szerokość, kolor_ramka, kolor_wypełnienie):
    """Funkcja rysuje prostokąty o zadanych bokach oraz kolorach ramki i wypełnienia"""

    color(kolor_ramka, kolor_wypełnienie)
    begin_fill()
    for i in range(2):
        fd(wysokość)
        rt(90)
        fd(szerokość)
        rt(90)
    end_fill()


def trapez_równoramienny(a, b, wysokość, kolor):
    """Funkcja rysuje trapezy równoramienne o zadanej dolnej (a) i górnej (b) podstawie oraz wysokości i kolorze
    wypełnienia (z czarnym konturem)"""

    color("black", kolor)
    połowa_różnicy_podstaw = abs(1/2 * (a - b))
    bok = sqrt(połowa_różnicy_podstaw**2 + wysokość**2)
    begin_fill()

    #trapez o dłuższej dolnej podstawie:
    if a > b:
        kąt = degrees(atan(wysokość / połowa_różnicy_podstaw))
        rt(90 - kąt)
        fd(bok)
        rt(kąt)
        fd(b)
        rt(kąt)
        fd(bok)
        rt(180 - kąt)
        fd(a)
        rt(90)

    #trapez o dłuższej górnej podstawie:
    else:
        """Rysuje trapez o krótszej dolnej podstawie"""
        kąt = degrees(atan(połowa_różnicy_podstaw / wysokość))
        kąt2 = 90 - kąt
        lt(kąt)
        fd(bok)
        rt(180 - kąt2)
        fd(b)
        rt(180 - kąt2)
        fd(bok)
        rt(90 - kąt)
        fd(a)
        rt(90)
    end_fill()


def piwnica(x, y, wysokość, szerokość):
    """Funkcja rysuje piwnicę w zadanym miejscu, o zadanej szerokości i wysokości"""

    up()
    goto(x, y)
    down()
    prostokąt(wysokość, szerokość, "LavenderBlush2", "LavenderBlush2")


def regał(wysokość, szerokość, ile_półek, kolor):
    """Funkcja rysuje jeden regał o zadanej wysokości, szerokości, ilości półek oraz kolorze"""

    wysokość_półki = wysokość / ile_półek
    width(10)
    color(kolor, kolor)
    begin_fill()

    #boki regału:
    fd(wysokość)
    hop(-wysokość, szerokość)
    fd(wysokość)
    hop(-wysokość, -szerokość)

    #półki regału:
    hop(0.5 * wysokość_półki, 0)
    for i in range(ile_półek):
        width(10)
        color(kolor, kolor)
        begin_fill()

        rt(90)
        fd(szerokość)
        lt(90)
        hop(5, -szerokość + 5)

        #wypełnianie zapasami:
        if i == ile_półek - 1: #wypełnianie ostatniej półki zapasów
            zapasy(szerokość - 10, 0.5 * wysokość_półki)
        else: #wypełnianie reszty półek
            zapasy(szerokość - 10, wysokość_półki)
        hop(wysokość_półki - 5, -szerokość + 5)

    #powrót do lewego, dolnego rogu regału
    hop(-0.5 * wysokość_półki, 0)
    hop(-wysokość, 0)
    width(1)


def regały(ile_regałów, szerokość_wszystkich, wysokość):
    """Funkcja rysuje wiele regałów"""

    szer_regal = szerokość_wszystkich // ile_regałów - 10 #uwzględnienie grubości kreski rysującej regały (stąd -10)
    for i in range(ile_regałów):
        regał(wysokość, szer_regal, randrange(3, 6), choice(["tomato3", "turquoise3", "VioletRed3", "wheat4", "teal",
                                                             "tan2", "SteelBlue3", "SkyBlue1", "SeaGreen3", "salmon", "red",
                                                             "PowderBlue", "plum4", "pink3", "PaleVioletRed4",
                                                             "PeachPuff4", "LightSlateGray"]))
        hop(0, szer_regal + 10)
    hop(0, -szerokość_wszystkich)


def zapasy(szerokość_półki, wysokość_półki):
    """Funkcja rysuje losowo wybrane obiekty w ciągu na półce"""

    pozostała_szerokość = szerokość_półki
    while pozostała_szerokość > 0:

        width(1)
        wysokość_obiektu = randrange(int(wysokość_półki) // 2 - 10, int(wysokość_półki) - 10)
        kolor_obiektu = choice(["tomato3", "turquoise3", "VioletRed3", "wheat4", "teal", "tan2", "SteelBlue3",
                                "SkyBlue1", "SeaGreen3", "salmon", "red", "PowderBlue", "plum4", "pink3",
                                "PaleVioletRed4", "PeachPuff4", "LightSlateGray"])
        lista_obiekt = [słoik, kawiarka, czekolada]

        if szerokość_półki // 8  < pozostała_szerokość < szerokość_półki // 3: #w przypadku, gdy dostępnego miejsca
            # jest mniej niż maksymalna szerokość obieku; zapobiega 'uciekaniu' obiektów poza regał
            szerokość_obiektu = pozostała_szerokość
            choice(lista_obiekt)(wysokość_obiektu, szerokość_obiektu, kolor_obiektu)

        else:
            szerokość_obiektu = randrange(szerokość_półki // 8, szerokość_półki // 3)
            if 0 <= (pozostała_szerokość - szerokość_obiektu) <= szerokość_półki // 8:
                szerokość_obiektu = pozostała_szerokość
                choice(lista_obiekt)(wysokość_obiektu, szerokość_obiektu, kolor_obiektu)
                hop(0, szerokość_obiektu)
                break
            elif pozostała_szerokość - szerokość_obiektu > szerokość_półki // 8:
                choice(lista_obiekt)(wysokość_obiektu, szerokość_obiektu, kolor_obiektu)

        hop(0, szerokość_obiektu)
        pozostała_szerokość -= szerokość_obiektu



def słoik(wysokość, szerokość, kolor):
    """Funkcja rysuje słoiki"""

    wysokość_słoika = 6/7 * wysokość
    wysokość_pokrywki = 1/7 * wysokość
    wysokość_zawartości = 9 / 10 * wysokość_słoika
    wysokość_etykiety = 1/2 * wysokość_słoika
    szerokość_etykiety = 1/2 * szerokość
    szerokość_pokrywki = 4/5 * szerokość

    #słoik z zawartością
    prostokąt(wysokość_zawartości, szerokość, kolor, kolor)
    prostokąt(wysokość_słoika, szerokość, "black", "")

    #etykieta
    hop(1/2 * wysokość_etykiety, 1/2 * szerokość_etykiety)
    prostokąt(wysokość_etykiety, szerokość_etykiety, "orange", "orange")
    hop(-1/2 * wysokość_etykiety, -1/2 * szerokość_etykiety)

    #pokrywka
    hop(wysokość_słoika, 1/2 * (szerokość - szerokość_pokrywki))
    prostokąt(wysokość_pokrywki, szerokość_pokrywki, "azure3", "azure3")
    hop(-wysokość_słoika, -1/2 * (szerokość - szerokość_pokrywki))


def kawiarka(wysokość, szerokość, kolor):
    "Funkcja rysuje kawiarkę, o zadanej wysokości, szerokości i kolorze (z czarną ramką)"

    grubość_rączki = 2
    a = 0.9 * szerokość
    b = 0.5 * a
    połowa_różnicy_podstaw = 0.5 * b
    miejsce_rączki = 0.1 * szerokość
    wysokość_części = 4.5/12 * wysokość
    wysokość_pokrywki = 2/12 * wysokość
    wysokość_uchwytu = 1/12 * wysokość
    a_uchwytu = 0.1 * a
    b_uchwytu = 0.2 * a

    #Część dolna kawiarki
    hop(0, miejsce_rączki)
    trapez_równoramienny(a, b, wysokość_części, kolor)
    hop(wysokość_części, połowa_różnicy_podstaw)

    #Górna część kawiarki
    trapez_równoramienny(b, a, wysokość_części, kolor)
    hop(wysokość_części, -połowa_różnicy_podstaw)

    #Pokrywka z uchwytem
    trapez_równoramienny(a, b, wysokość_pokrywki, kolor)
    hop(wysokość_pokrywki, 0.4 * szerokość)
    trapez_równoramienny(a_uchwytu, b_uchwytu, wysokość_uchwytu, "black")
    hop(- wysokość_pokrywki, - 0.4 * szerokość)

    #Rączka do kawiarki
    width(grubość_rączki)
    color("black", "black")
    lt(90)
    fd(miejsce_rączki)
    lt(90)
    fd(wysokość_części)
    hop(wysokość_części, 0)
    rt(180)
    width(1)


def czekolada(wysokość, szerokość, kolor_opakowania):
    """Funkcja rysuje otwarte od góry tabliczki czekolady"""

    #czekolada
    prostokąt(wysokość, szerokość, "black", "chocolate4")

    #opaokwanie
    prostokąt(4/5 * wysokość, szerokość, "black", kolor_opakowania)

    #opakowanie od wewnątrz
    color("black", "white")
    begin_fill()
    hop(4/5 * wysokość, 0)
    rt(100)
    po_skosie = szerokość / cos((10 * pi)/ 180)
    y = sqrt(-szerokość**2 + po_skosie**2)
    fd(po_skosie)
    lt(100)
    fd(y)
    lt(90)
    fd(szerokość)
    rt(90)
    end_fill()
    hop(-4/5*wysokość, 0)


def spiżarnia(x, y, wysokość, szerokość):
    """Funkcja rysuje całą spiżarnię w zadanym miejscu o zadanych wymiarach"""

    piwnica(x, y, wysokość, szerokość)
    regały(randrange(szerokość // 150, szerokość // 100), szerokość, wysokość)


def main():

    inicjuj_grafikę()
    spiżarnia(-328, -200, 400, 650)
    done()


main()
