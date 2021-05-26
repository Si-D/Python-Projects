import numpy as np

file = open("mlp_ID.txt", 'r')
a = []
text_lines = file.readlines()  #reads all lines in the document
word = "Computing GE"

for line in text_lines:
    if word in line: 
        GE = line.split("(34):",1)[1]  #splits each line 
        a.append(GE)
#print(a)

converted = []
for element in a:
    converted.append(element.strip())  #removes \n at eol
data_main = [s.replace(")", " ") for s in converted]
#print(data_main)

for i in range(0, len(data_main)):  #converts string to float
    data_main[i] = float(data_main[i])
#print(data_main)

N = 100
subList = [data_main[n:n+N] for n in range(0, len(data_main), N)]

for arr in subList:
    mean = np.mean(arr)
    print("Mean:", mean)
    print("Length:", len(arr))