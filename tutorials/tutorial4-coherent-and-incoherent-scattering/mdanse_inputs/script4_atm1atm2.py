from MDANSE.Chemistry import ATOMS_DATABASE
from MDANSE.Framework.Jobs.IJob import IJob

# Create the custom atom types
if "Atm1Atm2" not in ATOMS_DATABASE.atoms:
    ATOMS_DATABASE.add_atom("Atm1Atm2")
ATOMS_DATABASE.set_value("Atm1Atm2", "b_coherent", 5.5)
ATOMS_DATABASE.set_value("Atm1Atm2", "b_incoherent", 4.5)
ATOMS_DATABASE.set_value("Atm1Atm2", "color", "0;0;255")
ATOMS_DATABASE.set_value("Atm1Atm2", "vdw_radius", 0.188)
# uncomment the line below if you wish to save Atm1Atm2 to your
# local atom database
# ATOMS_DATABASE.save()


# Generate a mapping which transmutes all atoms to Atm1Atm2
mapping = {str(i): "Atm1Atm2" for i in range(256)}

# setup to parameters to run the trajectory editor.
parameters = {
    'atom_charges': '{}',                               # atom_charges
    'atom_selection': '{}',                             # atom_selection
    'atom_transmutation': str(mapping).replace("'", '"'),  # atom_transmutation
    'frames': [0, 1001, 1],                             # frames
    'molecule_tolerance': [False, 0.04],                # molecule_tolerance
    'output_files': ('../mdanse_outputs/converted_atm1atm2', 64, 128, 'gzip', 'INFO'),  # MDANSE trajectory (filename, format)
    'trajectory': '../mdanse_outputs/converted_trajectory.mdt',  # trajectory
}


if __name__ == "__main__":
    trajectoryeditor = IJob.create('TrajectoryEditor')
    trajectoryeditor.run(parameters, status=True)
