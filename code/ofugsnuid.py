#https://open.kattis.com/problems/ofugsnuid

out = []

for i in range(int(input())): out.append(input())

for i in range (len(out)-1, -1, -1): print(out[i])