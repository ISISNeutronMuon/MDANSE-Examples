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
    "frames": [0, 1000, 1],  # frames
    "interpolation_order": 3,  # velocities
    "output_files": (
        "../mdanse_outputs/temperature",
        ["MDAFormat"],
        "INFO",
    ),  # output_files
    "trajectory": "../mdanse_outputs/converted_trajectory.mdt",  # trajectory
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    temperature = IJob.create("Temperature")
    # Progress bars only available if tqdm available.
    # Install with `cli` optional dependency.
    temperature.run(parameters, status=True, prog_bar=True)
