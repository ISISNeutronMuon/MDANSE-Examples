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
A(t) = \int_{V} \mathrm{d}^3 r\ a(\vec{r}, t)
```
where $a(\vec{r}, t)$ is the local density of this property. The rate 
of change of $A(t)$ over time is
```math
\frac{\mathrm{d} A(t)}{\mathrm{d}t} = - \int_{S} \mathrm{d}\vec{s} \cdot \vec{J}_{a}(\vec{r}, t) + \int_{V} \mathrm{d}^3 r\ \sigma_{a}(\vec{r}, t)
```
where the first integral on the right describes the current flow of $a$ into or
out of the volume $V$ and $\sigma_{a}(\vec{r}, t)$ is a function which describes 
a change in property $a$ due to some internal sink or source of $a$. From 
Gauss' theorem we can change the above surface integral to a volume integral
so that
```math
\int_{V} \mathrm{d}^3 r\ \left[ \frac{\partial a(t)}{\partial t} + \vec{\nabla} \cdot \vec{J}_{a}(\vec{r}, t) - \sigma_{a}(\vec{r}, t) \right] = 0
```
and since the volume $V$ was arbitrary 
```math
\frac{\partial a(\vec{r}, t)}{\partial t} + \vec{\nabla} \cdot \vec{J}_{a}(\vec{r}, t) = \sigma_{a}(\vec{r}, t).
```

To obtain the hydrodynamic equations requires the application of the above conservation 
equation to the properties of mass, momentum, and energy where in all cases
$\sigma_{a}(\vec{r}, t) = 0$ since there will be no sinks or sources of
mass, momentum, or energy in our system. 
```math
\frac{\partial a(\vec{r}, t)}{\partial t} + \vec{\nabla} \cdot \vec{J}_{a}(\vec{r}, t) = 0.
```
Therefore, what remains is to find a form of the current density for mass,
momentum, and energy.
```math
\frac{\partial \rho(\vec{r}, t)}{\partial t} + \vec{\nabla} \cdot (\rho(\vec{r}, t) \vec{v}(\vec{r}, t)) = 0.
\\
\frac{\partial \rho(\vec{r}, t)\vec{v}(\vec{r}, t)}{\partial t} + \vec{\nabla} \cdot \left[ (\rho(\vec{r}, t) \vec{v}(\vec{r}, t)) \otimes \vec{v}(\vec{r}, t)) - \overleftrightarrow{\sigma} \right] = 0.
```


# Further reading
Boon, J. P., Yip, S. (1991). Molecular Hydrodynamics. Dover Publications.

Berne, B. J., Pecora, R. (2000). Dynamic Light Scattering: With Applications to Chemistry, Biology, and Physics. Dover Publications.

Landau, L. D., Lifshitz, E. M. (1959). Fluid Mechanics. Pergamon Press.
