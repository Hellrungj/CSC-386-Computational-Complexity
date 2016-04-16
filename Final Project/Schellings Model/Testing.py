# ------------------------------------------------------------------------------------------------------------
# Purpose: Contains tests for Shelling Model Class
#
# Author: Ben Quesada
# -------------------------------------------------------------------------------------------------------------
import sys
from board_class import*
from shelling_model import Shellings_Model


def testit(did_pass):
    """ Print the result of a test. """

    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_series1():
    '''
    series of tests that are run on definitions with returns other than None.
    :return: None
    '''
    matrix = Shellings_Model()
    g = matrix.create_pos()
    B1 = Board(matrix.width+1,matrix.height+1,g)
    B1.create_board()
    testmatrix = [['red', 'blue', 'red'],['red', 'white', 'blue'],['blue', 'red', 'blue']]
    testit(matrix.turn(testmatrix,B1)==[['red', 'red', 'blue'],['red', 'blue', 'blue'],['red', 'white', 'blue']])
    print(matrix.moved_list)

def main():
    test_series1()

main()
