# Updating `~/.bashrc`
>...steps here

# Updating `~/.zshrc`
>...steps here

# Some Useful Commands
## Creating an alias
**Creating an alias** (a short command) to run a command. [See more here](https://linuxize.com/post/how-to-create-bash-aliases/)  
```bash
alias alias_name="command_to_run"
```
## Creating a symbolic link
**Creating a symbolic link** (a shortcut) to frequently necessary paths.
**Resources**:  
1. https://unix.stackexchange.com/questions/207294/create-symlink-overwrite-if-one-exists?newreg=234448a7da2c4c59b7b6cbd183fbf379
2. https://askubuntu.com/questions/56339/how-to-create-a-soft-or-symbolic-link
3. https://askubuntu.com/questions/486461/how-to-create-folder-shortcut-in-ubuntu-14-04
4. https://askubuntu.com/questions/543516/what-is-a-failed-to-create-a-symbolic-link-file-exists-error
5. https://superuser.com/questions/81164/why-create-a-link-like-this-ln-nsf

### Command to create symbolic links to paths
The command to create symbolic links (soft links) is as follows.  
```bash
# Explanation from the "man ln" page:
# -f    If the target file already exists, then unlink it so that the
#       link may occur.  (The -f option overrides any previous -i options.)
#
# -n    Same as -h, for compatibility with other ln implementations.
#
# -s    Create a symbolic link.
##------------------------------------------------------------------##
ln -sfn "/mnt/c" Cdrive
ln -sfn "/mnt/d" Ddrive
```

### Removing an existing symbolic-link
Command to remove a symbolic link: `rm sum-link`

## Loading Windows 10 drives onto WSL
**Access from WSL-Ubuntu and load a path from Windows 10**
```bash
cd "~/mnt/c"  # without symbolic-link
cd Ddrive     # with symbolic-link
```
