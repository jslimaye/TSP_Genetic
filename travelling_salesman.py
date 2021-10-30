from math import floor
from Genetic_Functions import cal_fitness, crossover, generate_cost_matrix, generate_population, mutate, sortanddivide

with open("TSP_Genetic\cities.txt","r") as file:
    Cities = file.read().split(",")
# List of Cities

Cost_Matrix = generate_cost_matrix("TSP_Genetic\cost-matrix.txt")
#Cost Matrix maybe asymmetric, i.e. cost(a,b) != cost(b,a)
#Read from "cost-matrix.txt" file

print("Generation\t Best Fitness Value\t Best Tour")

#Generating Gen0
population = generate_population(5,len(Cities),Cities)
#print(population)

best_fitness = 0
best_streak = 1
best_genome = list()

generation = 0


while(generation < 100):
#We run this code for a maximum of 100 iterations or
#until we get the same fitness value for 10 consecutive iterations.
    if best_streak == 10:
        break
   
    #Calculate Fitness of each Genome.
    fitness = list()
    for genome in population:
        fitness.append((cal_fitness(genome,Cost_Matrix,Cities), genome))
        #Update the best_fitness value

    #Sort the population based on Fitness value
    sorted_population, min_fitness = sortanddivide(fitness) 
    

    if best_fitness == 0:
        best_fitness = min_fitness
    elif min_fitness < best_fitness:
        best_fitness = min_fitness
        best_streak = 1
        best_genome = sorted_population[0]
    else:
        best_streak += 1
        #add 1 to streak if same fitness value continues.


    #Divide the population to work a crossover function.
    br = floor(len(population)/2)
    best_population = sorted_population[0:br]
    worst_population = sorted_population[br:]

    #Add some specimens to next generation by crossover
    children = list()
    for j in range(len(best_population)):
        children.append(crossover(best_population[j], worst_population[j]))
    
    #Add more specimen to the next generation by mutation
    for genome in best_population:
        children.append(mutate(genome))


    #Match the size of current and next generation populations by 
    #elitistly adding best specimens from current generation
    k = 0
    while len(children) < len(population):
        children.append(best_population[k])
        k+=1

    '''print("\n")
    print("Current Generation: ", i)
    print("Current Population: ", population)
    print("Best fitness : ", best_fitness)
    print("Best Sequence", best_genome)
    '''
    print(f"{generation}\t  {best_fitness}\t\t {best_genome}")
    #We have our Child Generation now...
    population = children
    generation += 1
    


print(f"\nBest Tour Sequence : {best_genome}")
print(f"This best was sequence found in  {generation - 1} generations")
print(f"The minimum cost of the sequence is {best_fitness}")
