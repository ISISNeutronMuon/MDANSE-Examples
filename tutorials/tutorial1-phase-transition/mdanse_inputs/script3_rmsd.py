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

from MDANSE.Framework.Jobs.IJob import IJob

########################################################
# Job parameters                                       #
########################################################

parameters = {
    "atom_transmutation": "{}",  # atom_transmutation
    "frames": [0, 1000, 1],  # frames
    "grouping_level": "atom",  # grouping_level
    "output_files": (
        "../mdanse_outputs/root_mean_square_displacement",
        ["MDAFormat"],
        "INFO",
    ),  # output_files
    "reference_frame": "0",  # reference_frame
    "running_mode": ("single-core",),  # running_mode
    "trajectory": "../mdanse_outputs/converted_trajectory.mdt",  # trajectory
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    rootmeansquaredeviation = IJob.create("RootMeanSquareDeviation")
    # Progress bars only available if tqdm available.
    # Install with `cli` optional dependency.
    rootmeansquaredeviation.run(parameters, status=True, prog_bar=True)
