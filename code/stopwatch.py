#https://open.kattis.com/problems/stopwatch

n = int(input())
times = []
total = 0
cont = True

if n % 2 == 1: 
    cont = False
    print('still running')


if cont: 
    for i in range(n): #first press = starts n % 2 == 1 is a start press
        times.append(int(input()))

    for i in range(0,len(times),2):
        total += times[i+1] - times[i]
    print(total)