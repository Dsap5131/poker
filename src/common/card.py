"""Code for a playing card"""

from typing import Self

from src.common.suit import Suit
from src.common.rank import Rank

class Card():
    """Represents a playing card.

    @param: rank: Rank
    @param: suit: Suit
    """

    def __init__(self: Self, rank: Rank, suit: Suit) -> None:

        self.__test_constructor_parameters(rank, suit)
        self.__rank = rank
        self.__suit = suit


    def __test_constructor_parameters(self: Self,
                                      rank: Rank,
                                      suit: Suit) -> None:
        """Check the parameters passed to __init__"""

        if not isinstance(rank, Rank):
            raise TypeError("rank must be type Rank.")
        if not isinstance(suit, Suit):
            raise TypeError("suit must be type Suit.")


    def get_rank(self: Self) -> Rank:
        """Return the rank of the card."""

        return self.__rank


    def get_suit(self: Self) -> Suit:
        """Return the suit of the card."""

        return self.__suit


    def __eq__(self: Self, other: object) -> bool:
        return (isinstance(other, Card) and
                self.get_rank() == other.get_rank() and
                self.get_suit() == other.get_suit())
