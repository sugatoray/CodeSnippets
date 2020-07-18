# gitlike_contrib_chart.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Tuple

def gitlike_contribution_chart(df: pd.DataFrame,
                              figsize: Tuple[int] = (18, 10),
                              vmin = 0,
                              xticklabels: List = None,
                              yticklabels: List = None,
                              xticklabel_On: bool = True,
                              yticklabel_On: bool = True,
                              xticklabel_top: bool = True,
                              yticklabel_left: bool = True,
                              xticklabel_rotation: int = 0,
                              yticklabel_rotation: int = 0,
                              cmap = None,
                              heatmapdict: Dict = None,
                              show_figure: bool = True):
    """Creates a github/lab like contribution chart and returns (Figure, Axes).

    Example
    -------

    gitlike_contribution_chart(df: pd.DataFrame,
                              figsize: Tuple[int] = (18, 10),
                              vmin = 0,
                              xticklabels: List = None,
                              yticklabels: List = None,
                              xticklabel_On: bool = True,
                              yticklabel_On: bool = True,
                              xticklabel_top: bool = True,
                              yticklabel_left: bool = True,
                              xticklabel_rotation: int = 0,
                              yticklabel_rotation: int = 0,
                              cmap = None,
                              heatmapdict: Dict = None,
                              show_figure: bool = True)

    Short example:
    import numpy as np
    import pandas as pd

    contributions = np.random.randint(low=0, high=30, size=12*7*5).reshape(7,-1)

    MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    xticklabels = MONTHS.copy()
    yticklabels = DAYS.copy
    df = pd.DataFrame(contributions, index=DAYS)
    # Shortest
    fig, ax = gitlike_contribution_chart(df, show_figure=True)
    # Option-2
    fig, ax = gitlike_contribution_chart(df, show_figure = True,
                                             xticklabels = MONTHS,
                                             yticklabels = DAYS,
                                             cmap = "Greens")
    """
    # Choice of cmaps: Greens, Blues, BuPu, custom-cmap
    CUSTOM_MAP = {
        'multihue_5-level': [
            '#edf8fb', '#b2e2e2', '#66c2a4', '#2ca25f', '#006d2c'
        ],
        'Greens': 'Greens',
        'Blues': 'Blues',
        'BuPu': 'BuPu'
    }
    # Define Default Months (xticklabels)
    MONTHS = ['Jan', 'Feb', 'Mar',
              'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']
    # Define Default Days (yticklabels)
    DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    if cmap is None:
        # CUSTOM_MAP['multihue_5-level'], "Greens", "Blues", "BuPu"
        cmap = CUSTOM_MAP['multihue_5-level']

    _vmin = vmin
    if heatmapdict is None:
        heatmapdict = dict(
            linewidths = 5,
            linecolor = 'white',
            cbar = False,
            square = True,
            vmin = _vmin,
            xticklabels = 6, # select every 6th column-name
            yticklabels = 1, # select every row (index-value)
        )

    if xticklabels is None: xticklabels = MONTHS.copy()
    if yticklabels is None: yticklabels = DAYS.copy()

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)
    # Add heatmap
    sns.heatmap(df, **heatmapdict, cmap = cmap, ax = ax)
    # Set x and y-ticklabels
    if yticklabels is not None:
        ax.set_yticklabels(days)
    ax.set_xticklabels(xticklabels)
    ax.xaxis.set_tick_params(
        labelrotation = xticklabel_rotation, # 0
        labeltop = xticklabel_top, # True
        labelbottom = not xticklabel_top # False
    )
    ax.yaxis.set_tick_params(
        labelrotation = yticklabel_rotation, # 0
        labelleft = yticklabel_left # True
    )

    # Let the horizontal axes labeling appear on top.
    # ax.tick_params(top=True, bottom=False,
    #                labeltop=True, labelbottom=False)

    # Set xticklabel visibility
    ax.xaxis.set_visible(xticklabel_On) # True
    # Set yticklabel visibility
    ax.yaxis.set_visible(yticklabel_On) # True
    if show_figure: plt.show()

    return (fig, ax)
