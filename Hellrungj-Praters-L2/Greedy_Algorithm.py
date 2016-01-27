"""
the pseudocode for the greedy algorithm applied to TSP:

NearestNeighbor(Graph g): |# incoming data: Graph([Vertex('w'), Vertex('v')], set([Edge(Vertex('v'), Vertex('w'))]))
    bestTourSoFar = null |# Makes sense
    costOfBestTourSoFar = inf # set value > than possible for a tour |# Does make any fucking sense
    For each city s: |# City = Vertex
        mark all cities as unvisited |# This a problem of it own
        tour = empty partial tour |# Makes a emtpy tour
        startCity = s |# Set a city as a starting city
        add s to tour |# Add that Starting city to tour
        tourCost = 0 |# Setting the cost of the tour to zero
        mark s as visited |# mark the current visited city as marked
        currentCity = startCity |# Set the current City to the started city

        while there are unvisited cities:
            c is the nearest unvisited neighbor of currentCity
            add c to tour
	            tourCost += the cost of the edge from currentCity to c
            mark c as visited
            currentCity = c # travel to c
        tourCost += ost of the edge from currentCity to startCity
        if (costOfBestTourSoFar > tourCost):
            bestTourSoFar = tour cost
            OfBestTourSoFar = tourCost
"""
import math

# Graph([Vertex('w'), Vertex('v')], set([Edge(Vertex('v'), Vertex('w'))]))
class GreedyNearestNeighbor():
    def __init__(self, Cor):
        self.CorOfCites = Cor

    def NearestNeighbor(self):
        BestTour = None
        CostOfBestTour = 0
        for City in self.CorOfCites:
            print(City)
            UnmarkedCities = self.CorOfCites
            Tour = []
            TourCost = 0
            CurrentCity = UnmarkedCities[0]
            UnmarkedCities.pop()
            for i in self.CorOfCites:
                City_Dis = 0
                for index in UnmarkedCities:
                    A = (int(CurrentCity[0]) - int(index[0])) 
                    B = (int(CurrentCity[1]) - int(index[1])) 
                    A = A ** 2
                    B = B ** 2
                    print A
                    print B
                    C = A + B  # Compares the Distances of both Vertices using Pythagorean Theorem
                    print C
                    Temp_City_Dis = math.sqrt(C)
                    if City_Dis == 0:
                        City_Dis = Temp_City_Dis
                        NearestCity = index
                    elif City_Dis > Temp_City_Dis: #Compares the Past Distances to the Best Distance
                        City_Dis = Temp_City_Dis
                        NearestCity = index
                    else:
                        pass
                    Tour.append(NearestCity)
                    TourCost += City_Dis
                    UnmarkedCities.pop
                if (TourCost < CostOfBestTour):
                    BestTour = Tour
                    CostOfBestTour = TourCost
        return BestTour

















