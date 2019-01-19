from cards import Card
from cards import Deck
import unittest
class CardTests(unittest.TestCase):
  def setUp(self):
    self.card = Card("A", "Hearts")
  
  def test_init(self):
    """a card should have a suit and a value"""
    self.assertEqual(self.card.suit, "Hearts")
    self.assertEqual(self.card.value, "A")

  def test_repr(self):
    """ _repr_ should return a string in the form of 'Value of Suit' """
    self.assertEqual(repr(self.card), "A of Hearts")
  
class DeckTests(unittest.TestCase):
  def setUp(self):
    self.deck = Deck()
  
  def test_init(self):
    """ a deck should have a cards attribute which is a list consisting of 52 cards """
    self.assertIsInstance(self.deck.cards, list)
    self.assertEqual(len(self.deck.cards), 52)
  
  def test_repr(self):
    self.assertEqual(repr(self.deck), "Deck of 52 cards")
  
  def test_count(self):
    """ count should return count of the number of cards in the deck"""
    self.assertEqual(self.deck.count(), 52)
    self.deck.cards.pop()
    self.assertEqual(self.deck.count(), 51)

  def test_deal_sufficient_cards(self):
    """ _deal should deal number of cards specified """
    self.cards = self.deck._deal(10)
    self.assertEqual(len(self.cards), 10)
    self.assertEqual(self.deck.count(), 42)
  
  def test_deal_insufficient_cards(self):
    """_ deal should deal number of cards left in the deck if specified number is high"""
    self.cards = self.deck._deal(100)
    self.assertEqual(len(self.cards), 52)
    self.assertEqual(self.deck.count(), 0)
  
  def test_deal_no_cards(self):
    """_deal should throw a ValueError if there is no cards left in the deck"""
    self.deck._deal(self.deck.count()) 
    with self.assertRaises(ValueError):
      self.deck._deal(1)
  
  def test_deal_card(self):
    """deal_card should deal a single card from the deck """
    card = self.deck.cards[-1]
    dealt_card = self.deck.deal_card()
    self.assertEqual(card, dealt_card)
    self.assertEqual(self.deck.count(), 51)
  
  def test_deal_hand(self):
    """ deal_hand should deal number of cards specified from the deck"""
    hand = self.deck.deal_hand(20)
    self.assertEqual(len(hand), 20)
    self.assertEqual(self.deck.count(), 32)
  
  def test_shuffle_deck(self):
    """ shuffle should shuffle the deck only when it is full"""
    cards = self.deck.cards[:]
    self.deck.shuffle()
    self.assertNotEqual(cards, self.deck.cards)
    self.assertEqual(self.deck.count(), 52)
  
  def test_shuffle_not_full_deck(self):
    """shuffle should throw a ValueError when tried shuffling not a full deck"""
    self.deck._deal(1) 
    with self.assertRaises(ValueError): 
      self.deck.shuffle()
  
if __name__ == '__main__':
  unittest.main()
