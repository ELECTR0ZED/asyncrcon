
import setuptools

with open('README.md', encoding='utf-8') as f:
    long_desc = f.read()

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

setuptools.setup(
    version="1.0.0",
    name="asyncrcon",
    author="zekro",
    author_email="contact@zekro.de",
    description="Client implementation of Minecrafts RCON protocol using asyncio",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/zekrotja/pytter",
    download_url='https://github.com/zekrotja/pytter/archive/master.tar.gz',
    packages=setuptools.find_packages(),
    # install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Licence 2.0",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries',
    ],
)
