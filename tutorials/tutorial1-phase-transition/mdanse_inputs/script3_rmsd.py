#!/usr/bin/env python

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE.Framework.Jobs.IJob import IJob

########################################################
# Job parameters                                       #
########################################################

parameters = {
    'atom_selection': '{"all": true}',                  # atom_selection
    'atom_transmutation': '{}',                         # atom_transmutation
    'frames': [0, 1000, 1],                             # frames
    'grouping_level': 'atom',                           # grouping_level
    'output_files': ('../mdanse_outputs/root_mean_square_displacement', ['MDAFormat']),  # output_files
    'reference_frame': '0',                             # reference_frame
    'running_mode': ('single-core',),                   # running_mode
    'trajectory': '../mdanse_outputs/converted_trajectory.mdt',  # trajectory
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    rootmeansquaredeviation = IJob.create('RootMeanSquareDeviation')
    rootmeansquaredeviation.run(parameters, status=True)
