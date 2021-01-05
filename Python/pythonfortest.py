import timeit

jenisIterasi = "for"
jumlahIterasi = 100000
loop = """ 
for x in range(100000):
    pass


"""
waktu = timeit.timeit(loop, number=2)
output = """
Waktu untuk menjalankan {} iterasi pada {} loop adalah:
{} sekon
""".format(jumlahIterasi,jenisIterasi,waktu)

print(output)