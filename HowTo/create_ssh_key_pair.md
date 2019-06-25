# Creating SSH public-private key-pair

You can create an rsa key-pair with the following single line command. Run it in PuTTy, Git Bash, CygWin, etc.
```console
ssh-keygen -f ~/.ssh/id_rsa_<file-name> -t rsa -b 4096 -C "your.email.id@your_email.com"
```

And follow the instructions: 

1. Resource: https://techsupportallbugs.wordpress.com/2018/06/05/using-git-with-colab-via-ssh/
1. Resource: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
1. Resource: https://stackoverflow.com/questions/2505096/cloning-a-private-github-repo
1. Resource: https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account
1. Resource: https://help.github.com/en/articles/checking-for-existing-ssh-keys
