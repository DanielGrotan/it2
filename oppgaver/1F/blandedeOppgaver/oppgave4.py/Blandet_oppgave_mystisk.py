def encode(text: str, cipher: int) -> str:
    """Encodes a message using the given cipher

    Parameters
    ----------
    text : str
        The message
    cipher : int
        The cipher to use when encoding

    Returns
    -------
    str
        The encoded message
    """

    new_text = ""

    for letter in text:
        ascii_code = ord(letter)
        ascii_code += cipher
        new_text += chr(ascii_code)

    return new_text


def decode(text: str, cipher: int) -> str:
    """Decodes an encoded message using a given cipher

    Parameters
    ----------
    text : str
        The encoded message
    cipher : int
        The cipher used when encoding the message

    Returns
    -------
    str
        The decoded message
    """

    new_text = ""

    for letter in text:
        ascii_code = ord(letter)
        ascii_code -= cipher
        new_text += chr(ascii_code)

    return new_text
