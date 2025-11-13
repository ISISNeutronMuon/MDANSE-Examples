#!/usr/bin/env python

import os

os.environ.update(
    OMP_NUM_THREADS="1",
    OPENBLAS_NUM_THREADS="1",
    MKL_NUM_THREADS="1",
    VECLIB_MAXIMUM_THREADS="1",
    NUMEXPR_NUM_THREADS="1",
)

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE.Framework.Converters.Converter import Converter

########################################################
# Job parameters                                       #
########################################################

parameters = {
    "atom_aliases": '{"mass=36.0": {"1": "Ar36"}}',  # Atom mapping
    "config_file": "../md_inputs/argon_start_structure.txt",  # LAMMPS configuration file
    "fold": False,  # Fold coordinates in to box
    "lammps_units": "real",  # LAMMPS unit system
    "n_steps": "0",  # Number of time steps (0 for automatic detection)
    "output_files": (
        "../mdanse_outputs/converted_trajectory",
        64,
        128,
        "gzip",
        "INFO",
    ),  # MDANSE trajectory (filename, datatype, chunk size, compression, logfile output)
    "time_step": "2.0",  # Time step (lammps units, depends on unit system)
    "trajectory_file": "../md_outputs/argon_traj_120fs_85k.txt",  # LAMMPS trajectory file
    "trajectory_format": "custom",  # LAMMPS trajectory format
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    lammps = Converter.create("LAMMPS")
    # Progress bars only available if tqdm available.
    # Install with `cli` optional dependency.
    lammps.run(parameters, status=True, prog_bar=True)
