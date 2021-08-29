from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(name='hado',
      version='1.0',
      description='Unoffical Discord Api Wrapper. The library works on discord.py 1.7.3',
      license='MIT',
      packages=['hado'],
      author_email='kirasimshow@gmail.com',
      python_requires='>=3.5.8',
      zip_safe=False)