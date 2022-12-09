from pathlib import Path
from icecream import ic
import dumper

contents = Path("file1.txt").read_text()

print(f"{type(contents)} -> {contents}")
print("Dumper:")
dumper.dump(contents)
print("-------------")
print(ic(contents))


with open("file1.txt", 'r') as plik:
    contents = plik.readlines()

print(f"{type(contents)} -> {contents}")
print("Dumper:")
dumper.dump(contents)
print("-------------")

print(ic(contents))

