from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='revGigaChat',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.3',
    author='Denis Ponomar',
    packages=['revGigaChat'],
    install_requires=[
        'requests',
        'telethon'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
)
