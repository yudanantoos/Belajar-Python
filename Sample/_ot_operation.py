main_menu = False
nilai_gapok = 0
penyimpanan = []
tanggal = ""
bulan = ""
tahun = ""
jam_lembur = 0

def data_overtime():
    return

def input_overtime():
    if nilai_gapok == 0:
        print("Gapok masih 0, mau masukkin gapoknya?")
        print("1. Ya")
        print("2. Tidak")
        p = int(input())
        if p == 1:
            o = int(input())
            input_gapok(o)
    print("Masukkan Tanggal: ")
    tanggal = int(input())
    print("Masukkan Bulan: ")
    bulan = int(input())
    print("Masukkan Tahun: ")
    tahun = int(input())
    print("Masukkan Jam Lembur: ")
    jam_lembur = float(input())

    rumus = nilai_gapok * 1 / 176
    tem = {tahun : {"Tanggal" : tanggal, "Bulan" : bulan, "Tahun" : tahun, "Jam Lembur" : jam_lembur}}


def edit_overtime():
    return

def hapus_overtime():
    return

def input_gapok():
    print("Silahkan masukkan gapoknya.")
    nilai_gapok = input()

    print(f"Gapok sudah diisi: {nilai_gapok}")