# Discussion of the results

## Question 1:

By now it is quite clear that the system in the simulation
started off as a solid, and ended up being a liquid.

## Question 2:

The answer to this problem is in the trajectory sampling
chosen in the LAMMPS script. In this run, LAMMPS was writing
out the positions only every 100 steps, which means that
20 fs of the simulation time would pass between each two
consecutive writeouts. This makes it unlikely that the
reconstruction of the velocities based on the atom positions
could ever succeed.

While it is common practice not to write out every single
simulation step, please be keep in mind that not all the
properties can be accurately reproduced based on the
incomplete trajectory sampling. In the case of the
temperature here, we can simply rely on the simulation
logs.

## Question 3:

Based on the simulation logs, the melting temperature
of molybdenum in this simulation was close to 4200-4300 K.
This is not particularly close to the real-life value of the
molybdenum melting point (which is ca. 2900 K.)

While ultimately it is the force field used in the simulation
that defines what properties can be accurately reproduced,
it is important to remember that a typical MD simulation
is rather short compared to the time scale of real-life
phenomena. Looking at the LAMMPS script for this simulation,
you will notice that the temperature ramp was going
from 2000 to 8000 K within 80 ps. This is an extremely fast
heating rate, and is likely to result in a superheated
system. This is, of course, not a problem that MDANSE
should be dealing with. We just like to remind the users
to be aware of the limitations of the methods they are using.
