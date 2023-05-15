## Version: {{cookiecutter.version}}

# {{cookiecutter.repo_name}} description

{{cookiecutter.project_short_description}}

Author: {{cookiecutter.full_name}}
Email: {{cookiecutter.email}}

Reviewers: {{cookiecutter.reviewer_1}}, {{cookiecutter.reviewer_2}}

# Run options

``` 
```

# Testing

```
```

{%- if cookiecutter.pkg_name|lower != 'not applicable' and cookiecutter.language|lower == "python"%}
# Package installation
This is done by going to the root folder of this package, and running pip install -e . This will install a development version of the package locally. That means that if you make local changes, the package will automatically reflect them. It is recommended to do this in a virtual environment such as `venv`.

If you want to develop in a notebook, you will also need to reload the {{cookiecutter.pkg_name}} package whenever you run from {{cookiecutter.pkg_name}} import x. This can be achieved by putting the following lines at the top of every notebook:

```
%load_ext autoreload
%autoreload 1
%aimport {{cookiecutter.pkg_name}}
```

This will reload {{cookiecutter.pkg_name}} everytime you run a new cell. The third line is optional: if you leave it out, you will reload every import every cell, instead of only those from {{cookiecutter.pkg_name}}.

{%- endif %}


{%- if cookiecutter.documentation == 'y' or cookiecutter.language|lower != "python"%}

# Documentation

Building the documentation can be done through the following command within the main directory:

```
sphinx-build -b html ./docs/source/ ./docs/build/
```

You will need to have the following packages:
```
pip install Sphinx==1.8.5
pip install sphinx_rtd_theme
pip install recommonmark
pip install numpydoc
```

Sphinx 2.0 is currently still broken when used together with numpydoc.
{%- endif %}
