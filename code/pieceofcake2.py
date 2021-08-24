#https://open.kattis.com/problems/pieceofcake2

square, length, width = input().split(' ')
square = int(square)
length = int(length)
width = int(width)
pieces = [length*width,(square-width)*length,(square-length)*width,(square-length)*(square-width)]
#print('pieces:', pieces)
print(max(pieces)*4)