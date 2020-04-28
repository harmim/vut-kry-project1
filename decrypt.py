from sys import argv
from urllib.request import urlopen

message = urlopen(f'http://pcocenas.fit.vutbr.cz/?login={argv[2]}').read()
with open(argv[1], 'r') as key:
    key = bytes.fromhex(key.read())
    print(bytes(a ^ b for (a, b) in zip(key, message)).decode('utf-8'))
