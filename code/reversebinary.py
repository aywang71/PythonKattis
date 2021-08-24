#https://open.kattis.com/problems/reversebinary

#inputs for original number
n = int(input())
#converts that number to binary
binary = list(bin(n))
#formats number
binary.remove('b')
binary.remove('0')
#debugging
print(binary)
#reverse variable is binary but reverse
reverse = ''.join(binary[::-1])
#print integer of reverse
print(int(reverse,2))

