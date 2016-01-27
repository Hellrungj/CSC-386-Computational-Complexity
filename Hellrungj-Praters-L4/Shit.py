#John Hellrung & Shadia Prater
# A8/L4
# CSC 386

class Binary_Tree():
    def __init__(self):
        self.Node = [[None],[None],[None]]
        
    def cal(self, List):
        SortedList = sorted(List)
        print(SortedList)
        MiddleElement = len(SortedList)/2
        RootValue = SortedList[MiddleElement]
        SortedList.pop(MiddleElement)
        
    def MakeNode(self, Root):
        self.Tree[0] = RootValue
        self.Tree[1] = self.Node
        self.Tree[2] = self.Node
            
    def MakeTree(self, Lenght):
        for i in range(Lenght):
            Root = self.Node
            Left = self.Node
            Right = self.Node
        
        
'''
Test = Binary_Tree()
print(Test.Tree)
Test.MakeTree([1,15,3])
print(Test.Tree) 
'''


