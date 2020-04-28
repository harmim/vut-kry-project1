from sys import argv
from urllib.request import urlopen
from base64 import b64decode

messages = \
    urlopen(f'http://pcocenas.fit.vutbr.cz/?login={argv[2]}&cnt={argv[3]}')
with open(argv[1], 'w') as f:
    for line in messages:
        print(b64decode(line).hex(), file=f)
