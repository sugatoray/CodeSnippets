# What is `.pre-commit-config.yaml` file for?

[Pre-commit](https://pre-commit.com/) is a python package that helps prevent wrong code getting into a commit. 
It automates the checking such that small bugs are caught early. It can also be customised!

- https://calmcode.io/pre-commit/the-problem.html
- https://calmcode.io/pre-commit/the-concept.html
- https://calmcode.io/pre-commit/installation.html
- https://calmcode.io/pre-commit/first-run.html
- https://calmcode.io/pre-commit/json-checks.html
- https://calmcode.io/pre-commit/flake8-for-python.html
- https://calmcode.io/pre-commit/how-it-works.html
- https://calmcode.io/pre-commit/spelling.html
- https://calmcode.io/pre-commit/no-tests.html
- https://calmcode.io/pre-commit/auto-update.html

## Examples

### 1. Example from a smaller repo

source: https://github.com/dr-prodigy/python-holidays

```yml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.3.0
    hooks:
      - id: check-ast
      - id: check-builtin-literals
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: fix-encoding-pragma
      - id: mixed-line-ending
        args: [--fix=lf]

  - repo: https://github.com/python/black
    rev: 20.8b1
    hooks:
      - id: black
        language_version: python3

  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.4
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/pygrep-hooks
    rev: v1.7.0
    hooks:
      - id: rst-backticks

  - repo: https://github.com/myint/rstcheck
    rev: 3f92957478422df87bd730abde66f089cc1ee19b
    hooks:
      - id: rstcheck
        additional_dependencies: [rstcheck]

  - repo: https://github.com/asottile/setup-cfg-fmt
    rev: v1.16.0
    hooks:
      - id: setup-cfg-fmt
```

### 2. Example from a larger repo

source: https://github.com/PyTorchLightning/lightning-bolts

```yml
default_language_version:
  python: python3.8


repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-case-conflict
      - id: check-yaml
      - id: check-toml
      - id: pretty-format-json
      - id: check-added-large-files
      - id: check-docstring-first
      - id: detect-private-key

  - repo: https://github.com/PyCQA/isort
    rev: 5.9.1
    hooks:
      - id: isort

  - repo: https://github.com/pre-commit/mirrors-yapf
    rev: 'v0.31.0'
    hooks:
      - id: yapf

  - repo: https://github.com/PyCQA/flake8
    rev: 3.9.2
    hooks:
      - id: flake8
```
