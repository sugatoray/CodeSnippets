# Installing Plotly on Google Colab

Plotly comes installed on Google Colab VM by default. However, if you are trying to save the figures as images, 
you will run into error saying amother library called `plotly-orca` is not available and must be installed for 
saving figures as static images. 

Relevant Links:  

1. [Orca executable in Colab not recognized #290](https://github.com/plotly/orca/issues/290)
1. [Plotly/orca @github](https://github.com/plotly/orca)
1. [Saving or downloading plotly iplot images on Google Colaboratory][#stachoverflow]


[#stachoverflow]: https://stackoverflow.com/questions/57262385/saving-or-downloading-plotly-iplot-images-on-google-colaboratory/57272111#57272111

## What I did finally

Installed plotly-orca on Colab by following [this stackoverflow][#stachoverflow] link.

- Note: if you see a code block has a bang (exclamation) sign **`!`**, know that it means 
        that the code block is written to run froma Jupyter Notebook code-cell. If you want 
        to run it from outside the notebook, just drop the bang sign and run it from a terminal.

### Option-1

Keep the plotly version unchanged on colab. This will not require any environment-restart.

```python
import plotly
!pip install plotly==$plotly.__version__ # 4.4.1
!wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca
!chmod +x /usr/local/bin/orca
!apt-get install xvfb libgtk2.0-0 libgconf-2-4
```

### Option-2

Update the plotly version on Colab to the latest available version. Restart the environment for the installation to take effect.

```python
# update plotly and restart VM environment
!pip install -U plotly
```

After VM restarts...

```python
import plotly
print('plotly version: {}'.format(plotly.__version__))
print("=============================================")
!pip install plotly==$plotly.__version__ # 4.7.1
!wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca
!chmod +x /usr/local/bin/orca
!apt-get install xvfb libgtk2.0-0 libgconf-2-4
```

This should install plotly completely on Colab.

## How to save a figure as image using plotly?

Refer to the documents: 

+ [Static Image Export][#static-image-import]
+ [Interactive Html Export][#interactive-html-export]

[#static-image-import]: https://plotly.com/python/static-image-export/
[#interactive-html-export]: https://plotly.com/python/interactive-html-export/

```python
# Make figure
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displaying Itself", 
    layout_xaxis_title = 'x-label', 
    layout_yaxis = {'title': 'y-label', 
                        'visible': False, 
                        'showticklabels': False}
)
fig.show()

# Save figure
fig.write_html('plotly_figure.html') # html
fig.write_image('plotly_figure.png') # png
fig.write_image('plotly_figure.svg') # svg
```

## Some Good Resources

1. https://plotly.com/python/creating-and-updating-figures/
1. https://plotly.com/python/creating-and-updating-figures/#adding-traces
1. https://plotly.com/python/renderers/
1. [how to hide plotly yaxis title (in python)? -- **BEST**][#stackoverflow-plotly-hide-yaxis] :star: :star: :star: :star: :star:

[#stackoverflow-plotly-hide-yaxis]: https://stackoverflow.com/questions/61693014/how-to-hide-plotly-yaxis-title-in-python/61693190#61693190
