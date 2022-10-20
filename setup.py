from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = open(this_directory / 'README.md', encoding='utf-8').read()

setup(
    name='camp_parser',
    description="""unofficial api to get information from camphub and other camp/competition news website. in thai""",
    long_description_content_type='text/markdown',
    long_description=long_description,
    version='0.2',
    license='MIT',
    author="HRNPH",
    author_email='hirunkul2548@gmail.com',
    packages=find_packages('camp_parser'),
    package_dir={'': 'camp_parser'},
    url='https://github.com/HRNPH/Camphub_api_unofficial',
    keywords='camp_parser',
    install_requires=[
          'requests',
            'bs4',
      ],

)