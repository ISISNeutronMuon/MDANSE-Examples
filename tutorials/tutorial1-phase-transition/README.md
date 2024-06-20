## MDANSE Tutorial: finding a phase transition

This tutorial will show you:
* how to convert a LAMMPS trajectory to the MDANSE format,
* how to run an analysis on the converted trajectory,
* how to plot the results of the analysis.

# Background

Most of the commonly taught thermodynamics and mechanical
statistics deals with equilibrium processes. That is,
the underlying assumption of most analysis types in MDANSE
is that the average quantities calculated for the simulated
system are constant.

In an MD simulation, the equilibrium state of the studied
system is not guaranteed. As the duration of a simulation
increases, it is possible that the simulated system
will undergo a transition to a qualitatively different state.
For this reason, it is important to verify the stability
of a trajectory.

# Scenario of this tutorial

We will analyse a trajectory of metallic molydenum. This
trajectory is blatantly not equilibrated, as the thermostat
used here was intrioducing a temperature ramp.

## Files

This tutorial contains the following files:

# md_inputs
These are the input files needed to re-run the MD simulation:
* structure.txt - a LAMMPS structure file
* molybdenum_script.lmp - a LAMMPS script 
* Mo5.2.mgpt.potin - a LAMMPS potential file
* Mo5.2.mgpt.parmin - a LAMMPS potential file

# md_outputs
These are the _trimmed_ output files:
* trajectory.txt - a LAMMPS custom format trajectory
* simulation_log.txt - part of LAMMPS log output (thermostat)

## Steps to follow

# Convert the trajectory



# 
