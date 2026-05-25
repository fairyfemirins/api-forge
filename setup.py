from setuptools import setup, find_packages

setup(
    name="api-forge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "typer>=0.9.0",
        "rich>=13.7.0",
    ],
    entry_points={
        "console_scripts": [
            "api-forge=api_forge.cli:app",
        ],
    },
)