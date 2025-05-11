.. _model:

piegy.model
===========

This section documents the core of the ``piegy`` package: the stochastic model.

To run a simulation, first use the ``simulation`` class to set up a model, then run simulation by ``run`` function.

The simulations are computationally intensive. See brief discussion of runtime at :ref:`runtime<runtime>`.

.. _simulation:

.. py:class:: model.simulation(N, M, maxtime, record_itv, sim_time, boundary, I, X, P, print_pct = 25, seed = None, UV_dtype = 'float32', pi_dtype = 'float64')

    .. line-block::
        A ``simulation`` object contains all the parameters and data storage bins for a model. Initialize such an object to set up your model.

    :param N: spatial dimension, number of rows of patches in space.
    :type N: int
    
    :param M: spatial dimension, number of columns of patches in space.
    :type M: int

    :param maxtime: how long you want the simulation to run.
    :type maxtime: float or int

    :param record_itv: record interval. Stores data every ``record_itv`` of time. Smaller values give finer data but also take more space.
    :type record_itv: float or int

    :param boundary: boundary condition. ``True`` for zero-flux ("with boundary"), ``False`` for periodical ("no boundary").
    :type boundary: bool

    :param I: initial population. Expect shape ``N x M x 2``. The shape 2 is for init population of U and V in a patch, stored in that order.
    :type I: list or numpy.ndarray

    :param X: payoff matrices. Expect shape ``N x M x 4``. The shape 4 is for the flattened 2 x 2 payoff matrix in a patch.
    :type X: list or numpy.ndarray

    :param P: patch variables. Expect shape ``N x M x 6``. There are 6 patch variables: mu1, mu2, w1, w2, kappa1, kappa2, stored in that order.
    :type P: list or numpy.ndarray

    :param print_pct: print progress. Print how much percentage has finished in current round. Messages look like ``round 16, 36%``. Use ``None`` to avoid printing.
    :type print_pct: int

    :param seed: seed for random number generator. Used to initialize a numpy random generator.
    :type seed: int

    :param UV_dtype: data type for population storage. Passed to ``numpy.array``.
    :type UV_dtype: str

    :param pi_dtype: data type for payoff storage. Passed to ``numpy.array``.
    :type pi_dtype: str

    We use the following instance variables for data saving.

    .. attribute:: max_record

        Total number of records this object stores. Equals ``int(maxtime / interval)``.

        :type: int

    .. attribute:: compress_itv
        
        Number of data points to take average over and then save. Intended to reduce data size. See details at :ref:`Clarifications-compress_data<compress_data>`

        :type: int

    .. attribute:: U
        
        Storage bin for U's population. Has shape ``N x M x max_record`` and data type specified by ``UV_dtype``.

        :type: ``numpy.ndarray``

    .. attribute:: V
        
        Storage bin for V's population. Has shape ``N x M x max_record`` and data type specified by ``UV_dtype``.

        :type: ``numpy.ndarray``

    .. attribute:: U_pi
        
        Storage bin for U's population. Has shape ``N x M x max_record`` and data type specified by ``pi_dtype``.

        :type: ``numpy.ndarray``

    .. attribute:: V_pi
        
        Storage bin for V's population. Has shape ``N x M x max_record`` and data type specified by ``pi_dtype``.

        :type: ``numpy.ndarray``

    Below are the public methods of ``simulation`` class.

    .. method:: copy(copy_data = True)

        Return a deep copy of self.
        
        :param copy_data: whether to copy data as well. Set to False if you want an empty copy. 
        :type copy_data: bool

        :return: a deep copy of self.
        :rtype: ``piegy.model.simulation``


    .. method:: change_maxtime(maxtime)

        Change ``maxtime`` and re-initialize data storage bins. 

        Warning: this will result in loss of data, all entries set to 0.

        :param maxtime: the new maxtime
        :type maxtime: float or int

    
    .. method:: set_seed(seed)

        Set a new seed.

        :param seed: the new seed
        :type seed: int


    .. method:: clear_data()

        Clear all data storage bins (``U``, ``V``, ``U_pi``, ``V_pi``): set all entries to 0.
        Data type and shape are not changed.

    .. method:: compress_data(compress_itv = 5)

        
        .. line-block::
            Significantly reduces data size by taking average of every some number of data points and store these averages. See implementation details at :ref:`Clarifications-compress_data<compress_data>`.
            The update is in-place, no return value. 

            Notice this results in loss of orginal data.

        :param compress_itv: over how many data points to take average and re-save.
        :type compress_itv: int

        .. note::
            Regarding considerations about conflict with ``interval`` param in ``figures`` module, see :ref:`Clarifications, interval-compress_itv<interval_compress_itv>`

|

.. _run:

.. py:function:: model.run(sim, predict_runtime = True, message = '')

    .. line-block::
        Run simulations on ``sim``. All data are stored in ``sim``, no return value.

    :param sim: where all parameters of the model are stored. 
    :type sim: ``piegy.model.simulation`` object

    :param predict_runtime: whether to predict how much runtime the simulation still needs.
    :type predict_runtime: bool

    :param message: add a message in front of the print line. Only works if ``sim.print_pct`` is not ``None``. Not intended for public usage.
    :type message: str

|

.. _demo_model:

.. py:function:: model.demo_model()

    .. line-block::
        Returns an demo-purpose ``piegy.model.simulation`` object. See its parameters at :ref:`Demo_Params<demo_params>`
    
    :return: a demo model.
    :rtype: ``piegy.model.simulation``

|

.. _model_examples:

Examples
---------

Here we give a detailed example for model setup.

First please import the ``piegy.model`` module:

.. code-block:: python

    import piegy.model as model

A simulation begins with defining a set of parameters and storing them in a ``piegy.model.simulation`` object. 
To get started right away, you can simply call ``piegy.model.demo_model`` and get a pre-made model:

.. code-block:: python

    sim = model.demo_model()


Or you can define your own set of parameters. Here is a full list of parameters with values same as ``sim`` above.

.. code-block:: python

    N = 10                  # Number of rows
    M = 10                  # Number of cols
    maxtime = 300           # how long you want the model to run
    record_itv = 0.1        # how often to record data.
    sim_time = 1            # repeat the simulation a few times
    boundary = True         # boundary condition.

    # initial population for the N x M patches. 
    I = [[[44, 22] for _ in range(M)] for _ in range(N)]
    
    # flattened payoff matrices, total resource is 0.4, cost of fighting is 0.1
    X = [[[-0.1, 0.4, 0, 0.2] for _ in range(M)] for _ in range(N)]
    
    # patch variables
    P = [[[0.5, 0.5, 200, 200, 0.001, 0.001] for _ in range(M)] for _ in range(N)]

    print_pct = 5           # print progress
    seed = 36               # seed for random number generation
    UV_dtype = 'float32'    # data type for population
    pi_dtype = 'float64'    # data type for payoff

    # store in a piegy.model.simulation object
    sim = model.simulation(N, M, maxtime, record_itv, sim_time, boundary, I, X, P, 
                            print_pct = print_pct, seed = seed, UV_dtype = UV_dtype, pi_dtype = pi_dtype)

.. line-block::
    Now we can run the simulation: simply call ``piegy.model.run``. Runtime may vary based on what parameters you use.

.. code-block:: python

    model.run(sim)

.. line-block::
    It will print out current progress while running the simulation. To run silently, set ``print_pct = None`` in the above parameters and re-create ``sim`` and run the simulation.

.. line-block::
    Data generated during the simulation will be stored in the ``sim`` variable. You can either examine them directly or save for later use by :ref:`piegy.data_tools<data_tools>`

    Here is a short script for saving:

.. code-block:: python

    from piegy.data_tools import save_data
    save_data(sim, 'some_directory')


But there is one problem (and you may have noticed): the data size is too large! 

For our demo simulation, we are saving :math:`12 \cdot 10^6` numbers in total (see: :ref:`Clarifications-compress_data<compress_data>`).
We can decrease reduce this size by 10 times using the ``compress_data`` method (see above for method details):

.. code-block:: python

    sim.compress_data(10)

This directly modifies ``sim`` variable and only stores average values over every 10 original data points.

Please note that the change is in-place: ``sim`` itself will be changed and you will lose the original data permanently.
If you are not sure, please make a copy of ``sim`` first:

.. code-block:: python

    sim_copy = sim.copy()

And then call ``compress_data`` on ``sim_copy``.


