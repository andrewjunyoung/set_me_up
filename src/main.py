from yaml import safe_load
from multiprocessing import Pool
import subprocess
from typing import Callable
from argparse import ArgumentParser

from src.data import Step

apps_yaml_path = './static/apps.yml'
downloads_dir = './downloads'
apps_dir = 'apps'
output_dir = f'{downloads_dir}/{apps_dir}'
n_threads = 7


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


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
