# TSP_Genetic
My solution to Travelling Salesman Problem using Genetic Algorithm

'cities.txt' is the file with all the city names our salesman has to cover 

'cost-matrix.txt' is the cost-matrix that gives us costs associated with travelling between cities
Cost-Matrix should not be just the distance but a consolidated measure of multiple possible factors..
Cost-matrix may be asymmetric. i.e cost('a','b') may or may not be equal to cost('b','a').
        **cost('a','b') is the cost of travel from city 'a' to city 'b'

'Genetic Functions' contains all the functions used in Genetic algorithms viz., 
    crossover, mutate, fitness etc.

'travelling_salesman.py' has the solution to TSP.