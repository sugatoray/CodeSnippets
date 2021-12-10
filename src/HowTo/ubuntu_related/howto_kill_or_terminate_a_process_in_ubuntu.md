# Terminating a process in Ubuntu

This is a summary of how you can kill a given process on a Ubuntu system.

1. Open **System Monitor** and close the intended process.
   
   - [x] Select the intended running process (you can also use the search functionality).
   - [x] Click <kbd>End Process</kbd>.

2. Kill the target process with:
 
   - [x] `kill <PID>` or `kill -9 <PID>`.
   
        - Here you need to provide the `<PID>` of the intended process.
   
   - [x] `pkill <ProcessName>`. 
   
       - Example: `pkill teamviewer`.   
       - In this case, 
         `pkill` does the pattern matching and then closes the relevant 
         `<PID>` of the given `<ProcessName>`.
   
   - [x] `killall <ProcessName>`. 
   
       - Example: `killall teamviewer`. 
       - In this case, `killall` does the pattern matching and then closes 
         all the instances of the `<ProcessName>`. :fire:

3. You can also search for the `<PID>` of a given `<ProcessName>` with:

   - [x] `ps aux | grep <ProcessName>`. 
   
       - Example: `ps aux | grep teamviewer`. 
       - The first number appearing after the left most user column is the `<PID>`.
       
   - [x] `pgrep <ProcessName>`. 
   
       - Example: `pgrep teamviewer`. 
       - In this case, `pgrep` does the pattern matching and returns the `<PID>` of the `<ProcessName>`.

## HelpDocs for `pkill`

```sh
$ pkill --help            

Usage:
 pkill [options] <pattern>

Options:
 -<sig>, --signal <sig>    signal to send (either number or name)
 -e, --echo                display what is killed
 -c, --count               count of matching processes
 -f, --full                use full process name to match
 -g, --pgroup <PGID,...>   match listed process group IDs
 -G, --group <GID,...>     match real group IDs
 -i, --ignore-case         match case insensitively
 -n, --newest              select most recently started
 -o, --oldest              select least recently started
 -P, --parent <PPID,...>   match only child processes of the given parent
 -s, --session <SID,...>   match session IDs
 -t, --terminal <tty,...>  match by controlling terminal
 -u, --euid <ID,...>       match by effective IDs
 -U, --uid <ID,...>        match by real IDs
 -x, --exact               match exactly with the command name
 -F, --pidfile <file>      read PIDs from file
 -L, --logpidfile          fail if PID file is not locked
 -r, --runstates <state>   match runstates [D,S,Z,...]
 --ns <PID>                match the processes that belong to the same
                           namespace as <pid>
 --nslist <ns,...>         list which namespaces will be considered for
                           the --ns option.
                           Available namespaces: ipc, mnt, net, pid, user, uts

 -h, --help     display this help and exit
 -V, --version  output version information and exit
```

## HelpDocs for `killall`

```sh
$ killall --help

Usage: killall [ -Z CONTEXT ] [ -u USER ] [ -y TIME ] [ -o TIME ] [ -eIgiqrvw ]
               [ -s SIGNAL | -SIGNAL ] NAME...
       killall -l, --list
       killall -V, --version

  -e,--exact          require exact match for very long names
  -I,--ignore-case    case insensitive process name match
  -g,--process-group  kill process group instead of process
  -y,--younger-than   kill processes younger than TIME
  -o,--older-than     kill processes older than TIME
  -i,--interactive    ask for confirmation before killing
  -l,--list           list all known signal names
  -q,--quiet          don't print complaints
  -r,--regexp         interpret NAME as an extended regular expression
  -s,--signal SIGNAL  send this signal instead of SIGTERM
  -u,--user USER      kill only process(es) running as USER
  -v,--verbose        report if the signal was successfully sent
  -V,--version        display version information
  -w,--wait           wait for processes to die
  -n,--ns PID         match processes that belong to the same namespaces
                      as PID
  -Z,--context REGEXP kill only process(es) having context
                      (must precede other arguments)
```

## HelpDocs for `pgrep`

```sh
$ pgrep --help  

Usage:
 pgrep [options] <pattern>

Options:
 -d, --delimiter <string>  specify output delimiter
 -l, --list-name           list PID and process name
 -a, --list-full           list PID and full command line
 -v, --inverse             negates the matching
 -w, --lightweight         list all TID
 -c, --count               count of matching processes
 -f, --full                use full process name to match
 -g, --pgroup <PGID,...>   match listed process group IDs
 -G, --group <GID,...>     match real group IDs
 -i, --ignore-case         match case insensitively
 -n, --newest              select most recently started
 -o, --oldest              select least recently started
 -P, --parent <PPID,...>   match only child processes of the given parent
 -s, --session <SID,...>   match session IDs
 -t, --terminal <tty,...>  match by controlling terminal
 -u, --euid <ID,...>       match by effective IDs
 -U, --uid <ID,...>        match by real IDs
 -x, --exact               match exactly with the command name
 -F, --pidfile <file>      read PIDs from file
 -L, --logpidfile          fail if PID file is not locked
 -r, --runstates <state>   match runstates [D,S,Z,...]
 --ns <PID>                match the processes that belong to the same
                           namespace as <pid>
 --nslist <ns,...>         list which namespaces will be considered for
                           the --ns option.
                           Available namespaces: ipc, mnt, net, pid, user, uts

 -h, --help     display this help and exit
 -V, --version  output version information and exit
```

## References

- Article: [_How to Kill a Desktop Application or Background Process on Linux_][#article]

  [#article]: https://www.howtogeek.com/211153/how-to-kill-a-desktop-application-or-background-process-on-linux/

  <details>
  <summary>Screenshot of the Article: Click to Expand</summary>
  <p>
  ![article-image][#howto-kill-process-on-ubuntu-article-image]  
  </p>
  </details>

  [#howto-kill-process-on-ubuntu-article-image]: resources/howto-kill-process-on-ubuntu-article-image.png
