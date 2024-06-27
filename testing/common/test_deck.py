"""Code to test a deck."""

import pytest

from src.common.suit import Suit
from src.common.rank import Rank
from src.common.card import Card
from src.common.deck import Deck


def test_valid_constructor() -> None:
    """Test a valid use of the constructor."""

    Deck([Card(Rank.TEN, Suit.CLUB)])


def test_invalid_constructor_not_list() -> None:
    """Test constructor by passing not a list."""

    with pytest.raises(TypeError):
        Deck("Not a list :)")


def test_invalid_constructor_bad_list() -> None:
    """Test constructor by passing a bad list."""

    with pytest.raises(TypeError):
        Deck(["Jack of Clubs",
              Card(Rank.JACK, Suit.CLUB)])


def test_view_draw_pile() -> None:
    """Test view draw pile."""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.KING, Suit.SPADE),
                 Card(Rank.TWO, Suit.HEART)])
    expected = [Card(Rank.JACK, Suit.CLUB),
                Card(Rank.KING, Suit.SPADE),
                Card(Rank.TWO, Suit.HEART)]
    assert deck.view_draw_pile() == expected, \
            'view_draw_pile() not working'


def test_view_draw_pile_muta() -> None:
    """Test view_draw_pile mutability"""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.KING, Suit.SPADE),
                 Card(Rank.TWO, Suit.HEART)])
    expected = [Card(Rank.JACK, Suit.CLUB),
                Card(Rank.KING, Suit.SPADE),
                Card(Rank.TWO, Suit.HEART)]
    draw_pile = deck.view_draw_pile()
    assert draw_pile == expected, 'Test setup failed.'

    expected_muta = [Card(Rank.KING, Suit.SPADE),
                     Card(Rank.KING, Suit.SPADE),
                     Card(Rank.TWO, Suit.HEART)]
    draw_pile[0] = Card(Rank.KING, Suit.SPADE)
    assert draw_pile != expected and draw_pile == expected_muta, \
            'Test setup failed.'

    muta_deck = Deck([Card(Rank.KING, Suit.SPADE),
                      Card(Rank.KING, Suit.SPADE),
                      Card(Rank.TWO, Suit.HEART)])
    orig_deck = Deck([Card(Rank.JACK, Suit.CLUB),
                      Card(Rank.KING, Suit.SPADE),
                      Card(Rank.TWO, Suit.HEART)])
    assert deck == orig_deck and deck != muta_deck, \
            'deck is mutable.'


def test_view_discard_pile() -> None:
    """Test view_discard_pile"""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.KING, Suit.SPADE),
                 Card(Rank.TWO, Suit.HEART)])
    deck.draw(2)
    expected = [Card(Rank.JACK, Suit.CLUB),
                Card(Rank.KING, Suit.SPADE)]
    discard_pile = deck.view_discard_pile()
    assert discard_pile == expected, \
            'view_discard_pile not working.' 
    
    deck_orig = Deck([Card(Rank.JACK, Suit.CLUB),
                      Card(Rank.KING, Suit.SPADE),
                      Card(Rank.TWO, Suit.HEART)])
    deck_orig.draw(2)
    assert deck_orig == deck, 'view_discard_pile not working.'


def test_view_discard_pile_muta() -> None:
    """Test view_discard_pile mutability"""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.KING, Suit.SPADE),
                 Card(Rank.TWO, Suit.HEART)])
    deck.draw(2)
    expected = [Card(Rank.JACK, Suit.CLUB),
                Card(Rank.KING, Suit.SPADE)]
    discard_pile = deck.view_discard_pile()
    assert discard_pile == expected, \
            'view_discard_pile not working.' 
    
    deck_orig = Deck([Card(Rank.JACK, Suit.CLUB),
                      Card(Rank.KING, Suit.SPADE),
                      Card(Rank.TWO, Suit.HEART)])
    deck_orig.draw(2)
    assert deck_orig == deck, 'view_discard_pile not working.'


    discard_pile[0] = Card(Rank.KING, Suit.SPADE)
    expected_muta = [Card(Rank.KING, Suit.SPADE),
                     Card(Rank.KING, Suit.SPADE)]
    assert discard_pile != expected and discard_pile == expected_muta, \
            'Test setup failed.'

    deck_muta = Deck([Card(Rank.KING, Suit.SPADE),
                      Card(Rank.KING, Suit.SPADE),
                      Card(Rank.TWO, Suit.HEART)])
    deck_muta.draw(2)
    assert deck == deck_orig and deck != deck_muta, \
            'Deck is mutable'


def test_draw() -> None:
    """Test basic usage of draw(n)."""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.TWO, Suit.SPADE)])
    card = deck.draw()

    assert card == [Card(Rank.JACK, Suit.CLUB)], \
            'draw not returning the top card.'
    assert deck.view_discard_pile() == [Card(Rank.JACK, Suit.CLUB)], \
            'simple draw not working.'
    assert deck.view_draw_pile() == [Card(Rank.TWO, Suit.SPADE)], \
            'simple draw not working.'


def test_draw_consecutive() -> None:
    """Test chained uses of draw(n)."""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.TWO, Suit.SPADE)])
    assert deck.draw() == [Card(Rank.JACK, Suit.CLUB)], \
            'simple draw not working'
    assert deck.view_draw_pile() == [Card(Rank.TWO, Suit.SPADE)], \
            'simple draw not working'
    assert deck.view_discard_pile() == [Card(Rank.JACK, Suit.CLUB)], \
            'simple draw not working'

    assert deck.draw() == [Card(Rank.TWO, Suit.SPADE)], \
            'consecutive draw not working'
    assert deck.view_draw_pile() == [], \
            'consecutive draw not working'
    assert deck.view_discard_pile() == [Card(Rank.JACK,Suit.CLUB),
                                        Card(Rank.TWO,Suit.SPADE)], \
            'consecutive draw not working'


def test_multi_draw() -> None:
    """Test usage of draw(n) when drawing multiple."""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.TWO, Suit.SPADE),
                 Card(Rank.KING, Suit.HEART)])
    cards = deck.draw(2)
    expected_cards = [Card(Rank.JACK, Suit.CLUB),
                      Card(Rank.TWO, Suit.SPADE)]

    assert cards == expected_cards, \
            'Draw not returning the top two cards.'


def test_muta_multi_draw() -> None:
    """Test draw(n > 1) does not cause mutability risks."""

    deck = Deck([Card(Rank.JACK, Suit.CLUB),
                 Card(Rank.TWO, Suit.SPADE),
                 Card(Rank.KING, Suit.HEART)])
    cards = deck.draw(2)
    expected = [Card(Rank.JACK, Suit.CLUB),
                Card(Rank.TWO, Suit.SPADE)]

    assert cards == expected, 'Multi draw not working.'

    deck_orig = Deck([Card(Rank.JACK, Suit.CLUB),
                      Card(Rank.TWO, Suit.SPADE),
                      Card(Rank.KING, Suit.HEART)])
    deck_orig.draw(2)
    assert deck == deck_orig, 'Test Setup failed.'    

    cards[0] = Card(Rank.KING, Suit.HEART)
    expected_muta = [Card(Rank.KING, Suit.HEART),
                     Card(Rank.TWO, Suit.SPADE)]
    assert cards != expected and cards == expected_muta, \
            'Test Setup failed.'
    
    deck_muta = Deck([Card(Rank.KING, Suit.HEART),
                      Card(Rank.TWO, Suit.SPADE),
                      Card(Rank.KING, Suit.HEART)])
    deck_muta.draw(2)

    assert deck != deck_muta and deck == deck_orig, \
            'deck is mutable from draw.'


def test_draw_empty_deck() -> None:
    """Test draw on an empty deck."""

    with pytest.raises(StopIteration):
        deck = Deck([])
        deck.draw()


def test_draw_overdraw() -> None:
    """Test overdrawing on a deck."""

    with pytest.raises(ValueError):
        deck = Deck([Card(Rank.KING, Suit.HEART)])
        deck.draw(2)


def test_draw_non_integer() -> None:
    """Test draw with invalid parameter that isn't an integer."""

    with pytest.raises(TypeError):
        deck = Deck([Card(Rank.KING, Suit.HEART)])
        deck.draw("1")


def test_draw_negative() -> None:
    """Test draw against negative int parameter."""

    with pytest.raises(ValueError):
        deck = Deck([Card(Rank.KING, Suit.HEART)])
        deck.draw(-1)


def test_draw_zero() -> None:
    """Test draw against zero."""

    with pytest.raises(ValueError):
        deck = Deck([Card(Rank.KING, Suit.HEART)])
        deck.draw(0)


def test_draw_size() -> None:
    """Test draw_size()."""

    deck = Deck([Card(Rank.KING, Suit.HEART),
                 Card(Rank.KING, Suit.HEART)])
    assert deck.draw_size() == 2, 'Incorrect draw_size amount'
    deck.draw(1)
    assert deck.draw_size() == 1, 'Incorrect draw_size amount'
    deck.draw(1)
    assert deck.draw_size() == 0, 'Incorrect draw_size amount'


def test_deck_size() -> None:
    """Test deck_size()."""

    deck = Deck([Card(Rank.KING, Suit.HEART),
                 Card(Rank.KING, Suit.HEART)])
    assert deck.deck_size() == 2, 'Incorrect deck_size amount'
    deck.draw(1)
    assert deck.deck_size() == 2, 'Incorrect deck_size amount'

def test_draw_extensive() -> None:
    """Test that after drawing all cards the deck is empty and errors."""

    deck = Deck([Card(Rank.KING, Suit.HEART)])
    assert deck.draw_size() == 1, 'draw_size not working correctly.'
    deck.draw(1)
    assert deck.draw_size() == 0, 'draw_size or draw not working correctly.'
    with pytest.raises(StopIteration):
        deck.draw(1)


def test_shuffle() -> None:
    """
    Test that the deck is shuffled in a random order 
    and draw pile is reset.
    """

    deck = Deck([Card(Rank.KING, Suit.HEART),
                 Card(Rank.TEN, Suit.SPADE)])
    actual_1 = deck.draw(2)
    expected_1 = [Card(Rank.KING, Suit.HEART),
                  Card(Rank.TEN, Suit.SPADE)]
    assert actual_1 == expected_1, 'initial draw not working'

    deck.shuffle()
    assert deck.deck_size() == deck.draw_size(), 'Deck not properly reset.'
    actual_2 = deck.draw(2)
    deck_expected = Deck([Card(Rank.TEN, Suit.SPADE),
                          Card(Rank.KING, Suit.HEART)])
    expected_2 = deck_expected.draw(2)
    assert actual_2 == expected_2 and deck == deck_expected, \
            'shuffle not working.'


def test_eq_other_obj() -> None:
    """Test __eq__ against other object."""

    deck = Deck([Card(Rank.TEN, Suit.SPADE)])

    assert deck != 'deck', 'Deck should not equal a non-Deck'


def test_eq_diff_basic_deck() -> None:
    """Test __eq__ against a different deck."""

    deck_1 = Deck([Card(Rank.TEN, Suit.SPADE),
                   Card(Rank.TEN, Suit.SPADE)])
    deck_2 = Deck([Card(Rank.TEN, Suit.SPADE)])

    assert deck_1 != deck_2, \
            'Two different basic decks should be unequal.'


def test_eq_diff_complex_deck() -> None:
    """Test __eq__ against a deck with the same cards but different piles."""

    deck_1 = Deck([Card(Rank.TEN, Suit.SPADE),
                   Card(Rank.TWO, Suit.HEART)])
    deck_1.draw()
    deck_2 = Deck([Card(Rank.TEN, Suit.SPADE),
                   Card(Rank.TWO, Suit.HEART)])

    assert deck_1 != deck_2, \
            'Two different complex deck should be unequal.'

def test_eq_same_complex_deck() -> None:
    """Test __eq__ against a deck with the same cards and same piles."""

    deck_1 = Deck([Card(Rank.TEN, Suit.SPADE),
                   Card(Rank.TWO, Suit.HEART)])
    deck_1.draw()
    deck_2 = Deck([Card(Rank.TEN, Suit.SPADE),
                   Card(Rank.TWO, Suit.HEART)])
    deck_2.draw()

    assert deck_1 == deck_2, \
            'Two equal complex decks should return true.'


def test_eq_same_basic_deck() -> None:
    """Test __eq__ against a equal deck."""

    deck_1 = Deck([Card(Rank.TEN, Suit.SPADE),
                   Card(Rank.TWO, Suit.HEART)])
    deck_2 = Deck([Card(Rank.TEN, Suit.SPADE),
                   Card(Rank.TWO, Suit.HEART)])
    assert deck_1 == deck_2, \
            "Two of the same basic decks should be equal."
