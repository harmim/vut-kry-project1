from sys import argv

with open(argv[1], 'r') as key:
    with open(argv[2], 'wb') as f:
        f.write(bytes.fromhex(key.read()))
