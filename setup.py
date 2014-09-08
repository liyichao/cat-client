from setuptools import setup, find_packages

setup(
    name='tracing',
    version='0.0.5',
    license='Private',
    description='sending traces to zipkin',
    author='liyichao',
    author_email='lyc@zhihu.com',
    url='http://git.in.zhihu.com/lyc/tracing',
    packages=find_packages('.'),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
        ],
    }
)
