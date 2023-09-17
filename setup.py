from setuptools import setup

setup(
    name='revGigaChat',
    version='1.0',
    author='Denis Ponomat',
    packages=['revGigaChat'],
    install_requires=[
        'requests',
        'telethon'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3.0 (GPL-3.0)',
        'Programming Language :: Python :: 3'
    ],
)
