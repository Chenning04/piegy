'''
Payoff-Driven Stochastic Spatial Model for Evolutionary Game Theory
-----------------------------------------------------------

Provides:
    1.  A stochastic model to simulate interaction between two species in a 2D space.
    2.  Plot & video functions to visualize simulation results.
    3.  Test influence of certain variables on results.
    4.  Additional analytical tools.

Technical Details:
    1.  Interaction between two spcies are simulated by a 1x4 payoff matrix, 
        obtained by flattening the canonical 2x2 matrix.
    2.  The random process of picking events is based on Gillespie Algorithm.
    3.  Both 'rates' (weight of events) and time step are continuous, as defined in Gillespie Algorithm.
    4.  Supports both 1D and 2D. For 1D case, please make N = 1. Doesn't support 1x1 spatial dimension.


Last update: Mar 28, 2025
'''


from .model import simulation, run, demo_model
from .videos import make_video, SUPPORTED_FIGURES
from .data_tools import save_data, read_data

from .analysis import rounds_expected, scale_maxtime, check_convergence, combine_sim

from .figures import (UV_heatmap, UV_bar, UV_dyna, UV_hist, UV_std, UV_expected_val, UV_expected, 
                      pi_heatmap, pi_bar, pi_dyna, pi_hist, pi_std, UV_pi)

from .test_var import (test_var1, var_UV1, var_pi1, var_convergence1, get_dirs1, 
                       test_var2, var_UV2, var_pi2, var_convergence2, get_dirs2)


model_members = ['simulation', 'run', 'get_demo_model']

videos_members = ['make_video', 'SUPPORTED_FIGURES']

data_members = ['save_data', 'read_data']

analysis_members = ['expected_rounds', 'scale_maxtime', 'check_convergence', 'combine_sim']

figures_members = ['UV_heatmap', 'UV_bar', 'UV_dyna', 'UV_hist', 'UV_std', 'UV_expected_val', 'UV_expected', 
                   'pi_heatmap', 'pi_bar', 'pi_dyna', 'pi_hist', 'pi_std', 'UV_pi']

test_var_members = ['test_var1', 'var_UV1', 'var_pi1', 'var_convergence1', 'get_dirs1', 
                    'test_var2', 'var_UV2', 'var_pi2', 'var_convergence2', 'get_dirs2']


__all__ = model_members + videos_members + data_members + figures_members + analysis_members + test_var_members







# Below might be better suited for documents
'''
To run a simulation, start by defining some parameter. Here is a complete set of params::

    >>> N = 5
    >>> M = 5
    >>> maxtime = 300
    >>> sim_time = 3
    >>> I = [[[22, 44] for i in range(N)] for j in range(M)]
    >>> X = [[[-0.1, 0.4, 0, 0.2] for i in range(N)] for j in range(M)]
    >>> X[1][1] = [0.1, 0.6, 0.2, 0.4]
    >>> P = [[[0.5, 0.5, 100, 100, 0.001, 0.001] for i in range(N)] for j in range(M)]
    >>> boundary = True
    >>> print_pct = 5
    >>> seed = None

These parameters essentially define the spatial size, initial population, payoff matrices...
For a detailed explanation, see simulation object.

Then create a 'simulation' object with those parameters::

    >>> sim = simulation(N, M, maxtime, sim_time, I, X, P, boundary, print_pct, seed)

This 'sim' object will be the basis of our simulation. It carries all the necessary parameters
and storage bin for the results.

Now let's run the simulation (assuming you imported)::

    >>> multi_test(sim)

And that's the simulation! It takes 30s ~ 1min. You can see the progress.

Now, to see the results, let's use figures::

    >>> fig = UV_heatmap(sim)
    

'''
