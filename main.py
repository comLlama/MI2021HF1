import math
import copy

class Node:
    def __init__(self, index, x=None, y=None):
        self.index = index
        self.x = x
        self.y = y
        self.ne = []

    def getManhattanDistance(self, node):
        return calcDistance(self.x, node.x, self.y, node.y)

class NodeScore:
    def __init__(self, node, dist, heur):
        self.node = node
        self.dist = dist
        self.heur = heur

    def getScore(self):
        return self.dist + self.heur


#self.traced = self.traced.sort(key=lambda x: x[1]+x[2])
    
def calcDistance(x1, x2, y1, y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

def calcNodeDistance(node1, node2):
    return calcDistance(node1.x, node2.x, node1.y, node2.y)


def routeDistance(nodes, startNodeIdx, endNodeIdx): #has redundancy in node scores
    endNode = nodes[endNodeIdx]
    startNode = nodes[startNodeIdx]
    nodeScores = [NodeScore(startNode, 0, startNode.getManhattanDistance(endNode))]
    while (nodeScores[0].node != endNode):
        for neighbour in nodeScores[0].node.ne:
            nodeScores.append(NodeScore(neighbour, calcNodeDistance(nodeScores[0].node, neighbour),neighbour.getManhattanDistance(endNode)))
        nodeScores.sort(key=lambda x: x.dist + x.heur)
    return nodeScores[0].dist

def routeDistance2(nodes, startNodeIdx, endNodeIdx):
    lnodes = copy.copy(nodes)
    #print("{0}, {1}".format(len(lnodes), endNodeIdx))
    endNode = lnodes[endNodeIdx]
    nodeScores = []
    for i in range(len(lnodes)):
        nodeScores.append(NodeScore(None, math.inf, math.inf))
    nodeScores[startNodeIdx].dist = 0
    nodeScores[startNodeIdx].heur = lnodes[startNodeIdx].getManhattanDistance(lnodes[endNodeIdx])

    tempNode = lnodes[0]
    lnodes[0] = lnodes[startNodeIdx]
    lnodes[startNodeIdx] = tempNode

    while(lnodes[0].index != endNodeIdx): # explores all neighbour nodes instead of the cheapest one
        for neighbour in lnodes[0].ne:
            newdist = calcNodeDistance(neighbour, lnodes[0]) + nodeScores[lnodes[0].index].dist
            newheur = neighbour.getManhattanDistance(endNode)
            #print("for Node[{0}] newdist={1}, newheur={2}".format(neighbour.index, newdist, newheur))
            if (nodeScores[neighbour.index].getScore() > newdist + newheur):
                nodeScores[neighbour.index].dist = newdist
                nodeScores[neighbour.index].heur = newheur
        lnodes.remove(lnodes[0])
        lnodes.sort(key=lambda x: nodeScores[x.index].getScore())

    return nodeScores[endNodeIdx].dist


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
    nodes.append(Node(i, line[0], line[1]))
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
    print("%.3f" % routeDistance2(nodes, route[0], route[1]), end="\t")

