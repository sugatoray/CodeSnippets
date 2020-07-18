import numpy as np
import numpy.ma as ma
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.patches as mpatches
# This imports are made following the standard scipy conventions, as mentioned 
# on MatplotLib Contribution Guideline: 
#     https://matplotlib.org/3.1.1/devel/contributing.html


def fancy_format_axis_labels(ax = None, which_axis = 'y', label_range_spec = None):
    """Formats axis label according to label range format specification(s).

    This method fetches the current label-values for x or y axis of the 
    axis-object (ax), formats the labels according to the format specification 
    (label_range_spec) for ranges of values of the label; and finaly, 
    updates the axis-label in the axis-object.


    Parameters
    ----------
    ax: axis-object. (matplotlib.pyplot.gca() is default)
    which_axis: 'x', 'y'. ('y' is default)
    label_range_spec: list. (None is default)
        See format_labels() for more details. If None is used the following is 
        used instead.
    >>> abel_range_spec = [{'min': -np.inf, 'max': np.inf, 'format': ':.1f'}, ]


    Refernces
    ---------
    Relevant Stackoverflow thread: 
        https://stackoverflow.com/questions/11244514/modify-tick-label-text


    Example
    -------

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> # Comment out the following three lines 
    >>> #        if not using jupyter notebook.
    >>> %matplotlib inline
    >>> %config InlineBackend.figure_format = 'svg' # 'svg', 'retina'
    >>> plt.style.use('seaborn-white')
    >>> 
    >>> # Make data
    >>> x = np.arange(-0.7, 7, 0.1)
    >>> y = 0.6*(x**2 - 8*x + 10)
    >>> 
    >>> #Make figure
    >>> fig, ax = plt.subplots()
    >>> # Draw canvas and initiate labels on the figure
    >>> fig.canvas.draw()
    >>> ax.plot(x,y, label='Dummy Data')
    >>> 
    >>> which_axis ='y' # specify which axis to apply fancy-formatting
    >>> # Make fancy-formatting specifications
    >>> label_range_spec = [{'min': -np.inf, 'max': 2.000, 'format': ':.0f'}, 
    ...                     {'min': 2.001, 'max': 5.000, 'format': ':.1f'}, 
    ...                     {'min': 5.001, 'max': 11.000, 'format': ':.2f'}, 
    ...                     {'min': 11.001, 'max': np.inf, 'format': ':.3e'}, 
    ...                     ]
    >>> # Apply fancy-formatting to axis-labels                    
    >>> fancy_format_axis_labels(ax = ax, 
    ...                          which_axis = which_axis, 
    ...                          label_range_spec = label_range_spec)
    >>> plt.xlabel('x')
    >>> plt.ylabel('y')
    >>> plt.title('Demo: Fancy Label Format on {}-axis'.format(which_axis))
    >>> plt.legend()
    >>> plt.show()    

    """
    if ax is None: ax = plt.gca()
    if which_axis!='y': which_axis = 'x'
    labels = fetch_labels(ax = ax, which_axis = 'y')
    formatted_labels = format_labels(labels = labels, 
                                 label_range_spec = label_range_spec)
    ax.set_yticklabels(labels = formatted_labels)

def fetch_labels(ax = None, which_axis = 'y'):
    """Fetch axis labels.

    Parameters
    ----------
    ax: axis-object. (matplotlib.pyplot.gca() is default)
    which_axis: 'x', 'y'. ('y' is default)

    Ouput
    -----
    labels: list. 
        A list of strings of the axis-labels.

    Example
    -------
    >>> ax = plt.gca()
    >>> labels = fetch_labels(ax = ax, which_axis = 'y')
    
    """
    if ax is None: ax = plt.gca()
    if which_axis=='y':
        # The following option does not work. Hence, commented out.
        # >>> labels = [label.get_text() for label in ax.get_yticklabels()][1:]
        labels = ax.get_yticks().tolist()[1:] # drop the first element
    else:
        labels = ax.get_xticks().tolist()[1:] # drop the first element         
    return labels

def format_labels_subgroup(subgroup_labels, dataformat = ':.0f'):
    """Formats labels of a subgroup.
        
    Parameters
    ----------
    subgroup_labels: list.
        A list of labels from a subgroup defined by format-specifications.
    dataformat: string. (':.0f' is default)
        See process_labels_subgroup() for more information.

    Output
    ------
    labels: list.
        A list of formatted subgroup labels.
    """
    #minval, maxval, digits = -np.inf, np.inf, 0
    s = ('{'+ dataformat + '}')
    labels = [s.format(label) for label in subgroup_labels]
    return labels

def process_labels_subgroup(label_array, minval = -np.inf, maxval = np.inf, dataformat = ':.0f'):
    """Returns formatted labels for a subgroup (subset) of all the labels.

    This method returns the formatted labels for a subgroup of all the labels. 
    The subgroup is determined by the range specified. And the range contains 
    information on minimum, maximum and the dataformat.


    Parameters
    -----------
    label_array: numpy array. 
        a numpy numeric array of the axis-labels from a figure. 
        By axis we mean x or y.
        
    minval: float, int. (-inf by default) [optional]
        a numeric (float or int). Minimum of a range specification. 
        
    maxval: float, int. (inf by default) [optional]
        A numeric (float or int). Maximum of a range specification.
        
    dataformat: String. (':.0f' by default) 
        A string representation of the format mentioned in the 
        range specification. This follows the same formatting rule 
        as in the case for format string. 


    Output 
    -------
    sg_labels: formatted labels for the subgroup. A list of strings.


    See also
    --------


    Example:
    >>> label_array = np.array([-2.20, 0, 2.1, 4.279])
    >>> process_labels_subgroup(label_array, 
    ...                         minval = -np.inf, 
    ...                         maxval = np.inf, 
    ...                         dataformat = ':.2f')
    >>> ['-2.20', '0.00', '2.10', '4.28']
    """
    if minval is None: minval = -np.inf
    if minval is None: maxval = np.inf
    sg_labels = label_array[(label_array>=minval) & (label_array<=maxval)].tolist()
    sg_labels = format_labels_subgroup(subgroup_labels = sg_labels, 
                                       dataformat = dataformat)
    return sg_labels

def format_labels(labels, label_range_spec = None):
    """
    Returns formatted labels based on label range specification.

    Parameters:
    -----------
    labels: list. 
        A list of labels, each as a string of a number in the range [-inf, inf].
    label_range_spec: list. (None is default)
        A list of range-specification dictionaries, specifying 
        min, max and number format. If None is given, then the default value is 
        used.
        default is: [{'min': -np.inf, 'max': np.inf, 'format': ':.1f'}, ]                        


    Output 
    -------
    formatted_labels: a list of labels formatted as strings as per specification. 


    Example 
    --------
    To display a single digit after the decimal, for all numbers in the range 
    [-inf, inf], you could use the following label_range_spec.

    >>> label_range_spec = [{'min': -np.inf, 'max': np.inf, 'format': ':.1f'}, ]

    A complete example:
    >>> labels = ['-2.5', '0.5', '3.5', '7.0']
    >>> label_range_spec = [{'min': -np.inf, 'max': 0.000, 'format': ':.0f'}, 
    ...                     {'min': 0.001, 'max': 6.000, 'format': ':.1f'}, 
    ...                     {'min': 6.001, 'max': np.inf, 'format': ':.2e'}, 
    ...                     ]
    >>> format_labels(labels = labels, label_range_spec = label_range_spec)
    >>> ['-2', '0.5', '3.5', '7.00e+00']
    """
    if label_range_spec is None:
        label_range_spec = [{'min': -np.inf, 'max': np.inf, 'format': ':.1f'}, ]
    if isinstance(label_range_spec, list):
        label_array = np.array([float(label) for label in labels]) #.astype(float)
        formatted_labels = list()
        for format_group in label_range_spec:    
            #print(format_group)
            sg_labels = process_labels_subgroup(label_array = label_array, 
                                                minval = format_group['min'], 
                                                maxval = format_group['max'], 
                                                dataformat = format_group['format'])
            formatted_labels += sg_labels.copy()

        return formatted_labels
    else:
        message = ['label_range_spec = a list of dicts in a specific format. ', 
                   'Non-list input provided.', ]
        message = ''.join(message)
        raise TypeError(message)
