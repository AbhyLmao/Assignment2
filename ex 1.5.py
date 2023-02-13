import time
import matplotlib.pyplot as plt

cache = {}

def func(n):
    if n in cache:
        return cache[n]
    elif n == 0 or n == 1:
        result = n
    else:
        result = func(n-1) + func(n-2)
    cache[n] = result
    return result

def func2(n):
    if n == 0 or n == 1:
        return n
    else:
        return func2(n-1) + func2(n-2)


time1 = []
time2 = []
xdata = []
for i in range(0,36):
    start_time = time.time()

    func(i)
        
    end_time = time.time()

    time1.append(end_time - start_time)

    start_time2 = time.time()

    func2(i)
        
    end_time2 = time.time()

    time2.append(end_time2 - start_time2)
    xdata.append(str(i))

plt.scatter(xdata,time1 )
plt.scatter(xdata,time2 )
plt.xlabel('number')
plt.ylabel('time')
plt.title('Time taken vs number')
plt.show()