from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]
# requirements = ["numpy"]

setup(name='toto',
      description="package description",
      packages=find_packages(),
      install_requires=requirements,
      scripts=["scripts/toto-script"])
