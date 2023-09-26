personer = {}

while True:
    if input("Vil du fortsette (j/n)? ").lower() != "j":
        break

    navn, alder = input("Skriv et navn og en alder separert med ', ': ").split(", ")

    while True:
        try:
            alder = int(alder)
            break
        except ValueError:
            print("Alderen må være et tall")
            alder = input("Skriv alderen: ")

    personer[navn] = alder

while True:
    bokstav = input("Oppgi en bokstav: ")

    if len(bokstav) == 1:
        break

    print("Du må oppgi kun én bokstav")

for navn, alder in personer.items():
    if navn[0] == bokstav:
        print(f"{navn} er {alder} år gammel")
