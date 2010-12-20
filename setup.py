from distutils.core import setup
from jinzou import version

setup(
    name='jinzou',
    version=version,
    description='Jinzou. A very simple IRC bot.',
    author='Brandon R. Stoner',
    author_email='monokrome@monokro.me',
    url='http://jinzou.monokro.me/',
    packages=['jinzou'],
)

