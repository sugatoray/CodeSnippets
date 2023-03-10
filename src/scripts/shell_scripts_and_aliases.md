# A compilation of various functions and aliases

## Single Line Functions and Aliases

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

## VS Code generated Core Files handling
getpath() { _PATH=$1; if [[ -z "${_PATH}" ]]; then _PATH="."; fi; echo ${_PATH}; unset _PATH; }
getabspath() { (realpath $(getpath $1);) }
# Create dummy core files: pattern is "core.#####...##"
mkcoredumps() { _PATH=$(getpath $1); for f in {891..899}; do touch ${_PATH}/core.${f}; done; unset _PATH; }
# Get a list of core dump files
getcoredumps() { _PATH=$(getpath $1); ls $_PATH | grep -E 'core\.[0-9]+'; unset _PATH; }
# Remove core dump files
rmcoredumps() { (_PATH=$(getpath $1); target_files=$(getcoredumps $_PATH); echo -e "\nDeleting files: \n${target_files}"; _CWD="$(realpath $(pwd))"; cd ${_PATH} && rm ${target_files}; cd ${_CWD}; unset target_files _PATH _CWD;) }

## Generate Hash with OpenSSL
showopensslver() { echo -e "Using $(openssl version)\n\n"; }
genhash-sha256() { openssl sha256 ${1} | cut -d "=" -f2 | xargs; }
genhash-md5() { openssl md5 ${1} | cut -d "=" -f2 | xargs; }

## Get All Admin Users
# lines to list: seq 5 | xargs
alias getadmins='cut -d ":" -f1 < /etc/passwd | sort | xargs'

## Date Functions and Aliases
alias timestamp='date +%Y%m%d_%H%M%S'
alias timestampx='date +%Y%m%d %H:%M:%S'

## Create backup (tar.gz) files
# source: sending output to logfile and console: https://stackoverflow.com/a/18462920/8474894
stringrep() { (_char=$1; _numrep=${2:-20}; _PYTHON=${3:-$(which python3)}; if [[ -z "${_numrep}" ]]; then _numrep=20; fi; "${_PYTHON}" -c "print('${_char}'*${_numrep})"; unset _char _numrep;); }
createpkg() { (_SEP=$(stringrep - 60); _PORTFOLIO=${PROJ_PORTFOLIO:-Auto}; _WFTKT=${1:-00000}; _ADTKT=${2:-00000}; _PROJ_PATH="/sasdata/crptrs1/pad"; _LOGDIRNAME="logs"; if [[ -z "${_WFTKT}" ]]; then _WFTKT=00000; fi; if [[ -z "${_ADTKT}" ]]; then _ADTKT=00000; fi; _SOURCE_PATH="${_PROJ_PATH}/Truist/${_PORTFOLIO}"; if [[ -d "${_SOURCE_PATH}" ]]; then _CWD=$(realpath $(pwd)); _TIMESTAMP=$(date +%Y%m%d_%H%M%S); _TARGET_PATH="${_PROJ_PATH}/DevOps/${_PORTFOLIO}"; _TAR_GZ_FILE_PATH="${_TARGET_PATH}/codefreeze/code_${_PORTFOLIO}_WF${_WFTKT}_AD${_ADTKT}_${_TIMESTAMP}_package.tar.gz"; _LOGFILE_PATH="${_TARGET_PATH}/${_LOGDIRNAME}/$(basename ${_TAR_GZ_FILE_PATH} | cut -d '.' -f1).log"; mkdir -p $(dirname ${_LOGFILE_PATH}); exec 3>&1 1>>${_LOGFILE_PATH} 2>&1; _HEADER="\n- [x] User: \`${USER}\`\n- [x] Timestamp: \`${_TIMESTAMP}\`  (YYYY-MM-DD HH:MM:SS)\n- [x] Logfile: \`${_LOGFILE_PATH}\`\n- [x] Portfolio Source Location: \`${_SOURCE_PATH}\`\n- [x] Archiving Portfolio Code: ${_PORTFOLIO}\n"; echo -e "\n${_SEP}\n\n# Process Log:\n${_HEADER}${_SEP}\n\n" | tee /dev/fd/3 && cd ${_SOURCE_PATH} && tar -cvzf ${_TAR_GZ_FILE_PATH} ./code; if [[ -f "${_TAR_GZ_FILE_PATH}" ]]; then echo -e "\n${_SEP}\n\n## [x] Portfolio: \`${_PORTFOLIO}\`\n${_HEADER}\n\n### [x] Ticket Details:\n\n- [x] WorkFront Ticket: \`${_WFTKT}\`\n- [x] Azure DevOps WorkItem: \`#${_ADTKT}\`\n\n### [x] Code Archive File:\n\n- [x] Path: \`${_TAR_GZ_FILE_PATH}\`\n  - [x] Location: \`$(dirname ${_TAR_GZ_FILE_PATH})\`\n  - [x] Location: \`$(basename ${_TAR_GZ_FILE_PATH})\`\n- [x] SHA256 Hash: \`$(genhash-sha256 ${_TAR_GZ_FILE_PATH})\`\n\n- [x] Status: $(if [[ $? == 0 ]]; then echo 'SUCCESS [x]'; else echo 'FAILURE [x]'; fi;)\n${_SEP}\n\n" | tee /dev/fd/3; unset _TAR_GZ_FILE_PATH; fi; cd ${_CWD}; fi; unset _WFTKT _AD_TKT _SOURCE_PATH _TARGET_PATH _LOGFILE_PATH _HEADER;) }

## Search for Passwords
# for f in $(ls .); do grep -nHi -E "password=\"(\&\S+\.)?\"" $f; done;
searchpass() { (_PATH=${1:-$(pwd)}; _HOW=$(echo ${2:-"--simple"} | xargs); _SEP=$(stringrep - 60); if [[ ${_HOW} == "-s" || ${_HOW} == "-simple" ]]; then _SEARCHWITH="(\S+)?"; else _SEARCHWITH="(\&\S+\.)?"; fi; _SEARCH_PATTERN="password=\"${_SEARCHWITH}\""; echo -e "\n${_SEP}\n\nPath: $(realpath ${_PATH})\nSearch Pattern: \"${_SEARCH_PATTERN}\"\n\n${_SEP}\n\n"; if [[ -d "${_PATH}" ]]; then _CWD="$(realpath $(pwd))"; cd ${_PATH}; for f in $(ls ${_PATH}); do if [[ -f "${f}" ]]; then grep -nH -E "${_SEARCH_PATTERN}" "${_PATH}/${f}"; fi; done; cd ${_CWD}; fi; unset f _PATH _HOW _CWD _SEARCHWITH _SEARCH_PATTERN _SEP;) }


## Setting up SSH
mkdir -p ~/.ssh
mkfile() { _FPATH=$1; if [[ -f "${_FPATH}" ]]; then touch ${_FPATH}; fi; unset _FPATH; }
mkfile ~/.ssh/known_hosts
mkfile ~/.ssh/authorized_keys
mkfile ~/.ssh/sshd_config
mkfile ~/.ssh_setup

```

## Multiline Functions

Here we expand some of the single line shellscript functions into multilines 
for enhanced readability and maintainability.

```sh

stringrep() { (
    #----------------
    # Example Usage:
    # stringrep - 30
    #----------------
    _char=$1; 
    _numrep=${2:-20}; 
    _PYTHON=${3:-$(which python3)}; 
    if [[ -z "${_numrep}" ]]; then _numrep=20; fi; 
    "${_PYTHON}" -c "print('${_char}'*${_numrep})"; 
    unset _char _numrep;
    )
}

createpkg() { (
    # read in portfolio name from the environment variable ${PROJ_PORTFOLIO}
    _PORTFOLIO=${PROJ_PORTFOLIO:-Auto}; 
    # workfront ticket number
    _WFTKT=${1:-00000}; 
    # azure-devops ticket (workitem) number
    _ADTKT=${2:-00000}; 
    # define the path of the project root
    _PROJ_PATH="/sasdata/crptrs1/pad"; 
    # define the name of the logfile directory
    _LOGDIRNAME="logs"; 
    # generate and save formatted-separator for log and console outputs
    _SEP=$(stringrep - 60); 
    # assign default values if empty value is passed
    if [[ -z "${_WFTKT}" ]]; then _WFTKT=00000; fi; 
    if [[ -z "${_ADTKT}" ]]; then _ADTKT=00000; fi; 
    # define source folder path of the portfolio
    _SOURCE_PATH="${_PROJ_PATH}/Truist/${_PORTFOLIO}"; 
    # process iff valid source path: ${_SOURCE_PATH}
    if [[ -d "${_SOURCE_PATH}" ]]; then 
        # capture current working directory (full path)
        _CWD=$(realpath $(pwd)); 
        # generate timestamp string to use in "*.tar.gz" filename
        _TIMESTAMP=$(date +%Y%m%d_%H%M%S); 
        # define target folder path of the portfolio
        _TARGET_PATH="${_PROJ_PATH}/DevOps/${_PORTFOLIO}";
        _TAR_GZ_FILE_PATH="${_TARGET_PATH}/codefreeze/code_${_PORTFOLIO}_WF${_WFTKT}_AD${_ADTKT}_${_TIMESTAMP}_package.tar.gz"; 
        _LOGFILE_PATH="${_TARGET_PATH}/${_LOGDIRNAME}/$(basename ${_TAR_GZ_FILE_PATH} | cut -d '.' -f1).log"; 
        mkdir -p $(dirname ${_LOGFILE_PATH}); 
        exec 3>&1 1>>${_LOGFILE_PATH} 2>&1; 
        # prepare message header
        _HEADER="";
        _HEADER="${_HEADER}\n- [x] User: \`${USER}\`";
        _HEADER="${_HEADER}\n- [x] Timestamp: \`${_TIMESTAMP}\`  (YYYY-MM-DD HH:MM:SS)";
        _HEADER="${_HEADER}\n- [x] Logfile: \`${_LOGFILE_PATH}\`";
        _HEADER="${_HEADER}\n- [x] Portfolio Source Location: \`${_SOURCE_PATH}\`";
        _HEADER="${_HEADER}\n- [x] Archiving Portfolio Code: ${_PORTFOLIO}\n"; 
        # prepare message preamble (formatted header)
        _PREAMBLE="\n${_SEP}\n\n# Process Log:\n${_HEADER}${_SEP}\n\n";
        # send preamble to both logfile and the console
        echo -e "${_PREAMBLE}" | tee /dev/fd/3 \
            # change directory to the ${_SOURCE_PATH}
            && cd ${_SOURCE_PATH} \
            # create "*.tar.gz" file from the "code" folder contents
            && tar -cvzf ${_TAR_GZ_FILE_PATH} ./code; 
        # conditionally prepare log message body iff the previous command was successful
        if [[ -f "${_TAR_GZ_FILE_PATH}" ]]; then 
            # prepare message body
            _BODY="";
            _BODY="${_BODY}\n### [x] Ticket Details:\n";
            _BODY="${_BODY}\n- [x] WorkFront Ticket: \`${_WFTKT}\`";
            _BODY="${_BODY}\n- [x] Azure DevOps WorkItem: \`#${_ADTKT}\`\n";
            _BODY="${_BODY}\n### [x] Code Archive File:\n\n- [x] Path: \`${_TAR_GZ_FILE_PATH}\`";
            _BODY="${_BODY}\n  - [x] Location: \`$(dirname ${_TAR_GZ_FILE_PATH})\`";
            _BODY="${_BODY}\n  - [x] Location: \`$(basename ${_TAR_GZ_FILE_PATH})\`";
            _BODY="${_BODY}\n- [x] SHA256 Hash: \`$(genhash-sha256 ${_TAR_GZ_FILE_PATH})\`\n";
            _BODY="${_BODY}\n- [x] Status: $(if [[ $? == 0 ]]; then echo 'SUCCESS [x]'; else echo 'FAILURE [x]'; fi;)";
            # prepare complete message
            _MESSAGE="\n${_SEP}\n\n## [x] Portfolio: \`${_PORTFOLIO}\`\n${_HEADER}\n${_BODY}\n${_SEP}\n\n";
            # send message to both logfile and the console
            echo -e "${_MESSAGE}" | tee /dev/fd/3; 
            unset _BODY _MESSAGE; 
        else:
            # send error message to both logfile and the console
            echo -e "ERROR:: Archive file failed to generate at path: \`${_TAR_GZ_FILE_PATH}\`\n" | tee /dev/fd/3;
        fi; 
        # change directory back to original working directory
        cd ${_CWD}; 
        unset _CWD _TIMESTAMP _TARGET_PATH _TAR_GZ_FILE_PATH _LOGFILE_PATH _HEADER _PREAMBLE;
    else:
        # send error message to both logfile and the console
        echo -e "ERROR:: Invalid Source Path: \`${_SOURCE_PATH}\`\n" | tee /dev/fd/3;
    fi; 
    unset _WFTKT _ADTKT _SOURCE_PATH _LOGDIRNAME _PORTFOLIO;
    ) 
}
```
