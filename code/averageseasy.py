#https://open.kattis.com/problems/averageseasy

#iteration input
test_cases = int(input())
for i in range(test_cases):
  #resets count value
  count = 0
  #for the blank line
  blank = input()
  #input for studetns of CS and econ
  cs_s, econ_s = input('').split(' ')
  # makes a list out of the IQs for CS students
  cs_iq = [int(i) for i in input().split(' ')]
  # makes a list out of the IQs for econ students
  econ_iq = [int(i) for i in input().split(' ')]
  #sorts IQs from lowest to highest IQ
  cs_iq.sort()
  econ_iq.sort()
  #debugging
  #print(cs_iq)
  #print(econ_iq)
  #finds average IQs for each group
  cs_avg = sum(cs_iq) / len(cs_iq)
  econ_avg = sum(econ_iq) / len(econ_iq)
  # goes through the CS IQs
  for i in range(0, len(cs_iq)):
    #when a CS IQ is lower than the CS average but higher than the econ average
    if cs_iq[i] < cs_avg and cs_iq[i] > econ_avg:
      count += 1
  #output
  print(count)
