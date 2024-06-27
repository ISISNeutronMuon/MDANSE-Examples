#!/usr/bin/env python

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE.Framework.Jobs.IJob import IJob

########################################################
# Job parameters                                       #
########################################################

parameters = {
    'atom_aliases': '{"mass=96.0": {"1": "Mo"}}',       # Atom mapping
    'config_file': '../md_inputs/structure.txt',  # LAMMPS configuration file
    'fold': False,                                      # Fold coordinates in to box
    'lammps_units': 'electron',                         # LAMMPS unit system
    'n_steps': '0',                                     # Number of time steps (0 for automatic detection)
    'output_file': ('../mdanse_outputs/converted_trajectory', 32, 'gzip'),  # MDANSE trajectory (filename, format)
    'time_step': '0.2',                                 # Time step (lammps units, depends on unit system)
    'trajectory_file': '../md_outputs/trajectory.txt',  # LAMMPS trajectory file
    'trajectory_format': 'custom',                      # LAMMPS trajectory format
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    lammps = IJob.create('LAMMPS')
    lammps.run(parameters, status=True)
