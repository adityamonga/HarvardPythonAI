from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
puzzle0ClaimA = (And(AKnight, AKnave),)
knowledge0 = And(
    # structure
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnight)),

    #claim
    Implication(AKnight, *puzzle0ClaimA),
    Implication(AKnave, Not(*puzzle0ClaimA)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
puzzle1ClaimA = (And(AKnave, BKnave),)
knowledge1 = And(
    # structure
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)),
    Not(Or(And(AKnight, AKnight), And(BKnight, BKnave))),

    # claim
    Implication(AKnight, *puzzle1ClaimA),
    Implication(AKnave, Not(*puzzle1ClaimA))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
puzzle2claimA = (Or(And(AKnight, BKnight), And(AKnave, BKnave)),)
puzzle2claimB = (Or(And(AKnight, BKnave), And(AKnave, BKnight)),)
knowledge2 = And(
    # structure
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)),
    Not(Or(And(AKnight, AKnave), And(BKnight, BKnave))),

    # claim
    Implication(AKnight, *puzzle2claimA),
    Implication(AKnave, Not(*puzzle2claimA)),
    Implication(BKnight, *puzzle2claimB),
    Implication(BKnave, Not(*puzzle2claimB))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
puzzle3claimA = (Or(AKnight, AKnave),)
puzzle3claimB = (Implication(*puzzle3claimA, AKnave),)
puzzle3claimB = (And(*puzzle3claimB, CKnave),)
puzzle3claimC = (AKnight,)
knowledge3 = And(
    # structure
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)),
    Not(Or(And(AKnight, AKnave), And(BKnight, BKnave), And(CKnight, CKnave))),

    # claim
    Implication(AKnight, *puzzle3claimA),
    Implication(AKnave, Not(*puzzle3claimA)),
    Implication(BKnight, *puzzle3claimB),
    Implication(BKnave, Not(*puzzle3claimB)),
    Implication(CKnight, *puzzle3claimC),
    Implication(CKnave, Not(*puzzle3claimC)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
