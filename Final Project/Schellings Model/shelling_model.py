# ------------------------------------------------------------------------------------------------------------
# Purpose: Contains the Shelling_model class that does all the simulation to make agents hahppy
#
# Authors: Ishwar Agarwal, William Mosier
# Acknowledgements: Ben Quesada debugged turn() method, Team Awesome Lemmings debugged similarity_cal()
# John Hellrung for board_class
#
# -------------------------------------------------------------------------------------------------------------
import random

class Shellings_Model:
    """
    This class creates a random matrix of red, blue, white(none) agents and
    makes each agent happy for a given happiness threshold.
    """

    def __init__(self, width=3, height=3, occupation=0.8, discrimination=0.5, contentedness=0.5):
        '''
        initializer method aka Constructor
        :param width:
        :param height:
        :param occupation:
        :param discrimination:
        :param contentedness:
        :return:
        '''
        self.width = width-1
        self.height = height-1
        self.occupation = occupation
        self.discrimination = discrimination
        self.contentedness = contentedness
        self.white = int((width*height)*(1-self.occupation))
        self.blue = int(((width*height)-self.white)*self.discrimination)
        self.red = int(((width*height)-self.blue-self.white))
        self.move_counter = 0    # to keep track of total agents moved
        self.moved_list = [] # A list of the moved agents

    def create_pos(self):
        '''
        Creates a matrix of given width and height
        and randomly places given number of 'red', 'blue' and 'white' agents in the matrix
        :return:
        '''
        color_list = []
        matrix = []

        # creates a random colored list using the given amount of red, blue and white
        for i in range(self.red):
            color_list.append('red')
        for i in range(self.blue):
            color_list.append('blue')
        for i in range(self.white):
            color_list.append('white')

        # starts creating matrix
        for x in range(self.width + 1):
            temp_list = []
            for y in range(self.height + 1):
                random.shuffle(color_list)
                p = color_list.pop()
                temp_list.append(p)
            matrix.append(temp_list)
        return matrix

    def similar_cal(self, pos, color, list):
        '''
        Calculates the similarity for an agent by checking all the possible agents around the current agent
        Similarity being the ratio of agents of the given color to the not given color
        '''
        count_red = 0               # counter to count red agents around the current agent
        count_blue = 0              # counter to count blue agents around the current agent
        similarity = 0

        x = pos[0] -1               # selects the agent to the top left corner of the current agent
        while x <= pos[0] + 1:
            y = pos[1] - 1
            while y <= pos[1] + 1:
                if x >= 0 and x <= self.width and y>= 0 and y<= self.height:  # checks if agent exists at this position
                    if list [x][y] == 'red':
                        count_red += 1
                    elif list [x][y] == 'blue':
                        count_blue += 1
                y += 1
            x += 1
        # counting all agent around the current agent ends

        # numerical calculation for similarity if the agent is red
        if color == 'red':
            if list[pos[0]][pos[1]] == 'red':

                try:
                    similarity = (count_red-1)/float(count_blue + count_red-1)
                except:
                    similarity = 0
            else:
                try:
                    similarity = count_red/float(count_blue + count_red)
                except:
                    similarity = 0

        # numerical calculation for similarity if the agent is blue
        if color == 'blue':
            if list[pos[0]][pos[1]] == 'blue':
                try:
                    similarity = (count_blue-1)/float(count_red + count_blue-1)
                except:
                    similarity = 0
            else:
                try:
                    similarity = count_blue/float(count_red + count_blue)
                except:
                    similarity = 0

        return similarity

    def check_move(self, pos1, pos2, list):
        """
        :param pos1: position of the first agent
        :param pos2:  position of the second agent
        :param list:  list of all position of agents
        :return: True or False, if the given agent can move to another given position in the matrix
        """
        color = list[pos1[0]][pos1[1]]
        happiness1 = self.similar_cal(pos1, color, list)    # calculate happiness at current position
        happiness2 = self.similar_cal(pos2, color, list)    # calculates happiness at new position

        if happiness1 < self.contentedness and happiness2 >= self.contentedness:  # checks with happiness threshold
            if happiness1 < happiness2:
                return True
            else:
                return False
        else:
            return False

    def move_distance_cal(self, pos1, pos2):
        '''
        Calculates the distance between two positions
        '''
        distance = ((pos2[1]-pos1[1])**2 + (pos2[0]-pos1[0])**2)**0.5   # uses the mathematical distance formula
        return distance

    def search_new_pos(self, pos, list):
        '''
        Searches all the possible new positions and works with check_move.
        And outputs a list containing the possible new positions.
        '''
        possible_pos = []
        x = 0
        while x <= self.width:
            y = 0
            while y <= self.height:
                if list[x][y] == 'white':
                    if self.check_move(pos, [x,y], list):
                        possible_pos.append([x,y])
                y += 1
            x += 1

        return possible_pos

    def new_pos(self, pos, list):
        '''
        calls search new position to find all possible positions and
        uses distance_cal to output the best position to swap with
        '''
        best_pos = pos
        possible_pos = self.search_new_pos(pos, list)
        best_dis = ((self.height-1)**2 + (self.width-1)**2)**0.5  # sets worst distance initially
        for i in possible_pos:
            temp_dis = self.move_distance_cal(pos, i)
            if temp_dis <= best_dis:
                best_pos = i
        return best_pos

    def turn(self,matrix,class_object,t=0):
        '''
        This turn function goes to every agent in the matrix once and finds a possible new position for it
        If new position is not available it keeps it there.
        '''

        pos_x = 0
        pos_y = 0
        for i in matrix:
            for agent in i:
                class_object.agents()
                if agent != 'white': # skips if agent is 'white' that is no agent is present
                    if self.similar_cal([pos_x, pos_y], agent, matrix) == self.contentedness:
                        pass
                    elif self.similar_cal([pos_x, pos_y], agent, matrix) < self.contentedness:
                        new_pos = self.new_pos([pos_x, pos_y], matrix)

                        color1 = matrix [pos_x][pos_y]              # get the color of unhappy agent
                        color2 = matrix[new_pos[0]][new_pos[1]]     # get the replaceable position's color
                        if color1 == color2:                        # checks to see if the color is the same
                            pass                                    # passes equal colors to insure no false positives
                        else:
                            # Replaces the colors
                            matrix[pos_x][pos_y] = color2
                            matrix[new_pos[0]][new_pos[1]] = color1
                            self.move_counter += 1
                            self.moved_list.append("(" + str(pos_x) + ',' + str(pos_y) + "),(" + str(new_pos[0]) + "," + str(new_pos[1]) + "),(" + str(color1) + "),(" + str(color2) + ")" )
                pos_y += 1
            pos_x +=1
            pos_y = 0

        # Calls Agent method from Board Class
        class_object.agent.setpos(class_object.startpos_x, class_object.startpos_y)
        class_object.agent.color("Green")
        # Prints Segregation Level and Agents Moved on Screen
        class_object.agent.write("Segregation Level = " + str(int(self.segregation_level(matrix)))+ "%    Agents Moved = " + str(self.move_counter),False,"Left",("Arial",20,"normal"))
        # Reiterates the turn method
        if t == 2:
            pass
        elif self.segregation_level(matrix) < self.contentedness:
            t += 1
            self.turn(matrix,class_object,t)
        class_object.agent.setpos(class_object.startpos_x-class_object.startpos_x,class_object.startpos_y-class_object.startpos_y)
        class_object.agent.color("Green")
        # Prints Maximum Happiness Attained on Screen
        class_object.agent.write("Maximum Happiness Attained!",False,"Center",("Arial",20,"normal"))
        return matrix

    def segregation_level(self, matrix):
        '''
        Calculates the segregation level by averaging the similarity of all the agents in the matrix
        '''
        total_similarity = 0
        pos_x = 0
        for i in matrix:
            pos_y = 0
            for agent in i:
                if agent != 'white':  # skips if agent is 'white' that is no agent is present
                    total_similarity += self.similar_cal([pos_x, pos_y], agent, matrix)  # totals the similarity
                pos_y += 1
            pos_x += 1

        seg_level = (total_similarity/(self.red+self.blue)*100)  # calculates the average similarity
        return seg_level
