from setuptools import setup, find_packages
import re

def _get_version():
    VERSION_FILE = f"iris_model_training/_version.py"
    with open(VERSION_FILE, "rt") as f:
        contents = f.read()

    version_ptrn = re.compile(r"^__version__\s=\s['\"](?P<version>[^'\"]*)['\"]")
    mo = version_ptrn.search(contents, re.M)
    try:
        return mo.group("version")
    except:
        raise RuntimeError("Unable to find version string in %s." % (VERSION_FILE,))


# requirements needed for others to build / use the model
requirements = [
    "pandas",
    "pandera",
    "sklearn",
]

# requirements needed to run any "extra stuff", like notebooks /
# graphs / experiments / etc
dev_requirements = [
    "jupyter",
    "matplotlib",
    "seaborn",
    "pytest"
]


setup(
    name='IrisModelTraining',
    version=_get_version(),
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements
    },
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)