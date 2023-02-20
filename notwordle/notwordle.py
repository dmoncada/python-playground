import contextlib
import pathlib
import random
from typing import List
from string import ascii_letters, ascii_uppercase

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({'warning': 'red on yellow'}))

NUM_LETTERS = 5
NUM_GUESSES = 6
WORDS_PATH = pathlib.Path(__file__).parent / 'wordlist.txt'

def get_random_word(word_list: List[str]) -> str:
    """Gets a random five-letter word from a list of string.

    ## Example:

    >>> get_random_word(["snake", "worm", "it'll"])
    'SNAKE'
    """
    if words := [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(words)

    console.print('No words of length 5 in the word list', style='warning')
    raise SystemExit()

def guess_word(previous_guesses: List[str]) -> str:
    while True:
        guess = console.input('\nGuess word: ').upper()

        if guess in previous_guesses:
            console.print(f"You have already guessed: '{guess}'.", style='warning')
            continue

        if len(guess) != 5:
            console.print('Your guess must be exactly 5 letters long.', style='warning')
            continue

        if any((invalid := letter) not in ascii_letters for letter in guess):
            console.print(f"Invalid letter: '{invalid}'. Please use English letters.",
                          style='warning')
            continue

        return guess

def show_guesses(guesses: List[str], word: str):
    letter_status = {letter: letter for letter in ascii_uppercase}

    for guess in guesses:
        styled_guess = []

        for letter, correct in zip(guess, word):
            if letter == correct:
                style = 'bold white on green'
            elif letter in word:
                style = 'bold white on yellow'
            elif letter in ascii_letters:
                style = 'white on #666666'
            else:
                style = 'dim'

            styled_guess.append(f'[{style}]{letter}[/]')

            if letter != '_':
                letter_status[letter] = f'[{style}]{letter}[/]'

        console.print(''.join(styled_guess), justify='center')

    console.print('\n' + ''.join(letter_status.values()), justify='center')

def refresh_page(headline: str):
    console.clear()
    console.rule(f'[bold blue]:leafy_green: {headline} :leafy_green:[/]\n')

def game_over(guesses: List[str], word: str, won: bool):
    refresh_page(headline='Game Over')
    show_guesses(guesses, word)

    if won:
        console.print(f'\n[bold white on green]Correct! The word is: {word}![/]')
    else:
        console.print(f'\n[bold white on red]Sorry, the word was: {word}...[/]')

def main():
    # Pre-process.
    word_list = WORDS_PATH.read_text(encoding='utf-8').split('\n')
    word = get_random_word(word_list)
    guesses = ['_' * NUM_LETTERS] * NUM_GUESSES

    # Process (main loop.)
    with contextlib.suppress(KeyboardInterrupt):
        for index in range(NUM_GUESSES):
            refresh_page(headline=f'Guess {index + 1}')
            show_guesses(guesses, word)

            guesses[index] = guess_word(previous_guesses=guesses[:index])
            if guesses[index] == word:
                break

    # Post-process.
    game_over(guesses, word, won=guesses[index] == word)

if __name__ == '__main__':
    main()
