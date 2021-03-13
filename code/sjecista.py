#https://open.kattis.com/problems/sjecista

n = int(input())
output = n*(n-1)*(n-2)*(n-3)
#print('output:',output)
output = output/24
print(int(output))