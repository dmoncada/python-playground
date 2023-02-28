ENV     = venv
PIP     = venv/bin/pip
PYTHON  = venv/bin/python3
SRC     = notwordle.py

.PHONY: all update reqs freeze frozen lint test run venv clean help

all: venv frozen lint test run

update: clean venv reqs freeze

reqs:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

freeze:
	$(PIP) freeze > frozen.txt

frozen:
	$(PIP) install -r frozen.txt

lint:
	$(PYTHON) -m mypy $(SRC)
	$(PYTHON) -m pylint $(SRC)

test:
	$(PYTHON) -m doctest $(SRC) --verbose --fail-fast
	$(PYTHON) -m pytest --verbose

run:
	$(PYTHON) $(SRC)

venv:
	[[ -d $(ENV) ]] || python3 -m venv $(ENV)

clean:
	rm -fr $(ENV)

help:
	@echo 'Targets:'
	@echo ''
	@echo ' all      - Builds all targets marked with [*].'
	@echo ' update   - Updates the required packages to the latest version.'
	@echo ' reqs     - Installs the required packages.'
	@echo ' freeze   - Outputs the installed packages in requirements format.'
	@echo ' *frozen  - Installs the required packages from the frozen requirements file.'
	@echo ' *lint    - Runs various linters and static code analysis tools on the source.'
	@echo ' *test    - Runs the tests.'
	@echo ' *run     - Runs the app.'
	@echo ' *venv    - Creates the virtual environment.'
	@echo ' clean    - Removes the virtual environment.'

