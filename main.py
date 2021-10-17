p = int(input())
n = int(input())
e = int(input())
#print("p={0}, n={1}, e={2}".format(p,n,e))

input()
routes = []
for i in range(p):
    line = input().split("\t")
    line[0] = int(line[0])
    line[1] = int(line[1])
    routes.append(line)

input()
crossroads = []
for i in range(n):
    line = input().split("\t")
    line[0] = int(line[0])
    line[1] = int(line[1])
    crossroads.append(line)

input()
roads = []
for i in range(e):
    line = input().split("\t")
    line[0] = int(line[0])
    line[1] = int(line[1])
    roads.append(line)