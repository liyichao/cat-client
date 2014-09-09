from setuptools import setup, find_packages

setup(
    name='cat',
    version='0.0.1',
    license='Private',
    description='sending traces to cat',
    author='liyichao',
    author_email='liyichao.good@gmail.com',
    url='https://github.com/liyichao/cat-client',
    packages=find_packages('.'),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
        ],
    }
)
