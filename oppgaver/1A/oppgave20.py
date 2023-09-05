# a
string = "100 m"

number = int(string[:3])
print(number, type(number))

# b
string = "300 000 km/s"

number = int(string[:3] + string[4:7])
print(number, type(number))

# c (antar at det er ett tall som er splittet opp)
string = "2,718 281 828 459 045"

number = float(string.translate(str.maketrans({" ": "", ",": "."})))

print(number, type(number))
