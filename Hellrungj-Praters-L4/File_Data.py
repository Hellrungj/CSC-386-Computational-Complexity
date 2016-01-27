#John Hellrung & Shadia Prater
# A8/L4
# CSC 386

class File_Data():
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

    def VertexDisList(self, filename):
        '''
        :param filename: Takes in a string to be used as a filename        
        Read the file based on the filename and then appends the second and third number after line 5 until it see EOF        
        :return: A list of coordinates        
        '''  
        lines = self.file_writeread(filename,'r')
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
                        if Number == '':
                            pass
                        else:
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
        