import string


def main() -> None:
    alphabet = string.ascii_lowercase + "æøå"
    encryption_dict = {
        letter: alphabet[(i + 2) % len(alphabet)] for i, letter in enumerate(alphabet)
    }

    encryption_table = str.maketrans(encryption_dict)

    text = "Eiusmod nostrud ea exercitation do est elit aliqua."

    encoded_text = text.translate(encryption_table)

    decryption_dict = {v: k for k, v in encryption_dict.items()}
    decryption_table = str.maketrans(decryption_dict)

    decoded_text = encoded_text.translate(decryption_table)

    print(text)
    print(encoded_text)
    print(decoded_text)


if __name__ == "__main__":
    main()
