# Author: Dominik Harmim <harmim6@gmail.com>

LOGIN := xharmi00
CNT := 50

MESSAGES := messages.txt
KEY := key.txt
PACK := $(LOGIN).zip



.PHONY: generate
generate: clean $(MESSAGES)

$(MESSAGES): generate.py
	python3 $< $@ $(LOGIN) $(CNT)


.PHONY: keylen
keylen: keylen.py $(KEY)
	python3 $^


.PHONY: binarykey
binarykey: $(LOGIN).txt

$(LOGIN).txt: binarykey.py $(KEY)
	python3 $^ $@


.PHONY: decrypt
decrypt: decrypt.py $(KEY)
	python3 $^ $(LOGIN)


.PHONY: pack
pack: $(PACK)

$(PACK): $(LOGIN).txt
	zip $@ $^


.PHONY: clean
clean:
	rm -f $(MESSAGES) $(PACK)
