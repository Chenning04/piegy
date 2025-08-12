.. _figures:

piegy.figures
=============

..  Example: https://www.sphinx-doc.org/en/master/tutorial/describing-code.html
    Grammar: https://www.sphinx-doc.org/en/master/usage/domains/python.html

This section describes the ``figures`` module of our package: make figures to visualize simulation results.
We reserved the word "plot" for matplotlib plots, and use "figures" as the name of the module instead.

Dynamics Figures
---------------------------------

This subsection contains the functions for plotting dynamics of certain values, i.e., how the values change over time, from time t = 0 to maxtime.

.. py:function:: figures.UV_dyna(mod, ax = None, interval = 20)

    .. line-block::
        Plot population dynamics of the two species over time, specifically hawk's population ``U``, doves' population ``V``, and total population ``U + V``.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax: matplotlib axes to plot upon. A new axes will be created if ``None`` is given.
    :type ax: matplotlib axes

    :param interval: the function takes average over every ``interval`` many data points and makes plot. 
                    Used to smooth curves. See details at :ref:`Clarifications-interval<interval>`
    :type interval: int

    :return: a plot of the change of population over time.
    :rtype: matplotlib axes.

|

.. py:function:: figures.pi_dyna(mod, ax = None, interval = 20)

    .. line-block::
        Plot payoff dynamics of the two species over time, specifically hawk's population ``Hpi``, doves' population ``Vpi``, and total population ``Hpi + Vpi``.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax: matplotlib axes to plot upon. A new axes will be created if ``None`` is given.
    :type ax: matplotlib axes

    :param interval: the function takes average over every ``interval`` many data points and makes plot. 
                    Used to smooth curves. See details at :ref:`Clarifications-interval<interval>`
    :type interval: int

    :return: a plot of the change of population over time.
    :rtype: matplotlib axes.

|

.. py:function:: figures.UV_std(mod, ax = None, interval = 20)

    .. line-block::
        Plot dynamics of standard deviation of population over time.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax: matplotlib axes to plot upon. A new axes will be created if ``None`` is given.
    :type ax: matplotlib axes

    :param interval: the function takes average over every ``interval`` many data points and makes plot. 
                    Used to smooth curves. See details at :ref:`Clarifications-interval<interval>`
    :type interval: int

    :return: a plot of the change of population over time.
    :rtype: matplotlib axes.

|

.. py:function:: figures.pi_std(mod, ax = None, interval = 20)

    .. line-block::
        Plot dynamics of standard deviation of payoff over time.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax: matplotlib axes to plot upon. A new axes will be created if ``None`` is given.
    :type ax: matplotlib axes

    :param interval: the function takes average over every ``interval`` many data points and makes plot. 
                    Used to smooth curves. See details at :ref:`Clarifications-interval<interval>`
    :type interval: int

    :return: a plot of the change of population over time.
    :rtype: matplotlib axes.

|

.. py:function:: figures.UV_hist(mod, ax_H = None, ax_D = None, color_H = 'purple', color_D = 'green', start = 0.95, end = 1.0)

    Make two histograms of average population density in a specified time interval.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax_H: matplotlib axes to plot the histogram of U upon. A new axes will be created if ``None`` is given.
    :type ax_H: matplotlib axes

    :param ax_D: matplotlib axes to plot the histogram of V upon. A new axes will be created if ``None`` is given.
    :type ax_D: matplotlib axes

    :param color_H: color for the histograms, using regular matplotlib colors.
    :type color_H: str

    :param color_D: similar to ``color_H``.
    :type color_D: str

    :param start: start of the time interval. Default 0.9 means the interval starts from 90% of maxtime. 
    :type start: float or int, :math:`\le 1`

    :param end: end of the time interval. Default 1.0 means the interval ends at exactly maxtime. See details of ``start`` and ``end`` at :ref:`Clarifications-start-end<start_end>`.
    :type end: float or int, :math:`\le 1`

    :return: two density histograms for U, V population.
    :rtype: matplotlib axes.

|

.. py:function:: figures.pi_hist(mod, ax_H = None, ax_D = None, color_H = 'purple', color_D = 'green', start = 0.95, end = 1.0)

    Make two histograms of average payoff density in a specified time interval.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax_H: matplotlib axes to plot the histogram of U payoff upon. A new axes will be created if ``None`` is given.
    :type ax_H: matplotlib axes

    :param ax_D: matplotlib axes to plot the histogram of V payoff upon. A new axes will be created if ``None`` is given.
    :type ax_D: matplotlib axes

    :param color_H: color for the histograms, using regular matplotlib colors.
    :type color_H: str

    :param color_D: similar to ``color_H``.
    :type color_D: str

    :param start: start of the time interval. Default 0.9 means the interval starts from 90% of maxtime. 
    :type start: float or int, :math:`\le 1`

    :param end: end of the time interval. Default 1.0 means the interval ends at exactly maxtime. See details of ``start`` and ``end`` at :ref:`Clarifications-start-end<start_end>`.
    :type end: float or int, :math:`\le 1`

    :return: two density histograms for U, V payoff.
    :rtype: matplotlib axes.


Distribution Figures
----------------------

This subsection contains the distribution functions, i.e., the average distribution of either population or payoff in a specified time interval.


.. _figures_HV_heatmap:

.. py:function:: figures.UV_heatmap(mod, ax_H = None, ax_D = None, color_H = 'Purples', color_D = 'Greens', start = 0.95, end = 1.0)
    
    .. line-block::
        Make two heatmaps for average population distributions of hawks and doves in a specified time interval.
        Intended for the 2D spatial setting, where both ``N`` and ``M`` larger than 1. For 1D space, please use :ref:`UV_bar<figures_HV_bar>`.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax_H: matplotlib axes to plot the heatmap of U population upon. A new axes will be created if ``None`` is given.
    :type ax_H: matplotlib axes

    :param ax_D: matplotlib axes to plot the heatmap of V population upon. A new axes will be created if ``None`` is given.
    :type ax_D: matplotlib axes

    :param color_H: color to use for U's heatmap. Uses matplotlib color maps.
    :type color_H: str

    :param color_D: similar to ``color_H``.
    :type color_D: str

    :param start: start of the time interval. Default 0.9 means the interval starts from 90% of maxtime. 
    :type start: float or int, :math:`\le 1`

    :param end: end of the time interval. Default 1.0 means the interval ends at exactly maxtime. See details of ``start`` and ``end`` at :ref:`Clarifications-start-end<start_end>`.
    :type end: float or int, :math:`\le 1`

    :return: two heatmaps of distribution of U, V population.
    :rtype: matplotlib axes.

|

.. _figures_pi_heatmap:

.. py:function:: figures.pi_heatmap(mod, ax_H = None, ax_D = None, color_H = 'Purples', color_D = 'Greens', start = 0.95, end = 1.0)

    .. line-block::
        Make two heatmaps for average payoff distributions of hawks and doves in a specified time interval.
        Intended for 2D spatial setting, where both ``N`` and ``M`` larger than 1. For 1D space, please use :ref:`pi_bar<figures_pi_bar>`.

        Recommend using different colors for population and payoff to avoid confusion.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax_H: matplotlib axes to plot the heatmap of U payoff upon. A new axes will be created if ``None`` is given.
    :type ax_H: matplotlib axes

    :param ax_D: matplotlib axes to plot the heatmap of V payoff upon. A new axes will be created if ``None`` is given.
    :type ax_D: matplotlib axes

    :param color_H: color to use for U's heatmap. Uses matplotlib color maps.
    :type color_H: str

    :param color_D: similar to ``color_H``.
    :type color_D: str

    :return: two heatmaps of distribution of U, V population.
    :rtype: matplotlib axes.

|

.. _figures_HV_bar:

.. py:function:: figures.UV_bar(mod, ax_H = None, ax_D = None, color_H = 'purple', color_D = 'green', start = 0.95, end = 1.0)

    .. line-block::
        Make two heatmaps for average population distributions of hawks and doves in a specified time interval.
        Intended for 1D spatial setting, where ``N`` = 1. For 2D space, please use :ref:`UV_heatmap<figures_HV_heatmap>`.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax_H: matplotlib axes to plot the heatmap of U payoff upon. A new axes will be created if ``None`` is given.
    :type ax_H: matplotlib axes

    :param ax_D: matplotlib axes to plot the heatmap of V payoff upon. A new axes will be created if ``None`` is given.
    :type ax_D: matplotlib axes

    :param color_H: color for the barplots. Note we are not making heatmaps, so please use regular colors rather than color maps.
    :type color_H: str

    :param color_D: similar to ``color_H``.
    :type color_D: str

    :param start: start of the time interval. Default 0.9 means the interval starts from 90% of maxtime. 
    :type start: float or int, :math:`\le 1`

    :param end: end of the time interval. Default 1.0 means the interval ends at exactly maxtime. See details of ``start`` and ``end`` at :ref:`Clarifications-start-end<start_end>`.
    :type end: float or int, :math:`\le 1`

    :return: two baplots of distribution of U, V population.
    :rtype: matplotlib axes.

|

.. _figures_pi_bar:

.. py:function:: figures.pi_bar(mod, ax_H = None, ax_D = None, color_H = 'violet', color_D = 'yellowgreen', start = 0.95, end = 1.0)

    .. line-block::
        Make two heatmaps for average payoff distributions of hawks and doves in a specified time interval.
        Intended for 1D spatial setting, where ``N`` equal to 1. For 2D space, please use :ref:`pi_heatmap<figures_pi_heatmap>`.

        Recommend using different colors for population and payoff to avoid confusion.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax_H: matplotlib axes to plot the barplot of U population upon. A new axes will be created if ``None`` is given.
    :type ax_H: matplotlib axes

    :param ax_D: matplotlib axes to plot the barplot of V population upon. A new axes will be created if ``None`` is given.
    :type ax_D: matplotlib axes

    :param color_H: color for the barplots. Note we are not making heatmaps, so please use regular colors rather than color maps.
    :type color_H: str

    :param color_D: similar to ``color_H``.
    :type color_D: str

    :param start: start of the time interval. Default 0.9 means the interval starts from 90% of maxtime. 
    :type start: float or int, :math:`\le 1`

    :param end: end of the time interval. Default 1.0 means the interval ends at exactly maxtime. See details of ``start`` and ``end`` at :ref:`Clarifications-start-end<start_end>`.
    :type end: float or int, :math:`\le 1`

    :return: two baplots of distribution of U, V population.
    :rtype: matplotlib axes.

|

Other Functions
--------------------

.. py:function:: figures.UV_pi(mod, ax_H = None, ax_D = None, color_H = 'violet', color_D = 'yellowgreen', alpha = 0.25, start = 0.95, end = 1.0)

    .. line-block::
        Make a scatter plot for the correlation between average population and average payoff across a specified time interval.
        Every point denotes a patch, its x-coord is the patch's population, y-coord is payoff.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param ax_H: matplotlib axes to plot the corr plot of U population-payoff upon. A new axes will be created if ``None`` is given.
    :type ax_H: matplotlib axes

    :param ax_D: matplotlib axes to plot the corr plot of V population-payoff upon. A new axes will be created if ``None`` is given.
    :type ax_D: matplotlib axes

    :param color_H: color for the barplots. Note we are not making heatmaps, so please use regular colors rather than color maps.
    :type color_H: str

    :param color_D: similar to ``color_H``.
    :type color_D: str

    :param start: start of the time interval. Default 0.9 means the interval starts from 90% of maxtime. 
    :type start: float or int, :math:`\le 1`

    :param end: end of the time interval. Default 1.0 means the interval ends at exactly maxtime. See details of ``start`` and ``end`` at :ref:`Clarifications-start-end<start_end>`.
    :type end: float or int, :math:`\le 1`

    :return: two baplots of distribution of U, V population.
    :rtype: matplotlib axes.

    :return: two scatter plots for correlation between population and payoff, for U and V two species.
    :rtype: matplotlib axes.

|

.. py:function:: figures.UV_expected(mod, color_H = 'Purples', color_D = 'Greens')

    .. line-block::
        Calculate and plot expected population of every patch only based on payoff matrices, assuming no migration or any stochastic process. Handles both 1D and 2D case.
        For 2D, population is shown in heatmaps. And for 1D, uses barplots.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param color_H: color for U's plot. Please use matplotlib color map if your space is 2D, use regular colors if 1D.
    :type color_H: str

    :param color_D: same as ``color_H``.
    :type color_D: str

    :return: two heatmaps or barplots about the distribution of U, V expected population.
    :rtype: matplotlib figure

|

.. py:function:: figures.UV_expected_val(mod)

    .. line-block::
        Calculate expected U, V population based on payoff matrices, assuming no migration or any stochastic process.
        To differentiate from ``peigy.figures.UV_expected``, this funtion returns the exact values rather than figures.

        We recommend using ``peigy.figures.UV_expected`` instead for visualization purposes. Use this function if you want the exact values.

    :param mod: where the parameters of the model and data are stored. 
    :type mod: ``piegy.simulation.model`` object

    :return: two 2D arrays containing the expected population at each patch.
    :rtype: ``numpy.ndarray``

|

.. _figures_examples:

Examples
---------

.. line-block::
    Here are some usage examples for each of the ``piegy.figures`` functions. 

    First please import the ``piegy.simulation`` and ``piegy.figures`` modules:

.. code-block:: python

    from piegy import simulation, figures
    import matplotlib.pyplot as plt

.. line-block::
    All figures below are generated based on our :ref:`demo model<demo_params>`. You get a copy by ``piegy.simulation.get_demo`` function:

.. code-block:: python

    mod = simulation.demo_model()

.. line-block::
    Let's run the simulation:

.. code-block:: python

    simulation.run(mod)

.. line-block::
    After a simulation is completed, the first thing you probably want to do is convergence check: whether the population has reached equilibrium state.

    Make a population dynamics figure by ``piegy.figures.UV_dyna`` function:

.. code-block:: python

    fig_UV_dyna, ax_UV_dyna = plt.subplots()
    figures.UV_dyna(mod, ax_UV_dyna, interval = 10)

.. line-block::
    ``interval = 10`` means to take average over every 10 data points. See more at :ref:`Clarifications-interval<interval>`.

    It gives the following figure:

.. figure:: images/UV_dyna.png
    :width: 80%

    UV_dyna: Population Dynamics

.. line-block::
    We can similarly look at payoff dynamics by ``piegy.figures.pi_dyna`` function:

.. code-block:: python

    fig_pi_dyna, ax_pi_dyna = plt.subplots()
    figures.pi_dyna(mod, ax_pi_dyna, interval = 10)

.. figure:: images/pi_dyna_10.png
    :width: 80%

    pi_dyna: Payoff Dynamics

.. line-block::
    Note there are many fluctuations in the figure. You can smooth them out (a bit) with larger ``interval`` value:

.. code-block:: python

    fig_pi_dyna40, ax_pi_dyna40 = plt.subplots()
    figures.pi_dyna(mod, ax_pi_dyna40, interval = 40)

.. figure:: images/pi_dyna_40.png
    :width: 80%

    Smoother Payoff Dynamics with ``interval`` = 40

.. line-block::
    You can also look at change of standard deviation by ``piegy.figures.UV_std`` and ``piegy.figures.pi_std``.

|

Let's now look at distributions: the distribution of population and payoff in some certain time interval.
Call ``piegy.figures.UV_heatmap`` function:

.. code-block:: python

    fig_UV_hmap, ax_UV_hmap = plt.subplots(2, 1, figsize = (6.4, 9.6))
    figures.UV_hmap(mod, ax_UV_hmap[0], ax_UV_hmap[1], start = 0.95, end = 1.0)

.. line-block::
    ``start = 0.95`` and ``end = 1.0`` means we are plotting the average distribution over 95% ~ 100% of total time, i.e., the end of simulation.

.. figure:: images/UV_hmap.png
    :width: 80%

    U & V population Distribution in 95% ~ 100% Total Time

.. line-block::
    Interested in some other time intervals? You can plot any time interval by changing ``start`` and ``end`` values. 

    We can also make payoff distribution heatmaps by ``piegy.figures.pi_heatmap``:

.. code-block:: python

    fig_pi_hmap, ax_pi_hmap = plt.subplots(2, 1, figsize = (6.4, 9.6))
    figures.pi_hmap(mod, ax_pi_hmap[0], ax_pi_hmap[1], start = 0.95, end = 1.0)

.. figure:: images/pi_hmap.png
    :width: 80%

    U & V Payoff Distribution in 95% ~ 100% Total Time

You may notice the correlation between population and payoff: patches with higher population tend to have higher payoff. 
Let's visualize the correlation with scatter plots. Call ``piegy.figures.UDpi``:

.. code-block:: python

    fig_corr, ax_corr = plt.subplots(2, 1, figsize = (6.4, 9.6))
    figures.UV_pi(mod, ax_corr[0], ax_corr[1], alpha = 0.5, start = 0.95, end = 1.0)

.. line-block::
    ``alpha`` is used to make points semi-transparent since there are lots of overlaps.

.. figure:: images/corr.png
    :width: 80%

    U and V Population - Payoff Correlation Plot

So far we have introduced most of our ``piegy.figures`` functions and basic usages. Explore the rest as well!

