
daftar_buku = ['jack', 'what are', 'yoyo']
print(daftar_buku)

print("print with for in")
for buku in daftar_buku:
    print(buku)

print('')

print('tampilkan with index')
print(daftar_buku[0])
print(daftar_buku[2])

print('')

print('tampilkan dengan in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('')
daftar_buku = [1, 'kenji', -331, 4.144]
print("print with for in with different type data")
for buku in daftar_buku:
    print(buku)


print('')
daftar_buku = ['jack', 'what are', 'yoyo']
daftar_buku.append("how to make love")
print('with append')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nclear list')
daftar_buku.clear()

print('')
daftar_buku = ['jack', 'what are', 'yoyo']
daftar_buku[0] = 'jack sparrow'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nget elemen-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('buku yg diambil : ' + buku)

print('\npop it, get last element')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nzz")
daftar_buku = ['rena', 'sofi', 'irna', 'wulan']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\npop for delete')

ok = daftar_buku.pop(-2) #delet/ ambil irna
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nget : ' + ok)


print('\nperintah del')
daftar_buku = ['rena', 'sofi', 'irna', 'wulan']
#del rena
del daftar_buku[0]

for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nperintah del list comprehension')
daftar_buku = ['rena', 'sofi', 'irna', 'wulan']
del daftar_buku[1:3]
#[index:jumlah yg diambil]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del list comprehension minus -2')
daftar_buku = ['rena', 'sofi', 'irna', 'wulan']
del daftar_buku[0:-2]
#[index:jumlah yg diambil]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del list comprehension with step')
daftar_buku = ['rena', 'sofi', 'irna', 'wulan']
del daftar_buku[0::3]
#[index:jumlah yg diambil]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\ndaftar lama :')
daftar = ['syifa', 'sofi', 'irna', 'azizah']
daftar_baru = daftar[:]
for i in range(0, len(daftar)):
    print(daftar[i])

del daftar
print('\ndaftar baru :')

for i in range(0, len(daftar_baru)):
    print(daftar_baru[i])

print('\nMembuat list baru dengna compresension ganjil')
daftar = ['1 syifa', '2 sofi', '3 irna', '4 azizah']
daftar_baru = daftar[0::2]
for i in range(0, len(daftar_baru)):
    print(daftar_baru[i])


print('\nMembuat list baru dengna compresension genap')
daftar = ['1 syifa', '2 sofi', '3 irna', '4 azizah']
daftar_baru = daftar[1::2] #start stop end
for i in range(0, len(daftar_baru)):
    print(daftar_baru[i])


print('\ntipe data stack?????')