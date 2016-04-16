import math

# Graph([Vertex('w'), Vertex('v')], set([Edge(Vertex('v'), Vertex('w'))]))
class GreedyNearestNeighbor():
    def __init__(self, Cor):
        self.CorOfCites = Cor

    def NearestNeighbor(self):
        """
        :return: The Best Possable Tour
        It does this by:
            Step 1: Sets the Current City and deletes the Current City from the Stack
            Step 2: Compares the Current City with the next city using the distance formula.
            Step 3: The lowest distance of these city is add to the Tour.
            Step 4: Sets the Current City to the lower distance comparison.
            Step 5: Adds up the Tour Cost
            Step 6: Compares the Current Tour Cost with Lowest Founded Tour Cost.
            Step 7: Returned the Lowest Costing Tour
        """
        Final_Tour_Cost = 0
        Final_Tour = []
        IndexList = 0
        for a in self.CorOfCites:
            Cities = []
            INDEXList = 0
            for INDEX in self.CorOfCites:
                if IndexList == 0:
                    Cities.append(INDEX)
                else:
                    if IndexList+INDEXList >= (len(self.CorOfCites)-1):
                       Cities.append(self.CorOfCites[IndexList-INDEXList])

                    else:
                        Cities.append(self.CorOfCites[IndexList+INDEXList])
                INDEXList += 1
            IndexList += 1
            Tour = []
            TourCost = 0
            index = 0
            for i in Cities:
                ''' Step 1: Sets the Current City and deletes the Current City from the Stack '''
                CurrentCity = i
                Cities.pop(index)
                Tour.append(CurrentCity)
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
                    # print(Temp_City_Dis)
                    if City_Dis == 0:
                        City_Dis = Temp_City_Dis
                        NearestCity = i
                        TourCost += City_Dis
                    elif City_Dis > Temp_City_Dis: #Compares the Past Distances to the Best Distance
                        City_Dis = Temp_City_Dis
                        NearestCity = i
                        TourCost += City_Dis
                    else:
                        pass
                    counter += 1
                index += 1
                # print("===: " + str(NearestCity) + " NearestCity.")
                # print(str(index) + "------------------")
                Tour.append(NearestCity)
            # print(str(Tour) + " " + str(IndexList) + " Cost: " + str(TourCost))
            # print("=================================")
            if Final_Tour_Cost == 0:
                Final_Tour_Cost = TourCost
                Final_Tour = Tour
            elif Final_Tour_Cost > TourCost: #Compares the Past Distances to the Best Distance
                Final_Tour_Cost = TourCost
                Final_Tour = Tour
            else:
                pass
        return Final_Tour