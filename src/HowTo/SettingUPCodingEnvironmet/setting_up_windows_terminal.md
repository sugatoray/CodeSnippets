# Setting up Windows Terminal

- Color Schemes: 
  
  The color schemes can be changed as documented here: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes.
  
  - Default color schemes: 
  
    [**Included color schemes**][#included-color-schemes]
    
    [#included-color-schemes]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#included-color-schemes
    
    - [x] [Campbell][#campbell]:                `"colorScheme": "Campbell"`
    - [x] [Campbell Powershell][#campbell-ps]:  `"colorScheme": "Campbell Powershell"`
    - [x] [Vintage][#vintage]:                  `"colorScheme": "Vintage"`
    - [x] [One Half Dark][#one-half-dark]:      `"colorScheme": "One Half Dark"`
    - [x] [One Half Light][#one-half-light]:    `"colorScheme": "One Half Light"`
    - [x] [Tango Dark][#tango-dark]:            `"colorScheme": "Tango Dark"`
    - [x] [Tango Light][#tango-light]:          `"colorScheme": "Tango Light"`
    
    [#campbell]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#campbell
    [#campbell-ps]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#campbell-powershell
    [#vintage]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#vintage
    [#one-half-dark]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#one-half-dark
    [#one-half-light]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#one-half-light
    [#tango-dark]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#tango-dark
    [#tango-light]: https://docs.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes#tango-light
    
  - Custom color schemes: https://docs.microsoft.com/en-us/windows/terminal/custom-terminal-gallery/custom-schemes
    - [x] [Frosted Glass][#forsted-glass]:           `"colorScheme": "Frost"`
    - [x] [Powerline][#powerline]:                   `"colorScheme": "Powerline"`
    - [x] [Raspberry Ubuntu][#raspberry-ubuntu]:     `"colorScheme": "Raspberry"`
    - [x] [Retro Command][#retro-command]:           `"colorScheme": "Retro"`    
    
    [#forsted-glass]: https://docs.microsoft.com/en-us/windows/terminal/custom-terminal-gallery/custom-schemes#frosted-glass
    [#powerline]: https://docs.microsoft.com/en-us/windows/terminal/custom-terminal-gallery/custom-schemes#powerline
    [#raspberry-ubuntu]: https://docs.microsoft.com/en-us/windows/terminal/custom-terminal-gallery/custom-schemes#raspberry-ubuntu
    [#retro-command]: https://docs.microsoft.com/en-us/windows/terminal/custom-terminal-gallery/custom-schemes#retro-command
    
  - External Custom Color schemes
  
    - [x] [Dracula][#dracula]:                       `"colorScheme": "Dracula"`
    
    [#dracula]: https://draculatheme.com/windows-terminal

## Using Powerline Fonts

### Install fonts
See the video from here: [_Tutorial: Set up Powerline in Windows Terminal_][#ps-powerline-fonts-setup]

[#ps-powerline-fonts-setup]: https://docs.microsoft.com/en-us/windows/terminal/tutorials/powerline-setup

### Setup Windows PowerShell Profile


```bash
## Step - 1
echo $PROFILE
# C:\Users\raysu\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

## Step - 2
start C:\Users\raysu\Documents\WindowsPowerShell\
# this opens the location in explorer

## Step - 3
notepad $PROFILE
# this opens the file if it already exists 
# OR ... 
# creates a new powershell-profile with user's permission
```

Paste the following content to the `powershell-profile` file.

```bash
## Step - 4
# save the following content to $PROFILE
# >>> notepad $PROFILE
# change execution-policy from elevated PowerShell
# >>> Set-ExecutionPolicy RemoteSigned -Scope LocalMachine

Import-Module posh-git
Import-Module oh-my-posh
Set-Theme Paradox
```

**A known problem/bug**:

The defaault **`ExceutionPolicy`** in Windows is `Restricted`. This **blocks** execution of any `.ps1` script. As you can see, the following error was thrown right after PowerShell started and tried to run the script located at `$PROFILE`. The `$PROFILE` is an environment variable that points to the default location of `Microsoft.PowerShell_profile.ps1` file.

See [PowerShell Execution Policies][#ps-execution-policies] for more details.

[#ps-execution-policies]: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7

```bash
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

. : File C:\Users\raysu\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1 cannot be loaded because running
scripts is disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:3
+ . 'C:\Users\raysu\Documents\WindowsPowerShell\Microsoft.PowerShell_pr ...
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
PS C:\Users\raysu>
```

> **REMEDY**  
>
> Open PowerShell as an administrator (in *elevated* mode) and run the following command to change the `ExceutionPolicy` for local scripts. 
>
> ```bash
> Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
> ```
