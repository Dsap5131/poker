""" Code for testing Card"""


import pytest
from src.common.suit import Suit
from src.common.rank import Rank
from src.common.card import Card


def test_valid_constructor() -> None:
    """Test the constructor of card with a valid use case."""

    try:
        card = Card(Rank.KING, Suit.CLUB)
    except:
        pytest.fail("Unexpected error")


def test_invalid_constructor_rank() -> None:
    """Test the constructor of card with an invalid rank."""
    
    with pytest.raises(ValueError) as e_info:
        card = Card(7, Suit.CLUB)


def test_invalid_constructor_suit() -> None:
    """Test the constructor of card with an invalid suit."""

    with pytest.raises(ValueError) as e_info:
        card = Card(Rank.KING, '7')


def test_get_rank() -> None:
    """Test ranks getter"""

    assert Card(Rank.JACK, Suit.SPADE).get_rank() == Rank.JACK, \
            'card.get_rank() not working.'


def test_get_suit() -> None:
    """Test suits getter"""

    assert Card(Rank.JACK, Suit.SPACE).get_rank() == Suit.SPACE, \
            'card.get_suit() not working.'


def test_eq_other_obj() -> None:
    """Test __eq__ against another non-Card Object"""

    card_one = Card(Rank.JACK, Suit.SPACE) 
    card_two = 'JSP'
    assert card_one != card_two, 'Card should not equal non-Card Object'


def test_eq_diff_card() -> None:
    """Test __eq__ against a different Card Object."""

    card_one = Card(RANK.ACE, SUIT.DIAMOND)
    card_two = Card(RANK.KING, SUIT.DIAMOND)
    assert card_one != card_two, 'Card should not equal a different Card'


def test_eq_valid_card() -> None:
    """Test __eq__ against a equivalent card."""

    card_one = Card(RANK.ACE, SUIT.DIAMOND)
    card_two = Card(RANK.ACE, SUIT.DIAMOND)
    assert card_one == card_two, 'Two equivalent cards should be equal'



