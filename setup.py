from setuptools import setup

setup(
    name='revGigaChat',
    version='1.1',
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
