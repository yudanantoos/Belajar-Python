import configparser

pengaturan = configparser.ConfigParser()
pengaturan['DEFAULT'] = {'datadir' : '../Data',
                         'datafile' : '${datadir}/data-overtime.json',
                         'gapok' : 0}

def simpan_pengaturan():
    with open('tes.ini', 'w') as simpan:
        pengaturan.write(simpan)

def load_pengaturan():
    pengaturan.read('tes.ini')
    pengaturan.sections()
    return pengaturan