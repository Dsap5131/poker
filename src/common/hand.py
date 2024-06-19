"""Code for Hand"""

from typing import Self

from src.common.card import Card

class Hand():
    """A Hand represents a set of cards owned by a player.

    @param: cards: [Card]: List of cards from 0 to X
    """

    def __init__(self: Self, cards: list[Card]) -> None:
        self.__test_constructor_parameters(cards)
        self.__cards = cards


    def __test_constructor_parameters(self: Self, cards: list[Card]) -> None:
        """Check the parameters passed to __init__"""

        if not isinstance(cards, list):
            raise TypeError("cards needs to be a list of cards")

        for card in cards:
            if not isinstance(card, Card):
                raise TypeError("Every card in cards need to be a type Card")


    def get_cards(self: Self) -> list[Card]:
        """Return the list of cards."""

        return list(self.__cards)


    def __eq__(self: Self, other: object) -> bool:
        return (isinstance(other, Hand) and
                self.get_cards() == other.get_cards())
