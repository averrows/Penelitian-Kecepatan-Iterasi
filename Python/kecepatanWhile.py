import timeit

start = timeit.default_timer()

i = 1
while (i <= 100000):
    print(i)
    i += 1

stop = timeit.default_timer()

print('Elapsed time is ', (stop - start) * 1000, "milisecond")  