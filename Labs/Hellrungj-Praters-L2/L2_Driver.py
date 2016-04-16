from Greedy_Algorithm import *
# from Graphy import *
# from GraphyWorld import *

def fileread(filename,task):
    if task == "r":
        textfile = open(filename, "r")
        lines = textfile.readlines()
        textfile.close()
        return lines
    elif task == "w":
        textfile = open(filename, "w")
        lines = textfile.readlines()
        textfile.close()
        return lines
    else:
        print("Error!")
        return 0

def AmountOfVertics(textfile):
    lines = fileread(textfile,'r')
    Index = 6
    EOF = False
    counter = 0
    while EOF == False:
        if lines[counter] == "EOF":
            EOF = True
        counter += 1
    return int(counter)-7

def VertexDisList(textfile):
    lines = fileread(textfile,'r')
    Index = 6
    VertexDistanceList = []
    EOF = False
    while EOF == False:
        VertexDis = []
        VertexDis.append(lines[Index][2])
        VertexDis.append(lines[Index][4])
        VertexDistanceList.append(VertexDis)
        Index += 1
        if lines[Index] == "EOF":
            EOF = True
    return VertexDistanceList

def main():
    Textfile = raw_input("Textfile Name Please")
    Dis = VertexDisList(Textfile)
    print Dis
    NumberOfVertecs = AmountOfVertics(Textfile)
    print NumberOfVertecs
    Test1 = GreedyNearestNeighbor(Dis)
    Result = Test1.NearestNeighbor()
    print Result

main()