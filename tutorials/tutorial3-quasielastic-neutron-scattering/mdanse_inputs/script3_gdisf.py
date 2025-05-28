#!/usr/bin/env python

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE.Framework.Jobs.IJob import IJob

########################################################
# Job parameters                                       #
########################################################

parameters = {
    'atom_transmutation': '{}',                         # atom_transmutation
    'frames': [0, 1001, 1, 501],                        # frames
    'grouping_level': 'atom',                           # grouping_level
    'instrument_resolution': ('ideal', {}),             # instrument_resolution
    'output_files': ('../mdanse_outputs/gaussiandynamicincoherentstructurefactor.mda', ['MDAFormat'], 'INFO'),  # output_files
    'projection': ('NullProjector', []),                # project coordinates
    'q_shells': [10.0, 44.0, 2.0],                      # q_shells
    'running_mode': ('single-core',),                   # running_mode
    'trajectory': '../mdanse_outputs/converted_trajectory.mdt',  # trajectory
    'weights': 'equal',                                 # weights
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    gaussiandynamicincoherentstructurefactor = IJob.create('GaussianDynamicIncoherentStructureFactor')
    gaussiandynamicincoherentstructurefactor.run(parameters, status=True)
