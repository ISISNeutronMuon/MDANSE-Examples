# MDANSE Tutorial 5: Hydrodynamics

This tutorial will show you:
* how to run an analysis related to the coherent scattering

## Background
Tutorials 2 to 4, where built from a microscopic theory of the structure and 
dynamics of a simple fluid by describing our system from a sum of particles. 
However, we can instead begin from macroscopic theory of a continuous fluid and derive, for example, 
the scattering function from the correlation function of density 
fluctuations of the fluid. The derivation of a scattering function from the 
hydrodynamic equations and the derivation of the hydrodynamic equations 
themselves are quite involved. We will provide some of the essential idea 
and equations but a more thorough overview can be found else where, see the 
Further reading section.

To build up a macroscopic theory of a fluid we first require an equation
which describes the conservation of some extensive property such as mass.
Consider an element of a fluid with a fixed volume $V$ and surface $S$ in the bulk,
the property of this element is simply
```math
X(t) = \int_{V} \mathrm{d}V x(\vec{r}, t)
```
where $x(\vec{r}, t)$ is the local density of this property. The rate 
of change of $X(t)$ over time is
```math
\frac{\mathrm{d} X(t)}{\mathrm{d}t} = - \int_{S} \mathrm{}
```

# Further reading
Boon, J. P., Yip, S. (1991). Molecular Hydrodynamics. Dover Publications.

Berne, B. J., Pecora, R. (2000). Dynamic Light Scattering: With Applications to Chemistry, Biology, and Physics. Dover Publications.

Landau, L. D., Lifshitz, E. M. (1959). Fluid Mechanics. Pergamon Press.
