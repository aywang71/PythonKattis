#input format
left,right = input().split(' ')
#data format
left = int(left)
right = int(right)
#output format
if left == 0 and right ==0:
  print("Not a moose")
elif left>right:
  print("Odd %i" %(2*left))
elif right>left:
  print("Odd %i" %(2*right))
elif right == left:
  print("Even %i" %(2*right))