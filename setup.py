from setuptools import setup

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
      version='1.0',
      description='Unoffical Discord Api Wrapper. The library works on discord.py 1.7.3',
      license='MIT',
      packages=['hado'],
      author_email='kirasimshow@gmail.com',
      extras_require=extras_require,
      python_requires='>=3.5.8',
      zip_safe=False)