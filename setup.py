from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

extras_require = {
    'voice': ['PyNaCl>=1.3.0,<1.5'],
    'docs': [
        'sphinx==3.0.3',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
    ]
}

setup(name='hado',
      version='1.1',
      description='Unoffical Discord Api Wrapper. The library works on discord.py 1.7.3',
      license='MIT',
      packages=['hado'],
      author_email='kirasimshow@gmail.com',
      install_requires=requirements,
      extras_require=extras_require,
      python_requires='>=3.5.8',
      zip_safe=False)