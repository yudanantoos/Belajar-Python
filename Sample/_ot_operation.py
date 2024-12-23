import calendar
import json

nilai_gapok = 0
penyimpanan_harian = []
penyimpanan_bulanan = {}
penyimpanan_tahunan = {}
global tanggal
global bulan
global tahun
global jam_lembur
global jam_pertama
global jam_selanjutnya

def data_overtime():
    return

def input_overtime():
    if nilai_gapok == 0:
        print("Gapok masih 0, mau masukkin gapoknya?")
        print("1. Ya")
        print("2. Tidak")
        p = int(input())
        if p == 1:
            input_gapok()
    print("Masukkan Tanggal 1 - 31: ")
    tanggal = int(input())
    print("Masukkan Bulan 1 - 12: ")
    bulan = int(input())
    print("Masukkan Tahun 1970 - Sekarang: ")
    tahun = int(input())
    print("Masukkan Jam Lembur: ")
    jam_lembur = float(input())

    gaji_perjam =  nilai_gapok * 1 / 176
    jam_selanjutnya = (jam_lembur - 1) * 2
    cal = calendar.weekday(tahun, bulan, tanggal)

    if cal == 5 or cal == 6:
        jam_pertama = 2
    else:
        jam_pertama = 1.5

    hasil_perkalian_jam = jam_pertama + jam_selanjutnya
    hasil_uang_lemburan = gaji_perjam * hasil_perkalian_jam

    b = True
    for i in penyimpanan_harian:
        b = f"{tanggal}/{bulan}/{tahun}" not in i

    if b:
        penyimpanan_harian.append({'Tanggal' : f"{tanggal}/{bulan}/{tahun}", 'Jam lembur' : jam_lembur, "Perkalian jam lembur" : hasil_perkalian_jam, "Nominal uang lembur" : hasil_uang_lemburan})
    else:
        g = penyimpanan_harian.index({'Tanggal' : f"{tanggal}/{bulan}/{tahun}", 'Jam lembur' : jam_lembur, "Perkalian jam lembur" : hasil_perkalian_jam, "Nominal uang lembur" : hasil_uang_lemburan})
        penyimpanan_harian[g] = {'Tanggal' : f"{tanggal}/{bulan}/{tahun}", 'Jam lembur' : jam_lembur, "Perkalian jam lembur" : hasil_perkalian_jam, "Nominal uang lembur" : hasil_uang_lemburan}

    penyimpanan_bulanan[bulan] = penyimpanan_harian
    penyimpanan_tahunan[tahun] = penyimpanan_bulanan

    s = json.dumps(penyimpanan_tahunan)

    with open('../Data/data-overtime.json', 'w') as p:
        simpan = p.write(s)

    if simpan:
        print("Berhasil disimpan")
    else:
        print("Gagal menyimpan")

    p.close()

    print(nilai_gapok)

def edit_overtime():
    return

def hapus_overtime():
    return

def input_gapok():
    global nilai_gapok
    print("Silahkan masukkan gapoknya.")
    nilai_gapok = float(input())
    print(f"Gapok sudah diisi: {nilai_gapok}")