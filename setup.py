from setuptools import setup, find_packages

setup(
    name='cat',
    version='0.0.5',
    license='Private',
    description='sending traces to cat',
    author='liyichao',
    author_email='lyc@zhihu.com',
    packages=find_packages('.'),
    install_requires=[
        'kids',
    ],
    entry_points={
        'console_scripts': [
        ],
    }
)
