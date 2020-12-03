# How to enable SSH authentication between Colab and GitHub for private repositories.
This document will lay out the steps you need to take to create an SSH key-pair, followed by the steps necessary to establish the SSH authentication between Colab and GitHub for private repositories.

## A note to the reader
I started putting together this document with the intent to enable SSH based authentication between Colab and GitHub for private repositories. The steps involved are:  
1. Check for existing SSH keys. `DONE`
1. Create SSH public-private key-pair. `DONE`
1. Create a `.config` file in directory with only the key-pair files in it and gzip it. `TESTED` 
   => But have not written down the exact process here. `PENDING`
1. Upload the gzipped file to Colab. `TESTED`
1. Run script to set colab environment with the public-private key-pair. `PENDING`
1. Save the `public-key` in GitHub. `PENDING`
1. Test if it worked. `PENDING`

Note: 
+ I mostly followed [this document](https://techsupportallbugs.wordpress.com/2018/06/05/using-git-with-colab-via-ssh/) to implement these steps. There is also a [similar article available on Medium.com](https://towardsdatascience.com/using-git-with-colab-via-ssh-175e8f3751ec) by the same author. 
+ At this point I am not sure if this is a once-only activity or you need to run it everytime you fire up a new Colab VM. I plan on testing and documenting it. My ultimate goal with this document is to make Colab-GitHub SSH integeration as simple as possible. Worst-case-scenario: I would run a colab-script every time I open up a Colab VM and access my SSH key-pair from a predefined location on my Google Drive (and avoid uploading the SSH key-pair every time).

## Check for existing SSH keys

Use this command to list all existing SSH keys: `ls -al ~/.ssh`
Follow this article for more details: https://help.github.com/en/articles/checking-for-existing-ssh-keys


## Create SSH public-private key-pair

+ **Step-1**  
You can create an rsa key-pair with the following single line command. Run it in PuTTy, Git Bash, CygWin, etc.
```console
ssh-keygen -f ~/.ssh/id_rsa_<file-name> -t rsa -b 4096 -C "your.email.id@your_email.com"
```
+ **Step-2**  
You will be prompted for a `passphrase`. Just press **`enter`** to proceed without a passphrase.
---
For example, if your email is `john.doe@gmail.com` and you want to create SSH key-pairs using `rsa` algorithm with key-size of `4096`, and you would like to name your SSH key-pairs `id_rsa_colab`, you could do that by running the following command from [Git Bash](https://gitforwindows.org/) and when prompted for a `passphrase`, just press **`enter`** to proceed without a passphrase. 

```console
ssh-keygen -f ~/.ssh/id_rsa_colab -t rsa -b 4096 -C "john.doe@gmail.com"
```
The letters `-f`, `-t`, `-b`, `-C` are called switches and are used to let the user specify details about key-pair filename, ssh algorithm, key-size, user email respectively.

| Switch | Use | Example |
|:---:|:---|:---:|
| -f | Specify filename to store generated key-pair. <br> Usually, the keys are named as follows: <li> private-key: `id_rsa_colab` </li>  <li> public-key: `id_rsa_colab.pub` </li> | `-f ~/.ssh/id_rsa_colab` |
| -t | Specify the type of algorithm to use. See all available types [here](https://www.ssh.com/ssh/keygen). | `-t rsa` |
| -b | Specify the key-size of the algorithm. For instance, here we are <br> using `rsa` algorithm with a key-size of `4096`. <br> The larger the key size the better. | `-b 4096` |
| -C | Specify user email | `-C john.doe@gmail.com` |

### Additional Resources
+ To know more about the types of algorithms and available options for key-size while creating an SSH key-pair, refer to [this document](https://www.ssh.com/ssh/keygen/).
+ You may download Git Bash from here: https://gitforwindows.org/
# References: 

1. Resource: https://techsupportallbugs.wordpress.com/2018/06/05/using-git-with-colab-via-ssh/
1. Resource: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
1. Resource: https://stackoverflow.com/questions/2505096/cloning-a-private-github-repo
1. Resource: https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account
1. Resource: https://help.github.com/en/articles/checking-for-existing-ssh-keys
1. Resource: https://towardsdatascience.com/using-git-with-colab-via-ssh-175e8f3751ec
1. Resource: https://www.ssh.com/ssh/keygen/
