import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jelly-fpga-client",
    version="0.0.2",
    install_requires=[
        "requests",
    ],
    author="Ryuji Fuchikami",
    author_email="ryuji.fuchikami@nifty.com",
    description="fpga control client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryuz/jelly-fpga-client-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
