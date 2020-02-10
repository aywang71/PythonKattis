#https://open.kattis.com/problems/relocation

#inputs
total_companies, queries = input().split(' ')
#list of locations
company_location = input().split(' ')
#conversion to integer
for i in range (0,len(company_location)):
  company_location[i] = int(company_location[i])
#n amount of queries
for i in range (0,int(queries)):
  #further input
  action, data1, data2 = input().split(' ')
  data1 = int(data1)
  data2 = int(data2)
  #type splice for actions
  if action == "1":
    company_location[data1-1] =data2
    #debugging
    print(company_location)
    continue
  if action == "2":
    #debugging
    print(company_location)
    #output if action type 2 
    print(abs(company_location[data1-1]-company_location[data2-1]))
