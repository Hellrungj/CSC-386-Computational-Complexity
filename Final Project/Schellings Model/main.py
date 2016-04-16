# ------------------------------------------------------------------------------------------------------------
# Purpose: This is the driver program that imports Board and Shelling Model class and generates the program
#
# Authors: Team Awesome Lemmings
# Contributors: Ishwar Agarwal, William Mosier, Haleigh George, Ben Quesada, John Hellrung
# Date Created:
# Acknowledgements: Ishwar Agarwal, William Mosier, John Hellrung
# -------------------------------------------------------------------------------------------------------------
from shelling_model import *
from board_class import *

def ask_input(messasge):
    ans = 0
    while True:
        try:
            ans = int(raw_input(messasge))
        except:
            print ('Please enter integers')
            continue
        break

    return ans

def ask_percentage(messasge):
    ans = 0
    while True:
        try:
            ans = int(raw_input(messasge))
            if ans < 0 or ans > 100:
                raise
        except:
            print ('Please enter a value between 0-100')
            continue

        break

    return ans


def main():

    ans = ask_input('What size board do you want?(integers)')
    ans2 = ask_percentage('What percentage of the board should be occupied?')
    ans3 = ask_percentage('What percentage of the population should be discriminated?')
    ans4 = ask_percentage('What is the percentage of happiness threshold?')

    matrix = Shellings_Model(ans,ans,int(ans2)/100.0,int(ans3)/100.0,int(ans4)/100.0)
    g = matrix.create_pos()
    B1 = Board(matrix.width+1,matrix.height+1,g)
    B1.create_board()
    n = matrix.turn(g, B1)
    print(matrix.moved_list)
    B1.screen.exitonclick()

main()