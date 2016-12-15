from setuptools import setup



setup(name = 'umbrella-top-sites',
	  version = '0.1',
	  packages = ['umbrella'],
	  install_requires = ['beautifulsoup4', 'requests','coverage'],
	  url = 'https://github.com/retornam/umbrella-top-sites.git',
	  author = 'retornam',
	  author_email = 'me@retornam.com')