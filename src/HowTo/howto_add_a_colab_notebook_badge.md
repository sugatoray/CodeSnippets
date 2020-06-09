# How to add a colab notebook badge

Google Collaboratory (colab) offers free jupyter notebooks hosted on cloud with CPU, GPU and TPU access. Any notebook on github can be opened in colab with a colab-badge link, such as this Colab [notebook][#colab-notebook]: 

[![Open In Colab][#colab-badge]][#colab-notebook]

[#colab-badge]: https://colab.research.google.com/assets/colab-badge.svg
[#colab-notebook]: https://colab.research.google.com/github/sugatoray/stackoverflow/blob/master/src/answers/Q_62273183/Q_62273183.ipynb

## Example: _with `markdown`_

Let us assume that the target notebook is located at:   
```
https://github.com/sugatoray/stackoverflow/blob/master/src/answers/Q_62273183/Q_62273183.ipynb
```
Then, replace `https://github.com` by `https://colab.research.google.com/github` to create the link to the colab-notebook. Here is an example. The following markdown will produce:  

[![Open In Colab][#colab-badge]][#colab-notebook]

```markdown
[![Open In Colab][#colab-badge]][#colab-notebook]

[#colab-badge]: https://colab.research.google.com/assets/colab-badge.svg
[#colab-notebook]: https://colab.research.google.com/github/sugatoray/stackoverflow/blob/master/src/answers/Q_62273183/Q_62273183.ipynb
```

## Example: _with `html`_

The rule to creating the link to colab-notebook is the same as before. The html code that produces the following badge (same as before) is in the following code-block. 
<a href="https://colab.research.google.com/github/sugatoray/stackoverflow/blob/master/src/answers/Q_62273183/Q_62273183.ipynb" target="_parent">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

```html
<a href="https://colab.research.google.com/github/sugatoray/stackoverflow/blob/master/src/answers/Q_62273183/Q_62273183.ipynb" target="_parent">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
```

## Suggestion

Needless to say, the `markdown` syntax is much cleaner as compared to the `html` syntax. But they both have their own places and use-cases.
