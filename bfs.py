import queue

graph = {}
option = int(input("Enter 1.Maximisation 2.Minimization"))
size = int(input("Enter no of nodes"))

for i in range(size):
    node = input("Enter the node")
    values = []
    values = input("Enter child nodes").split()
    children = {}

    for j in range(len(values)):
        if option == 1:
            v = int(input("Enter heuristic values")) * -1
        else:
            v = int(input("Enter heuristic values"))
        child = {values[j]: v}
        children.update(child)
        print(children)
    graph[node] = children
print(graph)

goalList = queue.PriorityQueue()
for key, val in graph.items():
    for ckey, cval in val.items():
        goalList.put((cval, ckey))

start = input("Start")
shvalue=int(input('Enter hvalue of start node'))
goalList.put((shvalue, start))

goal = goalList.get()[1]

def bfs(graph, start):
    check=0
    openList = queue.PriorityQueue()
    closedList = []
    visited=[]
    openList.put((shvalue, start))
    visited.append((start))
    while not openList.empty():
        temp = openList.get()
        node = temp[1]
        print(node)
        closedList.append(node)

        if node in goal:
            check=1
            break
        else:
            for value, key in graph[node].items():
                if value not in visited:
                    openList.put((key, value))
                    visited.append(value)
            print(node + "is examined")
    if check!=1:
        print('Goal node not found')

    print("Closed list is", end=" ")
    print(closedList)
    tempgoal = goal
    path = []
   # path.append(goal)

    for j in closedList:
        for value, key in graph[j].items():
            for cval,ckey in value.items():
                if tempgoal in cval:
                    path.append(goal)
                    tempgoal=cval

            #if tempgoal == value:
                #tempgoal = j
                #path.append(tempgoal)

    print('Path is ', end=' ')
    for i in reversed(path):
        print(i +"->",end="")

    print('\nVisited list is ', end=' ')
    print(visited)#visited has the nodes that are visited and prevents from duplicate insertions in open list

    while not openList.empty():#redundant code remove for exams
        item = openList.get()
        print(item)

bfs(graph, start)

