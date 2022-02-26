from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in krabi_addons/__init__.py
from krabi_addons import __version__ as version

setup(
	name="krabi_addons",
	version=version,
	description="Addons for krabi",
	author="Ebkar Technologies",
	author_email="admin@ebkar.ly",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
