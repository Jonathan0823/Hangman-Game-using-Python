import random

words = ["apple", "banana", "orange", "pear", "pineapple", "watermelon", "strawberry", "kiwi"]


hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def show_hangman(wrong):
    print("===============")
    for art in hangman_art[wrong]:
        print(f"{art:>9}")
    print("===============")

def display_hint(hint):
    print(" ".join(hint))
    pass

def main():

    is_running = True
    while is_running:
        wrong = 0
        answer = random.choice(words)
        hint = ["_" for word in range(len(answer))]
        guessed_answer = set()
        print("===============")
        print("HANGMAN")
        print("===============")

        while wrong < 6:
            show_hangman(wrong)
            display_hint(hint)
            print()
            guess = input("Guess a letter: ").lower()

            if guess.isalpha() == False or len(guess) > 1:
                print("Invalid input")
                continue
            
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
                        guessed_answer.add(guess)

                if len(guessed_answer) == len(set(answer)):
                    show_hangman(wrong)
                    display_hint(hint)
                    print("YOU WIN")
                    break
            else:
                wrong += 1
            if wrong == 6:
                show_hangman(wrong)
                print("YOU LOSE")
                print(f"The answer is {answer}")
        
        if input("Do you want to play again? (y/n): ").lower() == "y":
            continue
        else:
            is_running = False
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
