import timeit

#tes123

#Jumlah iterasi = 1juta
jumlahIterasi = 1000000
forLoop = """ 
for x in range(10000):
    pass


"""
waktu = timeit.timeit(forLoop, number=2)
print("waktu untuk mengerjakan "+str(jumlahIterasi)+" iterasi adalah "+str(waktu)+" sekon. Serta kecepatan iterasi adalah "+str(jumlahIterasi/waktu) + " iterasi/sekon")

#Jumlah iterasi = 10 juta
jumlahIterasi = 10000000
forLoop = """ 
for x in range(10000):
    pass


"""
waktu = timeit.timeit(forLoop, number=2)
print("waktu untuk mengerjakan "+str(jumlahIterasi)+" iterasi adalah "+str(waktu)+" sekon. Serta kecepatan iterasi adalah "+str(jumlahIterasi/waktu) + " iterasi/sekon")

#Jumlah iterasi = 100Juta
jumlahIterasi = 100000000
forLoop = """ 
for x in range(10000):
    pass


"""
waktu = timeit.timeit(forLoop, number=2)
print("waktu untuk mengerjakan "+str(jumlahIterasi)+" iterasi adalah "+str(waktu)+" sekon. Serta kecepatan iterasi adalah "+str(jumlahIterasi/waktu) + " iterasi/sekon")
