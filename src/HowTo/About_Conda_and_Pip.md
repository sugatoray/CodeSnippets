# Managing Environments with Conda and Pip

**List of resources**:  
1. [Managing environments - conda-docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
1. [A Minimalist Approach to Python Virtual Environments - towardsdatascience](https://towardsdatascience.com/a-minimalist-approach-to-python-virtual-environments-f5dacf76bfad)
1. [Python Virtual Environments: A Primer - realpython](https://realpython.com/python-virtual-environments-a-primer/)
1. [Conda and pip - managing environments - berkley](https://berkeley-stat159-f17.github.io/stat159-f17/lectures/06-conda-pip-environments..html)
1. [Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/)
1. [The Definitive Guide to Conda Environments - towardsdatascience](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533)
1. [**Conda configuration management: updating `.condarc` file**][#conda-config-condarc]


[#conda-config-condarc]: https://docs.conda.io/projects/conda/en/latest/configuration.html


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

## Creating conda environment:

1. **Create an environment with a `-n` or `--name` flag**. 
We also specify the python version and install some libraries using conda in a 
single line.  
    ```bash
    conda create -n env_name python=3.7 numpy scipy matplotlib pandas
    ```
1. **Create an environment from an `environment.yml` file**.  
The environment is created under a directory path given by `--prefix` flag as shown 
below. Preferably create the environment under a relative path for each project at: 
`"./.env"` where `"."` is the root directory of the project repo. 

    ```bash
    conda env create --prefix ./.env -f envirnment.yml
    ```
1. **Activation/deactivation of the environment**.  
When activating an environment which is located at a non-default location, post 
activation conda **_shows an entire path_** instead of just `(base)` or `(env_name)`. 
Only environments created with a `-n` or `--name` flag show the `(env_name)` in 
front of the path as the currently active conda environment -- this is convenient. 
Additionally, the list of environments thus created with `-n` flag could be searched 
using `conda env list` command.  

    So, there is a [quick fix](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment) to this. 
    You need to update the `.condarc` file using 
    `conda config --set env_prompt '({name})'` command. This will ensure that the 
    environment name is shortened and shows the name of the `.env` directory only. 

    But you must change it back to the original setting (for the `env_prompt` variable), 
    before deactivating the environment.

    The following lines of code explain this method.
    ```bash
    # for activating env
    conda config --set env_prompt '({name})'
    conda activate ./.env


    # for deactivating env
    conda config --set env_prompt '({default_env})'
    conda deactivate
    conda activate base
    ```
    + **Description of the `env_prompt` variable**  
    
        Source: [conda-config: `.condarc` file][#conda-config-condarc]
    
        ```bash
        ### .condarc file (env_prompt section)

        # # env_prompt (str)
        # #   Template for prompt modification based on the active environment.
        # #   Currently supported template variables are '{prefix}', '{name}', and
        # #   '{default_env}'. '{prefix}' is the absolute path to the active
        # #   environment. '{name}' is the basename of the active environment
        # #   prefix. '{default_env}' holds the value of '{name}' if the active
        # #   environment is a conda named environment ('-n' flag), or otherwise
        # #   holds the value of '{prefix}'. Templating uses python's str.format()
        # #   method.
        # # 
        # env_prompt: '({default_env}) '
        ```
    **Note**: The same has beed documented and answered in this [stackoverflow-question](https://stackoverflow.com/questions/60122569/how-to-revert-back-to-default-behavior-of-env-prompt-parameter-in-condarc/60122570#60122570).
