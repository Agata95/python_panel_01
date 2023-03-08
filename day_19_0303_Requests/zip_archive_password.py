# https://docs.python.org/3/library/zipfile.html

import pyminizip

filename = 'mini_archive.zip'
password = 'haselko'
compress_level = 4
lista_plikow = ["file1.txt", "file2.txt", "file3.txt"]

pyminizip.compress_multiple(lista_plikow, [], "miniarchive.zip", password, int(compress_level))

print(f'Archive file "{filename}" has been created with password "{password}".')
