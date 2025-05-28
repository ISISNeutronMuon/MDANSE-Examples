#!/usr/bin/env python

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE.Framework.Jobs.IJob import IJob

########################################################
# Job parameters                                       #
########################################################

parameters_atm1_atm2 = {
    'atom_transmutation': '{}',                         # atom_transmutation
    'frames': [0, 1001, 1, 501],                        # frames
    'grouping_level': 'atom',                           # grouping_level
    'instrument_resolution': ('ideal', {}),             # instrument_resolution
    'output_files': ('../mdanse_outputs/disf_atm1_atm2.mda', ['MDAFormat'], 'INFO'),  # output_files
    'projection': ('NullProjector', []),                # project coordinates
    'q_vectors': ('SphericalLatticeQVectors', {'seed': 1, 'shells': [10.0, 44.0, 2.0], 'n_vectors': 100, 'width': 0.2}),  # q_vectors
    'running_mode': ('single-core',),                   # running_mode
    'trajectory': '../mdanse_outputs/converted_atm1_atm2.mdt',  # trajectory
    'weights': 'b_incoherent2',                                 # weights
}
parameters_atm1atm2 = {
    'atom_transmutation': '{}',                         # atom_transmutation
    'frames': [0, 1001, 1, 501],                        # frames
    'grouping_level': 'atom',                           # grouping_level
    'instrument_resolution': ('ideal', {}),             # instrument_resolution
    'output_files': ('../mdanse_outputs/disf_atm1atm2.mda', ['MDAFormat'], 'INFO'),  # output_files
    'projection': ('NullProjector', []),                # project coordinates
    'q_vectors': ('SphericalLatticeQVectors', {'seed': 1, 'shells': [10.0, 44.0, 2.0], 'n_vectors': 100, 'width': 0.2}),  # q_vectors
    'running_mode': ('single-core',),                   # running_mode
    'trajectory': '../mdanse_outputs/converted_atm1atm2.mdt',  # trajectory
    'weights': 'b_incoherent2',                                 # weights
}


########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    dynamicincoherentstructurefactor = IJob.create('DynamicIncoherentStructureFactor')
    dynamicincoherentstructurefactor.run(parameters_atm1_atm2, status=True)
    dynamicincoherentstructurefactor = IJob.create('DynamicIncoherentStructureFactor')
    dynamicincoherentstructurefactor.run(parameters_atm1atm2, status=True)
