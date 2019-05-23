import random

WORDS = (
    "treehouse",
    "python",
    "learner"
)

def prompt_for_words(challengr):
    guesses = set()
    print("What words can you find in the word '{}'.".format(challenge))
    print("(Enter Q to Quit)");
    while True:
        guess = input("{} words > ".format(len(guesses)))
        if guess.upper() = "Q":
            break
        guesses.add(guess.lower())
    return guesses

challenge_word = random.choice(WORDS)

player1_words = prompt_for_words(challenge_word)
player2_words = prompt_for_words(challenge_word)

print("Player 1 Results:")
player1_unique = player1_words - player2_words
print("{} guesses, {} unique".format(len(player1_words), len(player1_unique)))
print("-" * 10)
print("Player 2 Results:")
player2_unique = player2_words - player1_words
print("{} guesses, {} unique".format(len(player2_words), len(player2_unique)))

print("Shared guesses:")
shared_words = player1_words
