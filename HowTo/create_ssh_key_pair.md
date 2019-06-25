# How to create SSH public-private key-pair

This document will lay out the steps you need to take to create an SSH key-pair.

## Check for existing SSH keys

Use this command to list all existing ssh keys: `ls -al ~/.ssh`
Follow this article for more details: https://help.github.com/en/articles/checking-for-existing-ssh-keys


## Create SSH public-private key-pair

You can create an rsa key-pair with the following single line command. Run it in PuTTy, Git Bash, CygWin, etc.
```console
ssh-keygen -f ~/.ssh/id_rsa_<file-name> -t rsa -b 4096 -C "your.email.id@your_email.com"
```
For example, if your email is `john.doe@gmail.com` and you want to create SSH key-pairs with rsa algorithm with key-size of `4096`, and you would like to name your ssh key-pairs `id_rsa_colab`, you could do that by running the following command from [Git Bash](https://gitforwindows.org/) and when prompted for a `passphrase`, just press <font color='red'>`enter`</font> to proceed without a passphrase. 

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
