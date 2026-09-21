#!C:\Users\xcb63893\AppData\Local\miniconda3\envs\MDANSE3\pythonw.exe

import os
os.environ.update(
    OMP_NUM_THREADS = '1',
    OPENBLAS_NUM_THREADS = '1',
    MKL_NUM_THREADS = '1',
    VECLIB_MAXIMUM_THREADS = '1',
    NUMEXPR_NUM_THREADS = '1'
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
        "../mdanse_outputs/dynamiccoherentstructurefactor.mda",
        ["MDAFormat"],
        "INFO",
    ),  # output_files
    "projection": ("NullProjector", []),  # project coordinates
    "q_vectors": (
        "SphericalLatticeQVectors",
        {
            "force_equal_weights": False,
            "n_samples": 100000,
            "n_vectors": 100,
            "seed": 1,
            "shells": [1.0, 25.0, 1.0],
            "width": 0.8
        },
    ),  # q_vectors
    "running_mode": ("single-core",),  # running_mode
    "trajectory": "../mdanse_outputs/converted_trajectory.mdt",  # trajectory
    'weights': 'b_coherent',  # Weights. Atom property selected here will be used for calculating the scaling factors of the results.
}

########################################################
# Setup and run the analysis                           #
########################################################

if __name__ == "__main__":
    dynamiccoherentstructurefactor = IJob.create("DynamicCoherentStructureFactor")
    # Progress bars only available if tqdm available.
    # Install with `cli` optional dependency.
    dynamiccoherentstructurefactor.run(parameters, status=True, prog_bar=True)
