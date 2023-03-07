# https://docs.python.org/3/library/zipfile.html
import zipfile

filename = 'archive.zip'
password = 'mypassword'

with zipfile.ZipFile(filename, mode='w', compression=zipfile.ZIP_DEFLATED) as archive:
    archive.setpassword(password)
    archive.write('file1.txt')
    archive.write('file2.txt')
    archive.write('file3.txt')

print(f'Archive file "{filename}" has been created with password "{password}".')
