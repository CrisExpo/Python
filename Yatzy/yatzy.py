class Yatzy:

    @staticmethod
    def chance(*dice):
        # *argv keeps a random number of arguments, you can run 3 or 5 arguments without changing de code
        score = 0
        for num_dice in dice:
            score += num_dice
        return score

    @staticmethod
    def yatzy(dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50

    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE

    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR

    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * FIVE

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX

    @staticmethod
    def score_pair(*dice):
        PAIR = 2
        for number in range(6, 0, -1):
            if dice.count(number) >= PAIR:
                return PAIR * number
        return 0

    @staticmethod
    def score_two_pairs(*dice):
        PAIR = 2
        pairs = 0
        score = 0
        number = 1
        while pairs < 2 and number <= 6:
            if dice.count(number) >= 2:
                pairs += 1
                score += PAIR * number
            number += 1
        if pairs == 2:
            return score
        else:
            return 0

    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        for number in range(6, 0, -1):
            if dice.count(number) >= FOUR:
                return FOUR * number
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        for numero in range(6, 0, -1):
            if dice.count(numero) >= THREE:
                return THREE * numero
        return 0

    @staticmethod
    def small_straight(*dice):
        for number in range(1, 6):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def large_straight(*dice):
        for number in range(2, 7):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0

    def __init__(self, *dice):
        PAIR = 2
        for numero in range(6, 0, -1):
            if dice.count(numero) == PAIR:
                return PAIR * numero
        return 0