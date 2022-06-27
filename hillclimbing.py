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

    graph[node] = children
print(graph)

goalList = queue.PriorityQueue()
for key, val in graph.items():
    for ckey, cval in val.items():
        goalList.put((cval, ckey))

start = input("Start")
shvalue=int(input('Enter hvalue of start node'))
goalList.put((shvalue, start))

goalcopy=goalList.get()
goal = goalcopy[1]

if goal==start:
    print('Start node is the goal state.')

def stHillClimbing (graph, start):
    openList = queue.PriorityQueue()
    closedList = []
    neighbours=[]
    localcheck=0
    platcheck = 0
    globalcheck=0
    values=[]

    openList.put((shvalue, start))
    while not openList.empty():
        temp = openList.get()
        node = temp[1]
        vals=temp[0]
        values.append(vals)

        closedList.append(node)
        while not openList.empty():
            a=openList.get()[0]
            neighbours.append(a)


        if temp[1]==goal:
            print('Global Maxima reached')
            print('Path is ', end=' ')
            for i in closedList:
                print(i + "->", end="")
            globalcheck = 1
            break
        elif len(neighbours)!=0 and temp[0]==(sum(neighbours)/len(neighbours)):
            print('Plateau reached')
            print('Path is ', end=' ')
            for i in closedList:
                print(i + "->", end="")
            platcheck=1
            break
        elif temp[0]>values[len(values)-2] and node!=start:
            print('Local Maxima reached')
            print('Path is ', end=' ')
            localcheck = 1
            for i in range(0,len(closedList)-1):
                print(closedList[i] + "->", end="")
            break

        for value, key in graph[node].items():
            openList.put((key, value))
        neighbours.clear()

    if localcheck==0 and platcheck==0 and globalcheck==0:
        print('Local Maxima reached')
        print('Path is ', end=' ')
        for i in closedList:
            print(i + "->", end="")

if goal==start:
    print('Start node is the goal state.')
else:
    stHillClimbing(graph, start)
