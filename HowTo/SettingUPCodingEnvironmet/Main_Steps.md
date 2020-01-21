# Setup Linux Environment
## For PC only:
Setup Windows Subsystem for Linux (WSL).
  1. Activate WSL.
  1. Install Linux distribution (Ubuntu) from Microsoft Store.
  1. Restart computer.

## Setting Up Your Environment: `~/.bashrc` and `~/.zshrc`

>This is appliable for both Ubuntu (Local or Remote) and WSL-Ubuntu 
already Installed.  
For a unix/linux machine we will assume the following steps are 
applicable to both local and remote machines, unless specified 
specifically.  

> A few tips and commands for linux (ubuntu): [link-to-file](...)

1. Update and upgrade linux (ubuntu).  
    ```bash
    # Run these commands in a bash shell to 
    # update and then upgrade linux.
    apt-get update
    apt-get upgrade
    ```
1. Install `zsh` and `git`.  
    ```bash
    # Run these commands in a bash shell
    sudo apt-get install zsh
    sudo apt-get install git
    ```
1. Download and Setup **oh-my-zsh**.  
   Visit [oh-my-zsh git-repo](https://github.com/ohmyzsh/ohmyzsh) and 
   download it directly into the linux home using `curl`, as shown in 
   the documentation at the github-repository.  
   ```bash
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   ```
   This step clones the repo and replaces the existing `~/.zshrc` with 
   a template from `oh-my-zsh`; it also makes a backup of the existing 
   `~/.zshrc` file.  
   + You could use `ls -la` command to enlist all the 
   files, including `~/.bashrc` and `~/.zshrc` (_which are otherwise 
   hidden files, and hence you would not see them with `ls` command_).  
   + Use `nano ~/.bashrc` or `nano ~/.zshrc` to open/edit the files 
   if need be.
   
1. Update `~/.bashrc` and `~/.zshrc` files.  
1. Further Updates to `~/.bashrc` file:  
  5.1. Setup symbolic links (shortcuts) to frequently used filepaths.  
  5.2. Setup aliases for frequently used and/or long commands.  
  5.3. Setup exports for environment variable names (if any).  
  
## Installing Necessary Fonts for Properly Viewing _oh-my-zsh_ Styling of the Terminal

1. If you are accessing WSL-Ubuntu or Remote-Ubuntu/Linux/Unix 
from a Windows 10 PC, you may observe that the `zsh` fonts at 
first do not look like the images here. In that case you will 
have to _**install** the necessary fonts_ on your **Windows 10 PC**. 
  1. Open PowerShell with administrator access in Windows 10.  
  > **`image-here`**
  1. Navigate to your desired directory where you would like to 
  download the fonts from GitHub. And issue the following lines 
  of command in the powershell window.  
  
  >_Suggestion_: maintain a folder `"GitHub"` for all the github 
  repositories that you would download or work on. Each such repo 
  will have its own folder under GitHub. This will make maintenance 
  easire later on.
   
  
  ```bash
  git clone https://github.com/powerline/fonts.git
  cd fonts
  powershell -ExecutionPolicy Bypass -File .\install.ps1
  ```

## Installing Miniconda to Manage Python Environments
1. Go to this site and download the miniconda distribution for 
`python 3.7` using `wget` directly into your home directory as follows.  
```bash
cd ~
mkdir Miniconda && cd Miniconda
wget <doenload_link_miniconda3_py37>
tar -zxvf <doenload_link_miniconda3_py37>
??
```
>**Notes for myself**: check the video and correct this part.  

## Installing VS Code
> <Image_VSCode_Download>  

VS Code is a freely available Integrated Developer Environment (IDE), 
where you could code in a number of coding languages. It also doubles 
up as a text-editor.  
The good thing is that it is available for Windows, Mac and Linux. 
Once installed, you can add various plugins and transform your coding 
environment into a more productive, effective and crisp developer 
experience.  
Additionally, now you can also use VS Code to connect to a remote server 
and directly code there. It also provides a seemless method to connect 
to WSL on Window 10. So, we can use VS Code in each of the follwoing cases:  
1. Coding on Windows 10 (PC).
1. Coding on Mac OSX. 
1. Coding on WSL with VS Code installed on Windows 10 (PC). 
1. Coding on Remote Server with Linux and accessing it from VS Code installed on PC or Mac. 

>**Note**: For technical clarity note that at the time of writing this document I 
used WSL 2.0  

> <Image_VSCode_Window_Screenshot>

### Download and Install VS Code
Go to https://code.visualstudio.com/ and download VS Code installer for your OS (Windows/Mac/Linux) and install it. 
See [this video](#ref) for installation demo.  

## Setting Up VS Code
Refer to these articles and videos to setup VS Code as you like. You may choose to use the following set of plugins that I personally would recommend. There are many more available, and you could choose them as per your development-needs. 
> <list of web-links | include Corey-Schafer video>

### Recommended Plugins for Python Development in VS Code
1. [Python _by_ Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
1. [Anaconda Extension Pack _by_ Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.anaconda-extension-pack)
1. [Remote - WSL _by_ Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
1. [Remote - SSH _by_ Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
1. [Remote - Container _by_ Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
1. [autoDocstring _by_ Nils Werner](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
1. [Better Comments _by_ Aaron Bond](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
1. [file-icons _by_ file-icons](https://marketplace.visualstudio.com/items?itemName=file-icons.file-icons)
1. [YAML _by_ Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
1. [Project Manager _by_ Alessandro Fragnani](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager)
1. [Output Colorizer _by_ IBM](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer)
1. [Path Intellisense _by_ Christian Kohler](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)
1. [neuron _by_ neuron](https://marketplace.visualstudio.com/items?itemName=neuron.neuron-IPE)
1. [SandDance for VSCode _by_ Microsoft DevLabs](https://marketplace.visualstudio.com/items?itemName=msrvida.vscode-sanddance)
1. [Sublime Text Keymap and Settings Importer _by_ Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode.sublime-keybindings)
1. [Instant Markdown _by_ David Bankier](https://marketplace.visualstudio.com/items?itemName=dbankier.vscode-instant-markdown)
1. [LaTeX Workshop _by_ James Yu](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
1. [Markdown PDF _by_ yzane](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)
1. [Image preview _by_ Kiss Tamás](https://marketplace.visualstudio.com/items?itemName=kisstkondoros.vscode-gutter-preview)
1. [Bookmarks _by_ Alessandro Fragnani](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)
1. [Material Theme Kit _by_ Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode.Theme-MaterialKit)
1. [GitHub Pull Requests _by_ GitHub _[Preview]_](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)

## Accessing WSL-Ubuntu or Remote Server (Linux) with VS Code
The setup procedure is quite simple and there is nice documentation available as well.  
+ [How to use VS Code Plugin for accessing WSL?](https://code.visualstudio.com/blogs/2019/09/03/wsl2)
+ [How to use VS Code Plugin for accessing Remote Server](https://code.visualstudio.com/blogs/2019/07/25/remote-ssh)


# References

1. Abhishek Thakur's Video: Setting up Code-Server 
(_VS Code-like-IDE_) [YouTube Video](https://youtu.be/ArygUBY0QXw)
1. Abhishek Thakur's Video: Setting up Environment
(_python_, _zsh_ and _oh-my-zsh_) [YouTube Video](https://www.youtube.com/watch?v=N9lo_UxSkWA)
1. Official VS Code Plugin for WSL and Remote Server - Guide:  
   + [How to use VS Code Plugin for accessing WSL?](https://code.visualstudio.com/blogs/2019/09/03/wsl2)
   + [How to use VS Code Plugin for accessing Remote Server](https://code.visualstudio.com/blogs/2019/07/25/remote-ssh)
1. SSH Client Related:  
  4.1. [Installing a supported SSH Client](https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client)  
  4.2. [Installing the Windows 10 OpenSSH Client](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse#installing-openssh-from-the-settings-ui-on-windows-server-2019-or-windows-10-1809)  
     > To install **`OpenSSH`** on Windows 10: 
     >1. start `Settings` then go to `Apps` > `Apps and Features` > `Manage Optional Features`.  
     >1. Scan this list to see if OpenSSH client is already installed. If not, then  
            + at the top of the page select **`Add a feature`**.  
            + locate **OpenSSH Client**, then click **`Install`**.  
1. [VS Code on remote server using https://coder.com/](https://forums.fast.ai/t/vs-code-on-remote-server-using-https-coder-com/44909)
1. [Managing Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
1. [Setting up Windows Subsystem for Linux with zsh + oh-my-zsh + ConEmu](https://blog.joaograssi.com/windows-subsystem-for-linux-with-oh-my-zsh-conemu/)
1. [PowerShell says “execution of scripts is disabled on this system.”](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system) `-->` `powershell -ExecutionPolicy Bypass -File script.ps1`.
1. [How to Access Your Ubuntu Bash Files in Windows (and Your Windows System Drive in Bash)](https://www.howtogeek.com/261383/how-to-access-your-ubuntu-bash-files-in-windows-and-your-windows-system-drive-in-bash/)
1. [How to Use Zsh (or Another Shell) in Windows 10](https://www.howtogeek.com/258518/how-to-use-zsh-or-another-shell-in-windows-10/) `-->` `wsl zsh` in `cmd`.
1. [oh-my-zsh: github-repo](https://github.com/ohmyzsh/ohmyzsh)
1. [Miniconda Installer Download Page](https://docs.conda.io/en/latest/miniconda.html)
1. [VS Code SSH: Getting STarted](https://code.visualstudio.com/docs/remote/ssh#_getting-started)
1. [WSL 2 with Visual Studio Code](https://code.visualstudio.com/blogs/2019/09/03/wsl2)
1. [Windows as a Linux developer machine](https://code.visualstudio.com/docs/setup/linux#_windows-as-a-linux-developer-machine)
1. [Visual Code Online](https://code.visualstudio.com/updates/v1_41#_visual-studio-online)
1. [Remote Development](https://code.visualstudio.com/updates/v1_41#_remote-development)
1. [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)
1. [Remote Developing in WSL: Getting Started](https://code.visualstudio.com/remote-tutorials/wsl/getting-started)
