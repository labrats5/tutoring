import re

with open("/Users/maxwellcorbin/vs_stuff/jason/word_bank.txt") as file:
    words = file.readlines()
    for word in words:
        if re.fullmatch(r"[a-z]a[a-z]ue", word.strip()):
            print(word.strip())
