import dipanggil

dipanggil.yang_dipanggil()

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