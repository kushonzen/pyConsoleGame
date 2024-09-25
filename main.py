import random

# список слів
words = ['ноутбук', 'кубік', 'університет', 'емоція', 'ліжко', 'яблуко', 'інтернет']


# рандомне слово зі списку
def get_random_word(word_list):
    return random.choice(word_list)


def display_game_state(word, guessed_letters, attempts_left):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print(f"Слово: {' '.join(display)}")
    print(f"Вгадані літери: {', '.join(guessed_letters)}")
    print(f"Залишилось спроб: {attempts_left}")


def play_hangman():
    word = get_random_word(words)
    guessed_letters = []
    attempts_left = 6
    word_guessed = False

    print("Ласкаво прошу в гру 'Шибениця'!")

    while attempts_left > 0 and not word_guessed:
        display_game_state(word, guessed_letters, attempts_left)

        guess = input("Введіть літеру: ").lower()

        if guess in guessed_letters:
            print(f"Літера '{guess}' вже була, спробуйте іншу.")
        elif guess in word:
            print(f"Супер! Літера '{guess}' є в слові.")
            guessed_letters.append(guess)
        else:
            print(f"Нажаль, літери '{guess}' нема в слові.")
            guessed_letters.append(guess)
            attempts_left -= 1

        # чекаємо чи вгадано все слово
        if all(letter in guessed_letters for letter in word):
            word_guessed = True

    if word_guessed:
        print(f"Вітаю! Ви вгадали слово: {word}")
    else:
        print(f"Ви програли. Загадане слово було: {word}")


if __name__ == "__main__":
    play_hangman()
