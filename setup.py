from setuptools import setup, find_packages


def readme():
    with open("README.rst", mode="r") as f:
        return f.read()


setup(
    name="myrepo_manager",
    version="0.1",
    description="Manage myrepo git repository",
    long_description=readme(),
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    install_requires=["GitPython", "black"],
    entry_points={"console_scripts": ["myrepo_manager=myrepo_manager.main:main"]},
    scripts=["bin/myrepo-manager"],
)
