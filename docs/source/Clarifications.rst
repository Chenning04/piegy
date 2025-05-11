.. _Clarifications:

Clarifications
==============

This section provides clarifications for some possibly confusing usages and parameters.


.. _runtime:

Runtime
----------

The simulations are computationally intensive. 
For example, in our :ref:`demo model<demo_params>`, there are around 230,000 time steps in total and the number of calculations is at the level of millions.

We're doing our best to maximize speed: the current model is about 600 times faster than our initial implementation. There might still be room for further speed boost.

There are two major sources for runtime: size of model and parameters. It's easy to see larger models (i.e. larger spatial dimension and ``maxtime``) take longer runtime.

As for parameters, larger values of payoff matrix and mu1, mu2, smaller values of kappa1 and kappa2 would result in longer runtime. These values are related to size of time step in our fundamental algorithm. 
Larger (or smaller, in terms of kappa) values of these parameters would result in more time steps and hence longer runtime, even if spatial dimension and ``maxtime`` are fixed.

|

.. _model_used:

Model Used
---------------

Many clarifications are based on examples. We will use our :ref:`demo model<demo_params>` in below. You can get a copy of it by ``piegy.model.demo_model``.

.. code-block:: python

    import piegy.model as model

    sim = model.demo_model()
    model.run(sim)


.. _interval:

``interval``
------------

.. line-block::
    Parameter in: (``piegy.`` omitted)
    ``analysis.check_convergence``, ``test_var.var_convergence1``, ``test_var.var_convergence2``, ``figures``
    

.. line-block:: 
    ``interval`` essentially means: take average over some data points.

    It denotes the length of a "data interval". We take the average value over every such interval of data points, and work with these average values. Helps to smooth out local randomness.

    For example, in our :ref:`demo model<demo_params>`, if we make a U, V payoff - time plot without taking any average (i.e., ``interval = 1``), the figure will be:

.. figure:: images/demo_model/pi_dyna_1.png

    pi_dyna with interval = 1

.. line-block:: 
    Notice the high local fluctuations. We can smooth out these fluctuations by ``interval``, say set it to 40:

.. figure:: images/demo_model/pi_dyna_40.png

    pi_dyna with interval = 40

.. line-block:: 
    Now it looks much cleaner. 

    You may notice the x-range is reduced to around 80. That is exactly because we are taking averages: every 40 original data points give a new "average point".

|


.. _compress_data:

``compress_data`` and ``compress_itv``
--------------------------------------------

* ``compress_data`` is a class method of ``piegy.model.simulation``. 
* ``compress_itv``:
    * parameter for ``compress_data``.
    * A ``piegy.model.simulation`` object also has ``compress_itv`` has a variable. Stores current ratio of data reduction, initialized as 1 and updated by ``compress_data``.


.. line-block::
    ``compress_data`` is an effort to reduce data size by only saving average data rather than every data point.

    For example, let's look at how many numbers are contained in ``sim`` (our demo model, see parameters at :ref:`Typical Params<Typical_Params>`)

#. About ``N * M * 12`` input parameters (initial population, matrices, patch variables, etc.) This is small compared to below:
#. For U population, ``N * M * maxtime / record_itv`` in total. That is :math:`10 \cdot 10 \cdot 3000 = 3 \cdot 10^6` in our case.
#. And similarly for V population, U and V payoff.
#. So we will be saving about :math:`12 \cdot 10^6` numbers in total --- that's a lot!

There is indeed a way to reduce data at the expense of losing accuracy: take average every some interval of data points and save these average values. This is done by ``compress_data``.

For example, by calling:

.. code-block:: python

    sim.compress_data(10)

we will go through every patch and takes average over every 10 original data points, store the average, then move on to the next 10.
The change is in-place, i.e., directly modifies ``sim``.

Then for ``sim.U`` (U population), we used to store ``10 * 10 * 3000`` values, and now its size is reduced to ``10 * 10 * 300``. 
In terms of the total number of data points, we only need to save :math:`12 \cdot 10^5` numbers now, reduced by 10 times.

However, the actual size shown in your file system is probably not divided by 10. That may due to some ``json`` behaviors (data are stored in json format).

The size reduction comes at the expense of:

* The original data are lost; we only have average values now.
* The new data become coarser as we use larger ``compress_itv``.

You can call ``compress_data`` repeatedly, and data will become coarser and coarser as well. For example, calling ``sim.compress_data(10)`` again takes average over every :math:`10 \cdot 10` points; essentially the same as ``sim.compress_data(100)``.

You can check the current reduction ratio by printing out ``compress_itv`` variable of ``sim``:

.. code-block:: python

    print(sim.compress_itv)

|


.. _interval_compress_itv:

Considerations about ``interval`` and ``compress_itv``
-------------------------------------------------------

* Here ``interval`` refers to parameters of functions in ``piegy.figures``, ``piegy.analysis``, ``piegy.test_var``.
* ``compress_itv`` refers to variable of a ``piegy.model.simulation`` object, which records ratio of data reduction.

There might be considerations whether ``interval`` and ``compress_itv`` would have conflicts. The answer is **No**.

Our codes are specifically designed to accommodate both two intervals, in the following way:

#. Say ``interval = 10``.
#. If ``compress_itv`` is 1, then make plots / perform other analysis as they were: take average over every 10 data points and proceed.
#. If ``compress_itv`` is not 1, scale ``interval`` by:

    .. code-block:: python

        interval = int(interval / compress_itv)

    and then proceed. So that we will still be taking average over the same number of data points (in terms of the original data).
#. If ``compress_itv`` is larger than ``interval``, the above code would result in the new ``interval`` being 0. We then set it to 1 and print a warning message: data is coarser than the expected interval.

|

.. _start_end:

``start`` and ``end``
---------------------

.. line-block::
    Parameter in: (``piegy.`` omitted)
    ``analysis.check_convergence``, ``figures``, ``test_var``

.. line-block::
    The ``start`` and ``end`` parameters specify two time points by pointing to some proportion of maxtime.
    They are combined together to specify a time interval, with ``start`` being the lower bound and ``end`` being upper bound.

    For example, for ``maxtime`` = 300 in the our :ref:`demo model<demo_params>`, ``start`` = 0.9 points to the time point at 300 * 0.9 = 270, and ``end`` = 1.0 points to 300 * 1.0 = 300.
    
    We can then specify a time interval of 270~300 by combining ``start`` and ``end``, essentially the last 10% of time.

|

.. _convergence_fluc:

Convergence and ``fluc``
------------------------

.. line-block::
    ``fluc`` is a param in: (``piegy.`` omitted)
    ``analysis.check_convergence``, ``test_var.var_convergence1``, ``test_var.var_convergence2``

.. line-block::
    We check convergence by looking at some last-proportion of time and check whether the fluctuation of both U and V population is less than the ``fluc`` threshold.

    The implementation is:

#. For U population:
#. Get the average data points based on ``interval`` param (all 3 functions have this paramter).
#. Get the max and min of the average data
#. Fluctuation of U is then given by :math:`\frac{(max - min)}{min}`. Similarly for V. 
#. Consider the result convergent if both fluctuations are less than ``fluc``.




