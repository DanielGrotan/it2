import math
from dataclasses import dataclass


@dataclass
class Store:
    name: str
    prices: dict[str, int]


def get_total_price(shopping_list: list[str], store: Store) -> int | None:
    """Returns the total price of the given shopping list if it were purchased in the given stores

    Parameters
    ----------
    shopping_list : list[str]
        A list of product names
    store : Store
        The store with specified prices for all products in stock

    Returns
    -------
    int | None
        Either the total price, or None if at least one of the products doesn't exist in the store
    """

    total_price = 0

    for product in shopping_list:
        price = store.prices.get(product)

        if price is None:
            return

        total_price += price

    return total_price


def find_cheapest_store(shopping_list: list[str], stores: list[Store]) -> str | None:
    """Find the cheapest store to purchase a list of products from

    Parameters
    ----------
    shopping_list : list[str]
        A list of product names
    stores : list[Store]
        A list of stores to compare prices from

    Returns
    -------
    str | None
        Either the name of the cheapest store, or None if none of the stores contain all the wanted products
    """

    if not shopping_list:
        return

    cheapest_price = math.inf
    cheapest_store_name = None

    for store in stores:
        total_price = get_total_price(shopping_list, store)

        if total_price is None:
            continue

        if total_price < cheapest_price:
            cheapest_price = total_price
            cheapest_store_name = store.name

    return cheapest_store_name


def main() -> None:
    stores = [
        Store("REMA 1000", {"salat": 12, "fisk": 99, "melk": 12, "brod": 12}),
        Store("Meny", {"salat": 22, "fisk": 60, "melk": 18, "brød": 21}),
        Store("Kiwi", {"salat": 8, "fisk": 120, "melk": 10, "brød": 19}),
        Store("Spar", {"salat": 18, "fisk": 40, "melk": 30, "brød": 59}),
        Store("Joker", {"salat": 15, "fisk": 200, "melk": 40, "brød": 9}),
    ]

    print(find_cheapest_store(["salat", "fisk", "melk", "brød"], stores))


if __name__ == "__main__":
    main()
