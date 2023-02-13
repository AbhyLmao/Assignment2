import sys
import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high :
            if array[high] >= p:
                high = high - 1
            if array[low] <= p:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


# Opening JSON file
f = open('file.json')
  
# returns JSON object as 
# a dictionary
datalol = json.load(f)
  
# Iterating through the json
# list

times = []
lenslol = []

for sublist in datalol:
    start_time = time.time()

    func1(sublist, 0, len(sublist)-1)
        
    end_time = time.time()

    times.append(end_time - start_time)
    lenslol.append((str(len(sublist))))

for i in range (0,len(lenslol)):
    print("time taken for length", lenslol[i], "was", times[i],"s")

print(datalol[0])

plt.scatter(lenslol, times)
plt.xlabel('lenslol')
plt.ylabel('times')
plt.title('Time vs. List Length')
plt.show()



    

