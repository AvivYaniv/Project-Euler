
# Poker Hands File
POKER_HANDS_FILE_NAME       = "poker.txt"
CARDS_SEPERATOR             = " "
CARDS_IN_HAND               = 5
VALUE_INDEX                 = 0
SUIT_INDEX                  = 1

# Players
THIS_PLAYER                 = 0
OTHER_PLAYER                = 1

# Suits
# Clubs (♣), Diamonds (♦), Hearts (♥), Spades (♠)
SUITS               = ["C", "D", "H", "S"]

class Suits:
    @staticmethod
    def GetDictionary():
        return { SUITS[s] : [] for s in xrange(len(SUITS)) }

# Values
VALUES                  = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
NUMBER_OF_VALUES        = len(VALUES)
VALUES_TO_INDEXES       = { VALUES[vi] : vi for vi in xrange(NUMBER_OF_VALUES)}
# VALUES_TO_INDEXES["A"] = (1, 14)

class Values:
    @staticmethod
    def GetDictionary():
        return { VALUES[v] : [] for v in xrange(len(VALUES)) }

    @staticmethod
    def GetIndex(value):
        return VALUES_TO_INDEXES[value]

class PokerHand:  
    def __init__(self, cards_list):
        self.cards  = cards_list
        self._Sort()
       
    def _Sort(self):
        self.by_value = Values.GetDictionary()
        self.by_suit = Suits.GetDictionary()
        for card in self.cards:
            value = card[VALUE_INDEX]
            suit = card[SUIT_INDEX]
            self.by_value[value].append(suit)
            self.by_suit[suit].append(value)

    def _GetRankLimitedCheck(self, stopRank):
        rankIndex = 0
        for rank in PokerHandRanks[0:stopRank]:
            if rank(self):
                return rankIndex
            rankIndex += 1
        return rankIndex

    def _GetRank(self):
        return self._GetRankLimitedCheck(RANKS_NUMBER)

    def GetWinner(self, other):
        thisRankIndex = self._GetRank()
        otherRankIndex = other._GetRankLimitedCheck(thisRankIndex+1)
        if thisRankIndex < otherRankIndex:
            return THIS_PLAYER
        elif otherRankIndex < thisRankIndex:
            return OTHER_PLAYER
        else:
            return self._TieArbitrament(other)

    def _TieArbitrament(self, other):
        thisAmountsValues = self._GetCardAmountsValueSorted()
        otherAmountsValues = other._GetCardAmountsValueSorted()
        for a in xrange(CARDS_IN_HAND, 0, -1):
            amountCardsNumbe = len(thisAmountsValues[a])
            for i in xrange(amountCardsNumbe):
                if thisAmountsValues[a][i] > otherAmountsValues[a][i]:
                    return THIS_PLAYER
                elif otherAmountsValues[a][i] > thisAmountsValues[a][i]:
                    return OTHER_PLAYER
        return THIS_PLAYER
    
    def _GetCardAmountsValueSorted(self):
        amounts = [[] for i in xrange(CARDS_IN_HAND + 1)]
        for vi in xrange(NUMBER_OF_VALUES-1, -1, -1):
            value = VALUES[vi]
            amount_of_value = len(self.by_value[value])
            amounts[amount_of_value].append(vi)
            amounts[amount_of_value] = sorted(amounts[amount_of_value], None, None, True)
        return amounts
        
    # One Pair: Two cards of the same value.
    def _IsOnePair(self):
        for v in self.by_value:
            if 2 == len(self.by_value[v]):
                return True
        return False
    
    # Two Pairs: Two different pairs.
    def _IsTwoPairs(self):
        pairCounter = 0
        for v in self.by_value:
            if 2 == len(self.by_value[v]):
                pairCounter += 1
            if 2 == pairCounter:                
                return True
        return False
    
    # Three of a Kind: Three cards of the same value.
    def _IsThreeOfAKind(self):
        for v in self.by_value:
            if 3 == len(self.by_value[v]):
                return True
        return False

    # Straight: All cards are consecutive values.
    def _IsStraight(self):
        return self._IsAllConsecutiveValues()

    # Flush: All cards of the same suit.
    def _IsFlush(self):
        return self._IsAllSameSuit()

    # Full House: Three of a kind and a pair.
    def _IsFullHouse(self):
        isPairFound = False
        isThreeFound = False
        for v in self.by_value:
            amout_of_value = len(self.by_value[v])
            if 2 == amout_of_value:
                isPairFound = True
            elif 3 == amout_of_value:
                isThreeFound = True
            if isPairFound and isThreeFound:
                return True
        return False

    # Four of a Kind: Four cards of the same value.
    def _IsFourOfAKind(self):
        for v in self.by_value:
            if 4 == len(self.by_value[v]):
                return True 
        return False

    def _IsAllSameSuit(self):
        for s in self.by_suit:
            if CARDS_IN_HAND == len(self.by_suit[s]):
                return True 
        return False

    def _IsAllConsecutiveValues(self):
        values_indexes = []
        for v in self.by_value:
            same_value = self.by_value[v]
            length_same_value = len(same_value)
            if 1 == length_same_value:
                values_indexes.append(Values.GetIndex(v))
            elif 1 < length_same_value:
                return False
        min_value_index = min(values_indexes)
        value_index = min_value_index
        for i in xrange(CARDS_IN_HAND-1):
            if not self.by_value[VALUES[value_index + 1]]:
                return False
            value_index += 1
        return True

    # Flush: All cards of the same suit.
    def _IsFlush(self):
        return self._IsAllSameSuit()

    # Straight Flush: All cards are consecutive values of same suit.  
    def _IsStraightFlush(self):
        return self._IsAllSameSuit() and self._IsAllConsecutiveValues()

    # Wheel Of Steel: Ace, Two, Three, Four, Five, in same suit.
    def _IsWheelOfSteel(self):
        return self.by_value["A"]   == \
               self.by_value["2"]   == \
               self.by_value["3"]   == \
               self.by_value["4"]   == \
               self.by_value["5"]   != []

    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    def _IsRoyalFlush(self):
        return self.by_value["T"]  == \
               self.by_value["J"]   == \
               self.by_value["Q"]   == \
               self.by_value["K"]   == \
               self.by_value["A"]   != []

# Ranks
PokerHandRanks = \
	[PokerHand._IsRoyalFlush, \
	 PokerHand._IsWheelOfSteel, \
	 PokerHand._IsStraightFlush, \
	 PokerHand._IsFourOfAKind, \
	 PokerHand._IsFullHouse, \
	 PokerHand._IsFlush, \
	 PokerHand._IsStraight, \
	 PokerHand._IsThreeOfAKind, \
	 PokerHand._IsTwoPairs, \
	 PokerHand._IsOnePair]
RANKS_NUMBER = len(PokerHandRanks)

def Debug():
##    playercards_list = "5H 8H 6H 4H 7H".split(CARDS_SEPERATOR)
##    hand = PokerHand(cards_list)
    # {'H': ['5'], 'S': ['6', '7'], 'C': ['5'], 'D': ['K']}
    # print hand.by_suit
    # {'A': [], '10': [], 'K': ['D'], 'J': [], 'Q': [], '3': [], '2': [], '5': ['H', 'C'], '4': [], '7': ['S'], '6': ['S'], '9': [], '8': []}
    # print hand.by_value
    
    ReadPokerHandsFile(POKER_HANDS_FILE_NAME)

def ReadPokerHandsFile(name):
    rounds = []
    with open(name) as f:
        lines = f.readlines()
    for line in lines:
        cards = line.strip().split(CARDS_SEPERATOR)
        player1_cards = cards[0:CARDS_IN_HAND]
        player2_cards = cards[-CARDS_IN_HAND::]
        rounds.append((player1_cards, player2_cards))
    return rounds

def PokerGame(rounds):
    player1_victories = 0
    player2_victories = 0
    for round_hands in rounds:
        player1_cards = round_hands[THIS_PLAYER]
        player2_cards = round_hands[OTHER_PLAYER]
        player1_hand = PokerHand(player1_cards)
        player2_hand = PokerHand(player2_cards)
        winner = player1_hand.GetWinner(player2_hand)
        if THIS_PLAYER == winner:
            player1_victories += 1
        else:
            player2_victories += 1
    return (player1_victories, player2_victories)
    
# Main
def main():

    # 376
    rounds = ReadPokerHandsFile(POKER_HANDS_FILE_NAME)
    print PokerGame(rounds)[THIS_PLAYER]
    
if __name__ == "__main__":
    main()
