#!/bin/bash

### Include this in all files
# source: ~/systemsetup/preamble.sh
_SCRIPT=$(realpath -s $BASH_SOURCE)
_SCRIPTPATH=$(dirname "$_SCRIPT")
_USER=$(stat -c '%U' $_SCRIPT)
_GROUP=$(stat -c '%G' $_SCRIPT)
_HOME='/home/'$_USER


# Define installation directory
MINICONDA_INSTALLATION_DIR=$_HOME'/miniconda3'

# Download miniconda installer
MINICONDA_INSTALLER_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
MINICONDA_INSTALLER_LOCAL=$_HOME"/temp/miniconda.sh"
wget $MINICONDA_INSTALLER_URL -O $MINICONDA_INSTALLER_LOCAL

# Install miniconda (silently)
bash $MINICONDA_INSTALLER_LOCAL -b -p $MINICONDA_INSTALLATION_DIR

# Setup bash for use with conda
SHELL_NAME="bash"
eval "$($MINICONDA_INSTALLATION_DIR/bin/conda shell.$SHELL_NAME hook)"
# Setup "conda init" in bash 
conda init

### Tear-down
unset \
    _SCRIPT \
    _SCRIPTPATH \
    _USER \
    _GROUP \
    _HOME \
    MINICONDA_INSTALLATION_DIR \
    MINICONDA_INSTALLATION_LOCAL \
    MINICONDA_INSTALLATION_URL \
    SHELL_NAME
