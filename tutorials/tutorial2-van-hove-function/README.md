# MDANSE Tutorial 2: The van Hove functions

This tutorial will show you:
* how to run an analysis related to the van Hove functions,
* how to plot the results of the analysis

**Questions** will be asked in different sections
of this tutorial. The **answers** will be provided
at the end of the tutorial.

## Background

### Pair distribution function
The pair distribution function (PDF) provides us with some information about 
how atoms are distributed in the system. It tells us what the average 
number of particles will be at a distance $\mathbf{r}$ in volume 
$\mathrm{d}\mathbf{r}$ from an atom.

```math
n_0 g(\mathbf{r}) \mathrm{d}\mathbf{r} = \mathrm{d}N(\mathbf{r})$$
```

Here $n_0$ is the bulk density, $g(\mathbf{r})$ is the PDF and 
$\mathrm{d}N(\mathbf{r})$ is the average number of particles in the 
volume $\mathrm{d}\mathbf{r}$. The PDF is can be written so that it is a 
function of the distance atoms. In this case the pair distribution 
function tells us the average number of particles in the shell volume 
$4 \pi r^2 \mathrm{d}r$ from a distance $r$ of an atom.

```math
n_0 g(r) 4 \pi r^2 \mathrm{d}r = \mathrm{d}N(r)
```

Now the PDF $g(r)$ is a function of distance and 
$\mathrm{d}N(r)$ is the average number of particles in the shell volume 
$\mathrm{d}\mathbf{r}$. The PDF can be written as a sum of delta 
functions. 

```math
n_0 g(r) = \frac{1}{4 \pi r^2} \frac{1}{N} \sum_{k \neq j} \langle \delta (r - \vert \mathbf{r}_k - \mathbf{r}_j \vert) \rangle
```

**Question 1**: Try to derive this equation. Think about what $N(r)$ is 
and therefore what $\mathrm{d}N(r) = N(r + \mathrm{d}r) - N(r)$ should be.

For more details on the PDF see **MDANSE Tutorial 1: a phase transition**.

### The van Hove function

```math
n_0 g(\mathbf{r}) = \frac{1}{N} \sum_{k \neq j} \langle \delta (\mathbf{r} - \mathbf{r}_k - \mathbf{r}_j) \rangle
```

Is the PDF as a function of $\mathbf{r}$, the van Hove function is closely 
related and is also a sum of delta functions.

```math
G(\mathbf{r}, t) = \frac{1}{N} \sum_{k j} \langle \delta (\mathbf{r} - \mathbf{r}_k(t) - \mathbf{r}_j(0)) \rangle
```

The PDF gives use some insights into the structure of our system while 
the van Hove function gives us insights into the structure and dynamics 
of the system. The van Hove function can be split into self and distinct 
parts.

```math
G_{\mathrm{s}}(\mathbf{r}, t) = \frac{1}{N} \sum_{j} \langle \delta (\mathbf{r} - \mathbf{r}_j(t) - \mathbf{r}_j(0)) \rangle
G_{\mathrm{d}}(\mathbf{r}, t) = \frac{1}{N} \sum_{k \neq j} \langle \delta (\mathbf{r} - \mathbf{r}_k(t) - \mathbf{r}_j(0)) \rangle
```

At $t=0$ the distinct-part of the van Hove function is the PDF 
$G_{\mathrm{d}}(\mathbf{r}, 0) = n_0 g(\mathbf{r})$. At other times
the distinct-part of the van Hove function describes distance between 
atom at different times.

![temperature_analysis](pictures/vhd_diagram.png)

The above figure shows the distances (red arrows) that the distinct-part 
of the van Hove function depends on. At $t=0$ the van Hove function is simply 
the PDF. After a some time the blue and green atoms move 
some distance, the distinct-part of the van Hove function depends on the 
distances between atoms at $t=0$ and $t=1$.

![temperature_analysis](pictures/vhs_diagram.png)

The self-part of the van Hove function is closely related to the 
diffusion of a particle. The above figure shows the distances (red arrows) 
that the self-part of the van Hove function depends on. At $t=0$ there 
are no arrows since the distance of at atom with itself is zero so that 
the van Hove function is a delta function 
$G_{\mathrm{s}}(\mathbf{r}, 0) = \delta(\mathbf{r})$. At $t \neq 0$ the 
self-part of the van Hove function depends on distances between atoms 
with itself at different times.

## Scenario of this tutorial

We will analyse a trajectory of liquid argon using the self and 
distinct-parts of the van Hove functions and see how they change as a 
function of time.

# Files

This tutorial contains the following files:

## md_inputs
These are the input files needed to re-run the MD simulation:
* argon_start_structure.txt - a LAMMPS structure file
* argon.lmp - a LAMMPS script

## md_outputs
These are the LAMMPS files:
* argon_traj_120fs_85k.txt - a LAMMPS custom format trajectory

## mdanse_inputs

## mdanse_outputs
All the files created by MDANSE will be written here.

# The actual tutorial, step by step.
In the text of the tutorial, we will concentrate on the
MDANSE GUI. However, the conversion and analysis jobs can
be run also without the GUI. The scripts for running all
the parts of the tutorial are provided in `md_inputs/script*`.

## Convert and load the trajectory
The trajectory in this example has been created using LAMMPS.
The LAMMPS script which produced this trajectory is available
in `md_inputs/argon.lmp` and you will need to open it
to find some information needed to convert the trajectory
correctly.

Go to the 'Converters' tab in the GUI, and pick the LAMMPS
converter. Now you have to pass the correct inputs to the
converter. The LAMMPS configuration file is
`md_inputs/argon_start_structure.txt`, and the LAMMPS trajectory file
is `md_outputs/argon_traj_120fs_85k.txt`. Change the LAMMPS time step to '2',
since this is the value found in the LAMMPS script for this simulation. Use 
the generic output filename `mdanse_outputs/converted_trajectory.mdt`.

![temperature_analysis](pictures/conversion_gui.png)

## Calculate the distinct part of the van Hove function
Select the VanHoveFunctionDistinct job leaving the setting to the 
defaults. To speed the calculation up you may want to swtich the 
running mode to multicore and the number of processes to a number 
greater than 1. Set the outputs file to saving the output
to `mdanse_outputs/vanhovefunctiondistinct.mdt`, hit run and wait 
for the job to complete, you check the running jobs tab to check the 
progress of the job.

![temperature_analysis](pictures/vhd_gui.png)

Once complete the results would load up automatically. Go to the 
plot creator and plot the `g(r,t)_total` result. Go to the plot holder 
and in the dataset table set the `g(r,t)_total` to have a main axis for 
`r` and the Use it? setting to `0,10,20`.

![temperature_analysis](pictures/vhd_plotting_gui.png)

We can see that time advances, the van Hove function begins to flatten 
and the correlation hole around each atom begins to fill up. The 
correlation hole is 

**Question 2**: We calculated the distinct-part of the van Hove 
function for a liquid. What do you think the distinct-part of 
the van Hove function would look like for a solid?

**Question 3**: We know that at $t=0$ that the distinct-part of the van 
Hove function is the PDF. What does the van Hove function become as 
$t \rightarrow infty$ for solid, liquid and gaseous systems?

## Question 1:

```math
n_0 g(\mathbf{r}) 4 \pi r^2 \mathrm{d}r = \mathrm{d}N(r)
```

The function $N(r)$ is a sum of step functions so that $N(r)$
increases by one as $r$ increases each time it comes across an atom on average. 
Therefore, $\mathrm{d}N(r) = N(r + \mathrm{d}r) - N(r)$ and $\mathrm{d}N(r)$ will be the 
average number of particles in the shell volume. The derivative of $N(r)$ will be 
the derivative of the step functions which are delta functions each 
centered on the distances away to another atom.

```math
\frac{\mathrm{d}N(r)}{\mathrm{d}r} = \frac{1}{N} \sum_{k \neq j} \langle \delta (r - \vert \mathbf{r}_k - \mathbf{r}_j \vert) \rangle
```

Where we have written the sum of delta functions inside $\langle \cdot \rangle$ 
so that the positions are thermally averaged and average the thermal average
over all possible atom origins.
