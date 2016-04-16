from Graphy import *
from GraphyWorld import *
import math
import random
import copy

class Test_2_OPT():
    def __init__(self,Textfile='tsp-small.txt', Rounds = 1, ):
        '''
        :param Textfile: A string for a Textfile
        :param Rounds: Number of Rounds Desired
        '''
        self.Cities_Dis = [] # Empty List Of Pos
        self.TotalDis = 0 # Empty Total Dis
        self.RoundLenght = Rounds # The amount of times of the algorithm run on a tour
        self.ListOC = self.VertexDisList(Textfile) # A list of coordinates from the file
        self.StartingTour = self.RandomListOfCites() # A list of greedy coordinates
        self.DictOfVertex = {Vertex(i):self.ListOC[i] for i in range(len(self.ListOC))} # A Dictionary of coordinates from the file
        self.ListOfVertex = self.cover_coordTOvertexs() # A list of Vertices
        self.ListOfEdges = self.make_edges() # A list of Edges

    def file_writeread(self,filename,task, CorList=[]):
        '''
        :param filename: Takes in a string to be used as a filename
        :param task: a char and that tell the method read or write
        :param CorList: a list of item that is to writen in the file
        Read or Write to a file or return 0 if the the task is not 'w' or 'r'
        :return: A list, None, or 0
        '''
        if task == "r":
            textfile = open(filename, "r")
            oldlines = textfile.readlines()
            lines = []
            for i in oldlines:
                lines.append(i.split('\n')[0] + " |")
            textfile.close()
            return lines
        elif task == "w":
            textfile = open(filename, "w")
            for i in CorList:
                textfile.write(i)
            textfile.close()
        else:
            print("Error!")
            return 0

    def VertexDisList(self, Textfile):
        '''
        :param Textfile: Takes in a string to be used as a filename
        Read the file based on the filename and then appends the second and third number after line 5 until it see EOF
        :return: A list of coordinates
        '''
        lines = self.file_writeread(Textfile,'r')
        Index = 6
        EOF = False
        VertexDisList = []
        while EOF == False:
            spaces = 0
            VertexDis = []
            NumberList = []
            index = 0
            # print("NewLine ---------------------------")
            for i in lines[Index]:
                # print("T " + str(Index-6) + " I " + str(i) + " IN " + str(index) + " S " + str(spaces) + " L " + str(NumberList) + " VL " + str(VertexDis) + " FVL " + str(VertexDisList))
                if i == ' ':
                    if spaces > 0:
                        Number = "".join(str(i) for i in NumberList)
                        NumberList = []
                        VertexDis.append(int(Number))
                    else:
                        spaces += 1
                else:
                    if spaces > 0:
                        NumberList.append(i)
                index += 1
                if i == "|":
                    VertexDisList.append(tuple(VertexDis))
            Index += 1
            if lines[Index] == "EOF |":
                EOF = True
        return VertexDisList

    def RandomListOfCites(self):
        '''
        Uses self.ListOC (list of coordinates) and loops until it find the greediest possible
        Loop thought Cites and Does the Following:
            Step 1: Sets the Current City and deletes the Current City from the Stack
            Then Loop thought Cites Again and Do the Following:
                Step 1: Compares the Current City with the next city using the distance formula.
                Step 2: The lowest distance of these city is add to the Tour.
                Step 3: Sets the Current City to the lower distance comparison.
        :return: A list of Greedy List
        '''
        Cities_Dis = []
        Cities = copy.deepcopy(self.ListOC)
        Tour = []
        TourCost = 0
        index = 0
        for i in Cities:

            CurrentCity = i
            Cities.pop(index)
            Tour.append(tuple(CurrentCity))
            City_Dis = 0
            NearestCity = []
            counter = 0
            for i in Cities:

                # print(i)
                C1 = (int(CurrentCity[0]) - int(i[0])) **2
                C2 = (int(CurrentCity[1]) - int(i[1])) **2
                C3 = C1 + C2  # Compares the Distances of both Vertices using Pythagorean Theorem
                Temp_City_Dis = math.sqrt(C3)
                if City_Dis == 0:
                    City_Dis = Temp_City_Dis
                    NearestCity = i
                    TourCost += City_Dis
                elif City_Dis >= Temp_City_Dis:
                    City_Dis = Temp_City_Dis
                    NearestCity = i
                    TourCost += City_Dis
                else:
                    pass
                Cities_Dis.append(City_Dis)
                counter += 1
            index += 1
            Tour.append(tuple(NearestCity))
            self.Cities_Dis = Cities_Dis
            self.TotalDis = TourCost
        return Tour

    def cover_coordTOvertexs(self):
        '''
        Uses self.DictOfVertex (A Dictionary of Vertex:Pos)
        :return: List of Vertices List based on there positions
        '''
        VertexList = []
        for i in self.DictOfVertex.keys():
            for i2 in self.StartingTour:
                if self.DictOfVertex[i] == i2:
                    VertexList.append(i)
        return VertexList

    def make_edges(self):
        '''
        Uses self.ListOfVertex (List of Vertices)
        :return: A list of edges -> [[Edge(Vertex(0),Vertex(1))],....]
        '''
        ListOfEdges = []
        index = 0
        for i in self.ListOfVertex:
            EdgeCoord = []
            EdgeCoord.append(self.ListOfVertex[index])
            try:
                EdgeCoord.append(self.ListOfVertex[index + 1])
            except:
                EdgeCoord.append(self.ListOfVertex[0])
            index += 1
            TempEdge = ['Edge' + str((tuple(EdgeCoord)))]
            ListOfEdges.append(TempEdge)
        return ListOfEdges

    def tranlate(self):
        '''
        Uses self.ListOfEdges (A list of edges) -> [[Edge(Vertex(0),Vertex(1))],....]
        :return: A list of just the number of each vertices in each edge -> [[0,1],...]
        '''
        EdgeNumbers = []
        for i in self.ListOfEdges:
            numbers = []
            State = None
            Counter = 0
            for letter in i[0]:
                if letter == "(":
                    if Counter == 1:
                        State = "S"
                    else:
                        Counter += 1
                elif letter == ")":
                    State = "E"
                else:
                    if State == "S":
                        numbers.append(int(letter))
            EdgeNumbers.append(numbers)
        self.ListOfEdgeCoord = EdgeNumbers
        return EdgeNumbers

# ------- PostWork ----------------------------
    def Picking(self):
        '''
        Uses self.tranlate (A list of Edges) [[0,1],...]
        Take this list and choice to Edges at random and see if any of the Vertex are same. If not uses those two Edges
        Then the Two Edges switch y1 and x2 Vertices then replace the old the two selected edges back into the list
        :return: return a updated temp list of edges [[0,1],...]
        '''
        EdgeC = self.tranlate()
        print(EdgeC)
        i = True
        while i is True:
            Edge1 = random.choice(EdgeC)
            Edge2 = random.choice(EdgeC)

            if int(Edge1[0]) != int(Edge2[1]) and int(Edge1[1]) != int(Edge2[0]) and Edge1 != Edge2:
                DuelEdges = [Edge1,Edge2]
                i = False
        print DuelEdges
        temp = DuelEdges[0][1]
        back_up = DuelEdges[1][0]
        Vertex1 = EdgeC.index(DuelEdges[0])
        Vertex2 = EdgeC.index(DuelEdges[1])
        DuelEdges[0][1] = back_up
        DuelEdges[1][0] = temp
        EdgeC[Vertex1] = DuelEdges[0]
        EdgeC[Vertex2] = DuelEdges[1]
        print(EdgeC)


    def Dis_Formual(self, Vertex1, Vertex2):
        '''
        Does the Distance Formual
        :param Edge1: Vertex1 is a tuple of a position on a graph (0,1)
        :param Edge2: Vertex2 is a tuple of a position on a graph (0,1)
        :return: The Distance between these two points
        '''
        C1 = (int(Vertex1[0]) - int(Vertex2[0])) **2
        C2 = (int(Vertex1[1]) - int(Vertex2[1])) **2
        C3 = C1 + C2  # Compares the Distances of both Vertices using Pythagorean Theorem
        Trip_Dis1 = math.sqrt(C3)
        return Trip_Dis1

    def CompairTrips(self):
        """ Uses the distance formula to compair to trip
        ;return; The best trip
        """
        pass

