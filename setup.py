from setuptools import setup
from glob import glob


# helper function to get valid files
def cleaned_list(files):
    cleaned = []
    for file in files:
        if "." in file:
            cleaned.append(file)
    return cleaned


# Loading the contents from readme for long disc
with open("README.md", 'r', encoding="utf-8") as f:
    long_disc = f.read()


resources = glob('anti_viral_protocol/resources/**/*', recursive=True)
setup(
    name='Anti-Viral-Protocol',
    version='1.0.1',
    packages=['anti_viral_protocol'],
    url='https://github.com/Team-De-bug/Anti-Viral-Protocol',
    author='marudhu',
    author_email='marudhupaandian@gmail.com',
    description='2d platformer, side scroller game',
    long_description=long_disc,
    long_description_content_type='text/markdown',
    install_requires='pygame',
    include_package_data=True,
    data_files=[('resources', cleaned_list(resources))],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
                 ]
)
