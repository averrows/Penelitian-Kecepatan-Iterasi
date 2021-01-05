import timeit

start = timeit.default_timer()

for i in range(0,100001):
    print(i)

stop = timeit.default_timer()

print('Elapsed time is ', (stop - start) * 1000, "milisecond")  