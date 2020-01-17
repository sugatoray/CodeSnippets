# Managing Environments with Conda and Pip

**List of resources**:  
1. [L](L)


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
