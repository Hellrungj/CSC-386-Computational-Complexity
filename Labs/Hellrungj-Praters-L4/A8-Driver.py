#John Hellrung & Shadia Prater
# A8/L4
# CSC 386

#from Graphy.py import *
#from GraphWorld.py import *
from BBB import *

def main():
    filename = raw_input("Filename: ")
    H = BBB()
    H.Dis_Table(filename)
    H.Binary_Tree()
    H.Bound("A")
    # Makes the needed for the Algomthim
    ''' Plan:
    # Then I will made Binary tree
    binarytree = test.Binary_Tree()
    
    # Then I will made a Bound based on the Binary tree
    bound = test.Bound()
    
    # Then runs the algorithm called Back_Tracking
    result = test.Back_Tracking
    '''
    
    # Make a file with the best tour
    # Then I will convert the data with Graphy.py
    # Then display with Graphy.py 
    # Finaily will display the data with GraphWorld.py
    g = Graph(H.Letter)
    g.add_all_edges()
    layout = RandomLayout(g)
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
    
main()
