# Accessing GitHub Repository Releases from Commandline with GitHub CLI

## Primary Command

```sh
gh release --help
```

<details>
<summary><strong><font color="cyan">Sample output</font> [<font color="orange"><em>&nbsp; Click to expand &nbsp;</em></font>]</strong></summary>
<p>

```sh
$ gh release --help

Manage GitHub releases

USAGE
  gh release <command> [flags]

CORE COMMANDS
  create:     Create a new release
  delete:     Delete a release
  download:   Download release assets
  list:       List releases in a repository
  upload:     Upload assets to a release
  view:       View information about a release

FLAGS
  -R, --repo [HOST/]OWNER/REPO   Select another repository using the [HOST/]OWNER/REPO format

INHERITED FLAGS
  --help   Show help for command

LEARN MORE
  Use 'gh <command> <subcommand> --help' for more information about a command.
  Read the manual at https://cli.github.com/manual
```

</p>
</details></br>

## View a list of releases for a given repository

```sh
# -R, --repo              Select another repository using the [HOST/]OWNER/REPO format
gh release list -R https://github.com/facebook/watchman
```

<details>
<summary><strong><font color="cyan">Sample output</font> [<font color="orange"><em>&nbsp; Click to expand &nbsp;</em></font>]</strong></summary>
<p>

```sh
v2021.11.29.00  Latest  (v2021.11.29.00)  about 4 days ago
v2021.11.15.00          (v2021.11.15.00)  about 17 days ago
v2021.11.08.00          (v2021.11.08.00)  about 22 days ago
v2021.11.01.00          (v2021.11.01.00)  about 1 month ago
v2021.10.25.00          (v2021.10.25.00)  about 1 month ago
v2021.10.18.00          (v2021.10.18.00)  about 1 month ago
v2021.10.11.00          (v2021.10.11.00)  about 1 month ago
v2021.10.04.00          (v2021.10.04.00)  about 2 months ago
v2021.09.27.00          (v2021.09.27.00)  about 2 months ago
v2021.09.20.00          (v2021.09.20.00)  about 2 months ago
v2021.09.13.00          (v2021.09.13.00)  about 2 months ago
v2021.09.06.00          (v2021.09.06.00)  about 2 months ago
v2021.08.30.00          (v2021.08.30.00)  about 3 months ago
v2021.08.23.00          (v2021.08.23.00)  about 3 months ago
v2021.08.02.00          (v2021.08.02.00)  about 4 months ago
v2021.07.22.00          (v2021.07.22.00)  about 4 months ago
v2021.07.20.00          (v2021.07.20.00)  about 4 months ago
v2021.07.19.00          (v2021.07.19.00)  about 4 months ago
v2021.07.12.00          (v2021.07.12.00)  about 4 months ago
v2021.07.05.00          (v2021.07.05.00)  about 5 months ago
v2021.06.14.00          (v2021.06.14.00)  about 5 months ago
v2021.06.07.00          (v2021.06.07.00)  about 5 months ago
v2021.05.31.00          (v2021.05.31.00)  about 6 months ago
v2021.05.24.00          (v2021.05.24.00)  about 6 months ago
v2021.05.17.00          (v2021.05.17.00)  about 6 months ago
v2021.05.10.00          (v2021.05.10.00)  about 6 months ago
v2021.05.03.00          (v2021.05.03.00)  about 7 months ago
v2021.04.26.00          (v2021.04.26.00)  about 7 months ago
v2021.04.19.00          (v2021.04.19.00)  about 7 months ago
v2021.04.12.00          (v2021.04.12.00)  about 7 months ago
```

</p>
</details></br>

## View only the latest release for a given repository

```sh
# -R, --repo              Select another repository using the [HOST/]OWNER/REPO format
# -L, --limit int         Maximum number of items to fetch (default 30)
gh release list -L 1 -R https://github.com/facebook/watchman
```

<details>
<summary><strong><font color="cyan">Sample output</font> [<font color="orange"><em>&nbsp; Click to expand &nbsp;</em></font>]</strong></summary>
<p>

```sh
v2021.11.29.00  Latest  (v2021.11.29.00)  about 4 days ago
```

</p>
</details></br>

## Extract the tag of the latest release

```sh
# -R, --repo              Select another repository using the [HOST/]OWNER/REPO format
# -L, --limit int         Maximum number of items to fetch (default 30)
echo $(gh release list -L 1 -R https://github.com/facebook/watchman) | cut -d " " -f1
```

<details>
<summary><strong><font color="cyan">Sample output</font> [<font color="orange"><em>&nbsp; Click to expand &nbsp;</em></font>]</strong></summary>
<p>

```sh
v2021.11.29.00
```

</p>
</details></br>

## Open the release information in a browser

You can open a release with its tag directly in your browser using Github CLI.

```sh
# -R, --repo              Select another repository using the [HOST/]OWNER/REPO format
# -w, --web               Open the release in the browser
gh release view "v2021.11.29.00" -w -R https://github.com/facebook/watchman
```

The command above will open [this](https://github.com/facebook/watchman/releases/tag/v2021.11.29.00) release in the default browser.

<details>
<summary><strong><font color="cyan">Sample output</font> [<font color="orange"><em>&nbsp; Click to expand &nbsp;</em></font>]</strong></summary>
<p>

![figure](https://i.imgur.com/oyt0z1u.png)

</p>
</details></br>

https://github.com/facebook/watchman/releases/download/v2021.11.29.00/watchman-v2021.11.29.00-linux.zip

## Download the release archive

You can download the release archive either with GitHub CLI (repo: public/private) with its tag. Alternatively, you could also use `curl` or `wget` to download the release archive from commandline.

For instance, the following shows you the typical URL structure of a `.zip` archive associated with a release in the repository, `https://github.com/facebook/watchman`.

- `https://github.com/`<code><font color="orange">facebook</font></code>`/`<code><font color="cyan">watchman</font></code>`/releases/download/`<code><font color="red">v2021.11.29.00</font></code>`/`<code><font color="cyan">watchman</font></code>`-`<code><font color="red">v2021.11.29.00</font></code>`-linux.zip`

This can be parametrized as:

```sh
OWNER="facebook"
REPO="watchman"
TAG="v2021.11.29.00"
URL="https://github.com/${OWNER}/${REPO}/releases/download/${TAG}/${REPO}-${TAG}-linux.zip"
```
You can also dowload the whole archive using the common archive URL structure for any repository. This will point to the [archived source code (`zip` or `tar.gz`)](https://github.com/facebook/watchman/releases/tag/v2021.11.29.00) in a given release, specified by the `TAG`.

![figure](https://i.imgur.com/FRwGzqj.png)

- Specific example

    https://github.com/facebook/watchman/archive/refs/tags/v2021.11.29.00.zip

- Parametrized example

    ```jinja
    https://github.com/{{ OWNER }}/{{ REPO }}/archive/refs/tags/{{ TAG }}.zip
    ```

```sh
# -R, --repo              Select another repository using the [HOST/]OWNER/REPO format
# -A, --archive format    (format is zip or tar.gz)

## Method-1: whole archive
gh release download "v2021.11.29.00" \
    -R https://github.com/facebook/watchman \
    -p --archive=zip # or use --archive=tar.gz

## Method-2: specific file
OWNER="facebook"
REPO="watchman"
TAG="v2021.11.29.00"
gh release download "${TAG}" \
    -R "https://github.com/${OWNER}/${REPO}" \
    -p "${REPO}-${TAG}-linux.zip"
```

The command above will open [this](https://github.com/facebook/watchman/releases/tag/v2021.11.29.00) release in the default browser.

<details>
<summary><strong><font color="cyan">Sample output</font> [<font color="orange"><em>&nbsp; Click to expand &nbsp;</em></font>]</strong></summary>
<p>

![figure](https://i.imgur.com/oyt0z1u.png)

</p>
</details></br>