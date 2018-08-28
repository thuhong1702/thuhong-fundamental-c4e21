import string
alphatbet = string.ascii_uppercase

counter = [int(0)]*30

line = input("input: ")

line = line.upper()

for i in line:
    counter[alphatbet.index(i)] = counter[alphatbet.index(i)] + 1
i = 0

while(i<26):
    if(counter[i]>0): print(alphatbet[i]+': '+ str(counter[i])) 
    i=i+1 

