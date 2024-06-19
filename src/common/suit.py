"""Source code of the suit of a playing card."""


from enum import Enum


class Suit(Enum):
    """Represents the suit of a playing card."""

    CLUB = 1
    SPADE = 2
    HEART = 3
    DIAMOND = 4
