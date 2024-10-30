import random
import time
import numpy as np

def calculate_profit(agents , tasks , distribution):
    profit = 0
    for i in range(len(distribution)):
        profit += (agents[i] * tasks[distribution[i]]) / 100
    return profit

######### BRUTE FORCE #########

def allocate( a , distribution , result , n , m) :
    if a >= n :
        result.append(distribution.copy())
        return
    # Assign a-th agent one of the m tasks
    for t in range(m):
        distribution.append(t)
        allocate(a+1 , distribution , result , n , m)
        distribution.pop()


def brute_force(agents, tasks):
    n = len(agents)
    m = len(tasks)

    #Generating result matrix
    result = []
    allocate(0,[],result,n,m)
    
    #Calculating the profit for each distribution , and finding the distribution with maximum profit
    max_profit = 0
    max_distribution = []

    for distribution in result:
        # if not all tasks have been assigned atleast one agent in given distribution , then skip currrent distribution
        if len(set(distribution)) != m:
            continue
        
        # else , calculate the profit for the given distribution
        profit = calculate_profit(agents , tasks , distribution)

        if profit > max_profit:
            max_profit = profit
            max_distribution = distribution
        
    return max_distribution
        

######### GREEDY #########

def greedy(agents, tasks):
    # Sorting the agents and tasks in ascending order
    agents.sort()
    n = len(agents)
    tasks.sort()
    m = len(tasks)

    print("Agents : " , agents)
    print("Tasks : " , tasks)

    # Initialize the result array , where element at index i specifies the index of the task that ith agents has been assigned
    result = [-1 for _ in range(n)]

    for a in range(m):
        # Assigning the first least-efficient 'm' agents the first 'm' least-profitable tasks
        result[a] = a

    # For the remaining (n-m) agents , allocate them to the task with most profit
    for a in range(n-m , n):
        result[a] = m-1

    return result


if __name__ == "__main__":
    
    n = int(input("Enter number of agents :"))
    m = int(input("Enter number of tasks :"))

    # agents = []
    # tasks = []

    # appending a random number between 1 and 100 to the agents list
    # for i in range(n):
    #     agents.append(random.randint(1, 100))
    
    # appending a random number between 100 and 1000 to the tasks list
    # for i in range(m):
    #     tasks.append(random.randint(100 , 1000))

    agents = np.random.uniform(0 , 1, size=n)       #agents' utility score
    tasks = np.random.uniform(100 , 500 , size=m)    #tasks' profit value



    print("Agents : " , agents)
    print("Tasks : " , tasks)

    start_time = time.time()
    res_brute = brute_force(agents , tasks)
    brute_force_time = time.time() - start_time
    print(f"Time taken by brute_force: {brute_force_time} seconds")
    print("Result by brute-force approach:")
    for i in range(n):
        print(f"Agent {i} is assigned to task {res_brute[i]}")
    brute_profit = calculate_profit(agents , tasks , res_brute)
    print(f"Maximum Profit by Brute Force Method: {brute_profit}")

    print("----------------------------------------------------------- \n")
    """
    start_time = time.time()
    res_greedy = greedy(agents , tasks)
    greedy_time = time.time() - start_time
    print(f"Time taken by greedy: {greedy_time} seconds")
    print("Result by greedy approach:")
    for i in range(n):
        print(f"Agent {i} is assigned to task {res_greedy[i]}")
    greedy_profit = calculate_profit(agents , tasks , res_greedy)
    print(f"Maximum Profit by Greedy Method: {greedy_profit}")
    """


