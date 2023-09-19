def is_palindrome(text: str) -> bool:
    return text == text[::-1]


def main() -> None:
    assert is_palindrome("121")
    assert not is_palindrome("123")
    assert is_palindrome("1221")


if __name__ == "__main__":
    main()
