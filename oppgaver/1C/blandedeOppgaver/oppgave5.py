def main() -> None:
    text = """Gaining er en eldgammel livsstil som har eksistert i mange tusen år. Ifølge norrøn mytologi skal denne livsstilen være skapt av Gain Gainson i år 1734 f.kr. Gainson bodde i en hule like ovenfor Siljan med Gainsonstammen med om lag 48 personer. En dag tok han turen ned til Kikuthytta hvor han skulle finne steiner for det nye BBQ –bordet sitt. Da han løftet opp en 30 kg stein rik på jern kjente han en euforisk følelse igjennom hele kroppen. Han visste straks hva han skulle gjøre og tente opp et bål for å utvinne jernet fra alle steinene rundt. Han lagde da første versjon av manualer og vektskiver. Han tok så med seg masse ris og villsvin tilbake til hulensin og begynte å forberede mat. Ifølge historien droppet han faktisk BBQ sausen da det reduserte gainsopptaket. Hver dag reiste han ned til Kikkuthytta for å pumpe jern, forså og spise masse gains hjemme i hulen. Etter flere år med dette bygde han fort en flott kropp som medførte til at alle jentene i hulene villa ha Gainson, og som man har sett i nyere tid ble det mange avkom."""

    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    letters = set(alphabet)
    letter_counts = {letter: 0 for letter in letters}

    for letter in text.lower():
        if letter in letters:
            letter_counts[letter] += 1

    for letter in alphabet:
        print(f"Antall {letter}: {letter_counts[letter]}")


if __name__ == "__main__":
    main()
