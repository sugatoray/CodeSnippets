# Git Commands

## `git pull`

```sh
git pull --help

```

## `git rebase`

```sh
git rebase --help

```

## `git merge`

```sh
git merge --help

```

## `git stash`

```
$ git stash --help
GIT-STASH(1)                                                                    Git Manual                                                                   GIT-STASH(1)

NAME
       git-stash - Stash the changes in a dirty working directory away

SYNOPSIS
       git stash list [<log-options>]
       git stash show [-u|--include-untracked|--only-untracked] [<diff-options>] [<stash>]
       git stash drop [-q|--quiet] [<stash>]
       git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
       git stash branch <branchname> [<stash>]
       git stash [push [-p|--patch] [-S|--staged] [-k|--[no-]keep-index] [-q|--quiet]
                    [-u|--include-untracked] [-a|--all] [-m|--message <message>]
                    [--pathspec-from-file=<file> [--pathspec-file-nul]]
                    [--] [<pathspec>...]]
       git stash clear
       git stash create [<message>]
       git stash store [-m|--message <message>] [-q|--quiet] <commit>

DESCRIPTION
       Use git stash when you want to record the current state of the working directory and the index, but want to go back to a clean working directory. The command
       saves your local modifications away and reverts the working directory to match the HEAD commit.

       The modifications stashed away by this command can be listed with git stash list, inspected with git stash show, and restored (potentially on top of a different
       commit) with git stash apply. Calling git stash without any arguments is equivalent to git stash push. A stash is by default listed as "WIP on branchname ...",
       but you can give a more descriptive message on the command line when you create one.

       The latest stash you created is stored in refs/stash; older stashes are found in the reflog of this reference and can be named using the usual reflog syntax (e.g.
       stash@{0} is the most recently created stash, stash@{1} is the one before it, stash@{2.hours.ago} is also possible). Stashes may also be referenced by specifying
       just the stash index (e.g. the integer n is equivalent to stash@{n}).

COMMANDS
       push [-p|--patch] [-S|--staged] [-k|--[no-]keep-index] [-u|--include-untracked] [-a|--all] [-q|--quiet] [-m|--message <message>] [--pathspec-from-file=<file>
       [--pathspec-file-nul]] [--] [<pathspec>...]
           Save your local modifications to a new stash entry and roll them back to HEAD (in the working tree and in the index). The <message> part is optional and gives
           the description along with the stashed state.

           For quickly making a snapshot, you can omit "push". In this mode, non-option arguments are not allowed to prevent a misspelled subcommand from making an
           unwanted stash entry. The two exceptions to this are stash -p which acts as alias for stash push -p and pathspec elements, which are allowed after a double
           hyphen -- for disambiguation.

       save [-p|--patch] [-S|--staged] [-k|--[no-]keep-index] [-u|--include-untracked] [-a|--all] [-q|--quiet] [<message>]
           This option is deprecated in favour of git stash push. It differs from "stash push" in that it cannot take pathspec. Instead, all non-option arguments are
           concatenated to form the stash message.

       list [<log-options>]
           List the stash entries that you currently have. Each stash entry is listed with its name (e.g.  stash@{0} is the latest entry, stash@{1} is the one before,
           etc.), the name of the branch that was current when the entry was made, and a short description of the commit the entry was based on.

               stash@{0}: WIP on submit: 6ebd0e2... Update git-stash documentation
               stash@{1}: On master: 9cc0589... Add git-stash

           The command takes options applicable to the git log command to control what is shown and how. See git-log(1).

       show [-u|--include-untracked|--only-untracked] [<diff-options>] [<stash>]
           Show the changes recorded in the stash entry as a diff between the stashed contents and the commit back when the stash entry was first created.
```

1. `git stash`: Adds currently staged changes to a new stash
2. `git stash --staged -m "message"`: Adds a stash with the staged changes and a custom message
3. `git stash list | lolcat`: Shows all stashes as a list
4. `git stash clear`: Clear all stashes
5. `git stash apply 1`: This will apply the stash with number `1` (you check this with `git stash list | lolcat`)

## Notes

While running `git pull --force`, I was shown the following. The fact is, 
I tried use `git rebase` on the repository and I have no clue what the 
hell I did! It was messed up. Luckily, I had backed up the changes 
already and was able to handle the situation.

```sh
git pull --force
fatal: It seems that there is already a rebase-merge directory, and
I wonder if you are in the middle of another rebase.  If that is the
case, please try
        git rebase (--continue | --abort | --skip)
If that is not the case, please
        rm -fr ".git/rebase-merge"
and run me again.  I am stopping in case you still have something
valuable there.
```

After I saw this, I ran `git rebase --abort` and that fixed some of the things.
VS Code was earlier showing. But this was not enough. 

See this: [What does git pull --rebase origin master means?][#so_git-pull-rebase]

[#so_git-pull-rebase]: https://stackoverflow.com/questions/34059893/what-does-git-pull-rebase-origin-master-means

I kept getting errors while trying to pull from the remote. 

```sh
CONFLICT (content): Merge conflict in .gitignore
error: could not apply ac8c2e6... update gitignore
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
```

So, after I ran the following to fix it:
- `git add .github/workflows/checks.yml`: Added the file with unchecked changes to staging.
- `git stash --staged -m "save workflow changes"`: This added the staged content to a stash (and removed the changed file content from the branch). 
- `git rebase --continue`: This rebased the branch with its remote.
- Note that alternatively I could have done the following as well:
  - `git pull --rebase origin master`: This will pull from the remote (`origin`) repository's `master` branch and **`rebase`** the current branch with the contents of the remote master branch. 

I am not sure which commands I used in which order! Let's write down most of them from bash-history. I will recreate the scenario later and try them out to realize what I needed to do.

1. `git pull origin add_chalk_utils --rebase`
2. `git rebase --continue`
3. `git fetch --all`
4. `git pull origin update_package-setup --force`
5. `git log -3 | lolcat`


## How to `git pull` from remote branch and overwrite local branch?

[](https://koukia.ca/how-do-i-git-pull-and-overwrite-my-local-changes-4b6e3a8de955)
