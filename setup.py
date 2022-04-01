import setuptools
import fmiketsu

print(fmiketsu.package_name, fmiketsu.__version__)

# Readme
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Module dependencies
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name=fmiketsu.package_name,
    version=fmiketsu.__version__,
    author='FrostBit Software laboatory',
    author_email="mikko.pajula@lapinamk.fi",
    description='Offer functions that use fmiopendata -python library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/datamikko/fmiketsu',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
    python_requires='>=3.6'
)