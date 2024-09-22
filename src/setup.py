from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'An easy-to-use and flexible tool for automating data collection on the web'

setup(
        name="rapidscraper", 
        version=VERSION,
        author="Patrick Pospisil",
        author_email="patpospisil@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'beautifulsoup4==4.12.3',
            'requests==2.32.3',
            'tqdm==4.66.5',
        ], 

        keywords=['python', 'web scraping', 'automation'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)