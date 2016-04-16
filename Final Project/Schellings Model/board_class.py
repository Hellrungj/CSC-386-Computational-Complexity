# -------------------------------------------------------------------------------
# Your Name: John Hellrung
# File Name: Board.py
# Purpose: To handle the turtle part of the assignment
#
#
#
#
# Author: John Hellrung & Shadia Prater
#
# Acknowledgements:
# Shadia Prater
# http://michael0x2a.com/blog/turtle-examples

#
# Attribution-Noncommercial-Share Alike 3.0 United States License.
# -------------------------------------------------------------------------------
import turtle

class Board:
    def __init__(self, width=3, height=3, input_list=([["red","blue","white"],["white","red","blue"],["white","red","blue"]]), size=500):
        self.x = width
        self.y = height
        self.size = size
        self.x_length = size/width
        self.y_length = size/height
        self.agent = turtle.Turtle()
        self.startpos_x = -size/2
        self.startpos_y = size/2
        self.agentlist = input_list
        self.screen = turtle.Screen()

    def create_board(self):
        def pen(object, ang=0):
            object.agent.penup()
            object.agent.setpos((object.startpos_x, object.startpos_y))
            object.agent.pendown()
            object.agent.right(ang)

        def com_row(object, LorW, length, d=1):
            for i in range(LorW - 1): # draws the columns
                object.agent.forward(length)
                object.agent.right(90)
                if d == 2:
                    object.agent.backward(object.size)
                    object.agent.left(90)
                    object.agent.left(90)
                    object.agent.backward(object.size)
                else:
                    object.agent.forward(object.size)
                    object.agent.left(90)
                    object.agent.left(90)
                    object.agent.forward(object.size)
                object.agent.right(90)
        self.agent.speed(0)
        self.agent.pensize(5)
        pen(self)
        for i in range(4):
            self.agent.forward(self.size)
            self.agent.right(90)
        com_row(self, self.x, self.x_length)
        pen(self, 90)
        com_row(self, self.y, self.y_length, 2)

    def agents(self):
        self.agent.tracer()
        self.agent.color("red")
        self.agent.penup()
        self.agent.setpos((self.startpos_x + (self.x_length/2), self.startpos_y - (self.y_length/2)))
        self.agent.setheading(0)
        self.agent.pensize(150/self.x)
        for y in range(self.y):
            for i in range(self.x):
                self.agent.color(self.agentlist[y][i])
                self.agent.dot()
                self.agent.forward(self.x_length)
            self.agent.backward(self.x_length * self.x)
            self.agent.right(90)
            self.agent.forward(self.x_length)
            self.agent.left(90)
        self.agent._update()


 # Test Function
"""
def main():
    ans = raw_input("What height do want the board to be.")
    ans1 = raw_input("What length do want the board to be.")
    if ans == '1' and ans1 == '1':
        board1 = Board(int(ans),int(ans1),[["red"]])
    elif ans == '2' and ans1 == '2':
        board1 = Board(int(ans),int(ans1),[["red","white"],])
    elif ans == "4" and ans1 == "4":
        board1 = Board(int(ans),int(ans1),[["red","blue","white","blue"],["white","blue","red","blue"],["white","red","white","blue"],["red","red","blue","white"]])
    else:
        board1 = Board()
    board1.create_board()
    board1.agents()

main()
"""