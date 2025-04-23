import random
from MDANSE.Chemistry import ATOMS_DATABASE
from MDANSE.Framework.Jobs.IJob import IJob

# Create the custom atom types
if "Atm1" not in ATOMS_DATABASE.atoms:
    ATOMS_DATABASE.add_atom("Atm1")
if "Atm2" not in ATOMS_DATABASE.atoms:
    ATOMS_DATABASE.add_atom("Atm2")
ATOMS_DATABASE.set_value("Atm1", "b_coherent", 1e-5)
ATOMS_DATABASE.set_value("Atm1", "b_incoherent2", 0.0)
ATOMS_DATABASE.set_value("Atm1", "color", "255;0;0")
ATOMS_DATABASE.set_value("Atm1", "vdw_radius", 0.188)
ATOMS_DATABASE.set_value("Atm2", "b_coherent", 1e-4)
ATOMS_DATABASE.set_value("Atm2", "b_incoherent2", 0.0)
ATOMS_DATABASE.set_value("Atm2", "color", "247;0;255")
ATOMS_DATABASE.set_value("Atm2", "vdw_radius", 0.188)
# uncomment the line below if you wish to save Atm1 and Atm2 to your
# local atom database
# ATOMS_DATABASE.save()


# Generate a mapping which transmutes the atoms in the trajectory to
# Atm1 or Atm2 randomly.
isotopes = ["Atm1"] * 128 + ["Atm2"] * 128
mapping = {}
for i in range(256):
    random_element = random.choice(isotopes)
    isotopes.remove(random_element)
    mapping[str(i)] = random_element


# setup to parameters to run the trajectory editor.
parameters = {
    'atom_charges': '{}',                               # atom_charges
    'atom_selection': '{}',                             # atom_selection
    'atom_transmutation': str(mapping).replace("'", '"'),  # atom_transmutation
    'frames': [0, 1001, 1],                             # frames
    'molecule_tolerance': [False, 0.04],                # molecule_tolerance
    'output_files': ('../mdanse_outputs/converted_atm1_atm2', 64, 128, 'gzip', 'INFO'),  # MDANSE trajectory (filename, format)
    'trajectory': '../mdanse_outputs/converted_trajectory.mdt',  # trajectory
}


if __name__ == "__main__":
    trajectoryeditor = IJob.create('TrajectoryEditor')
    trajectoryeditor.run(parameters, status=True)
