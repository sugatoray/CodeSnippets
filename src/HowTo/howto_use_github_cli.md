# Quick intro on github cli

## Creating repository from CLI

```sh
$ gh repo create learn_kivy --license MIT --private -d "Learn making apps with Kivy."
? Would you like to add a .gitignore? Yes
? Choose a .gitignore template Python
? This will add an "origin" git remote to your local repository. Continue? No
Discarding...
```

<details>
<summary>
<strong>Help</strong>
</summary>
<p>

```sh
$ gh repo create --help

Create a new GitHub repository.

When the current directory is a local git repository, the new repository will be added
as the "origin" git remote. Otherwise, the command will prompt to clone the new
repository into a sub-directory.

To create a repository non-interactively, supply the following:
- the name argument;
- the `--confirm` flag;
- one of `--public`, `--private`, or `--internal`.

To toggle off `--enable-issues` or `--enable-wiki`, which are enabled
by default, use the `--enable-issues=false` syntax.


USAGE
  gh repo create [<name>] [flags]

FLAGS
  -y, --confirm               Skip the confirmation prompt
  -d, --description string    Description of the repository
      --enable-issues         Enable issues in the new repository (default true)
      --enable-wiki           Enable wiki in the new repository (default true)
  -g, --gitignore string      Specify a gitignore template for the repository
  -h, --homepage URL          Repository home page URL
      --internal              Make the new repository internal
  -l, --license string        Specify an Open Source License for the repository
      --private               Make the new repository private
      --public                Make the new repository public
  -t, --team name             The name of the organization team to be granted access
  -p, --template repository   Make the new repository based on a template repository

INHERITED FLAGS
  --help   Show help for command

ARGUMENTS
  A repository can be supplied as an argument in any of the following formats:
  - "OWNER/REPO"
  - by URL, e.g. "https://github.com/OWNER/REPO"

EXAMPLES
  # create a repository under your account using the current directory name
  $ git init my-project
  $ cd my-project
  $ gh repo create
  
  # create a repository with a specific name
  $ gh repo create my-project
  
  # create a repository in an organization
  $ gh repo create cli/my-project
  
  # disable issues and wiki
  $ gh repo create --enable-issues=false --enable-wiki=false

LEARN MORE
  Use 'gh <command> <subcommand> --help' for more information about a command.
  Read the manual at https://cli.github.com/manual

```
  
</p>
</details>
