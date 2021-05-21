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
        print(found_set)
        cards -= set(found_set)
        cards |= cards_from_string(input("Enter new cards: "))


