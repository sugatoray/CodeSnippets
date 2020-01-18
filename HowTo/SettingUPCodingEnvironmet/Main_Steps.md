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

1. Update and upgrade linux (ubuntu).  
1. Install `zsh`.  
1. Download and Setup **oh-my-zsh**.  
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

# References

1. Abhishek Thakur's Video: Setting up Code-Server 
(_VSCode-like-IDE_) [YouTube Video](https://youtu.be/ArygUBY0QXw)
1. Abhishek Thakur's Video: Setting up Environment
(_python_, _zsh_ and _oh-my-zsh_) [YouTube Video](https://www.youtube.com/watch?v=N9lo_UxSkWA)
1. Official VSCode Plugin for WSL and Remote Server - Guide:  
   + [How to use VSCode Plugin for WSL?](https://code.visualstudio.com/blogs/2019/09/03/wsl2)
   + [How to use VSCode Plugin for Remote Server](https://code.visualstudio.com/blogs/2019/07/25/remote-ssh)
1. SSH Client Related:  
  4.1. [Installing a supported SSH Client](https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client)  
  4.2. [Installing the Windows OpenSSH Client]()  
  > To install **`OpenSSH`** on Windows 10:  
      A. start `Settings` then go to `Apps` > `Apps and Features` > `Manage Optional Features`.  
      B. Scan this list to see if OpenSSH client is already installed. If not, then  
         + at the top of the page select **`Add a feature`**.  
         + locate **OpenSSH Client**, then click **`Install`**.  


