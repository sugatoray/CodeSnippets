# How to use `tree` command

[Source][#howto-tree-command]

[#howto-tree-command]: https://www.tecmint.com/linux-tree-command-examples/#:~:text=The%20tree%20is%20a%20tiny,of%20sub%2Ddirectories%20and%20files.

## Install `tree` command.

```bash
# yum install tree	 #RHEL/CentOS 7
# dnf install tree	 #Fedora 22+ and /RHEL/CentOS 8
$ sudo apt install tree	 #Ubuntu/Debian
# sudo zypper in tree 	 #openSUSE
```

My personal preference is `sudo apt install tree`, as I am using a Ubuntu system.

## Run `tree` command

Say you have a folder at current level: `./outputdir`. The `tree` command can show all the contents (recursively) inside the target folder.

1. Example of `tree -a`

    ```bash
    tree ./outputdir -a
    ```

    **Sample output**:  

    ```bash
    outputdir
    ├── audio
    │   ├── ear-state-06012020035108.mp3
    │   ├── tw-uk-06012020113435.mp3
    │   ├── us-pompeo-06012020072305.mp3
    │   └── wang-06012020103828.mp3
    └── headlines
        ├── ear-state-06012020035108.txt
        ├── hk-chan-06012020073718.txt
        ├── hk-innocent-06012020114634.txt
        ├── tw-uk-06012020113435.txt
        ├── us-pompeo-06012020072305.txt
        ├── us-wang-06012020135251.txt
        └── wang-06012020103828.txt

    2 directories, 11 files
    ```

1. Example of `tree -a -h -pug`

   + The flag `-h` is used for showing file/folder size. 
     Use the `-h` flag and specify a size letter for 
      - kilobytes (`K`) 
      - Megabytes (`M`) 
      - Gigabytes (`G`) 
      - Terabytes (`T`)
      
   + The combined flag `-pug` is made of three flags: 
      - `-p` (file type and permissions) 
      - `-u` (user-name) 
      - `-g` (group-name).

    ```bash
    tree ./outputdir -a -h -pug
    ```

    **Sample output**:  

    ```bash
    outputdir
    ├── [drwxr-xr-x root     root     4.0K]  audio
    │   ├── [-rw-r--r-- root     root     1.1M]  ear-state-06012020035108.mp3
    │   ├── [-rw-r--r-- root     root     1.5M]  tw-uk-06012020113435.mp3
    │   ├── [-rw-r--r-- root     root     1.2M]  us-pompeo-06012020072305.mp3
    │   └── [-rw-r--r-- root     root     1.5M]  wang-06012020103828.mp3
    └── [drwxr-xr-x root     root     4.0K]  headlines
        ├── [-rw-r--r-- root     root     1.6K]  ear-state-06012020035108.txt
        ├── [-rw-r--r-- root     root      934]  hk-chan-06012020073718.txt
        ├── [-rw-r--r-- root     root      727]  hk-innocent-06012020114634.txt
        ├── [-rw-r--r-- root     root     3.3K]  tw-uk-06012020113435.txt
        ├── [-rw-r--r-- root     root     2.6K]  us-pompeo-06012020072305.txt
        ├── [-rw-r--r-- root     root     7.1K]  us-wang-06012020135251.txt
        └── [-rw-r--r-- root     root     2.9K]  wang-06012020103828.txt

    2 directories, 11 files
    ```
    
1. Example of ...
