from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Generator for everything'


# Setting up

setup(
    name="GeneratorFE",
    version=VERSION,
    author="SamuraiCoder",
    author_email="<aelboutaheri@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['random', 'string'],
    keywords=['python', 'generator', 'random'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
