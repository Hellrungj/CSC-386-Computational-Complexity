from Test_2_OPT import *
from Graphy import *
from GraphyWorld import *

def main():
    Textfile = raw_input("Textfile Name Please")
    Test = Test_2_OPT(Textfile)
    print("List Of Cords(ListOC) " + str(Test.ListOC))
    print ("DictOfVertex " + str(Test.DictOfVertex))
    print("Rand Of Cords(StartingTour) " + str(Test.StartingTour))
    print("Vertex Of Rand(ListOfVertex) " + str(Test.ListOfVertex))
    print("Edge Of Vertex(ListOfEdges) " + str(Test.ListOfEdges))
    print(Test.Picking())
    g = Graph(Test.ListOfVertex)
    g.add_all_edges()
    layout = RandomLayout(g)
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
main()