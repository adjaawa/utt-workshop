import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Workshop_Test",
    version="0.1.0",
    author="UTT",
    author_email="utt",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src/api"},
    packages=setuptools.find_packages(where="src/api"),
    python_requires=">=3",
)
