.. _data_tools:

piegy.data_tools
================

This section documents the data saving and reading tools.

.. py:function:: data_tools.save_data(sim, dirs = '', print_msg = True)

    .. line-block::
        Saves all parameters and data of a model. No return value.
        Direcotry will be created if does not exist.

    :param sim: where the parameters of the model and data are stored. 
    :type sim: ``piegy.model.simulation`` object

    :param dirs: where to save data, should be the path of a folder. If ``''`` or ``'.'`` is given, will save in root directory. ``/`` will be added if not at the end of ``dirs``.
    :type dirs: str

    :param print_msg: whether to print a message after data is saved.
    :type print_msg: bool

|

.. py:function:: data_tools.read_data(dirs)

    .. line-block::
        Reads and returns a model from a directory.

    :param dirs: where the data is saved, should be path of the parent folder of data. ``/`` will be added if not at the end of ``dirs``.
    :type dirs: str

    :return: a model with its parameters and data.
    :rtype: ``piegy.model.simulation`` object

|

Examples
---------

.. line-block::
    We provide some small examples for ``piegy.data_tools`` functions. 

    First please import the ``piegy.data_tools.save_data`` and ``piegy.data_tools.read_data`` functions:

.. code-block:: python

    from piegy.data_tools import save_data, read_data


Assume you ran simulation on ``sim`` variable (``piegy.model.simulation`` object). Then save ``sim`` at ``some_directory`` directory by:

.. code-block:: python

    save_data(sim, 'some_directory')

``some_directory`` will be created if it does not exist.

You can read data by:

.. code-block:: python

    sim2 = read_data('some_directory')

Please pass in the same directory name as you used to save ``sim``.

Note that the data size can be very large. You can reduce size at the expense of losing accuracy by calling ``compress_data`` method of :ref:`piegy.model.simulation <simulation>`
