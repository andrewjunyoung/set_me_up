from yaml import safe_load
import wget
from os.path import exists
from os import mkdir
from multiprocessing import Pool
import subprocess
from typing import Callable
from dataclasses import dataclass
from argparse import ArgumentParser


apps_yaml_path = './static/apps.yml'
downloads_dir = './downloads'
apps_dir = 'apps'
output_dir = f'{downloads_dir}/{apps_dir}'
n_threads = 7


@dataclass
class Step:
    fn: Callable
    gui: bool = False


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def _run_bash_command(command: str) -> str:
    return subprocess.check_output(['bash','-c', command])


def get_apps():
    pass


def get_from_apple_store():
    return _run_bash_command(
        'for line in `cat static/app_store.txt`; do mas install "$line"; done'
    )


def get_repos():
    return _run_bash_command(
        'for line in `cat static/repos.txt`; \
        do git clone https://github.com/"$line" downloads/repos/$line; \
        done'
    )


def get_vim_plug():
    return _run_bash_command(
        'sh -c \'curl \
        -fLo \
        "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim \
        --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim\''
    )


def clear_dock_and_reset():
    return _run_bash_command(
        'defaults delete com.apple.dock persistent-apps; killall Dock'
    )


def all(settings) -> None:
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
                    prompt_logins(['firefox', 'lastpass', 'apple store']),
                    gui=True,
                ),
                Step(get_repos),
                Step(set_up_zsh),
                Step(set_up_neovim),
                Step(copy_system_preferences, gui=True),  # TODO: ?
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
                Step(get_from_apt_gui, gui=True),
            ],
            [
                Step(set_up_zsh),
                Step(set_up_neovim),
            ]
        ]


def get_args() -> ArgumentParser:
    """
    Returns:
        ArgumentParser: An ArgumentParser instance which will parse the
            arguments provided to Symboard when executed from the command line.
    """

    parser = ArgumentParser(
        description='Run installation scripts to set up (macOS | linux).',
        allow_abbrev=True,
    )

    parser.add_argument('--gui', '-g', type=str2bool, nargs='?', const=True,
        default=False, help='True iff you plan to use this OS with a GUI.'
    )
    parser.add_argument('--function', '-f', type=str, default='all',
        help='The installation script to run.'
    )  # Todo: list all possible values of -f

    return parser.parse_args()


def main():
    args = get_args()
    fns[args.fn](args)


if __name__ == '__main__':
    main()
