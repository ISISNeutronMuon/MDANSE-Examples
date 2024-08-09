#!/usr/bin/env python

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE.Framework.Jobs.IJob import IJob

########################################################
# Job parameters                                       #
########################################################

parameters = {
    'frames': [0, 1000, 1],                             # frames
    'interpolation_order': 3,                           # velocities
    'output_files': ('../mdanse_outputs/temperature', ['MDAFormat'], "INFO"),  # output_files
    'trajectory': '../mdanse_outputs/converted_trajectory.mdt',  # trajectory
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    temperature = IJob.create('Temperature')
    temperature.run(parameters, status=True)
