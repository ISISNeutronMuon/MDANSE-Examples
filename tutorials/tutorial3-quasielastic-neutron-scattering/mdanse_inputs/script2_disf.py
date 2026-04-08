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
    "frames": [0, 1001, 1, 501],  # frames
    "grouping_level": "atom",  # grouping_level
    "instrument_resolution": ("ideal", {}),  # instrument_resolution
    "output_files": (
        "../mdanse_outputs/dynamicincoherentstructurefactor.mda",
        ["MDAFormat"],
        "INFO",
    ),  # output_files
    "projection": ("NullProjector", []),  # project coordinates
    "q_vectors": (
        "SphericalQVectors",
        {
            "seed": 0,
            "shells": [10.0, 44.0, 2.0],
            "n_vectors": 1000,
            "width": 0.0,
        },
    ),  # q_vectors
    "running_mode": ("single-core",),  # running_mode
    "trajectory": "../mdanse_outputs/converted_trajectory.mdt",  # trajectory
    "weights": "equal",  # weights
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    dynamicincoherentstructurefactor = IJob.create("DynamicIncoherentStructureFactor")
    # Progress bars only available if tqdm available.
    # Install with `cli` optional dependency.
    dynamicincoherentstructurefactor.run(parameters, status=True, prog_bar=True)
