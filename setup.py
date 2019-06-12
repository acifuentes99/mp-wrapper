# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mp-wrapper',  
    version='0.1',
    author="Andrés Cifuentes",
    author_email="aecifuentesv@gmail.com",
    description="Wrapper para Mercado Pago para librerias API",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
 )
