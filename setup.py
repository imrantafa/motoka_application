from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in motoka_app/__init__.py
from motoka_app import __version__ as version

setup(
	name="motoka_app",
	version=version,
	description="for development purposes of motoka.com",
	author="imran mustafa",
	author_email="motoka@archiaterstudio.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
