from sys import argv

with open(argv[1], 'r') as f:
    print(len(bytes.fromhex(f.read())))
