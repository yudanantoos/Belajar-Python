import calendar
import configparser
import json

from Sample.pengaturan import pengaturan

"""
cal = calendar.month(2008, 1)
#print("Dibawah ini adalah kalender:")
#print(cal)

co = calendar.weekday(2024,12,20)
#print(co)
"""

"""
with open("../Notes/note", "r") as p:
    #baca = p.write("Tes membuat file lagi dan lagi \n")
    #baca = p.readlines()
    for a in p:
        print(a)

p.close()
"""

"""
t = {"nama" : "VCNC", "Agama" : "Islam", "TTD" : "04-10-1990"}

for i in t:
    print(f"{i} : {t[i]}")
"""

"""
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum\'at", "Sabtu", "Minggu"]
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

print("Pilih tanggalnya: ")
o = int(input())
print("Pilih bulan nya: ")
p = int(input())
print("Pilih tahun nya: ")
q = int(input())

ca = calendar.weekday(q, p, o)

print(f"Tanggal yang dipilih : {o}/{p}/{q} adalah hari: {hari[ca]}")
"""

"""
print("Masukkan Gapok:")
gapok = float(input())
print("Masukkan tanggal:")
tanggal = int(input())
print("Masukkan bulan:")
bulan = int(input())
print("Masukkan tahun:")
tahun = int(input())
print("Masukkan jam lembur:")
jam_lembur = float(input())

ca = calendar.weekday(tahun, bulan, tanggal)

if ca == 5 or ca == 6:
    jam_pertama = 2
else:
    jam_pertama = 1.5

gaji_perjam = gapok * 1 / 176
jam_selanjutnya = (jam_lembur - 1) * 2
jam_perkalian = jam_pertama + jam_selanjutnya
nominal_perkalian = gaji_perjam * jam_perkalian
"""

#q = oe.append("Tambahan")
#p = json.dumps(oe)
"""
with open('../Data/tes_file.json', 'r+') as o:
    baca = o.read()
l = json.loads(baca)

oe = l
print(oe[0])
"""
"""
isikan = penyimpanan_list.append({"Tanggal" : str(f"{tanggal}/{bulan}/{tahun}"), "Jam lembur" : jam_lembur, "Jam perkalian" : jam_perkalian, "Nominal" : nominal_perkalian})
penyimpanan_dict = {tahun : penyimpanan_list}

with open('../Data/tes_file', 'w') as p:
    tulis = p.write(str(penyimpanan_dict))

p.close()
"""
"""
ini_dict = {}
ini_list = [ini_dict]

ini_dict['satu'] = 1

ini_dict2 = {'dua':2}

print(f"ini_list sebelum ditambah {ini_list}")

ini_list.append(ini_dict2)

print(f"ini_list sesudah ditambah {ini_list}")

o ="dua"
k = 3

for i in ini_list:
    p = o not in i

if p:
    ini_list.append({o:k})
else:
    g = ini_list.index({o:2})
    ini_list[g] = {o:k}

print(f"Isi ini_list terbaru: {ini_list}")
"""

import _ot_calculation
import  _ot_operation
"""
o = _ot_calculation.ambil_data()

for u in o:
    print(u)
print(o)

y = o.pop('2024')
print(y)
print(o)
"""
import pengaturan

a = pengaturan.load_pengaturan()

print(a['DEFAULT']['datafile'])