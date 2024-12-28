import configparser

pengaturan = configparser.ConfigParser()
pengaturan['DEFAULT'] = {'DataDir' : '../Data',
                         'DataFile' : '${DataDir}/data.json'}
pengaturan['data.gapok'] = {'Gapok' : '0'}

def simpan_pengaturan():
    with open('example.in', 'w') as simpan:
        pengaturan.write(simpan)

def load_pengaturan():
    """"""

