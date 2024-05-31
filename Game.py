import random


def get_game_mode():
    print("Wybierz tryb gry:")
    print("1. Easy (1-50, 10 żyć)")
    print("2. Medium (1-100, 5 żyć)")
    print("3. Hard (1-200, 3 życia)")
    try:
        mode = int(input("Wybierz tryb (1, 2, 3): "))
        if mode == 1:
            return 1, 50, 10
        elif mode == 2:
            return 1, 100, 5
        elif mode == 3:
            return 1, 200, 3
        else:
            print("Nieprawidłowy wybór. Ustawiam tryb Medium.")
            return 1, 100, 5
    except ValueError:
        print("Nieprawidłowa wartość. Ustawiam tryb Medium.")
        return 1, 100, 5


def guess_the_number():
    print("Witaj w grze 'Zgadnij liczbę'!")

    min_value, max_value, lives = get_game_mode()

    number_to_guess = random.randint(min_value, max_value)
    number_of_guesses = 0
    guessed = False
    guess_history = []

    while not guessed and lives > 0:
        try:
            user_guess = int(input(f"Podaj liczbę ({min_value}-{max_value}): "))
            number_of_guesses += 1
            guess_history.append(user_guess)

            if user_guess < number_to_guess:
                print("Za niska!")
                lives -= 1
            elif user_guess > number_to_guess:
                print("Za wysoka!")
                lives -= 1
            else:
                if number_of_guesses == 1:
                    print("Szik Szak szok, zgadłeś za pierwszym razem!")
                else:
                    print(f"Gratulacje! Zgadłeś liczbę w {number_of_guesses} próbach.")
                guessed = True

            if lives > 0 and not guessed:
                print(f"Pozostało Ci {lives} żyć.")
                if len(guess_history) > 1:
                    if abs(user_guess - number_to_guess) < abs(guess_history[-2] - number_to_guess):
                        print("Cieplej!")
                    else:
                        print("Zimniej!")
            elif lives == 0:
                print("Koniec gry! Straciłeś wszystkie życia.")
                print(f"Poszukiwana liczba to: {number_to_guess}")

            print("Historia zgadywanych liczb:", guess_history)

        except ValueError:
            print("Proszę wprowadzić prawidłową liczbę.")


if __name__ == "__main__":
    guess_the_number()