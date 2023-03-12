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

## Create Directory Structure
# Example:
# -run "prepdirs ABC" from location "/sasdata/crptrs1/pad/DevOps" to create the folder structure for ABC portfolio
prepdirs() { (_PORTFOLIO_NAME=$1; _FOLDERS=${2:-"code codefreeze extractor logs codefreeze/archive"}; _CWD=$(realpath $(pwd)); if [[ ! -z "${_PORTFOLIO_NAME}" ]]; then mkdir -p ${_PORTFOLIO_NAME} && cd ${_PORTFOLIO_NAME} && mkdir -p ${_FOLDERS} && cd ${_CWD}; fi; unset _PORTFOLIO_NAME _CWD _FOLDERS;) }

## Search for Passwords
# for f in $(ls .); do grep -nHi -E "password=\"(\&\S+\.)?\"" $f; done;
searchpass() { (_PATH=${1:-$(pwd)}; _HOW=$(echo ${2:-"--simple"} | xargs); _SEP=$(stringrep - 60); if [[ ${_HOW} == "-s" || ${_HOW} == "-simple" ]]; then _SEARCHWITH="(\S+)?"; else _SEARCHWITH="(\&\S+\.)?"; fi; _SEARCH_PATTERN="password=\"${_SEARCHWITH}\""; echo -e "\n${_SEP}\n\nPath: $(realpath ${_PATH})\nSearch Pattern: \"${_SEARCH_PATTERN}\"\n\n${_SEP}\n\n"; if [[ -d "${_PATH}" ]]; then _CWD="$(realpath $(pwd))"; cd ${_PATH}; for f in $(ls ${_PATH}); do if [[ -f "${f}" ]]; then grep -nH -E "${_SEARCH_PATTERN}" "${_PATH}/${f}"; fi; done; cd ${_CWD}; fi; unset f _PATH _HOW _CWD _SEARCHWITH _SEARCH_PATTERN _SEP;) }

## YYYYMM Related
# Example:
# command: `pystr 202306 2:` | output: `2306`
pystr() { (_PYTHON=$(which python3); ${_PYTHON} -c "print(str(${1})[${2:-:}])";) }
## Func: extract `YYYYMM` part from a string with the format `##:YYYYMM`
# Example:
# commdand `getPartYYYYMM 33:202309` | output: `202309`
getPartYYYYMM() { (echo ${1:-$(date +%d:%Y%m)} | cut -d ":" -f2) }
## Func: generate a list of YYYYMM values with a start and stop specification
# Example:
# command: `genYYYMM 202101 202305` | output: `echo -e "1:202101\n2:202102\n...\n29:202305"`
genYYYYMM() { (_START=${1:-202101}; _STOP=${2:-$(expr $(date +%d:%Y%m) - 2)}; _NOINDEX=${3:-true}; _START_YYYY=$(pystr ${_START} :4); _STOP_YYYY=$(pystr ${_STOP} :4); _START_MM=$(pystr ${_START} -2:); _STOP_MM=$(pystr ${_STOP} -2:); idx=0; for YYYY in $(seq ${_START_YYYY} ${_STOP_YYYY}); do for MM in {01..12}; do idx=$(expr $idx + 1); YYYYMM=${YYYY}${MM}; if [[ ${_START} -le ${YYYYMM} && ${_STOP} -ge ${YYYYMM} ]]; then if [[ "${_NOINDEX}" == "true" ]]; then _PKG="${YYYYMM}"; else _PKG="${idx}:${YYYYMM}"; fi; echo -e "${_PKG}"; fi; done; done; unset _START _START_YYYY _START_MM _STOP _STOP_YYYY _STOP_MM YYYY MM YYYYMM _PKG;) }

## Func: generate SQL for tables with UNION ALL
# Example:
# command: `genSQLUnionAllTables 202101 202105 out some_table_name`
# output:
# select * from (
#         select &COL_NAMES. from outputs.pad_lns_auto_202101
#         ${_UNION_TYPE}
#         select &COL_NAMES. from outputs.pad_lns_auto_202102
#         ${_UNION_TYPE}
#         select &COL_NAMES. from outputs.pad_lns_auto_202103
#         ${_UNION_TYPE}
#         select &COL_NAMES. from outputs.pad_lns_auto_202104
#         ${_UNION_TYPE}
#         select &COL_NAMES. from outputs.pad_lns_auto_202105
# )
genSQLUnionAllTables() { (_START=${1:-202101}; _STOP=${2:-$(expr $(date +%d:%Y%m) - 2)}; _LIBREF=${3:-outputs}; _TABLE_PREFIX=${4:-pad_lns_auto}; _UNION_TYPE=${5:-"UNION ALL"}; idx=0; _SQL=""; for YYYYMM in $(genYYYYMM ${_START} ${_STOP}); do idx=$(expr $idx + 1); _SQL="${_SQL}$(if [[ $idx == 1 ]]; then echo ''; else echo '\n\t${_UNION_TYPE}'; fi;)\n\tselect &COL_NAMES. from ${_LIBREF}.${_TABLE_PREFIX}_${YYYYMM}"; done; echo -e "select * from (${_SQL}\n)"; unset _START _STOP _LIBREF _TABLE_PREFIX _UNION_TYPE YYYYMM idx _SQL;) }

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
        # define archive filename: *.tar.gz
        _TAR_GZ_FILE_PATH="${_TARGET_PATH}/codefreeze/code_${_PORTFOLIO}_WF${_WFTKT}_AD${_ADTKT}_${_TIMESTAMP}_package.tar.gz";
        # define logfile path (generated from the archive file's name)
        _LOGFILE_PATH="${_TARGET_PATH}/${_LOGDIRNAME}/$(basename ${_TAR_GZ_FILE_PATH} | cut -d '.' -f1).log";
        # create logfile directory if it does not exist already
        mkdir -p $(dirname ${_LOGFILE_PATH});
        # set the output to route to both logfile and the console
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
        # conditionally prepare log summary body iff the previous command was successful
        if [[ -f "${_TAR_GZ_FILE_PATH}" ]]; then
            # prepare summary body
            _BODY="";
            _BODY="${_BODY}\n### [x] Ticket Details:\n";
            _BODY="${_BODY}\n- [x] WorkFront Ticket: \`${_WFTKT}\`";
            _BODY="${_BODY}\n- [x] Azure DevOps WorkItem: \`#${_ADTKT}\`\n";
            _BODY="${_BODY}\n### [x] Code Archive File:\n\n- [x] Path: \`${_TAR_GZ_FILE_PATH}\`";
            _BODY="${_BODY}\n  - [x] Location: \`$(dirname ${_TAR_GZ_FILE_PATH})\`";
            _BODY="${_BODY}\n  - [x] Location: \`$(basename ${_TAR_GZ_FILE_PATH})\`";
            _BODY="${_BODY}\n- [x] SHA256 Hash: \`$(genhash-sha256 ${_TAR_GZ_FILE_PATH})\`\n";
            _BODY="${_BODY}\n- [x] Status: $(if [[ $? -eq 0 ]]; then echo 'SUCCESS [x]'; else echo 'FAILURE [x]'; fi;)";
            # prepare complete summary
            _SUMMARY="\n${_SEP}\n\n## [x] Portfolio: \`${_PORTFOLIO}\`\n${_HEADER}\n${_BODY}\n${_SEP}\n\n";
            # send summary to both logfile and the console
            echo -e "${_SUMMARY}" | tee /dev/fd/3;
            unset _BODY _SUMMARY;
        else:
            # send error message to both logfile and the console
            echo -e "ERROR:: Archive file failed to generate at path: \`${_TAR_GZ_FILE_PATH}\`\n" | tee /dev/fd/3;
        fi;
        # change directory back to original working directory
        cd ${_CWD};
        unset \
            _CWD \
            _TIMESTAMP \
            _TARGET_PATH \
            _TAR_GZ_FILE_PATH \
            _LOGFILE_PATH \
            _HEADER _PREAMBLE;
    else:
        # send error message to both logfile and the console
        echo -e "ERROR:: Invalid Source Path: \`${_SOURCE_PATH}\`\n" | tee /dev/fd/3;
    fi;
    unset \
        _WFTKT \
        _ADTKT \
        _SOURCE_PATH \
        _LOGDIRNAME \
        _PORTFOLIO;
    )
}
```
