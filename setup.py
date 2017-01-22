import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

about = {}
with open("app/__about__.py") as f:
    exec(f.read(), about)

with open('requirements.txt') as fl:
    install_reqs = [line for line in fl.read().split('\n') if line]
    tests_reqs = []

if sys.version_info < (2, 7):
    install_reqs += ['argparse']
    tests_reqs += ['unittest2']

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'info':
    for k, v in about.items():
        print('%s: %s' % (k, v))
    sys.exit()

readme = open('README.md').read()

setup_requires = [
    'pytest-runner'
    ]

tests_require = [
    'pytest-cov',
    'pytest'
    ]

setup(
    name='Maisha Goals',
    version='0.1',
    description='This is a Flask API implementing the classic bucketlist app.',
    long_description=readme,
    author='Joseph AKhenda',
    author_email='joseph.akhenda@andela.com',
    url='hhttps://github.com/andela-akhenda/maisha-goals',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=install_reqs,
    license='MIT',
    keywords='Maisha Goals',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    setup_requires=setup_requires,
    tests_require=tests_require,
    test_suite='tests',
)
