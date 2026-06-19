from setuptools import setup, find_packages

setup(
    name="irl-besty",
    version="1.0.0",
    description="An unhinged text-to-emoji cipher engine.",
    author="Anika Mukherjee - irl Professor Bones Team",
    packages=find_packages(),
    install_requires=[
        "rich>=13.0.0"
    ],
    entry_points={
        "console_scripts": [
            "besty=besty.main:main",
        ]
    },
)
