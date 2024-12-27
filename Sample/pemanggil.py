import dipanggil
from Sample.dipanggil import Nyobaan

#dipanggil.yang_dipanggil()

"""
Kesimpulan from dan import
- nama file 2 kata atau lebih tidak bisa pakai strip '-' tapi bisa pakai underscore '_'
Fungsi file __init__.py
- dieksekusi ketika file lain mengimport package
- digunakan ketika file lain import packagenya saja, di file __init__.py harus dideklarasikan "from" nya
- seperti from . import (nama_file)
- format di atas kalau di eksekusi langsung error
- kalau mau dieksekusi langsung harus disebutkan nama package nya
- jadi format di atas dipakai di file __init__.py yang tidak di eksekusi tapi sebatas deklarasi
"""

p = dipanggil
p.tes_var = 10
print(p.tes_var)
print(type(p))
print(type(p.tes_var))

q = Nyobaan()
q.tes_var_class = 10
print(q)
print(q.tes_var_class)
print(type(q))
print(type(q.tes_var_class))