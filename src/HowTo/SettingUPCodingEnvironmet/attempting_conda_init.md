# How to access `conda` command from Powershell and CMD in Windows 10

When you install `conda`, it by default asks you to use anaconda/miniconda prompt. However, if you want to access conda from PowerShell/CMD, you need to do this:

## Step-1

Open anaconda/miniconda prompt and run:

```
where conda
```

This will give an output similar to the following.

```bash
## miniconda prompt
(base) C:\Users\raysu>where conda
C:\Users\raysu\Miniconda3\Library\bin\conda.bat
C:\Users\raysu\Miniconda3\Scripts\conda.exe          <<<---- You will need this
C:\Users\raysu\Miniconda3\condabin\conda.bat
```

## Step-2

Now you need to open Powershell and run "C:\Users\raysu\Miniconda3\Scripts\conda.exe init". 

- This should make conda available to you on Powershell and CMD. 
- Just make sure to close Powershell/CMD once and open again. 
- Test by running `conda env list`.

```bash
## Powershell
raysu@ALPHA  ~                                                                                               [21:32]
❯ C:\Users\raysu\Miniconda3\Scripts\conda.exe init
no change     C:\Users\raysu\Miniconda3\Scripts\conda.exe
no change     C:\Users\raysu\Miniconda3\Scripts\conda-env.exe
no change     C:\Users\raysu\Miniconda3\Scripts\conda-script.py
no change     C:\Users\raysu\Miniconda3\Scripts\conda-env-script.py
no change     C:\Users\raysu\Miniconda3\condabin\conda.bat
no change     C:\Users\raysu\Miniconda3\Library\bin\conda.bat
no change     C:\Users\raysu\Miniconda3\condabin\_conda_activate.bat
no change     C:\Users\raysu\Miniconda3\condabin\rename_tmp.bat
no change     C:\Users\raysu\Miniconda3\condabin\conda_auto_activate.bat
no change     C:\Users\raysu\Miniconda3\condabin\conda_hook.bat
no change     C:\Users\raysu\Miniconda3\Scripts\activate.bat
no change     C:\Users\raysu\Miniconda3\condabin\activate.bat
no change     C:\Users\raysu\Miniconda3\condabin\deactivate.bat
modified      C:\Users\raysu\Miniconda3\Scripts\activate
modified      C:\Users\raysu\Miniconda3\Scripts\deactivate
modified      C:\Users\raysu\Miniconda3\etc\profile.d\conda.sh
modified      C:\Users\raysu\Miniconda3\etc\fish\conf.d\conda.fish
no change     C:\Users\raysu\Miniconda3\shell\condabin\Conda.psm1
modified      C:\Users\raysu\Miniconda3\shell\condabin\conda-hook.ps1
no change     C:\Users\raysu\Miniconda3\Lib\site-packages\xontrib\conda.xsh
modified      C:\Users\raysu\Miniconda3\etc\profile.d\conda.csh
modified      C:\Users\raysu\Documents\WindowsPowerShell\profile.ps1
modified      HKEY_CURRENT_USER\Software\Microsoft\Command Processor\AutoRun

==> For changes to take effect, close and re-open your current shell. <==

raysu@ALPHA  ~                                                                                               [21:33]
❯
```


## Check

Run `conda env list`.

```bash
## Open a new Powershell or CMD (now it works!!)
C:\Users\raysu>conda env list
# conda environments:
#
base                  *  C:\Users\raysu\Miniconda3
fav_env                  C:\Users\raysu\Miniconda3\envs\fav_env
h2owave_env              C:\Users\raysu\Miniconda3\envs\h2owave_env
mlflow_env               C:\Users\raysu\Miniconda3\envs\mlflow_env
pytorch_env              C:\Users\raysu\Miniconda3\envs\pytorch_env
test_tfcpu_env           C:\Users\raysu\Miniconda3\envs\test_tfcpu_env
test_tfgpu_env           C:\Users\raysu\Miniconda3\envs\test_tfgpu_env
```

---

## References

1. ['Conda' is not recognized as internal or external command][#stackoverflow-q-44515769]

[#stackoverflow-q-44515769]: https://stackoverflow.com/questions/44515769/conda-is-not-recognized-as-internal-or-external-command
