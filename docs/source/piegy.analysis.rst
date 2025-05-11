.. _analysis:

piegy.analysis
====================

This module contains several analysis tools for simulation results.

.. py:function:: analysis.UV_expected_val(sim)

    .. line-block::
        Calculate expected U, V population based on payoff matrices, assuming no migration or any stochastic process.
        To differentiate from ``peigy.figures.UV_expected``, this funtion returns the exact values rather than figures.

        We recommend using ``peigy.figures.UV_expected`` instead for visualization purposes. Use this function if you want the exact values.

    :param sim: where the parameters of the model and data are stored. 
    :type sim: ``piegy.model.simulation`` object

    :return: two 2D arrays containing the expected population at each patch.
    :rtype: ``numpy.ndarray``

|

.. py:function:: analysis.check_convergence(sim, interval = 20, start = 0.8, fluc = 0.07)

    .. line-block::
        Check whether simulation has reached convergence.

        Actually performs a "Cauchy check" since we do not know the limit. i.e., whether the fluctuation of population after some specified time is small enough.
        However, we know being Cauchy indicates convergent in real numbers. So this check works in terms of math.

        See implementation details at :ref:`Clarifications-Convergence<convergence_fluc>`.

    :param sim: where the parameters of the model and data are stored. 
    :type sim: ``piegy.model.simulation`` object

    :param interval: takes average over some number of data points to smooth data.
    :type interval: int

    :param start: defines a time point by how much percentage of maxtime. Calculate fluctuation of U, V population after this point.
    :type start: float

    :param fluc: threshold of fluctuation. Check whether max fluctuation of U, V population after ``start`` proportion of time is less than this threshold.
    :type fluc: float

    :return: whether fluctuation after ``start`` proportion of time is less than ``fluc`` threshold.
    :rtype: bool

|

.. py:function:: analysis.combine_sim(sim1, sim2)

    .. line-block::
        Combines the simulation results in two ``piegy.model.simulation`` objects. 
        Intended usage: if the fluctuation of one simulation is too large, you can run another simulation and then take average of the two.

        Raises error if ``sim1`` and ``sim2`` have different ``N``, ``M``, ``maxtime``, ``record_itv``, ``boundary``, ``I``, ``X``, or ``P`` (can't combine two different models).

        Raises error if ``sim1`` and ``sim2`` have the same seed: can't reduce randomness if models used the same random seed.

    :param sim1: the first model.
    :type sim: ``piegy.model.simulation`` object

    :param sim2: the second model.
    :type sim: ``piegy.model.simulation`` object

    :return: a third model whose parameters are the same as ``sim1`` and ``sim2``, but data are the weighted average of the two (wieghted by the number of rounds each simulation ran)
    :rtype: ``piegy.model.simulation`` object

|


Examples
----------

Here are some usage examples for the ``piegy.analysis`` module.

First import a few necessary modules. We import ``piegy.figures`` as well because we will need some figures for cross comparison.

.. code-block:: python

    import piegy.model as model
    import piegy.figures as figures
    import piegy.analysis as analysis

As for the model setup, the parameters are very similar to our :ref:`demo model<Demo_Params>`, except for:

* Smaller spatial dimension to reduce run time. 
* ``sim_time = 10`` to decrease randomness.
* ``print_pct = 25`` to have fewer print lines.


A full list is here:

.. code-block:: python

    N = 5                   # Number of rows, reduced for shorter runtime
    M = 5                   # Number of cols, reduced for shorter runtime
    maxtime = 300           # how long you want the model to run
    record_itv = 0.1        # how often to record data.
    sim_time = 10           # repeat simulation to reduce randomness
    boundary = True         # boundary condition.

    # initial population for the N x M patches. 
    I = [[[44, 22] for _ in range(M)] for _ in range(N)]
    
    # flattened payoff matrices, total resource is 0.4, cost of fighting is 0.1
    X = [[[-0.1, 0.4, 0, 0.2] for _ in range(M)] for _ in range(N)]
    
    # patch variables
    P = [[[0.5, 0.5, 100, 100, 0.001, 0.001] for _ in range(M)] for _ in range(N)]

    print_pct = 25          # print progress
    seed = 36               # seed for random number generation
    UV_dtype = 'float32'    # data type for population
    pi_dtype = 'float64'    # data type for payoff

    # create a simulation object
    sim = model.simulation(N, M, maxtime, record_itv, sim_time, boundary, I, X, P, 
                            print_pct = print_pct, seed = seed, UV_dtype = UV_dtype, pi_dtype = pi_dtype)

Let's then run the simulation and then see how to use this module to analyze the result.

.. code-block:: python

    model.run(sim)

* **check_convergence**

A familiar way to check convergence is by plotting population dynamics and look at the curves. ``piegy.figures.UV_dyna(sim)`` gives the following figure:

.. figure:: images/analysis/sim1.png

    Population Dynamics with ``sim_time = 10``

We can see it roughly converges, but some small fluctuations do exist due to randomness.

However, as we run more simulations and have lots of results, it is inconvenient to check convergence manually. Here we provide a automatic approach by ``piegy.analysis.check_convergence`` function:

.. code-block:: python

    print(analysis.check_convergence(sim, interval = 20, start = 0.8, fluc = 0.07))  # rigorous requirements
    print(analysis.check_convergence(sim, interval = 50, start = 0.8, fluc = 0.15))  # relax a bit

The first line prints ``False`` and the second prints ``True``. How to interpret?

#. Passing the second test means the simulation results do converge in some sense: there exists some relaxed condition under which the result is considered convergent.
#. Failing the rigorous test indicates existence of local fluctuations: the result is not smooth and stable enough.

And that's the power of ``check_convergence`` function. It automatically checks whether the result converges, and converges to what extent.

In terms of actual usage, we recommend the following:

#. Say you have lots of simulation results and want to know which ones didn't converge.
#. Set up a rigorous test and a relaxed test, and check each of the results with the two tests.
#. This should filter out many results that are already stable.
#. Then manually check the remaining uncertain ones by plotting population dynamics.

But what about the results that didn't converge? We provide an approach to possibly re-use these results rather than simply discarding them.

* **combine_sim**

First make a copy of ``sim`` without data, just the parameters. You can see ``copy`` method at :ref:`piegy.model.simulation <simulation>`.

.. code-block:: python

    sim2 = sim.copy(copy_data = False)

Then change the seed of sim2, set to either ``None`` or a different seed, and run the simulation on ``sim2``:

.. code-block:: python

    sim2.set_seed(42)  # a different seed or None
    model.run(sim2)

Now we have two simulation results, one in ``sim`` and the other one in ``sim2``. Both of them have ``sim_time = 10``, i.e., the simulation was repeated 10 times. 
But since they have different seeds (or ``None``), we can take average of two simulations and obtain a new result, as if it was ran 20 times:

.. code-block:: python

    sim3 = analysis.combine_sim(sim, sim2)

``sim3`` has a much more stable result:

.. figure:: images/analysis/sim3.png

    Population Dynamics of ``sim``, ``sim2`` Combined

However, if you try the above convergence tests again, you would note ``sim3`` still fails the strict one. A larger number of repetitions such as ``sim_time = 50`` may pass the test.

