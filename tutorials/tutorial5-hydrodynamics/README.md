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
X(t) = \int_{V} \mathrm{d}^3 r x(\vec{r}, t)
```
where $x(\vec{r}, t)$ is the local density of this property. The rate 
of change of $X(t)$ over time is
```math
\frac{\mathrm{d} X(t)}{\mathrm{d}t} = - \int_{S} \mathrm{d}\vec{s} \cdot \vec{J}(\vec{r}, t) + \int_{V} \mathrm{d}^3 r \sigma_{x}(\vec{r}, t)
```
where the first integral on the right describes the current flow of $x$ into or
out of the volume $V$ and $\sigma_{x}(\vec{r}, t)$ is a function which describes 
a change in property $x$ due to some internal sink or source of $x$. From 
Gauss' theorem we can change the above surface integral to a volume integral
so that
```math
\int_{V} \mathrm{d}^3 r \left[ \frac{\partial x(t)}{\partial t} + \vec{\nabla} \cdot \vec{J}(\vec{r}, t) - \sigma_{x}(\vec{r}, t) \right] = 0
```
and since the volume $V$ was arbitrary 
```math
\frac{\partial x(t)}{\partial t} + \vec{\nabla} \cdot \vec{J}(\vec{r}, t) = \sigma_{x}(\vec{r}, t).
```


# Further reading
Boon, J. P., Yip, S. (1991). Molecular Hydrodynamics. Dover Publications.

Berne, B. J., Pecora, R. (2000). Dynamic Light Scattering: With Applications to Chemistry, Biology, and Physics. Dover Publications.

Landau, L. D., Lifshitz, E. M. (1959). Fluid Mechanics. Pergamon Press.
