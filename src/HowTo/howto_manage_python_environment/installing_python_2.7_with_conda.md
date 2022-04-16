# Installing Python `2.7` using Conda

Once you have conda (miniconda) installed, use the following command to create a separate environment 
by the name `py27` (*you can choose any other name you like though*).

```sh
conda create -n py27 python=2.7
```

## Output

The following is a sample output of running a command mentioned above.

```sh
$ conda create -n py27 python=2.7

Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.11.0
  latest version: 4.12.0

Please update conda by running

    $ conda update -n base conda



## Package Plan ##

  environment location: /home/sugatoray/miniconda3/envs/py27

  added / updated specs:
    - python=2.7


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    certifi-2019.11.28         |   py27h8c360ce_1         149 KB  conda-forge
    libffi-3.2.1               |    he1b5a44_1007          47 KB  conda-forge
    pip-20.1.1                 |     pyh9f0ad1d_0         1.1 MB  conda-forge
    python-2.7.15              |h5a48372_1011_cpython        12.2 MB  conda-forge
    python_abi-2.7             |         1_cp27mu           4 KB  conda-forge
    setuptools-44.0.0          |           py27_0         663 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        14.1 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge
  _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-1_gnu
  ca-certificates    conda-forge/linux-64::ca-certificates-2021.10.8-ha878542_0
  certifi            conda-forge/linux-64::certifi-2019.11.28-py27h8c360ce_1
  ld_impl_linux-64   conda-forge/linux-64::ld_impl_linux-64-2.36.1-hea4e1c9_2
  libffi             conda-forge/linux-64::libffi-3.2.1-he1b5a44_1007
  libgcc-ng          conda-forge/linux-64::libgcc-ng-11.2.0-h1d223b6_15
  libgomp            conda-forge/linux-64::libgomp-11.2.0-h1d223b6_15
  libstdcxx-ng       conda-forge/linux-64::libstdcxx-ng-11.2.0-he4da1e4_15
  libzlib            conda-forge/linux-64::libzlib-1.2.11-h166bdaf_1014
  ncurses            conda-forge/linux-64::ncurses-6.3-h27087fc_1
  openssl            conda-forge/linux-64::openssl-1.1.1n-h166bdaf_0
  pip                conda-forge/noarch::pip-20.1.1-pyh9f0ad1d_0
  python             conda-forge/linux-64::python-2.7.15-h5a48372_1011_cpython
  python_abi         conda-forge/linux-64::python_abi-2.7-1_cp27mu
  readline           conda-forge/linux-64::readline-8.1-h46c0cb4_0
  setuptools         conda-forge/linux-64::setuptools-44.0.0-py27_0
  sqlite             conda-forge/linux-64::sqlite-3.38.2-h4ff8645_0
  tk                 conda-forge/linux-64::tk-8.6.12-h27826a3_0
  wheel              conda-forge/noarch::wheel-0.37.1-pyhd8ed1ab_0
  zlib               conda-forge/linux-64::zlib-1.2.11-h166bdaf_1014


Proceed ([y]/n)? y


Downloading and Extracting Packages
python-2.7.15        | 12.2 MB   | #################################################################################################################### | 100% 
setuptools-44.0.0    | 663 KB    | #################################################################################################################### | 100% 
certifi-2019.11.28   | 149 KB    | #################################################################################################################### | 100% 
pip-20.1.1           | 1.1 MB    | #################################################################################################################### | 100% 
python_abi-2.7       | 4 KB      | #################################################################################################################### | 100% 
libffi-3.2.1         | 47 KB     | #################################################################################################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate py27
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
