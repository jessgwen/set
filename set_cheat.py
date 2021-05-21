from itertools import combinations


class Card:
    counts = [1, 2, 3]
    suits = 'doz'
    colours = 'rgp'
    fills = 'efh'
    
    def __init__(self, count, suit, colour, fill):
        cls = self.__class__
        if count not in cls.counts:
            raise ValueError(f"Bad count: {''.join(cls.counts)} are valid")
        if suit not in cls.suits:
            raise ValueError(f"Bad suit: {cls.suits} are valid")
        if colour not in cls.colours:
            raise ValueError(f"Bad colour: {cls.colours} are valid")
        if fill not in cls.fills:
            raise ValueError(f"Bad fill: {cls.fills} are valid")
        self.count = count
        self.suit = suit
        self.colour = colour
        self.fill = fill
    
    
    def __repr__(self):
        return ("Card.fromstring('"
                f"{''.join([str(self.count), self.suit, self.colour, self.fill])}')"
                )
    
    def __str__(self):
        return ''.join([str(self.count), self.suit, self.colour, self.fill])
    
    
    @classmethod
    def fromstring(cls, s):
        return cls(int(s[0]), *s[1:4])
    
    # eq and hash are needed to make sets etc treat different instances 
    # that are the 'same' card as identical.
    
    def __eq__(self, other):
        return type(self) == type(other) and str(self) == str(other)
    
    def __hash__(self):
        return hash(repr(self))
    

def test_set_property(prop, a, b, c):
    p_a, p_b, p_c = getattr(a, prop), getattr(b, prop), getattr(c, prop)
    if p_a == p_b == p_c:
        return True
    if p_a != p_b and p_b != p_c and p_c != p_a:
        return True
    return False


def is_set(cards):
    properties  = ["count", "suit", "colour", "fill"]
    return all(test_set_property(prop, *cards) for prop in properties)



def find_set(cards):
    for trial_set in combinations(cards, 3):
        if is_set(trial_set):
            return trial_set
    return None


def cards_from_string(s):
    return {Card.fromstring(card_string) for card_string in s.split()}


def cheat():
    cards = cards_from_string(input("Enter cards: "))
    while True:
        found_set = find_set(cards)
        print(' '.join(str(card) for card in found_set))
        cards -= set(found_set)
        cards |= cards_from_string(input("Enter new cards: "))


def proof():
    """Proves* the theorem that a board of 16 cards may have no sets, 
    but any board of 17 has at least one.
    
    
    *Because crappy fragile Python with no type annotations is how all
    the cool mathematicians prove their theorems. Or so I hear.
    
    I do not claim this is the right way of doing anything.
    But it was pretty quick to write.
    """
    full_deck = {Card(count, suit, colour, fill)
                     for count in Card.counts
                     for suit in Card.suits
                     for colour in Card.colours
                     for fill in Card.fills}
    
    assert len(full_deck) == 81
    
    diabolical_board = {Card(count, suit, colour, fill)
                        for count in [1, 2]
                        for suit in 'do'
                        for colour in 'rg'
                        for fill in 'ef'}
    
    assert len(diabolical_board) == 16
    assert find_set(diabolical_board) is None

