def _run_bash_command(command: str) -> str:
    return subprocess.check_output(['bash','-c', command])


def get_from_app_store():
    return _run_bash_command(
        'for line in `cat static/app_store.txt`; do mas install "$line"; done'
    )


def get_repos():
    return _run_bash_command(
        'for line in `cat static/repos.txt`; \
        do git clone https://github.com/"$line" downloads/repos/$line; \
        done'
    )


def set_up_neovim():
    return _run_bash_command(
        'sh -c \'curl \
        -fLo \
        "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim \
        --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim\''
    )


def clear_and_restart_dock():
    return _run_bash_command(
        'defaults delete com.apple.dock persistent-apps; killall Dock'
    )


def get_brew() -> None:
    pass


def get_from_brew() -> None:
    pass


def get_from_brew_cask() -> None:
    pass


def get_brew_all() -> None:
    get_brew()
    get_from_brew()
    get_from_brew_cask()


def get_from_apt() -> None:
    pass


def get_from_apt_gui() -> None:
    pass


def set_up_system_preferences() -> None:
    pass


def get_repos() -> None:
    pass


def set_up_zsh() -> None:
    pass


def _prompt_logins() -> None:
    logging.info(str)


def get_all(settings) -> None:
    if sys.platform == 'darwin':  # macOS
        install_steps = [
            [
                Step(get_brew),
                Step(clear_dock_and_reset, gui=True),
            ],
            [
                Step(get_from_brew),
                Step(get_from_brew_cask, gui=True),
            ],
            [
                Step(
                    _prompt_logins(['firefox', 'lastpass', 'app store']),
                    gui=True,
                ),
                Step(get_repos),
                Step(set_up_zsh),
                Step(set_up_neovim),
                Step(set_up_system_preferences, gui=True),  # TODO: ?
            ],
            [
                Step(get_from_app_store, gui=True),
            ],
        ]

        # Manual steps:
        #   1: install apps you can't get from the above
        #   2: Set up your keyboards in system settings
        #   3: Set up Mozc
        #   4: Import ITerm settings from file
        #   5: Set up dock

    elif sys.platform == 'linux':  # «linux2» before python 3.3
        install_steps = [
            [
                Step(get_from_apt),
                # TODO: Step(get_from_apt_gui, gui=True),
            ],
            [
                Step(set_up_zsh),
                Step(set_up_neovim),
            ]
        ]


function_arg_to_fns_map = {
    'all': get_all,
    'app_store': get_from_app_store,
    'apt': get_from_apt,
    'apt_gui': get_from_apt_gui,
    'brew': get_brew_all,
    'brew_cask': get_from_brew_cask,
    'brew_formulas': get_from_brew,
    'clear_dock': clear_and_restart_dock,
    'neovim': set_up_neovim,
    'preferences': set_up_system_preferences,
    'repos': get_repos,
    'zsh': set_up_zsh,
}

