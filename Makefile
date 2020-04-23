BREW_PACKAGES = brew.txt
PYTHON_PACKAGES = python.txt

brew:
	brew install $$(<$(BREW_PACKAGES))
python:
	pip3 install -r $(PYTHON_PACKAGES)
