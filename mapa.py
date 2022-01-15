import os
import readchar
import random


def main():

    POS_X = 0
    POS_Y = 1
    MAP_WIDTH = 20
    MAP_HEIGHT = 15

    my_position = [3, 1]
    # map_objects = [[2, 3], [5, 4], [3, 4], [10, 6]]
    map_objects = []
    n_objects = 10
    obj=[]

    # creatring objects
    for num in range(n_objects):
        obj=[random.randint(0,MAP_WIDTH), random.randint(0,MAP_HEIGHT)]
        map_objects.append(obj)

    while True:
        # draw map

        print("+"+"-"*MAP_WIDTH*3+"+")

        for coordinate_y in range(MAP_HEIGHT):

            print("|", end="")

            for coordinate_x in range(MAP_WIDTH):

                char_to_draw = " "
                object_in_cell = None

                for map_object in map_objects:

                    if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                       char_to_draw = "*"
                       object_in_cell = map_object

                if my_position [POS_X] == coordinate_x and my_position [POS_Y] == coordinate_y:
                    # draw player
                    char_to_draw = "@"

                    # delete object
                    if object_in_cell:
                        map_objects.remove(object_in_cell)

                print(" {} ".format(char_to_draw), end="")

            print("|")
        print("+"+"-"*MAP_WIDTH*3+"+")

        print("\nPresione [q] para salir. ")

        # Ask user shere he wants to move
        # direction = input("¿Donde te quieres mover? [WSAD] > ")
        # direction = readchar.readchar().decode() en windows
        direction = readchar.readchar()

        if direction == "w":
            my_position[POS_Y] -= 1
        elif direction == "s":
            my_position[POS_Y] += 1
        elif direction == "a":
            my_position[POS_X] -= 1
        elif direction == "d":
            my_position[POS_X] += 1
        elif direction == "q":
            break

        """
        # this is other solution for the limits
        if direction == "w":
            my_position[POS_Y] -= 1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction == "s":
            my_position[POS_Y] += 1
            my_position[POS_Y] %= MAP_HEIGHT 
        elif direction == "a":
            my_position[POS_X] -= 1
            my_position[POS_X] %= MAP_WIDTH 
        elif direction == "d":
            my_position[POS_X] += 1
            my_position[POS_X] %= MAP_WIDTH 
        elif direction == "q":
            break
        """
        os.system("clear")

        # limits
        if my_position[POS_X] > MAP_WIDTH:
            my_position[POS_X] = 0
        elif my_position[POS_X] < 0:
            my_position[POS_X] = MAP_WIDTH
        elif my_position[POS_Y] > MAP_HEIGHT:
            my_position[POS_Y] = 0
        elif my_position[POS_Y] < 0:
            my_position[POS_Y] = MAP_HEIGHT


if __name__ == "__main__":
    main()
