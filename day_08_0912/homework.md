RODO ;-)

Za pomocą biblioteki https://pypi.org/project/pycrypto/

zrób tak, aby imię i nazwisko było szyfrowane, np. za pomocą AES:

```python
>>> from Crypto.Cipher import AES
>>> obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
>>> message = "The answer is no"
>>> ciphertext = obj.encrypt(message)
>>> ciphertext
'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
>>> obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
>>> obj2.decrypt(ciphertext)
'The answer is no'
```
wartość klucza niech będzie losowa tworzona w __init__ i zapisywana we właściwości private.

dodatkowo utwórz metodę zwracającą odszyfrowane dane

metoda info() niech korzysta z metody odszyfrowującej dane.