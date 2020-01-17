# Managing Environments with Conda and Pip

**List of resources**:  
1. [Managing environments - conda-docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
1. [A Minimalist Approach to Python Virtual Environments - towardsdatascience](https://towardsdatascience.com/a-minimalist-approach-to-python-virtual-environments-f5dacf76bfad)
1. [Python Virtual Environments: A Primer - realpython](https://realpython.com/python-virtual-environments-a-primer/)
1. [Conda and pip - managing environments - berkley](https://berkeley-stat159-f17.github.io/stat159-f17/lectures/06-conda-pip-environments..html)
1. [Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/)
1. [The Definitive Guide to Conda Environments - towardsdatascience](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533)


# Updating Conda Environments
Source: https://docs.conda.io/projects/conda/en/latest/commands/update.html  
**Command format**:  
Here is a short version of what I use often. For more details see 
[here](https://docs.conda.io/projects/conda/en/latest/commands/update.html).  
```bash
conda update [-n Environment] [-c Channel] [package_spec]
```

## Updating conda base environment: 
```bash
conda update -n base -c defaults conda
```
