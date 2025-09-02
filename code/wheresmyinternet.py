# https://open.kattis.com/problems/wheresmyinternet

n, m = input().split(' ')
n = int(n)
m = int(m)


# We want to find everything that has been connected to house 1, basically a graph connectivity problem

# We can do this by building an adjaceny list from the m pairs and then taking a set difference based on traversal of the list
houses_adj = {}
for i in range(1, n+1):
    houses_adj[i] = []

# Now take in m pairs
for i in range(m):
    h1, h2 = input().split(' ')
    h1 = int(h1)
    h2 = int(h2)
    houses_adj[h1].append(h2)
    houses_adj[h2].append(h1)


# After getting all pairs, build a set of everything touching house 1 off of BFS
touching = {1}
queue = houses_adj[1]

for h in queue:
    touching.add(h)
    queue.extend([house for house in houses_adj[h] if house not in touching])

houses = set(houses_adj.keys())

not_touching = houses.difference(touching)

for i in not_touching:
    print(i)

if len(not_touching) == 0:
    print('Connected')