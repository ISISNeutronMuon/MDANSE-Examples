#!/usr/bin/env python

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE.Framework.Jobs.IJob import IJob

########################################################
# Job parameters                                       #
########################################################

parameters = {
    'frames': [0, 1001, 1, 31],                         # frames
    'output_files': ('../mdanse_outputs/vanhovefunctionself', ['MDAFormat'], 'INFO'),  # output_files
    'r_values': [0.0, 1.14, 0.01],                      # r values (nm)
    'running_mode': ('single-core',),                   # running_mode
    'trajectory': '../mdanse_outputs/converted_trajectory.mdt',  # trajectory
    'weights': 'equal',                                 # weights
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    vanhovefunctionself = IJob.create('VanHoveFunctionSelf')
    vanhovefunctionself.run(parameters, status=True)
