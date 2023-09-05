string = "Datamaskiner er ubrukelige. De kan bare gi oss svar."

# Løsning 1
print(string[:12], string[31:34], string[40:])

# Løsning 2
words = string.split(" ")

print(words[0], words[4], words[6], words[7], words[8])
