### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# self needs to be removed in a function
  def check_for_ace(self, card):
    # here it should be "if card.value == 1"
    if card.value = 1:
      return True
    else
      return False
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
# it needs to be def instead of dif, also the comma is missing between card1 and card2 in ()
# return card1 else return card2, the 1 is missing after "return card"


def cards_total(self, cards):
  # this total can't stand alone without a value 
  total 
  for card in cards:
    total += card.value
    return "You have a total of" + total
 
```
