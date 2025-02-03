# MDANSE Tutorial 3: quasielastic neutron scattering (QENS)

This tutorial will show you:
* how to run an analysis related to the QENS experiements,
* how to plot the results of the analysis

**Questions** will be asked in different sections
of this tutorial. The **answers** will be provided
at the end of the tutorial.

## Background

### Diffusion
Quasielastic scattering is a special case of inelastic scattering and leads 
to a broad peak around $\omega = 0$. Incoherent 
QENS can be used to study the diffusion and other similar processes. To understand 
how QENS is related to the diffusion of a particle we can start from the 
self-part of the van Hove function (see **MDANSE Tutorial 2: the van Hove functions**).

The self dynamic structure factor can be accessed from neutron scattering 
experiments and is related to the van Hove function via Fourier transforms

```math
G_{\mathrm{s}}(\vec{r}, t) = \frac{1}{N} \sum_{j} \langle \delta (\vec{r} - \vec{r}_j(t) - \vec{r}_j(0)) \rangle
```
```math
F_{\mathrm{inc}}(\vec{q}, t) = \int \mathrm{d}\vec{r} \, G_{\mathrm{s}}(\vec{r}, t) \exp(-i\vec{q} \cdot \vec{r})
```
```math
S_{\mathrm{inc}}(\vec{q}, \omega) = \frac{1}{2 \pi}\int \mathrm{d}\omega \, F_{\mathrm{inc}}(\vec{q}, t) \exp(i \omega t)
```
This $G_{\mathrm{s}}(\vec{r}, t)$ is the self-part of the van Hove function which 
describes the probability of a particle at a time $t$ from its initial position 
at a time $0$. $F_{\mathrm{inc}}(\vec{q}, t)$ is the self intermediate scattering 
function, $S_{\mathrm{inc}}(\vec{q}, \omega)$ is the self dynamic structure 
factor and $\vec{q}$ and $\omega$ are the momentum and energy changes of the 
neutron after the scattering event respectively. If a neutron 
has an initial and final momentum of $\vec{k_{\mathrm{i}}}$ and $\vec{k_{\mathrm{f}}}$ 
with an initial and final energy of $E_{\mathrm{i}}$ and $E_{\mathrm{f}}$
then

```math
\vec{q} = \vec{k}_{\mathrm{i}} - \vec{k}_{\mathrm{f}}
```
and
```math
\hbar \omega = E_{\mathrm{i}} - E_{\mathrm{f}}.
```

There are a number of ways to show how the self dynamic structure 
factor is related to the diffusion constant of a particle. We will start 
by rewriting the self intermediate scattering function so that is an exponential 
of a series of cumulants of $\vec{d_{j}}(t) = \vec{q} \cdot \[r_{j}(t) - r_{j}(0)\]$ 
which is the displacement of atom $j$ after a time $t$ along the vector $\vec{q}$.
```math
F_{\mathrm{inc}}(\vec{q}, t) = \frac{1}{N} \sum_{j} \exp [-\frac{q^2}{2} \langle d^{2}_{j}(t) \rangle + \cdots ]
```
The Gaussian approximation is obtained by taking only the leading term of the 
exponent: $\langle d_{j}^{2}(t) \rangle$ which is the 2nd moment 
of $\vec{d_{j}}(t)$. For an isotropic system, 2nd moment is related to 
the mean squared displacement (MSD) of the atom $j$ and diffusion constant.
```math
\langle d^{2}_{j}(t) \rangle = 3 \mathrm{MSD}_{j}(t) = 2 D_{j} \vert t \vert
```
We therefore can rewrite the intermediate scattering function with the 
Gaussian approximation for isotropic systems as



# Further reading
Boothroyd, A. T. (2020). Principles of Neutron Scattering from Condensed Matter. 
United Kingdom: OUP Oxford.
Boon, J. P., Yip, S. (1991). Molecular Hydrodynamics. United Kingdom: Dover Publications.
