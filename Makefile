BREW_PACKAGES = brew.txt
PYTHON_PACKAGES = python.txt

get_brew:
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
get_amethyst:
	brew cask install amethyst
brew:
	brew install $$(<$(BREW_PACKAGES))
python:
	pip3 install -r $(PYTHON_PACKAGES)
