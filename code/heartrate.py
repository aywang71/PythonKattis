#https://open.kattis.com/problems/heartrate
#input format
n = int(input())
#final storage form
output_actual = []
# inputs of b,p n times
for i in range (0,n):
  #resets BPM list
  BeatsPerMinute = []
  b,p = input().split()
  #formats b and p
  beats = int(b)
  time = float(p)
  #there is only one segment of time if b==2
  if b==2:
    max_interval = time
  else:
    #this means how much time per segment beat
    max_interval = time/(beats-1)
  #this makes our minimum 60/the time per beat
  minABPM = 60/max_interval
  #debugging
  print(minABPM)
  #conversion formatting
  minABPM= str(minABPM)
  #appends to BPM
  BeatsPerMinute.append(minABPM)

  #calculates BPM
  bpm = (60*beats)/time
  bpm = str(bpm)
  BeatsPerMinute.append(bpm)
  
  min_interval = time/(beats+1)
  maxABPM = 60/min_interval
  #debugging
  print(maxABPM)
  #formats to string
  maxABPM = str(maxABPM)
  #adds on to BPM list
  BeatsPerMinute.append(maxABPM)
  #debugging
  print(BeatsPerMinute)

  #appends nested list
  output_actual.append(BeatsPerMinute)


#output format to join nested list array
for i in range (0,n): 
  print(' '.join(output_actual[i]))

