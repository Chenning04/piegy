.. _simulation:

piegy.simulation
========================

This section documents the core of the ``piegy`` package: model initialization and stochastic simulation.

To run a simulation, first use the ``model`` class to set up a model, then run simulation by ``run`` function. 
The simulations are computationally intensive. See brief discussion of runtime at :ref:`runtime<runtime>`.

.. _model:

.. py:class:: simulation.model(N, M, maxtime, record_itv, sim_time, boundary, init_popu, matrices, patch_params, print_pct = 50, seed = None)

    A ``simulation.model`` object contains the parameters and data storage bins for a model. Initialize such an object to set up your model. 
    See :ref:`below<_patch_vars>` for detailed explanation of ``init_popu``, ``matrices``, ``patch_params`` parameters. 

    :param N: spatial dimension, number of rows.
    :type N: int
    
    :param M: spatial dimension, number of columns.
    :type M: int

    :param maxtime: how long you wish the simulation to run.
    :type maxtime: float or int

    :param record_itv: record interval. Stores data every ``record_itv`` of time. Smaller values give finer data but also take more space.
    :type record_itv: float or int

    :param boundary: boundary condition. ``True`` for zero-flux ("with boundary"), ``False`` for periodical ("no boundary").
    :type boundary: bool

    :param init_popu: initial population. Expect shape ``N x M x 2``, the last dimension refers to the initial population of the two species in a patch.
    :type init_popu: list or numpy.ndarray

    :param matrices: payoff matrices. Expect shape ``N x M x 4``, the last dimension refers to flattened 2 x 2 payoff matrices in each patch.
    :type matrices: list or numpy.ndarray

    :param patch_params: patch parameters. Expect shape ``N x M x 6``. There are 6 parameters in a patch: :math:`\mu1`, :math:`\mu2`, :math:`w1`, :math:`w2`, :math:`\kappa1`, :math:`\kappa2`, stored in that order.
    :type patch_params: list or numpy.ndarray

    :param print_pct: current progress in percentage. Used to specify progress percentage being printed. Set to ``None`` to disable. Use multiples of 100 to print only every some rounds.
    :type print_pct: int or ``None``.

    :param seed: seed for random number generator. Used to initialize a numpy random generator.
    :type seed: int

    We use the following instance variables for data saving.

    .. attribute:: max_record

        Total number of records this object stores. Equals to ``int(maxtime / interval)``.

        :type: int

    .. attribute:: compress_ratio
        
        Number of data points to take average over and then save. Intended to reduce data size. See details at :ref:`Clarifications-compress_data<compress_data>`

        :type: int

    .. attribute:: U
        
        Hawk's population. Has shape ``N x M x max_record``.

        :type: ``numpy.ndarray``

    .. attribute:: V
        
        Dove's population. Has shape ``N x M x max_record``.

        :type: ``numpy.ndarray``

    .. attribute:: Hpi
        
        Hawk's payoff. Has shape ``N x M x max_record``.

        :type: ``numpy.ndarray``

    .. attribute:: Dpi
        
        Dove's payoff. Has shape ``N x M x max_record``.

        :type: ``numpy.ndarray``

    Below are the public methods of ``simulation`` class.

    .. method:: copy(copy_data = True)

        Return a deep copy of self.
        
        :param copy_data: whether to copy data as well. Set to False if you want an empty copy. 
        :type copy_data: bool

        :return: a deep copy of self.
        :rtype: ``piegy.simulation.model``


    .. method:: clear_data()

        Clear data (``U``, ``V``, ``Hpi``, ``Dpi``): set all 4 objects to ``None``.


    .. method:: change_maxtime(maxtime)

        Change ``maxtime`` and re-initialize data (set to None). 

        Warning: this will result in loss of data.

        :param maxtime: the new maxtime
        :type maxtime: float or int

    
    .. method:: set_seed(seed)

        Set a new seed.

        :param seed: the new seed, must be non-negative.
        :type seed: int


    .. method:: compress_data(compress_ratio = 5)

        .. line-block::
            Significantly reduces data size by taking average of every some number of data points and store these averages. See implementation details at :ref:`Clarifications-compress_data<compress_data>`.
            The update is in-place, no return value. 

            Notice this results in loss of orginal data.

        :param compress_ratio: over how many data points to take average and re-save.
        :type compress_ratio: int

        .. note::
            Regarding considerations about conflict with ``interval`` param in ``figures`` module, see :ref:`Clarifications, interval-compress_ratio<interval_compress_ratio>`

|

.. _run:

.. py:function:: simulation.run(mod, predict_runtime = False, message = '')

    Run simulations on ``mod``. All data will be stored in ``mod``. Only runs with empty model objects and raises error if not empty.

    :param mod: where all parameters of the model are stored. 
    :type mod: ``piegy.simulation.model`` object

    :param predict_runtime: whether to predict how much runtime the simulation still needs.
    :type predict_runtime: bool

    :param message: add a message in front of the print line. Only works if ``mod.print_pct`` is not ``None``. Not intended for public usage.
    :type message: str

|

.. _demo_model:

.. py:function:: simulation.demo_model()

    .. line-block::
        Returns an demo-purpose ``piegy.simulation.model`` object. See its parameters at :ref:`Demo_Params<demo_params>`
    
    :return: a demo model.
    :rtype: ``piegy.simulation.model``

|

.. _patch_vars:

``init_popu``, ``matrices``, and ``patch_params``
-------------------------------------------------------

There are three parameters in our model not explained in detail in the :ref:`piegy.simulation<simulation>` class above: ``I``, ``X``, ``P``, i.e., Initial Population, Payoff Matrices, and Patch Variables. 

We provide detailed explanation here.

* ``init_popu`` has dimension :math:`N \times M \times 2`. ``init_popu[i][j][0]`` is hawk's initial population at patch :math:`(i,j)`, and ``init_popu[i][j][1]`` is dove's initial population.
* ``matrices`` has dimension :math:`N \times M \times 4`. ``matrices[i][j]`` is payoff matrix flattened from the classical  :math:`2 \times 2` format, with U at first row & col, V at second row & col.
* ``patch_params`` has dimension :math:`N \times M \times 6`. ``patch_params[i][j][0]``, ``patch_params[i][j][1]`` characterize tendency of migration, which we denote by :math:`\mu1`, :math:`\mu2`, for hawks and doves, respectively. 
    Non-negative numbers. Use smaller values for weaker migration behavior, larger values on the contrary. In particular, set :math:`\mu=0` to disallow migration.
* ``patch_params[i][j][2]``, ``patch_params[i][j][3]`` measure sensitivity to payoff, i.e., the extent to which the direction of migration is biased by payoff. We denote by :math:`w1`, :math:`w2`, for hawks and doves, respectively.
    :math:`w1`, :math:`w2` can be any non-negative number. A typical range is :math:`[0, 500]`, with smaller values for lower sensitivity to payoff, larger values on the contrary. In particular, set :math:`w=0` for pure random walk.
    However, since ``w1`` and ``w2`` are used in the exponential function ``exp``, large values might result in overflow or reduced accuracy.
* ``patch_params[i][j][2]``, ``patch_params[i][j][3]`` measure carrying capacity, which we denote by :math:`\kappa1`, :math:`\kappa2`, respectively.
    :math:`\kappa1`, :math:`\kappa2` can also be any non-negative number, while we recommend around :math:`0.001`. Too large :math:`\kappa` values lead to very small equilibrium population.

Note by using :math:`N \times M \times x` lists/arrays, our model allows each patch to have different initial populations, payoff matrices, and patch variables. So don't restrict your model to uniform setups!

|

.. _model_examples:

Examples
---------

Here we give a detailed example for model setup.

First please import the ``piegy.simulation`` module:

.. code-block:: python

    import piegy.simulation as simulation

A simulation begins with defining a set of parameters and storing them in a ``piegy.simulation.model`` object. 
To get started right away, you can simply call ``piegy.simulation.demo_model`` and get a pre-made model:

.. code-block:: python

    mod = simulation.demo_model()


Or you can define your own set of parameters. Here is a full list of parameters with values same as ``mod`` above.

.. code-block:: python

    N = 10                  # Number of rows
    M = 10                  # Number of cols
    maxtime = 100           # how long you want the model to run
    record_itv = 0.1        # how often to record data.
    sim_time = 1            # repeat the simulation a few times
    boundary = True         # boundary condition.

    # initial population for the N x M patches. 
    init_popu = [[[200, 100] for _ in range(M)] for _ in range(N)]
    
    # flattened payoff matrices, total resource is 0.4, cost of fighting is 0.1
    matrices = [[[-1, 4, 0, 2] for _ in range(M)] for _ in range(N)]
    
    # patch variables
    patch_params = [[[1, 1, 10, 10, 0.001, 0.001] for _ in range(M)] for _ in range(N)]

    print_pct = 50           # print progress
    seed = 36               # seed for random number generation

    # store in a piegy.simulation.model object
    mod = simulation.model(N, M, maxtime, record_itv, sim_time, boundary, init_popu, matrices, patch_params, print_pct, seed)

.. line-block::
    Now we can run the simulation: simply call ``piegy.simulation.run``. Runtime may vary based on what parameters you use.

.. code-block:: python

    simulation.run(mod)

.. line-block::
    It will print out current progress while running the simulation. To run silently, set ``print_pct = None`` in the above parameters and re-create ``sim`` and run the simulation.

.. line-block::
    Data generated during the simulation will be stored in the ``sim`` variable. You can either examine them directly or save for later use by :ref:`piegy.data_tools<data_tools>`

    Here is a short script for saving:

.. code-block:: python

    from piegy.data_tools import save_data
    save_data(mod, 'some_directory')


But there is one problem (and you may have noticed): the data size is too large! 

For our demo simulation, we are saving :math:`12 \cdot 10^6` numbers in total (see: :ref:`Clarifications-compress_data<compress_data>`).
We can decrease reduce this size by 10 times using the ``compress_data`` method (see above for method details):

.. code-block:: python

    mod.compress_data(10)

This directly modifies ``sim`` variable and only stores average values over every 10 original data points.

Please note that the change is in-place: ``sim`` itself will be changed and you will lose the original data permanently.
If you are not sure, please make a copy of ``sim`` first:

.. code-block:: python

    sim_copy = mod.copy()

And then call ``compress_data`` on ``sim_copy``.


