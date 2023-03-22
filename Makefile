clean_dl:
	rm downloads/apps/*

clean_repos:
	rm -rf downloads/repos/*

get_brew: 
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
