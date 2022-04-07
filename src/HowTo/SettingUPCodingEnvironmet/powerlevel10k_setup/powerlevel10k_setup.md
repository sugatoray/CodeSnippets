# Setting up Powerlevel10k Theme in Zsh

See updated instructions for installation here:

- https://github.com/romkatv/powerlevel10k#oh-my-zsh

## Steps

1. Install with `oh-my-zsh`.

   ```sh
   git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
   ```

   And copy the contents of the following file to `~/.p10k.zsh`:

   - `sample_p10k.zsh`

2. Add the following at the top of `~/.zshrc` file.

   ```sh
   # Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
   # Initialization code that may require console input (password prompts, [y/n]
   # confirmations, etc.) must go above this block; everything else may go below.
   if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
     source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
   fi
   
   ```

3. Add the following at the bottom of `~/.zshrc` file.

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

4. Comment out the following line with `ZSH_THEME` variable:

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
