from yaml import safe_load
import wget
from os.path import exists
from os import mkdir

def main():
    apps_yaml_path = './apps.yml'
    output_dir = './downloaded_apps/'

    with open(apps_yaml_path) as file_:
        contents = safe_load(file_)

    if not exists(output_dir):
        mkdir(output_dir)

    for app_name, properties in contents.items():
        try:
            url = properties['url']
            extension = properties.get('extension')
            print(f'Installing {app_name}.')
            wget.download(url, f'{output_dir}')#/{app_name}')#.{extension}')
        except:
            print(f'An error ocurred when trying to download {app_name}')

if __name__ == '__main__':
    main()
