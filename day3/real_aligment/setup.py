from setuptools import find_packages, setup


setup(
    name="dna-protein-alignment",
    version="0.1.0",
    description="Translate DNA sequences and compute pairwise protein identity scores",
    packages=find_packages(),
    install_requires=[
        "biopython>=1.83",
        "pandas>=2.2.0",
        "matplotlib>=3.8.0",
    ],
)
