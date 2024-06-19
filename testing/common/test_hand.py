""" Code for testing Hand"""


import pytest
from src.common.suit import Suit
from src.common.rank import Rank
from src.common.card import Card
from src.common.hand import Hand


def test_valid_constructor() -> None:
    """Test the constructor of Hand with a valid use case."""

    Hand([Card(Rank.TEN, Suit.CLUB),
          Card(Rank.JACK, Suit.SPADE)])


def test_valid_constructor_empty_list() -> None:
    """Test the constructor of Hand with a valid case of an empty list."""

    Hand([])


def test_invalid_constructor_not_list() -> None:
    """Test the constructor of Hand with something other than a list."""

    with pytest.raises(TypeError):
        Hand(Card(Rank.TEN, Suit.CLUB))


def test_invalid_constructor_bad_list() -> None:
    """Test the constructor of Hand with a list of non-Cards."""

    with pytest.raises(TypeError):
        Hand([Card(Rank.TEN, Suit.CLUB),
              "Jack of Spades"])


def test_get_cards() -> None:
    """Test basic use of get cards."""

    hand = Hand([Card(Rank.TEN, Suit.CLUB),
                 Card(Rank.JACK, Suit.SPADE)])
    expected = [Card(Rank.TEN, Suit.CLUB),
                Card(Rank.JACK, Suit.SPADE)]
    assert hand.get_cards() == expected, \
            'Hand.get_cards() not working.'


def test_get_cards_mutability() -> None:
    """Test mutability of Hand through get_cards."""

    hand = Hand([Card(Rank.TEN, Suit.CLUB),
                 Card(Rank.JACK, Suit.SPADE)])
    expected = [Card(Rank.TEN, Suit.CLUB),
                  Card(Rank.JACK, Suit.SPADE)]
    actual_1 = hand.get_cards()
    assert actual_1 == expected, \
            'Hand.get_cards() not initially working.'

    actual_1[0] = 'Ten of Clubs'
    actual_2 = hand.get_cards()
    expected_altered = ['Ten of Clubs',
                        Card(Rank.JACK, Suit.SPADE)]
    assert (actual_1 != expected and
            actual_1 == expected_altered), \
            "actual_1 was not correctly altered."
    assert (actual_2 == expected and
            actual_2 != expected_altered), \
            "Hand is able to be mutated through .get_cards()."


def test_eq_other_obj() -> None:
    """Test __eq__ against another non-Hand Object"""

    hand = Hand([Card(Rank.TEN, Suit.CLUB),
                 Card(Rank.JACK, Suit.CLUB)])
    assert hand != 5, 'Hand should not equal non-Hand Object.'


def test_eq_diff_hand() -> None:
    """Test __eq__ against different Hand"""

    hand_1 = Hand([Card(Rank.TEN, Suit.CLUB),
                   Card(Rank.JACK, Suit.SPADE)])
    hand_2 = Hand([Card(Rank.TEN, Suit.CLUB),
                   Card(Rank.JACK, Suit.CLUB)])
    assert hand_1 != hand_2, 'Hand should not equal a different Hand Object'


def test_eq_same_hand() -> None:
    """Test __eq__ against same Hand"""

    hand_1 = Hand([Card(Rank.TEN, Suit.CLUB),
                   Card(Rank.JACK, Suit.SPADE)])
    hand_2 = Hand([Card(Rank.TEN, Suit.CLUB),
                   Card(Rank.JACK, Suit.SPADE)])
    assert hand_1 == hand_2, 'These Hands should be equal to each other'
