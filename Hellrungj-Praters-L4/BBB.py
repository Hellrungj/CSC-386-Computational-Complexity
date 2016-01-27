#John Hellrung & Shadia Prater
# A8/L4
# CSC 386 
import math
from File_Data import *
from Tree import *

class BBB():
    def __init__(self):
        self.Letter = [] # List of Letters used for each Postion ['A','B',...]
        self.ListOfElements = {} # "A":['A','B','C','D','E','F'],...
        self.DisDic = {} # {'(A,B)':Distance of the two point, ...}
        self.PosDic = {} # {'A':Postion of A, ...}
        self.DicOfBinary = {} # {'A':Tree with the root of A, ...}
    
    def distance(self, pos0, pos1):
        return int(math.sqrt((pos0[0] - pos1[0])**2 + (pos0[1] - pos1[1])**2))
    
    def Dis_Table(self, filename):
        """ Make a Table for every distance. """
        DATA = File_Data()
        VerList = DATA.VertexDisList(filename)
        VerListLen = len(VerList)
        for letter in range(VerListLen):
            ASCII_NUM = letter+65
            if ASCII_NUM > 90:
                ASCII_NUM = ASCII_NUM - 26
                self.Letter.append(chr(ASCII_NUM) + str(letter - 26))
            else:
                self.Letter.append(chr(ASCII_NUM))
        
        for a in range(VerListLen):
            self.PosDic.update({self.Letter[a]:VerList[a]})
            for i in range(VerListLen):
                if i <= a: # This is like a Magic!!!!!
                    pass                
                else:
                    key = '(' + str(self.Letter[a]) + ',' + str(self.Letter[i]) + ')'
                    value = self.distance(VerList[a],VerList[i])
                    self.DisDic.update({key:value})
    
    def Binary_Tree(self):
        """ Uses the Node Class and the Filedata to made a Binary Tree """
        for i in range(len(self.Letter)+1):
            if i != 0:
                List = self.Letter[i:]
                for num in range(i):
                    List.insert(0,str(self.Letter[num]))
                self.ListOfElements.update({List[0]:List})
        counter = 0
        for i in self.ListOfElements.values():
            self.DicOfBinary.update({self.Letter[counter]:binary_tree(i)})
            counter += 1
    
    def Bound(self, letter):
        """ This function finds a bound for every node return a list """ 
        BoundList = self.ListOfElements[letter]
        value = 0
        for i in range(len(BoundList)):
            try:
                value = value + self.DisDic['('+ BoundList[i]+","+BoundList[(i+1)]+')']
            except:
                value = value + self.DisDic['('+ BoundList[0]+","+BoundList[i]+')']
        return value
    
    def Back_Tracking(self):
        """ The main program (Recurrtion or loop)
        Keep track of the nodes in the tree that are looked at.
        Plus pruning the edge base on the bound node.
        Returns the best tour based on this algothim.
        """
        pass
    
    def Pruning(self,ListPart):
        """ Remove the subtree! Yeah! """
        pass
    

