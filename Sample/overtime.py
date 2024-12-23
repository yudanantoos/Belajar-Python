import _ot_operation

while(True):
    # Menu
    print("")
    print("="*45+" OVERTIME "+"="*45)
    print("Silahkan Pilih Menu")
    print("1. Data Overtime")
    print("2. Input Overtime")
    print("3. Edit Overtime")
    print("4. Hapus Overtime")
    print("5. Input Gapok")
    print("6. Exit Program")
    masukan = input()
    if masukan == '1':
        _ot_operation.data_overtime()
    elif masukan == '2':
        _ot_operation.input_overtime()
    elif masukan == '3':
        _ot_operation.edit_overtime()
    elif masukan == '4':
        _ot_operation.hapus_overtime()
    elif masukan == '5':
        _ot_operation.input_gaji_pokok()
    elif masukan == '6':
        print("Program ditutup!")
        exit()
    else:
        print("Kamu salah memasukkan perintah!")