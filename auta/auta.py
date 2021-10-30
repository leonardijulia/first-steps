# excercice for practicing function based programming (april 2020)

from turtle import *
from random import *


def graphic_init():
    mode("logo")
    speed(0)


def hop(y, x):
    up()
    fd(y)
    rt(90)
    fd(x)
    lt(90)
    down()


def rectangle(wid, height, col):
    color(col, col)
    begin_fill()
    for i in range(2):
        fd(height)
        rt(90)
        fd(wid)
        rt(90)
    end_fill()


def contour(wid, height):
    for i in range(2):
        fd(height)
        rt(90)
        fd(wid)
        rt(90)


def car_wheel(r):
    dot(2 * r, "black")
    dot(2 * ((3 * r) // 4), "silver")


def bus(wid, height, windows_no, col):

    # Bus parameters
    r = height // 10
    window_wid = (2 * wid) // (3 * windows_no + 1)
    spacing_windows = window_wid // 2
    window_height = (height - r) // 2
    verical_window_spacing = (height - r - window_height) // 2

    # main body
    hop(r, 0)
    rectangle(wid, height - r, col)

    # wheels
    hop(0, wid // 8)
    car_wheel(r)
    hop(0, 6 * wid // 8)
    car_wheel(r)

    # windows
    hop(0, -7 * wid // 8)  # wracam do lewego dolnego rogu karoserii
    hop(verical_window_spacing, 0)
    for i in range(windows_no):
        hop(0, spacing_windows)
        rectangle(window_wid, window_height, "silver")
        hop(0, window_wid)
    hop(-verical_window_spacing - r, -windows_no * (spacing_windows + window_wid))


def vehicles(lst):
    for vehicle in lst:
        bus(vehicle[0], vehicle[1], vehicle[2], vehicle[3])
        hop(0, vehicle[0] + 10)


def main():
    graphic_init()

    margin = 20
    hop(- window_height() // 2 + margin, - window_width() // 2 + margin)
    vehicles([[150, 100, 4, "red"], [100, 80, 2, "green"]])
    done()


main()
