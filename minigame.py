import random

VOCAB = [
    ["Hallo", "Hello"],
    ["Welt", "World"],
    ["Hund", "Dog"],
    ["Katze", "Cat"],
    ["Auto", "Car"],
    ["Haus", "House"],
    ["Baum", "Tree"],
    ["Blume", "Flower"],
    ["Buch", "Book"],
    ["Stuhl", "Chair"],
    ["Tisch", "Table"],
    ["Fenster", "Window"],
    ["Tür", "Door"],
    ["Maus", "Mouse"],
    ["Vogel", "Bird"],
]

def session():
    """
    Mini game session
    """
    # Shuffle the vocabulary list
    random.shuffle(VOCAB)
    i = 0
    while i < len(VOCAB):
        # Get the German word and its English translation
        item = VOCAB[i]
        german_word = item[0]
        english_translation = item[1]

        user_corret = False
        # Check if the user's input is correct
        while not user_corret:
            # Ask the user for the English translation
            user_input = input(f"What is the English translation of '{german_word}'? ")

            if user_input.lower() == english_translation.lower():
                print("Correct!")
                i += 1
                user_corret = True
            else:
                print(f"Incorrect! The correct answer is '{english_translation}'.")

    print("Congratulations! You've completed the mini-game.")

if __name__ == "__main__":
    session()
