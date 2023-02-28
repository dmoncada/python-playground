# NotWordle

A quick Python implementation of the Wordle game. Built by following along [this excellent step-by-step tutorial][rp-wordle] from the [Real Python][rp] team.

## Goal

The main motivation for building this was as a refresher on how to write Python code, which I had not used in quite some time.

## Usage

I've included a `Makefile` to make it easier to get set up. If this is your first time launching the game, you can run the following command to get started:

```bash
# The following will create a virtual environment, install the dependencies, and launch the game.
make venv frozen run
```

Then, you can just use the following in subsequent runs:

```bash
make run
```

## TODO
- [ ] Add stats.
- [ ] Add splash screen.
- [ ] Check guesses against an online dictionary.

[rp]: https://realpython.com/
[rp-wordle]: https://realpython.com/python-wordle-clone/
