#from Test_2_OPT import *
from Graphy import *
from GraphyWorld import *

def file_writeread(filename,task, CorList=[]):
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

def VertexDisList(textfile):
    lines = file_writeread(textfile,'r')
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

def RandomListOfCites(Cities):
        Tour = []
        TourCost = 0
        index = 0
        for i in Cities:
            ''' Step 1: Sets the Current City and deletes the Current City from the Stack '''
            CurrentCity = i
            Cities.pop(index)
            Tour.append(tuple(CurrentCity))
            City_Dis = 0
            NearestCity = []
            counter = 0
            for i in Cities:
                ''' Step 1: Compares the Current City with the next city using the distance formula.
                    Step 2: The lowest distance of these city is add to the Tour.
                    Step 3: Sets the Current City to the lower distance comparison. '''
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
                counter += 1
            index += 1
            Tour.append(tuple(NearestCity))
        return Tour

def cover_coordTOvertexs(Dict, Coords):
    VertexList = []
    for i in Dict.keys():
        for i2 in Coords:
            if Dict[i] == i2:
                VertexList.append(i)
    return VertexList

def make_edges(VertexList):
    ListOfEdges = []
    index = 0
    for i in VertexList:
        EdgeCoord = []
        EdgeCoord.append(VertexList[index])
        try:
            EdgeCoord.append(VertexList[index + 1])
        except:
            EdgeCoord.append(VertexList[0])
        index += 1
        TempEdge = ['Edge' + str((tuple(EdgeCoord)))]
        ListOfEdges.append(TempEdge)
    return ListOfEdges

# Test Suit
def TestSuit(Result):
    pass

def main():
    Textfile = raw_input("Textfile Name Please")
    # print(file_writeread(Textfile,"r"))
    Dis = VertexDisList(Textfile)
    print("List Of Cords(Dis) " + str(Dis))
    Dict = {Vertex(i):Dis[i] for i in range(len(Dis))}
    RC = RandomListOfCites(Dis)
    VList = cover_coordTOvertexs(Dict,RC)
    EdgesForVList = make_edges(VList)
    print ("Dict " + str(Dict))
    print("Rand Of Cords(RC) " + str(RC))
    print("Vertex Of Rand(VList) " + str(VList))
    print("Edge Of Vertex(EdgesForVList) " + str(EdgesForVList))

    #----------- Insert
    '''
    Test = Test_2_OPT(RC,EdgesForVList)
    print('Tranlate')
    print(Test.tranlate())
    '''
    #-------------------

    ''' Broken
    print(Dict.keys())
    for i in Dict.keys():
        print i
        print Dict[i]
        i.pos(Dict[i])
    '''
    g = Graph(VList)
    g.add_all_edges()
    layout = RandomLayout(g)
    # layout = CartesianLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()

main()