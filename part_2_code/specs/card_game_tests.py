import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    

    def test_check_has_ace_false(self):
        card = Card("diamond", 5)
        self.assertFalse(CardGame.check_for_ace(self,card))

    def test_check_has_ace_true(self):
        card = Card("heart", 1)
        self.assertTrue(CardGame.check_for_ace(self, card))
    
    def test_highest_card(self):
        card1 = Card("diamond", 2)
        card2 = Card("heart", 7)
        self.assertEqual(CardGame.highest_card(self, card1, card2), card2)
    
#    takes in 2 arguments when we put in the function and then what we actually expect
      
    def test_total(self):
        cards = []
        card1 = Card("diamond", 2)
        cards.append(card1)

        card2 = Card("heart", 7)
        cards.append(card2)

        self.assertEqual(CardGame.cards_total(self, cards),"You have a total of 9")

# 9 is an integer but must be turned into a string here
