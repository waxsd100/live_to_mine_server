"""Python setup.py for live_to_mine_server package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("live_to_mine_server", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="live_to_mine_server",
    version=read("live_to_mine_server", "VERSION"),
    description="Awesome live_to_mine_server created by waxsd100",
    url="https://github.com/waxsd100/live_to_mine_server/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="waxsd100",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["live_to_mine_server = live_to_mine_server.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
