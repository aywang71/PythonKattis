#https://open.kattis.com/problems/conquestcampaign

def valid_neighbors(point, maxr, maxc):
	# this should return the cells around "point" that are within the boundaries
	valid = []
	r, c = point
	if r + 1 <= maxr:
		valid.append((r+1, c))
	if r - 1 >= 1:
		valid.append((r-1, c))
	if c + 1 <= maxc:
		valid.append((r, c+1))
	if c - 1 >= 1:
		valid.append((r, c-1))
	return valid

# get inputs, i'm skipping this part and just putting them into variables
rows, columns, weak_points = input().split(' ')
rows = int(rows)
columns = int(columns)
weak = []
for i in range (0,int(weak_points)):
  x,y = input().split(' ')
  x = int(x)
  y = int(y)
  t = (x,y)
  weak.append (t)
#weak = [(2, 2), (2, 2), (3, 4)]

# try to eliminate repeats by using a set
# a set eliminates repeats automatically - and very fast - it messes up the order, but order is not important in this case
yesterday = set(weak)

# make another set for all the conquered cities (not just from yesterday)
conquered = set(weak) 
days = 1

while len(conquered) < rows*columns:
	# we start off with no cities conquered today (yet)
	today = set()
	for city in yesterday:
		for neighbor in valid_neighbors(city, rows, columns):
			if neighbor not in conquered:
				# if it's not yet conquered, conquer it!
				conquered.add(neighbor)
				today.add(neighbor)
	# update for the next iteration
	yesterday = today
	days += 1

print(days)