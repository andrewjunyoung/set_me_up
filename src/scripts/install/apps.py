from yaml import safe_load
import wget
from os.path import exists
from os import mkdir
from multiprocessing import Pool


apps_yaml_path = './static/apps.yml'
downloads_dir = './downloads'
apps_dir = 'apps'
output_dir = f'{downloads_dir}/{apps_dir}'
n_threads = 7



def download_package(contents, key):
    app_name = key
    properties = contents[key]
    try:
        url = properties['url']
        extension = properties.get('extension')
        print(f'Installing {app_name}.')
        wget.download(url, f'{output_dir}')
    except:
        print(f'An error ocurred when trying to download {app_name}')


def main():
    with open(apps_yaml_path) as file_:
        contents = safe_load(file_)

    if not exists(f'{downloads_dir}/{apps_dir}'):
        if not exists(downloads_dir):
            mkdir(downloads_dir)
        mkdir(f'{downloads_dir}/{apps_dir}')


    with Pool(n_threads) as pool:
        pool.starmap(download_package, [(contents, key) for key in contents.keys()])

if __name__ == '__main__':
    main()
