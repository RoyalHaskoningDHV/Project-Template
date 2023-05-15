from setuptools import setup, find_packages

setup(name='{{cookiecutter.pkg_name}}',
      version='{{cookiecutter.version}}',
      description='{{cookiecutter.project_short_description}}',
      long_description=open('README.md').read(),
      url='',
      author='{{cookiecutter.full_name}}',
      author_email='{{cookiecutter.email}}',
      license='',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[]
      )
