from distutils.core import setup
setup(
  name = 'pypokedex',
  py_modules = ['pypokedex'],
  version = '1.0',
  description = 'A Pokedex to look up Pokemon.',
  author = 'MWPuppire',
  author_email = 'mwpuppire@outlook.com',
  license='MIT',
  url = 'https://github.com/mwpuppire/py-pokedex',
  download_url = 'https://github.com/mwpuppire/py-pokedex/archive/1.0.tar.gz',
  keywords = ['pokemon', 'pokedex'],
  classifiers = [],
  requires=['requests'],
  scripts=['pypokedex']
)
