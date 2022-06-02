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
VS Code was earlier showing 

[#so_git-pull-rebase]: https://stackoverflow.com/questions/34059893/what-does-git-pull-rebase-origin-master-means


```sh
CONFLICT (content): Merge conflict in .gitignore
error: could not apply ac8c2e6... update gitignore
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
```
