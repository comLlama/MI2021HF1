import math

class Node:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.ne = []

    def getDistance(self, idx):
        return math.sqrt(((self.x - self.ne[idx].x)**2) + ((self.y - self.ne[idx].y)**2))
    

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
    nodes[i] = Node(line[0], line[1])
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