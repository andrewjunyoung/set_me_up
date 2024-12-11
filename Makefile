restart:
	echo "TODO"

clear_dock:  # TODO: remove
	defaults delete com.apple.dock persistent-apps; killall Dock

get_homebrew: 
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

get_magnet:
	mas install 441258766

get_repos:
	git clone https://github.com/andrewjunyoung/jdvorak; \
	git clone https://github.com/andrewjunyoung/mozc_resources; \
	git clone https://github.com/andrewjunyoung/terminal_config

setup_settings:
	echo "TODO"

setup_python_neovim:
	pip3 install -r set_me_up/static/python.txt
	pip3 install --upgrade pynvim

setup_vim_plug:
	sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

setup_omzsh:
	mv ~/.zshrc.orign ~/.zshrc
	cd ~/.oh-my-zsh/custom/plugins
	git clone https://github.com/zsh-users/zsh-syntax-highlighting
	git clone https://github.com/zsh-users/zsh-autosuggestions
	cd

setup_terminal:
	cd terminal_config/ && \
	cp .* * ~ && \
  cd - && \
	rmdir terminal_config/

setup_jdvorak:
	cd jdvorak && \
	make install && \
	cd -
	make restart

one:  # Install all necessary programs and restart.
	make get_homebrew  # 3. Install Homebrew.

	brew bundle  # 4. Install apps through Homebrew.

	make get_magnet  # 5. Install Magnet from the App Store. PREREQUISITE: user is logged into app store
	make get_repos  # 5. Clone repos.

	make setup_terminal  # 6. Setup terminal.
	make setup_jdvorak  # 6. Setup JDvorak and restart.

two:  # Set up System Settings and restart.
	make setup_settings
	make restart
