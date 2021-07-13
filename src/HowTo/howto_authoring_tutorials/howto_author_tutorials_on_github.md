# How to author tutorials on GitHub

If you are authoring tutorials on GiHub, chances are your tutorials have both code and text. 
Most often the common route for such tutorials is jupyter notebooks. Jupyter notebooks
are great in terms of presentation of both **code** and **text**, where text (as markdown) 
could include:

- media (images/videos)
- links
- LaTeX equations
- code blocks

However, they are a not at all a good fit for version controling. 
What if you could save your notebooks as `.py` or `.md` based on whether they contain more
code or more text? This is the requirement that is solved by `jupytext`.

The following is an [article][#lightning-borovec-article] by PyTorch Lightning's @borovec on how they are solving this 
problem using the following techstack:

- [JupyText](https://jupytext.readthedocs.io/en/latest/): convert the script to a notebook
- [pytest-nbval](https://github.com/computationalmodelling/nbval): testing the created notebook
- [papermill](https://papermill.readthedocs.io/en/latest/): executing notebooks in a command line
- [nbsphinx](https://nbsphinx.readthedocs.io/en/latest/): plugin for rendering ipynb file

|[![image](https://user-images.githubusercontent.com/10201242/125384649-dda5e580-e35e-11eb-87cd-9b017cb07076.png)][#lightning-borovec-article]|
|:---:|
| Image by Author [source][#lightning-borovec-article] |

[#lightning-borovec-article]: https://devblog.pytorchlightning.ai/publishing-lightning-tutorials-cbea3eaa4b2c
