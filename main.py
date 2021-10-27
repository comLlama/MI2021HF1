import math

class Node:
    def __init__(self, index, x=None, y=None):
        self.index = index
        self.x = x
        self.y = y
        self.ne = []

    def getNeighbourDistance(self, idx):
        return calcDistance(self.x, self.ne[idx].x, self.y, self.ne[idx].y)

    def getManhattanDistance(self, node):
        return calcDistance(self.x, node.x, self.y, node.y)

class TracedNodes:
    def __init__(self, start, end):
        self.traced = [[start, 0, start.getManhattanDistance(end)]]
        #   node, distance from start, heuristic distance to end
        self.end = end

    def reorder(self):
        self.traced = self.traced.sort(key=lambda x: x[1]+x[2])


    
def calcDistance(x1, x2, y1, y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))


def routeDistance(nodes, startNodeIdx, endNodeIdx):
    endNode = nodes[endNodeIdx]
    currentNodes = [nodes[startNodeIdx]]
    currentNodes
    return 0


p = int(input())
n = int(input())
e = int(input())

input()
routes = [] # from - to nodes TO SEARCH
for i in range(p):
    line = input().split("\t")
    line[0] = int(line[0])
    line[1] = int(line[1])
    routes.append(line)

input()
nodes = []
#crossroads = [] # nodes
for i in range(n):
    line = input().split("\t")
    line[0] = int(line[0])
    line[1] = int(line[1])
    nodes[i] = Node(i, line[0], line[1])
    #crossroads.append(line)

input()
#roads = [] # edges
for i in range(e):
    line = input().split("\t")
    line[0] = int(line[0])
    line[1] = int(line[1])
    nodes[line[0]].ne.append(nodes[line[1]])
    nodes[line[1]].ne.append(nodes[line[0]])
    #roads.append(line)

for route in routes:
    print(routeDistance(nodes, route[0], route[1]), end="\t")

