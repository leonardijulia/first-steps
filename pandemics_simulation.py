"""
    -- EN
    This program simulates the spreading of a virus in a population. It is possible to set the number of individuals in
    the populations, the base amount of individuals infected, the amount of individuals that are "social distancing"
    (i.e. not moving around), the duration of an infection, the size of the individuals and the discrete time of
    the simulation.

    --PL
    Program wykonuje symulacje rozprzestrzeniania się wirusa w populacji. Możliwe jest łatwe ustawienie liczby
    osobników w populacji, początkowej liczby zakażonych, liczby osób dystansujących się społecznie, czas chorowania,
    rozmiar osobników i liczba kolejek symulacji.

    Autor: Julia Leonardi
"""

from turtle import *
from random import *
from math import *

# const
margx = 20
left_marg = -window_width() // 2 + margx
width_margx = window_width() // 2 - margx
right_marg = width_margx
margy = 20
size_mess = 40
bottom_marg = -window_height() // 2 + margy
upper_marg = window_height() // 2 - (margy + size_mess)


def graphic_init():
    """
    EN: The function initializes the turtle graphic and sets the speed of the drawing
    PL: Funkcja inicjuje grafikę żółwia logo i ustawia szybkość rysunku
    """

    mode("logo")
    speed(0)


def plane(margx, margy, size_mess):
    """
    EN: The function draws the plane, on which the simulation will take place
    PL: Funkcja rysuje planszę, na której będzie wykonywana symulacja
    """
    # const
    height = window_height() - (2 * margy + size_mess)
    width = window_width() - 2 * margx

    up()
    goto(left_marg, bottom_marg)
    down()
    color("bisque", "bisque")
    begin_fill()
    for i in range(2):
        fd(height)
        rt(90)
        fd(width)
        rt(90)
    end_fill()


def individuals(characteristics_lst):
    """
    EN: The function draws the individuals defined by the characteristics of the individuals
    PL:Funkcja rysuje osoby zadane listą list cech poszczególnych osób
    """

    assert len(characteristics_lst) == 9
    state, pos_x, pos_y, size = characteristics_lst[:4]
    up()
    goto(pos_x, pos_y)
    down()
    dot(size, color_state(state))


def overlap_detection(chos_x, chos_y, characteristics_lst):
    """
    EN: The functio iterates through the characteristics list and detects, if the coordinatex from the list are
    overlapping with the chosen values x and y.
    PL:Funkcja przechodzi przez listę cech i wykrywa, czy współrzędne z listy cech się nakładają z wylosowanymi
    wartościami x i y
    """

    is_overlap = False
    if sqrt((characteristics_lst[1] - chos_x) ** 2 + (characteristics_lst[2] - chos_y) ** 2) < characteristics_lst[3]:
        is_overlap = True

    return is_overlap


def location_change(characteristics_lst):
    """
    EN: This function changes the x and y coordinates, such that won't overlap with other individuals
    PL: Funkcja zmienia współrzędne x i y na takie, które nie są w obrębie innego obiektu
    """

    size = characteristics_lst[3]
    diff = 2 * size
    max_x = (right_marg - size // 2) - diff
    max_y = (right_marg - size // 2) - diff
    marg_x = randrange(left_marg + size // 2, max_x)
    if marg_x >= characteristics_lst[1] - size:
        marg_x += diff
    marg_y = randrange(bottom_marg + size // 2, max_y)
    if marg_y >= characteristics_lst[2] - size:
        marg_y += diff

    return marg_x, marg_y


def collision_detection(individual1, individual2):
    """
    EN: The function detects the collision of two individuals and negates both individuals's speed components
    (if they are in motion).
    PL: Funkcja wykrywa zderzenie dwuch obiektów i neguje obie składowe prędkości obu zderzających się (i
    poruszających się) obiektów.
    """

    distance = (individual1[1] - individual2[1]) ** 2 + (individual1[2] - individual2[2]) ** 2
    if distance <= (individual2[3]) ** 2:
        infection(individual1, individual2)
        individuals = [individual1, individual2]
        for ind in individuals:
            if ind[4] != 0 and ind[5] != 0:
                ind[4] *= -1
                ind[5] *= -1

    return individual1, individual2


def ind_lst(ind_no, infected_no, social_dist_no, size, inf_time):
    """
    EN: The function generates a list of individuals according to the passed parameters.
    PL: Funkcja generuje listę obiektów o zadanej liczbie obiektów, obietów zakażonych, obiektów nieruchomych,
    o danym rozmiarze i czasie chorowania.
    """

    lst = []
    for i in range(ind_no):
        selected_x = randrange(left_marg + size // 2, right_marg - size // 2)  # randomly selecting the x coord
        selected_y = randrange(bottom_marg + size // 2, upper_marg - size // 2)  # randomly selecting the y coord
        select_x_speed, select_y_speed = choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), \
        choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])  # randomly selecting the speed components (different than 0)

        if len(lst) == 0:  # adding the first element to the list
            lst.append(["notInfected", selected_x, selected_y, size, select_x_speed, select_y_speed,
                        abs(select_x_speed), abs(select_y_speed), inf_time])
        else:  # checking if the next element will be overlapping with other elements.
            again = True
            while again:
                for ind in lst:
                    if overlap_detection(selected_x, selected_y, ind):
                        selected_x, selected_y = location_change(ind)
                        break
                else:
                    again = False  # it's not overlapping - exits the while loop
            else:
                lst.append(["notInfected", selected_x, selected_y, size, select_x_speed, select_y_speed,
                            abs(select_x_speed), abs(select_y_speed), inf_time])
    for i in range(infected_no):  # modifies the list of individuals by adding the infected folks
        lst[i][0] = "infected"

    for j in range(social_dist_no):  # the social distancig folks are not infected at the beginning of the simulation
        lst[len(lst) - (1 + j)][4:8] = 0, 0, 0, 0

    return lst


def drawing_ind(ind_lst):
    """
    EN: This function draws all the individuals from the list
    PL: Funkcja rysuje wszystkich ludzi podanych w liście
    """

    for ind in ind_lst:
        individuals(ind)


def color_state(state):
    """
    EN: This function changes the color of the individuals, according to their state
    PL: Funkcja zmienia kolor kulki w zależności od jej stanu"""

    col = ""
    if state == "notInfected":
        col = "yellow"
    elif state == "infected":
        col = "red"
    elif state == "convalescent":
        col = "green"
    return col


def infection(ind1, ind2):
    """
    EN: The function checks whether an infection had occured
    PL: Funkcja sprawdza czy nie doszło do zarażenia.
    """

    if ind1[0] == "infected" and ind2[0] == "notInfected":
        ind2[0] = "infected"
    if ind2[0] == "infected" and ind1[0] == "notInfected":
        ind1[0] = "infected"


def convalesceting(individual):
    """
    EN: The function checks wheather the infected individual feels good again and changes its state.
    PL: Funkcja sprawdza czy zarażona osoba już wyzdrowiała i zmienia jej stan.
    """

    if individual[0] == "infected":
        individual[8] -= 1

    if individual[0] == "infected" and individual[8] == 0:
        individual[0] = "convalescent"


def message(notInfected, infected, convalescent, socialDist):
    """
    EN: The function writes the statistics of the population.
    PL: Funkcja wypisuje statystyki populacji.
    """

    color("black", "black")
    begin_fill()
    up()
    goto(left_marg + 5, upper_marg + 10)
    write(f"Not infected = {notInfected}; Infected = {infected}; Convalescent = {convalescent}; Social Distancing = "
          f"{socialDist}%", False, "left", ('Calibri', 14, 'bold'))
    end_fill()


def horizontal_movement(characteristics_lst, time_discrete):
    """
    EN: The functions moves the individual horizontally.
    PL: Funkcja wykonuje ruch w poziomie dla zadanej listą cech osoby.
    """

    for i in range(time_discrete):
        if characteristics_lst[4] > 0:
            characteristics_lst[1] += 1
            if characteristics_lst[1] == right_marg - (characteristics_lst[3] // 2 - 1):
                characteristics_lst[4] *= -1
        elif characteristics_lst[4] < 0:
            characteristics_lst[1] -= 1
            if characteristics_lst[1] == left_marg + (characteristics_lst[3] // 2 - 1):
                characteristics_lst[4] *= -1
        elif characteristics_lst[4] == 0:
            pass
    return characteristics_lst


def vertical_movement(characteristics_lst, time_discrete):
    """
    EN: The functions moves the individual horizontally.
    PL: Funkcja wykonuje ruch w pionie dla zadanej listą cech jednej osoby.
    """

    for i in range(time_discrete):
        if characteristics_lst[5] > 0:
            characteristics_lst[2] += 1
            if characteristics_lst[2] == upper_marg - (characteristics_lst[3] // 2 - 1):
                characteristics_lst[5] *= -1
        elif characteristics_lst[5] < 0:
            characteristics_lst[2] -= 1
            if characteristics_lst[2] == bottom_marg + (characteristics_lst[3] // 2 - 1):
                characteristics_lst[5] *= -1
        elif characteristics_lst[5] == 0:
            pass
    return characteristics_lst


def infected_convalescent_count(individuals_lst):
    """
    EN: Function that counts the infected and immune to the virus.
    PL: Funkcja liczy osoby zakażone i uodpornione.
    """

    infected = 0
    convalescent = 0
    for ind in individuals_lst:
        if ind[0] == "infected":
            infected += 1
        if ind[0] == "convalescent":
            convalescent += 1
    return infected, convalescent


def simulation(infection_time, size_of_population, infected_no, distancing_no, discrete_time, ind_size):
    """
    EN: Function that simulates the whole pandemics for a given time (discrete). It generates an individual list
    for the given parameters: individuals number, base number of infected, number of immobile individuals, size of
    individuals and the infection time (discrete).
    PL: Główna funkcja programu wykonująca symulacje dla zadanej liczby kolejek. Generuje listę obiektów dla zadanych
    parametrów: liczba obiektów, liczba obiektów początkowo zakażonych, liczba obiektów nieruchomych i rozmiar
    obiektów oraz czas chorowania."""

    world = ind_lst(size_of_population, infected_no, distancing_no, ind_size, infection_time)

    for i in range(discrete_time):
        clear()
        plane(margx, margy, size_mess)
        drawing_ind(world)
        for j in range(len(world)):
            for i in range(len(world)):
                if i != j:
                    collision_detection(world[j], world[i])
            if world[j][6] == 0:
                for i in range(len(world)):
                    if i != j:
                        if (world[j][1] - world[i][1]) ** 2 + (world[j][2] - world[i][2]) ** 2 <= world[j][3] ** 2:
                            world[j][4] *= -1
                            horizontal_movement(world[j], 1)
                else:
                    horizontal_movement(world[j], 1)
                world[j][6] = abs(world[j][4])
            else:
                world[j][6] -= 1

            if world[j][7] == 0:
                for i in range(len(world)):
                    if i != j:
                        if (world[j][1] - world[i][1]) ** 2 + (world[j][2] - world[i][2]) ** 2 <= world[j][3] ** 2:
                            world[j][5] *= -1
                            vertical_movement(world[j], 1)
                else:
                    vertical_movement(world[j], 1)
                world[j][7] = abs(world[j][5])
            else:
                world[j][7] -= 1

            convalesceting(world[j])

        infected, convalescent = infected_convalescent_count(world)
        message(size_of_population - (infected + convalescent), infected, convalescent, round(distancing_no /
                                                                                              size_of_population * 100, 2))
        update()


def main():
    graphic_init()
    tracer(0, 0)
    hideturtle()
    simulation(4320, 25, 5, 5, 12960, 15)
    done()


main()
