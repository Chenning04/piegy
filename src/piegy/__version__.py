__version__ = '2.2.1'

'''
version history:

0.1.0: first publishing, May 11, 2025
0.1.1: fix dependency errors
0.1.2: fixing module not find error
0.1.3: restructuring package
0.1.4 ~ 0.1.6: fixing moviepy import issue
0.1.7: changed name back to 'piegy'
0.1.8: updated installation in README
0.1.9: first round of full debugging

1.0.0: first version in PyPI.
1.1.0: debugging. Updated a range of functions, in the following modules: figures, videos, test_var, model, figure_tools
1.1.1: minor debugging in model module.
1.1.2: fix text bad location in figure_tools, update labeling and titling in figures and test_var. Add dpi param to make_video in videos. Remove reset_data function in model.
1.1.3: update README.
1.1.4: changed name: ``model`` module to ``simulation``, and ``model.simulation`` class to ``simulation.model``. Bug fix in videos.
1.1.5: update README.
1.1.6: change name of variables in model class -- for compatability with the new C core. 1.1.6 is the last verion of v1. From v2 on, the piegy package has C core.

2.0.0: update simulation core to C-based.
2.0.1: re-upload, the C core is not included in package.
2.0.2: update version number in __version__.py and update README.
2.0.3: speed boost & debugging in C core. Add check_overflow feature in simulation module, checks whether overflow/too large numbers might be encountered in simulation.
2.0.4: minor debuggings.
2.0.5: fix error in random number generator.
2.1.0: redo random number generator. Update package upload so that more compatible across platforms.
2.1.1: fix import bug for the C core.
2.1.2 ~ 2.1.9: updating & fixing wheel.
2.1.10: fix print bug in run function.
2.1.11: fix .so duplicate error.
2.2.1: change heatmap plotting tool from Seaborn to Matplotlib. Change video maker to cv2 (opencv-python).
'''