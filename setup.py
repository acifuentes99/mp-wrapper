import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='mp-wrapper',  
     version='0.1',
     scripts=['mp-wrapper'] ,
     author="Andrés Cifuentes",
     author_email="aecifuentesv@gmail.com",
     description="Wrapper para Mercado Pago para librerias API",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "Operating System :: OS Independent",
     ],
 )
