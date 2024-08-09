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
    'frames': [0, 500, 1],                              # frames
    'output_files': ('../mdanse_outputs/pair_distribution_function_solid', ['MDAFormat'], "INFO"),  # output_files
    'r_values': [0.0, 1.32, 0.01],                      # r values (nm)
    'running_mode': ('single-core',),                   # running_mode
    'trajectory': '../mdanse_outputs/converted_trajectory.mdt',  # trajectory
    'weights': 'equal',                                 # weights
}


########################################################
# Setup and run the analysis                           #
########################################################

inputs = [([0,200,1], '../mdanse_outputs/pair_distribution_function_solid'),
          ([700,900,1], '../mdanse_outputs/pair_distribution_function_liquid'),]

if __name__ == "__main__":
    for inp in inputs:
        parameters['frames'] = inp[0]
        parameters['output_files'] = (inp[1], ['MDAFormat'], "INFO")
        pairdistributionfunction = IJob.create('PairDistributionFunction')
        pairdistributionfunction.run(parameters, status=True)
