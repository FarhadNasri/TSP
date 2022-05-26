import random 

np=4


def Population(w):
    p=[]
    for i in range(np):
        random_cities = random.sample(range(len(w[0])), len(w[0]))
        p.append(random_cities)
    return p


def FitnessEvaluation(w,p):
    i=0
    j=1
    fitness=0
    while(i<len(p)):
        if(j==(len(p))):
            j=0
        fitness+=w[p[i]][p[j]]
        i+=1
        j+=1
    return fitness


def ParentSelect(w,p):
    possibility=[]
    for i in range(len(p)):
        fitness=FitnessEvaluation(w,p[i])
        possibility.append(fitness)
    sum_fit=sum(possibility)
    for i in range(len(possibility)):
        possibility[i]/=sum_fit
    parent=random.choices(p, weights=possibility, k=4)
    return parent


def Crossover(w,p1,p2):
    child=[]
    
    for i in range(len(w[0])):
        child.append(None)

    while(True):
        rand_list=random.sample(range(len(w[0])), 2)
        min_number=min(rand_list)
        max_number=max(rand_list)
        if(max_number-min_number>=2):
            break
    index1=max_number
    index2=max_number
    child[min_number:max_number]=p1[min_number:max_number]
    while(None in child):
        if(index1==len(child)):
            index1=0
        if(index2==len(p2)):
            index2=0
        if(not(p2[index2] in child)):
            child[index1] = p2[index2]
            index1+=1
            index2+=1
        else:
            index2+=1
    Mutation_Swap(child)
    return child


def Mutation_Swap(child):
    rand_list=random.sample(range(len(w[0])), 2)
    min_number=min(rand_list)
    max_number=max(rand_list)
    temp=child[min_number]
    child[min_number]=child[max_number]
    child[max_number]=temp

"""
w=[
    [0,2,9,pow(10,10)],
    [1,0,6,4],
    [pow(10,10),7,0,8],
    [6,3,pow(10,10),0]
    ]
"""
w=[
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

population=Population(w)
print("population is : {0}\n".format(population))

l=1
while(l<=10):
    parents=ParentSelect(w,population)
    print("parents is : {0}\n".format(parents))
    childs=[]
    i=0
    while(i<len(parents)):
        if(i==(len(parents)-1)):
            childs.append(parents[i])
            break
        child1=Crossover(w,parents[i],parents[i+1])
        child2=Crossover(w,parents[i+1],parents[i])
        childs.append(child1)
        childs.append(child2)
        i+=2
    print("childs is : {0}\n".format(childs))
    SurvivorsSelection=population+childs
    SurvivorsFitness=[]
    for chro in SurvivorsSelection:
        SurvivorsFitness.append((chro,FitnessEvaluation(w,chro)))
    print("SurvivorsFitness is : {0}\n".format(SurvivorsFitness))
    SurvivorsFitness_sort=sorted(SurvivorsFitness,key=lambda x:x[1])
    survior_cut=SurvivorsFitness_sort[:np]
    print("Best SurvivorsFitness is : {0}\n".format(survior_cut))
    temp=[]
    sum_fitness=[]
    for item in survior_cut:
        temp.append(item[0])
        sum_fitness.append(item[1])
    avg=sum(sum_fitness)/len(sum_fitness)
    print("Fitness Average in {0} round is : {1}".format(l,avg))
    #update population
    population=temp
    l+=1
    print("==========================================================")
    print("new population is : {0}\n".format(population))