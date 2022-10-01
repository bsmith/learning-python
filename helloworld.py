#!python3
""" Hello World """
import hashlib

m = hashlib.sha256()
m.update(b"Hello World")
print("Hello World")
print(m.hexdigest())
