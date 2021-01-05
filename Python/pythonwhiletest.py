import timeit

jenisIterasi = "while"
jumlahIterasi = 100000
loop = """ 
x = 0
while x < 100000:
    x += 1


"""
waktu = timeit.timeit(loop, number=2)
output = """
Waktu untuk menjalankan {} iterasi pada {} loop adalah:
{} sekon
""".format(jumlahIterasi,jenisIterasi,waktu)

print(output)