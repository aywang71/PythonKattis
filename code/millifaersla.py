# https://open.kattis.com/problems/millifaersla

a = int(input())

b = int(input())

c = int(input())

if a < b and a < c:
    print('Monnei')

if b < a and b < c:
    print('Fjee')

if c < b and c < a:
    print('Dolladollabilljoll')