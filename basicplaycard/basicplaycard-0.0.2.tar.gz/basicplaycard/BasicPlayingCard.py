"""
A simple abstraction class for defining basic playing card objects
for arbitrary card games. Class comes pre-initialized with traditional 
playing card archetypes (such as Standard-52, Tarot, Hanfuda, etc.)
Class allows abstraction for defining custom playing card variants.

Playing Card Object Features:
- Card Value
- Card Rank
- Card Image
- Card Custom/Pre-Defined Name
- Card Value Hierarchy
- Card Rank Hierarchy
- Card Hierarchy Priority (Value vs. Rank)

What this class abstraction does NOT do:
- Advanced rulesets that are specific to paricular gameplay:
  i.e. Ace can be valued as both 1 and 14 in a standard 52-card deck

                              Examples
--------------------------------------------------------------------
TODO: Example of Creating Pre-set Cards
TODO: Example of Creating Custom Cards

TODO: Create Out-of-shelf Function To Create Custom Card Variations
lib
| _ CustomCardVariation
    | _ CustomCardProperties.csv
    | _ CustomCardValue.csv
    | _ CustomCardRank.csv
    | _ CustomCardImages
        | _ CustomCardImage1.png
        | _ ...

"""

from typing import Dict, List, Tuple
import re
import random

PRIORITY_VALUE = "PRI_VALU"
PRIORITY_RANK = "PRI_RANK"
PRIORITY_NEUTRAL = "PRI_NEUT"

SUBSTITUTION_VALUE = "{VALUE}"
SUBSTITUTION_RANK = "{RANK}"
DEFAULT_NAME_SCHEME = SUBSTITUTION_VALUE + " OF " + SUBSTITUTION_RANK

ATTRIBUTE_SEARCH_KEY = r"^[A-Z]*.*[A-Z]$"

# Card Rank Ordered By Alphabetical Lowest To Highest
STANDARD_52_VALUES = {"ACE": "A", "TWO": "2", "THREE": "3", "FOUR": "4",
                      "FIVE": "5", "SIX": "6", "SEVEN": "7", "EIGHT": "8",
                      "NINE": "9", "TEN": "10", "JACK": "J", "QUEEN": "Q", "KING": "K"}
STANDARD_52_RANKS = {"SPADES": "\u2664", "CLUBS": "\u2667", 
                     "HEARTS": "\u2665", "DIAMONDS": "\u2666"}
STANDARD_52_VALUE_HIERARCHY = {"ACE": 13, "TWO": 1, "THREE": 2, "FOUR": 3,
                               "FIVE": 4, "SIX": 5, "SEVEN": 6, "EIGHT": 7,
                               "NINE": 8, "TEN": 9, "JACK": 10, "QUEEN": 11, "KING": 12}
STANDARD_52_RANK_HIERARCHY = {"SPADES": 4, "CLUBS": 1, 
                              "HEARTS": 3, "DIAMONDS": 2}
STANDARD_52_NAME_SCHEME = SUBSTITUTION_VALUE + SUBSTITUTION_RANK

class CardVariation:
  """
  Card Variation Should Have All Information Required To Create Card
  This class can be called upon to create custom card variations
  """
  def __init__(self, cardValues: Dict[str, str], cardRanks: Dict[str, str],
               valueHierarchy: Dict[str, str], rankHierarchy: Dict[str, str],
               priority: str = PRIORITY_NEUTRAL, nameScheme: str = DEFAULT_NAME_SCHEME) -> None:
    self.VALUES = type("Values", (object,), {})
    self.RANKS = type("Ranks", (object,), {})
    self.VALUE_HIERARCHY = type("ValueHierarchy", (object,), {})
    self.RANK_HIERARCHY = type("RankHierarchy", (object,), {})
    self.PRIORITY = priority
    self.NAME_SCHEME = nameScheme
    
    for valueKey in cardValues.keys(): setattr(self.VALUES, valueKey, cardValues[valueKey])
    for rankKey in cardRanks.keys(): setattr(self.RANKS, rankKey, cardRanks[rankKey])
    for valueHierKey in valueHierarchy.keys(): setattr(self.VALUE_HIERARCHY, valueHierKey, valueHierarchy[valueHierKey])
    for rankHierKey in rankHierarchy.keys(): setattr(self.RANK_HIERARCHY, rankHierKey, rankHierarchy[rankHierKey])

STANDARD_52 = CardVariation(STANDARD_52_VALUES, STANDARD_52_RANKS,
                            STANDARD_52_VALUE_HIERARCHY, STANDARD_52_RANK_HIERARCHY,
                            nameScheme=STANDARD_52_NAME_SCHEME)

class Card:
  """
  Class: Card
  -----------
  Description:
  Simple abstraction class of a playing card. Individual playing Card
  is defined by the CardVariation schema class. Simple individual Card
  functionality includes the following
    - Follows custom string representation and printing scheme
    - Self identifies same value and rank definition with other Card objects
    - TODO: Self evaluates value and rank with other cards
    - TODO: Contains individual image of card face

  This class is ideally accessed using the Deck class but can be used directly
  to initialize specific Card representations.
  """

  def __init__(self, cardVariation: CardVariation,
                     value: str, rank: str, name: str = None) -> None:
    """
    Class Dunder Function: __init__
    -------------------------------
    Description:
    Initializes Card object specified by CardVariation scheme and specific
    card value and rank. Custom name can be set for individual card 
    initializations.

    Parameters:
      - cardVariation (CardVariation): Specified definition for Card objects
      - value (str): Value of Card object
      - rank (str): Rank of Card object
      - name (str): (Optional) Custom name for Card object
    """
    self._name = name
    self._value = value
    self._rank = rank
    self._cardVariation = cardVariation
    self._image = None  # TODO: Add Card Image Functionality

    # Default to CardVariation name scheme if custom name not provided
    if self._name is None:
      self._name = cardVariation.NAME_SCHEME.format(VALUE=value, RANK=rank)

  def __str__(self) -> str:
    """
    Class Dunder Function: __str__
    ------------------------------
    Description:
    Constructs string representation of Card object. 

    Returns:
      - name (str): String representation of Card object.
    """
    return self._name

  def __eq__(self, __o: object) -> bool:
    """
    Class Dunder Function: __eq__
    -----------------------------
    Description:
    Determines whether specified Card object have same value or rank as
    this Card representation. If specified object is not a Card, an assertion
    error is thrown.

    Returns:
      - default (bool): True if Card object is equivalent to this Card 
                        representation, False otherwise
    """
    assert(type(__o) is Card)
    return self._value == __o._value and self._rank == __o._rank

  def __ne__(self, __o: object) -> bool:
    """
    Class Dunder Function: __ne__
    -----------------------------
    Description:
    Determines whether specified Card object does not have same value or rank
    as this Card representation. If specified object is not a Card, an assertion
    error is thrown.

    Returns:
      - default (bool): True if Card object is not equivalent to this Card 
                        representation, False otherwise
    """
    assert(type(__o) is Card)
    return self._value != __o._value or self._rank != __o._rank

  def getValue(self) -> str:
    """
    Class Function: getValue
    ------------------------
    Description:
    Returns value of Card object.

    Returns:
      - value (str): Value of Card
    """
    return self._value

  def getRank(self) -> str:
    """
    Class Function: getRank
    -----------------------
    Description:
    Returns rank category of Card object.

    Returns:
      - rank (str): Rank of Card
    """
    return self._rank

  def getName(self) -> str:
    """
    Class Function: getName
    -----------------------
    Description:
    Returns name of Card. Name is initialized according to naming scheme
    defined in CardVariation.

    Returns:
      - name (str): Name of Card
    """
    return self._name

  def getImage(self):
    """
    Class Function: getImage
    ------------------------
    Description:
    Returns the image associated with this Card object
    TODO: Implement image feature of Card schema

    Returns:
      - image (None): Image of Card object
    """
    return self._image
  
  def getCardVariation(self) -> CardVariation:
    """
    Class Function: getCardVariation
    --------------------------------
    Description:
    Returns the CardVariation definition scheme used by this Card object

    Returns:
      - cardVariation (CardVariation): CardVariation definition schema
    """
    return self._cardVariation

class Deck:
  """
  Class: Deck
  -----------
  Description:
  Simple abstraction class of a deck of playing cards. Individual playing
  Card objects are defined by the CardVariation class. Simple Deck 
  functionality includes the following
    - Randomly shuffling the deck of Card objects
    - Reinitializing the deck
    - Checking the number of Card objects remaining in the deck
    - Drawing a specifed number of Card objects from the deck
    - Search for a specific Card object in the deck
  """

  def __init__(self, cardVariation: CardVariation, randomInit: bool = True) -> None:
    """
    Class Dunder Function: __init__
    -------------------------------
    Description:
    Initializes Deck object with Card objects specified by CardVariation
    definition.

    Parameters:
      - cardVariation (CardVariation): Specified definition for Card objects
      - randomInit (bool): Boolean setting to randomly initialize deck
    """
    self._deck = [Card(cardVariation, getattr(cardVariation.VALUES, cardValue), getattr(cardVariation.RANKS, cardRank))
                  for cardValue in dir(cardVariation.VALUES) if re.search(ATTRIBUTE_SEARCH_KEY, cardValue) is not None
                  for cardRank in dir(cardVariation.RANKS) if re.search(ATTRIBUTE_SEARCH_KEY, cardRank) is not None]
    self._length = len(self._deck)
    self._cardVariation = cardVariation
    self._randomInit = randomInit
    if self._randomInit:
      random.shuffle(self._deck)

  def __str__(self) -> str:
    """
    Class Dunder Function: __str__
    ------------------------------
    Description:
    Constructs string representation of Deck object. String representation
    includes number of Card objects remaining in the deck and the specific
    order of Card objects in the deck.

    Returns:
      - string (str): String representation of Deck object.
    """
    string = "Number of Cards In Deck: " + str(self._length) + "\nOrder:\n"
    for i in range(self._length):
      string += str(self._deck[i]) + "\n"
    return string
  
  def __len__(self) -> int:
    """
    Class Dunder Function: __len__
    ------------------------------
    Description:
    Returns current number of cards in the deck.

    Returns:
      - length (int): Number of Card objects remaining in deck
    """
    return self._length
  
  def getDeckSize(self) -> int:
    """
    Class Function: getDeckSize
    ---------------------------
    Description:
    Returns current number of cards in the deck.

    Returns:
      - length (int): Number of Card objects remaining in deck
    """
    return self._length

  def setRandomInit(self, randomInit: bool) -> None:
    """
    Class Function: setRandomInit
    -----------------------------
    Description:
    Sets the initialization setting for randomly shuffling
    the newly generated Deck. If randomInit is True, the next
    reinitialization of the deck (See Function reset) will be 
    randomly shuffled. If randomInit is False, the next 
    reinitialization will not be randomly shuffled (not recommended).

    Parameters:
      - randomInit (bool): Boolean setting to randomly initialize deck
    """
    self._randomInit = randomInit

  def search(self, searchCard: Card) -> int:
    """
    Class Function: search
    ----------------------
    Description:
    Searches through the existing cards in the deck for a
    specified Card object. If found, the index of the Card
    in the deck is returned. Otherwise, -1 is returned.

    Parameters:
      - searchCard (Card): Target search Card object
    
    Returns:
      - default (int): Index of specified Card object in deck.
                       Returns -1 if not found in deck
    """
    for i in range(self._length):
      if searchCard == self._deck[i]:
        return i
    return -1

  def draw(self, numCards: int = 1) -> Tuple[bool, List[Card]]:
    """
    Class Function: draw
    --------------------
    Description:
    Draws cards from the deck. Number of cards drawn is
    specified by numCards (default 1) parameter. Returns
    tuple of default boolean variable and list of drawn Card
    objects. Default boolean returns true if specified number
    of cards were successfully drawn.

    Parameters:
      - numCards (int): Number of Card objects to draw from deck
    
    Returns:
      - default (bool): True if successful, False otherwise
      - drawnCards (List[Card]): List of drawn Card objects
    """
    drawnCards = []
    if self._length >= numCards:
      self._length -= numCards
      for i in range(numCards):
        drawnCards.append(self._deck.pop())
    return len(drawnCards) > 0, drawnCards

  def shuffle(self) -> None:
    """
    Class Function: shuffle
    -----------------------
    Description:
    Shuffles the current deck if at least 1 card exists.
    """
    if self._length > 0:
      random.shuffle(self._deck)

  def reset(self) -> None:
    """
    Class Function: reset
    ---------------------
    Description:
    Reinitializes the deck to default. Reinitialization uses
    existing CardVariation definition and randomInit settings.
    """
    self.__init__(self._cardVariation, self._randomInit)