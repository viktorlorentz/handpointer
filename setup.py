from setuptools import find_packages, setup
import os

def _get_requirements():
  with open('requirements.txt') as f:
    return [ line.rstrip() for line in f if not (line.isspace() or line.startswith('#'))]

setup(
    name='handpointer',
    packages=find_packages(include=['handpointer']),
    version='0.1.0',
    description='Control something in 3D with a webcam and your hand',
    author='Viktor Lorentz',
    license='Apache 2.0',
    install_requires=_get_requirements(),
)