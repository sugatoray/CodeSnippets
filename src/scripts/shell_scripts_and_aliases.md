# A compilation of various functions and aliases

```sh
# A function to print a numeric value with a given number of leading digits
padnum() { VALUE=$1; NUMDIGITS=$2; $(which python3) -c "print(f'{${VALUE}:0${NUMDIGITS:-5}}')"; unset VALUE NUMDIGITS; }

alias filtergroups='cut -d ":" -f2 | xargs'
getgroups() { _G=$(groups $1); _G=(echo ${_G} | filtergroups); echo $_G; unset _G; }
alias mygroups="groups $USER | filtergroups"

# If a group name ends in "ro", return "ro"; else return "rw".
checkrorw() { _VAL=$1; if [[ ${_VAL#${_VAL%ro}} == "ro" ]]; then echo "ro"; else echo "rw"; fi; unset _VAL; }
getadgroups() { _ENV=$1; if [[ -z "$_ENV" ]]; then _ENV=PROD; fi; for g in $(getgroups $2); do if [[ $g != "staff" ]]; then echo "G-APP-SAS-$g-$(checkrorw $g)-${_ENV}"; fi; done; unset _ENV; }
alias myadgroups="getadgroups"

## Adding quotes in a for loop: https://stackoverflow.com/a/38558454/8474894
getquotedgroups() { (a=(); for g in $(getgroups $1); do a+=("\"${g}\", "); done; a="${a[@]}"; echo ${a::-2};) }
alias quotedmygroups="getquotedadgroups"

# Alternatively, use this:
alias quotemygroups='a=(); for g in $(groups); do a+=("\"${g}\", "); done; a="${a[@]}"; echo ${a::-2};'
# Or, run: enquote $(groups)
enquote() { (_G=$@; a=(); for g in ${_G}; do a+=("\"${g}\", "); done; a="${a[@]}"; echo ${a::-2};) }

## String Manipulation
# source:
# - https://en.wikipedia.org/wiki/Tr_%28Unix%29
# - https://stackoverflow.com/a/2264537

# Convert to lowercase:
#   example: echo "Hello" | tolower
#   output: hello
alias tolower='tr [:upper:] [:lower:]'
# Convert to uppercase:
#   example: echo "Hello" | toupper
#   output: HELLO
alias toupper='tr [:lower:] [:upper:]'

## Generate User Alias
alias genuseralias='echo $GIT_USER_NAME | cut -d " " -f1 | tolower'

## Setting up SSH
mkdir -p ~/.ssh
mkfile() { _FPATH=$1; if [[ -f "${_FPATH}" ]]; then touch ${_FPATH}; fi; unset _FPATH; }
mkfile ~/.ssh/known_hosts
mkfile ~/.ssh/authorized_keys
mkfile ~/.ssh/sshd_config
mkfile ~/.ssh_setup

```
