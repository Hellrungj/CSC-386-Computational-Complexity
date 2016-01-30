# John Hellrung

# Items in the World 
#  Reds or Blues
#   - Happiness - The amount of oneselfs neighors in a 9x9 area around the item 
#  Neighbors (9x9) 
#   - Reds, Blues, and Blanks (White)
#
# Rules
#  Reds and Blues can only move to the closest home meeting the happiness requiment
#  Reds and Blues take turns moving to where they feel happiness 

#   8x8 Board   
#   |--------|
#   |        |
#   |        |
#   |        |
#   |        |
#   |        |
#   |        |
#   |        |
#   |        |
#   |        |
#   |--------|

import random

class Unpack():
    def __inti__(self,x,y):
        self.board = board()

class person():
    def __inti__(self,color = "", location = (0,0), happiness = 1):
        self.happiness = happiness
        self.Type = color
        self.person_location = location
        
class board():
    def __inti__(self, width = 5, length = 5):
        self.width = width
        self.length = length
        self.size = width * length
        
    def Size(self):
        return self.size
        
class Model():
    def __inti__(self, happiness = .50, reds = 0, blue = 0,width = 4,length= 4):
        self.agreed_happiness = happiness
        self.amount_reds = reds
        self.amount_blues = blue
        self.boardwidth = width
        self.boardlength = length
        self.boardsize = width * length

    def Set_Up_Persons(self):
        def Set_up_Names(color = ""):
            name_list = []
            if color == "reds":
                for i in range(self.amount_reds):
                    name_list.append("reds" + str(i))
            else:
                for i in range(self.amount_blues):
                    name_list.append("blues" + str(i))
            return name_list
            
        def check_x_y(x,y,xlist,ylist):
            for i in range(xlist):
                if i == x:
                    for i in range(ylist):
                        if i == y:
                            return False 
            return True
        
        #---------------------------------------
        newboard = board()
        redlist = Set_up_Names("reds")
        bluelist = Set_up_Names("blues")
        xlist = []
        ylist = []
        persons_list = []
        for i in range(self.amount_reds):
            x = random.choice(self.boardsize)
            y = random.choice(self.boardsize)
            result = check_x_y(x,y,xlist,ylist)
            if result == False:
                redlist[i] = person("red",x,y)
                xlist.append(x)
                ylist.append(y)
        persons_list.append(redlist)
            
        for i in range(self.amount_blues):
            x = random.choice(self.boardsize)
            y = random.choice(self.boardsize)
            result = check_x_y(x,y,xlist,ylist)
            if result == False:
                bluelist[i] = person("red",x,y)
                xlist.append(x)
                ylist.append(y)
        persons_list.append(bluelist)
        return persons_list 
            
def main():
    firsttest = Model(.50,11,7)
    firsttest.Set_Up_Persons()
main()








