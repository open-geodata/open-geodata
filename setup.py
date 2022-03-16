from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

requirements = []
for line in open('requirements.txt'):
    li = line.strip()
    if not li.startswith('#'):
        requirements.append(line.rstrip())

#VERSION = (0, 0, 14)  # (1, 0, 7, 'dev0')
#__version__ = '.'.join(map(str, VERSION))

setup(
    name='open_geodata',  # Nome (não precisa ser o nome do repositório, nem de qualquer pasta...)
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='Dados Espaciais do Brasil',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/open-geodata/open-geodata',
    keywords='python, endereço aleatório, address',

    # Version
    # https://github.com/twisted/incremental
    # version=__version__,
    use_incremental=True,
    setup_requires=['incremental'],

    # Python and Packages
    python_requires='>=3',
    install_requires=requirements,

    # Entry
    # Our packages live under src but src is not a package itself
    package_dir={'': 'src'},

    # Quando são diversos módulos...
    packages=find_packages('src', exclude=['test']),

    # Apenas um módulo...
    # py_modules = ['traquitanas'],     # Quando trata-se apenas de um módulo

    # Dados
    include_package_data=True,
    package_data={'': ['data/*']},

    # Classificação
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
)
