from setuptools import setup

setup(
   name='my_package',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['my_package'],  #same as name
   install_requires=['numpy>1.20', 'scikit-learn'], #external packages as dependencies
)