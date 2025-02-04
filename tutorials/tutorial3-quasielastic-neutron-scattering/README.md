# MDANSE Tutorial 3: Quasielastic neutron scattering (QENS)

This tutorial will show you:
* how to run an analysis related to the QENS experiements,
* how to plot the results of the analysis

**Questions** will be asked in different sections
of this tutorial. The **answers** will be provided
at the end of the tutorial.

## Background

Quasielastic scattering is a special case of inelastic scattering and leads 
to a broad peak around $\omega = 0$. Incoherent 
QENS can be used to study the diffusion and other similar processes. To understand 
how QENS is related to the diffusion of a particle we can start from the 
self-part of the van Hove function (see **MDANSE Tutorial 2: the van Hove functions**).

The dynamic incoherent structure factor (DISF) can be accessed from neutron scattering 
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
where $G_{\mathrm{s}}(\vec{r}, t)$ is the self-part of the van Hove function which 
describes the probability of a particle at a time $t$ from its initial position 
at a time $0$. $F_{\mathrm{inc}}(\vec{q}, t)$ is the incoherent intermediate scattering 
function, $S_{\mathrm{inc}}(\vec{q}, \omega)$ is the DISF and 
$\vec{q}$ and $\omega$ are the momentum and energy changes of the 
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

There are a number of ways to show how the DISF is related to the 
diffusion constant of a particle. We will start by rewriting the incoherent 
intermediate scattering function so that is an exponential 
of the cumulants of $\vec{d_{j}}(t) = \vec{q} \cdot \[r_{j}(t) - r_{j}(0)\]$ 
which is the displacement of atom $j$ along $\vec{q}$.
```math
F_{\mathrm{inc}}(\vec{q}, t) = \frac{1}{N} \sum_{j} \exp [-\frac{q^2}{2} \langle d^{2}_{j}(t) \rangle + \cdots ]
```
The Gaussian approximation is obtained by taking only the leading term of the 
exponent: $\langle d_{j}^{2}(t) \rangle$ which is the 2nd moment 
of $\vec{d_{j}}(t)$. The 2nd moment is related to 
the mean squared displacement (MSD)
```math
\langle d^{2}_{j}(t) \rangle = \mathrm{MSD}_{j}(t) / 3.
```

Assuming that the atom or molecules undergoes brownian motion, the MSD of 
atom or molecule will be proportional to time
```math
\mathrm{MSD}(t) = 6 D \vert t \vert
```
where $D$ is diffusion constant. So for a monoatomic isotropic system, 
we can rewrite the intermediate scattering function with the Gaussian approximation as 
```math
F_{\mathrm{inc}}(\vec{q}, t) = \exp(- D q^2 \vert t \vert ),
```
Fourier transforming the intermediate scattering function we can obtain 
expression of the van Hove function and the DISF in terms of the diffusion 
constants
```math
G_{\mathrm{s}}(\vec{r}, t) = \left( \frac{1}{4 \pi D \vert t \vert} \right)^{3/2} \exp\left( - \frac{r^2}{4 D \vert t \vert} \right)
```
and
```math
S_{\mathrm{inc}}(\vec{q}, t) = \frac{1}{\pi} \frac{\hbar \Gamma(q) }{(\hbar \omega)^2 + (\hbar \Gamma(q))^2}
```
here $S_{\mathrm{inc}}(\vec{q}, t)$ is a Lorentzian function with a 
half-width at half maximum of $\hbar \gamma(q)$ and $\Gamma(q) = D q^2$.
The diffusion constant of can be obtained from a QENS experiment by measuring 
$\hbar \gamma(q)$ of the QENS peak as a function of $q^2$.

# Further reading
Boothroyd, A. T. (2020). Principles of Neutron Scattering from Condensed Matter. OUP Oxford.

Boon, J. P., Yip, S. (1991). Molecular Hydrodynamics. Dover Publications.
