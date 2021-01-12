from setuptools import setup
from glob import glob


# helper function to get valid files
def cleaned_list(files):
    cleaned = []
    for file in files:
        if "." in file:
            cleaned.append(file)
    return cleaned


resources = glob('anti_viral_protocol/resources/**/*', recursive=True)
setup(
    name='Anti-Viral-Protocol',
    version='1.0.1',
    packages=['anti_viral_protocol'],
    url='https://github.com/Team-De-bug/Anti-Viral-Protocol',
    author='marudhu',
    author_email='marudhupaandian@gmail.com',
    description='2d platformer, side scroller game',
    install_requires='pygame',
    include_package_data=True,
    data_files=[('resources', cleaned_list(resources))]
)
