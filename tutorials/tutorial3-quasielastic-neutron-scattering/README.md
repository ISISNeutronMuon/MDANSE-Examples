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
intermediate scattering function so that it is an exponential 
of the cumulants of $\vec{d_{j}}(t) = \vec{q} \cdot \[r_{j}(t) - r_{j}(0)\]$ 
which is the displacement of atom $j$ along $\vec{q}$.
```math
F_{\mathrm{inc}}(\vec{q}, t) = \frac{1}{N} \sum_{j} \exp [-\frac{q^2}{2} \langle d^{2}_{j}(t) \rangle + \cdots ]
```
The Gaussian approximation is obtained by taking only the leading term of the 
exponent: $\langle d_{j}^{2}(t) \rangle$ which is the 2nd moment 
of $\vec{d_{j}}(t)$. This approximation is exact for a system which undergoes Fickian diffusion 
(normal diffusion) where the MSD is linear in time so that
```math
\langle d^{2}_{j}(t) \rangle = \mathrm{MSD}_{j}(t) = 6 D_{j} \vert t \vert
```
where $D_j$ is diffusion constant of atom $j$, the higher order cumulants are zero. So 
for an isotropic monoatomic system, we can rewrite the intermediate scattering 
function with the Gaussian approximation as 
```math
F_{\mathrm{inc}}(\vec{q}, t) = \exp(- D q^2 \vert t \vert ),
```
Fourier transforming the intermediate scattering function we can obtain 
expression of the van Hove function and the DISF in terms of the diffusion 
constant
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

**Question 1**: Another example where the Gaussian approximation is 
exact is for a system of free particles. What is $\langle d^{2}_{j}(t) \rangle$ for 
this system given that the particles velocities are distributed following 
the Maxwell-Boltzmann distribution? Finally, what is the van Hove function, 
the intermediate scattering function and dynamic structure factor? 


## Scenario of this tutorial

First we will have a look at the differences in the scattering functions 
and dynamic structure factors when the Gaussian approximation is applied 
for a liquid argon system.


# Answers

## Question 1:

For an isotropic system of free particles
```math
\langle d^{2}_{j}(t) \rangle = \frac{1}{3} \langle \vert \vec{r}(t) - \vec{r}(0) \vert^2 \rangle.
```
Given their velocities will follow the Maxwell-Boltzmann distribution,
we must average the displacements over this distribution. By noting that 
$\vert \vec{r}(t) - \vec{r}(0) \vert^2 = (v t)^2$ where $v$ is the speed for a given
particle we can then integrate $(v t)^2$ over the Maxwell-Boltzmann distribution so that
```math
\langle d^{2}_{j}(t) \rangle = \frac{t^2}{3} \int_{0}^{\infty} \mathrm{d}v \, v^2 f(v)
```
where
```math
f(v) = \left( \frac{m}{2\pi k_{\mathrm{B}} T}\right)^{3 / 2} 4 \pi v^2 \exp\left(- \frac{m v^2}{2 k_{\mathrm{B}} T} \right)
```
is the Maxwell-Boltzmann distribution. Solving the above we obtain the following result
```math
\langle d^{2}_{j}(t) \rangle = \frac{1}{2} (v_{\mathrm{p}} t)^2
```
where $v_{\mathrm{p}} = \sqrt{3k_{\mathrm{B}} T / M}$ is the most probable 
speed and $M$ is the mass of the particles.

We can now plug this result into the Gaussian approximation of the intermediate 
function and Fourier transform to obtain the van Hove and dynamic structure 
factor for a system of free particles.
```math
G_{\mathrm{s}}(\vec{r}, t) = \left( \frac{1}{\pi v_{\mathrm{p}^2 t^2} \right)^{3/2} \exp\left[ - \left(\frac{r}{v_{\mathrm{p} t}\right)^2 \right]
```
```math
F_{\mathrm{inc}}(\vec{q}, t) =  \exp\left[ - \frac{1}{2} (q v_{\mathrm{p} t)^2 \right]
```
```math
S_{\mathrm{inc}}(\vec{q}, t) = \frac{1}{\sqrt{2 \pi} q v_{\mathrm{p}} \exp\left[ \frac{1}{2}\left(\frac{\omega}{q v_{\mathrm{p}}\right)^2 \right]
```


# Further reading
Boothroyd, A. T. (2020). Principles of Neutron Scattering from Condensed Matter. OUP Oxford.

Boon, J. P., Yip, S. (1991). Molecular Hydrodynamics. Dover Publications.
