import calendar
import json
from pkgutil import get_loader

databasenya = "../Data/data-overtime.json"
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

def ambil_data():
    with open(databasenya, 'r') as buka:
        g = buka.readline()

    konversi = json.loads(g)

    global penyimpanan_tahunan
    penyimpanan_tahunan = konversi
    print(penyimpanan_tahunan)

    global penyimpanan_bulanan
    penyimpanan_bulanan = penyimpanan_tahunan['2024']
    print(penyimpanan_bulanan)

    global penyimpanan_harian
    penyimpanan_harian = penyimpanan_bulanan['12']
    print(penyimpanan_harian)

def input_data():
    return

def edit_data():
    return

def hapus_data():
    return