from yaml import safe_load
import wget
from git import Repo
from os.path import exists
from os import mkdir

def main():
    repos_yaml_path = './static/repos.yml'
    output_dir = './downloaded_apps'

    with open(repos_yaml_path) as file_:
        contents = safe_load(file_)

    if not exists(output_dir):
        mkdir(output_dir)

    for user, repos in contents.items():
        try:
            for repo in repos:
                git_url = 'https://github.com/{user}/{repo}'
                print(f'Cloning {user}/{repo}.')
                Repo.clone_from(git_url) #, f'{output_dir}/{user}_{repo}')
        except:
            print(f'An error ocurred when trying to clone {repo}')

if __name__ == '__main__':
    main()
