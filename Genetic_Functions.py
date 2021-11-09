from math import floor
from random import randint
from typing import List, Tuple

Cities = Tuple[str]
Cost_Matrix = Tuple[Tuple[int]]
Genome = List[str]
Population = List[Genome]
#Defining Constructs of reused elements to create context...

def generate_cost_matrix(filename) -> Cost_Matrix:
    costs = []
    with open(filename,"r") as file:
        for line in file:
            temp = line.split(",")
            for i in range(len(temp)):
                temp[i] = int(temp[i])
            costs.append(temp)
    return costs
    

def generate_genome(length: int, cities: Cities) -> Genome:
    genome = list()
    while len(genome) < length:
        i = randint(0,len(cities) - 1)
        if cities[i] in genome:
            continue
        else:
            genome.append(cities[i])
    return genome
#Generates a Genome 

def generate_population(size: int, genome_length: int, cities:Cities) -> Population:
    return [generate_genome(genome_length,cities) for _ in range(size)]
#Generates a sequence of n Genomes; n = size

def crossover(a: Genome, b: Genome) -> Genome:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")
    
    result = a[0:floor(len(a)/2)]

    for charec in b :
        if charec in result:
            continue
        else:
            result.append(charec)
    
    return result
#Crossover Function 

def mutate(a: Genome) -> Genome:

    for k in range(1, floor( randint(1, len(a)/2 ) )):
            
        i = randint(0,len(a)-1)
        j = randint(0,len(a)-1)

        temp = a[j]
        a[j] = a[i]
        a[i] = temp
    return a
#Mutation Function: for a random number of times ranging from 1 to n/2, randomly swap any 2 cities from the genome.

def sortanddivide(listofTuples):
    listofTuples = sorted(listofTuples)
    genome = list()
    fitness = list()
    for l in listofTuples:
        genome.append(l[1])
        fitness.append(l[0])
    return genome, min(fitness)
#A function to sort and divide the list of tuples contianing genomes and their resp. fitnesses
#This function gives us 2 lists 
#1. sorted population
#2. sorted fitness values


def cal_fitness (a: Genome, costs: Cost_Matrix, c: Cities)-> int:
    sum = 0
    for i in range(1,len(a)):
        sum += costs[c.index(a[i]) ][ c.index(a[i-1])] 
    
    sum += costs[c.index(a[i]) ][ c.index(a[0])]
    return sum
#Function to calculate fitness