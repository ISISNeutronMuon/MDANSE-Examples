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
    "frames": [0, 1001, 1, 501],  # frames
    "output_files": (
        "../mdanse_outputs/vanhovefunctiondistinct",
        ["MDAFormat"],
        "INFO",
    ),  # output_files
    "r_values": [0.0, 1.14, 0.01],  # r values (nm)
    "running_mode": ("single-core",),  # running_mode
    "trajectory": "../mdanse_outputs/converted_trajectory.mdt",  # trajectory
    "weights": "equal",  # weights
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    vanhovefunctiondistinct = IJob.create("VanHoveFunctionDistinct")
    # Progress bars only available if tqdm available.
    # Install with `cli` optional dependency.
    vanhovefunctiondistinct.run(parameters, status=True, prog_bar=True)
