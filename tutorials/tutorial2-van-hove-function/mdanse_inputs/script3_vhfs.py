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
    "frames": [0, 1001, 1, 31],  # frames
    "grouping_level": "atom",  # grouping_level
    "output_files": (
        "../mdanse_outputs/vanhovefunctionself",
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
    vanhovefunctionself = IJob.create("VanHoveFunctionSelf")
    # Progress bars only available if tqdm available.
    # Install with `cli` optional dependency.
    vanhovefunctionself.run(parameters, status=True, prog_bar=True)
