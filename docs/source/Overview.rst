.. _Overview:

Overview
====================

This section provides an overview of the ``piegy`` package, including the fundamental model design, explanation of parameters, and runtime analysis.

Model Design
------------------

Our model can be summarized as "classical game theory endowed with a spatial structure and payoff-driven migration rules". 
Consider two species, predators and preys (denote by *U* and *V*), in a rectangular region. 
We divide the region into N by M patches and simulate their interaction within a patch by classical game theory (i.e., payoff matrices and carrying capacity). 
Interactions across patches are simulated by payoff-driven migration rules. An individual migrates to a neighboring patch with probability weighted by payoff in the neighbors.

We use the Gillepie algorithm as the fundamental event-selection algorithm. 
At each time step, one event is selected and let happen; and step sizes are continuous, dependent on the current state in the space. 
Data are recorded every some specified time interval.

Parameters
----------------

A ``piegy`` model consists of four parts: spatial structure, interaction within a patch, migration rules, and supportive parameters.

Spatial structure is determined by dimension and boundary condition. ``N`` and ``M`` count the number of rows and columns in the space, larger ``N``, ``M`` values mean larger space. 
The ``boundary`` parameter decides boundary condition, set ``boundary = True`` for zero-flux boundary condition ("with boundary") and set to ``False`` for periodical ("without boundary").

Species interaction within a patch is given by payoff matrix and carrying capacity. Payoff matrix measures the utility a individual gains through interaction with others. 
Carrying capacity (:math:`\kappa`) restricts population growth. Our model supports different payoff matrices and carrying capacity for different patches.

Migration rules consist of two parts: tendency of migration (:math:`\mu`) and sensitivity to payoff (:math:`w`). 
They decide how frequent migration events happen and to what extent the desination is biased by payoff.

There are also several supportive parameters on the technical side, such as data types, the time interval to record data, etc.

.. _runtime:

Runtime
----------------

The simulations are computationally intensive. 
For example, in our :ref:`demo model<demo_params>`, there are around 230,000 time steps in total and the total number of operations is at the level of millions.
We're doing our best to maximize speed: the current model is about 600 times faster than our initial implementation. There might still be room for further speed boost.

There are two major sources for runtime: size of model and parameters. It's easy to see larger models (i.e. larger spatial dimension and ``maxtime``) take longer runtime.
As for the parameters, larger values of :math:`\mu` and payoff matrix, smaller values of :math:`\kappa` would result in longer runtime. 

These parameters are related to the size of time step in our fundamental algorithm, 
and change of their values would result in more time steps and hence longer runtime, even if spatial dimension and ``maxtime`` are fixed.

