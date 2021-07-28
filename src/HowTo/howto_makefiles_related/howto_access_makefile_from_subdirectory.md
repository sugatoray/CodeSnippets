# How to access a `Makefile` from a subdirecyory of your project

The following is a modification of the Makefile used in 
[`PyTorchLightning/lightning-bolts`][#gh-repo-lightning_bolts] repo on GitHub.
I use this Makefile for running various commands in 
[`omry/omegaconf`][#gh-repo-omegaconf] project on GitHub. 

[#gh-repo-lightning_bolts]: https://github.com/PyTorchLightning/lightning-bolts
[#gh-repo-omegaconf]: https://github.com/omry/omegaconf/

> *Disclaimer*: Some of the commands may not work, however, overall it seems to work.

## The use-case

The `omegaconf` repository does not contain any Makefile of it's own. So, to use a Makefile 
just for myself, and not having to add an entry to ignore this Makefile in the `.gitignore` file, 
I placed the Makefile in the `.vscode` directory (since *.vscode* is already added to *.gitignore* file).
However, this meant that I will not be able to run the commands as `make [COMMAND]` from the 
project root directory (`omegaconf`). 

So, I looked up on Stackoverflow and found this answer: [How to run make file from any directory?][#soq]

[#soq]: https://superuser.com/questions/370575/how-to-run-make-file-from-any-directory/1258431

In a nutshell, the best answer there suggested either of the methods would work (but it did not fit my usecase).

```bash
# method-1
(cd /other/dir && make)

# method-2
make -C /other/dir
```

What I was looking for is: create a Makefile to run from the project root directory, but then move 
it into the .vscode subdirectory; and finally run the make commands from the project root directory. 
And the solution requires you to specify the location of the Makefile, while running the command 
from the project root direcyory.

```bash
make -f ./.vscode/Makefile [COMMAND]
```

Now in order to make life easier, I added another alias (`xmake`), such that I could simply replace the `make` 
command while running it from the project-root.

```bash
alias xmake="make -f ./.vscode/Makefile"
```

And now I can just do this:

```bash
# this will run the docs COMMAND from the Makefile
xmake docs
```

## Example Makefile

```makefile
.PHONY: test clean testcov docs env

# assume you have installed need packages
export SPHINX_MOCK_REQUIREMENTS=1

# We keep this makefile inside .vscode
# To run this file from the root of the project
# use: make -f ./.vscode/Makefile [COMMAND]
# For convenience, create an alias:
# $ alias xmake="make -f ./.vscode/Makefile"
# And then use xmake instead of make from the
# project-root.

clean:
	@echo "\n🗑️ Cleaning up... ⏳\n"
	# clean all temp runs
	rm -rf $(shell find . -name "mlruns")
	rm -rf _ckpt_*
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf ./docs/build
	rm -rf ./docs/source/generated
	rm -rf ./docs/source/*/generated
	rm -rf ./docs/source/api

test: clean env
	@echo "\n👀 Running tests... ⏳\n"
	# run tests with coverage
	python -m coverage run --source omegaconf -m pytest omegaconf tests -v
	python -m coverage report
	## For coverage reports
	# pytest --cov omegaconf --cov-report html
	## For running pytest on a single test_function
	#  use: pytest filepath::test_function
	# pytest tests/test_omegaconf.py::test_clear_resolver

testcov: clean env
	@echo "\n📊 Generating test-coverage report... ⏳\n"
	pytest --cov omegaconf --cov-report html

docs: clean
	@echo "\n📘📄 Creating docs... ⏳\n"
	# pip install --quiet -r docs/requirements.txt
	python -m sphinx -b html -W docs/source docs/build

env:
	@echo "\n🔥⚙️ Install dev-env-requirements... ⏳\n"
	pip install -r requirements/dev.txt

format:
	@echo "\n✨📐 Formatting files... ⏳\n"
	black .
	isort .
	# yapf . -rip

```
