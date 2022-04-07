# Setting up Powerlevel10k Theme in Zsh

See updated instructions for installation here:

- https://github.com/romkatv/powerlevel10k#oh-my-zsh

> **Note:**
>
> Whenever you make any changes inside `~/.zshrc` or `~/.p10k.zsh`, to see the effects do one of the following:
> 
> - close the current terminal and open a new terminal
> - run `exec zsh` without closing the current terminal

## Steps

### Install with `oh-my-zsh`.

   ```sh
   git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
   ```

   This will create a folder `powerlevel10k` under `$ZSH_CUSTOM/themes`.
   
   ![image](https://user-images.githubusercontent.com/10201242/162110694-60dbc9f0-b3f4-4267-9b4b-842c4235a403.png)


   Now, copy the contents of the following file to `~/.p10k.zsh`:

   - [`sample_p10k.zsh`](sample_p10k.zsh)
   
   Once you also setup the `~/.zshrc` file (as descrbed in the next step), 
   this will set the terminal look like this:
   
   - Inside VS Code:
   
     ![image](https://user-images.githubusercontent.com/10201242/162108322-7dee7c57-8ef0-43ef-abd7-3957c6292f97.png)

   - Inside ZSH in regular terminal:
   
     ![image](https://user-images.githubusercontent.com/10201242/162108633-e0384e37-a749-4ae9-b076-bea8f7396ca6.png)

### Setup `~/zshrc`

   This is a sample `~/.zshrc` file
   - [`sample_zshrc`](sample_zshrc)

1. Add the following at the top of `~/.zshrc` file.

   ```sh
   # Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
   # Initialization code that may require console input (password prompts, [y/n]
   # confirmations, etc.) must go above this block; everything else may go below.
   if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
     source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
   fi
   
   ```

2. Add the following at the bottom of `~/.zshrc` file.

   ```sh
   # For powerlevel10k
   # installed with:
   # git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
   # source:
   # - https://github.com/romkatv/powerlevel10k#oh-my-zsh
   source ~/powerlevel10k/powerlevel10k.zsh-theme
   
   # To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
   [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
   
   ```

3. Comment out the following line with `ZSH_THEME` variable:

   ```sh
   # ZSH_THEME="agnoster"
   ```
   And then add the following right after the line with `ZSH_THEME` variable.
   
   ```
   # powerlevel10k theme activation
   ZSH_THEME="powerlevel10k/powerlevel10k"
   
   # POWERLEVEL9K_DISABLE_RPROMPT=true
   # POWERLEVEL9K_PROMPT_ON_NEWLINE=true
   # POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX="▶"
   # POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=""
   ```
