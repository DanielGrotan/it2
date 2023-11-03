def minst_og_størst(liste: list[int]) -> tuple[int, int]:
    minst = liste[0]
    størst = liste[0]

    for tall in liste:
        minst = min(minst, tall)
        størst = max(størst, tall)

    return minst, størst


def main() -> None:
    print(
        f"Den minste og største verdien er {minst_og_størst([90, 26, 28, 88, 53, 67, 29, 18, 74, 95])}"
    )


if __name__ == "__main__":
    main()
