# What is MANIFEST.in file for?

Your repository could contain a lot of files which you may not always want to add 
to the python-package associated with the repository. So, in a nutshell, you want 
some mechanism to control which files and directories to include in or exclude from 
the packaged version of your repository.

> Enters `MANIFEST.in` file. See the 
> [documentation here][#docs-manifest-in]. :star:

[#docs-manifest-in]: https://packaging.python.org/guides/using-manifest-in/

[![image](https://user-images.githubusercontent.com/10201242/125386595-29a65980-e362-11eb-8842-3896da6cef1d.png)][#docs-manifest-in]


## Example

### 1. Minimal example

source: https://github.com/dr-prodigy/python-holidays

```sh
include *.py
include *.rst
include LICENSE
include CHANGES
```

### 2. A bit more advanced example

source: https://github.com/PyTorchLightning/lightning-bolts

```sh
# Manifest syntax https://docs.python.org/2/distutils/sourcedist.html
graft wheelhouse

recursive-exclude __pycache__  *.py[cod] *.orig

# Include the README and CHANGELOG
include *.md
recursive-include pl_bolts *.md

# Include the license file
include LICENSE

exclude *.sh
exclude *.toml
exclude *.svg
recursive-include pytorch_lightning *.py

# exclude tests from package
recursive-exclude tests *
recursive-exclude site *
exclude tests

# Exclude the documentation files
recursive-exclude docs *
exclude docs

# Include the Requirements
include requirements.txt
recursive-include requirements *.txt

# Exclude build configs
exclude *.yml

# Exclude Makefile
exclude Makefile

prune .git
prune .github
prune .circleci
prune notebook*
prune temp*
prune test*
prune benchmark*
```
