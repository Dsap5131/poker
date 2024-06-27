"""Code for Deck"""

import random

from typing import Self

from src.common.card import Card

class Deck():
    """A Deck represents a list of cards used for a game.

    @param: Cards: [Card]: List of cards from 0 to X
    """


    def __init__(self: Self, cards: list[Card]) -> None:
        self.__test_constructor_parameters(cards)
        self.__draw_pile = cards
        self.__discard_pile = []


    def __test_constructor_parameters(self: Self, cards: list[Card]) -> None:
        """Check the parameters passed to __init__"""

        if not isinstance(cards, list):
            raise TypeError("cards needs to be a list of cards")

        for card in cards:
            if not isinstance(card, Card):
                raise TypeError("Every card in cards need to be a type Card")


    def view_draw_pile(self: Self) -> list[Card]:
        """Return draw_pile"""

        return list(self.__draw_pile)


    def view_discard_pile(self: Self) -> list[Card]:
        """Return discard_pile"""

        return list(self.__discard_pile)

    def deck_size(self: Self) -> int:
        """Return the total number of cards in the deck."""

        return len(self.__draw_pile) + len(self.__discard_pile)


    def draw_size(self: Self) -> int:
        """Return the total number of cards left to draw."""
        
        return len(self.__draw_pile)


    def draw(self: Self, to_draw: int = 1) -> list[Card]:
        """Return to_draw number of cards from the deck.

        to_draw must be >= 1 and <= the number of cards in the deck."""
        
        self.__test_draw_parameters(to_draw)
        cards = self.__draw_pile[:to_draw]
        self.__draw_pile = self.__draw_pile[to_draw:]
        self.__discard_pile += cards
        return list(cards)

    def __test_draw_parameters(self: Self, to_draw: int) -> None:
        """Check the parameters passed to draw."""

        if not isinstance(to_draw, int):
            raise TypeError('to_draw must be type int')

        if self.draw_size() == 0:
            raise StopIteration('The deck is empty')

        if to_draw > self.draw_size():
            raise ValueError('You cannot overdraw the deck.')

        if to_draw < 1:
            raise ValueError('You must draw >= 1 number of Cards')


    def shuffle(self: Self) -> None:
        """Return all cards to the draw_pile in a random order."""

        self.__draw_pile += self.__discard_pile
        self.__discard_pile = []
        random.shuffle(self.__draw_pile)

    def __eq__(self: Self, other: object) -> bool:
        return (isinstance(other, Deck) and
                self.deck_size() == other.deck_size() and
                self.draw_size() == other.draw_size() and
                self.view_draw_pile() == other.view_draw_pile() and
                self.view_discard_pile() == other.view_discard_pile())
