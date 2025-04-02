# MDANSE Tutorial 4: Coherent and Incoherent Scattering

This tutorial will show you:
* how to run an analysis related to the coherent and incoherent scattering,

**Questions** will be asked in different sections
of this tutorial. The **answers** will be provided
at the end of the tutorial. We recommend completing 
**MDANSE Tutorial 3: Quasielastic neutron scattering (QENS)** before starting this one.

## Background

### Spin Incoherence

In MDANSE the separations of the coherent and incoherent parts of the 
neutron scattering functions are defined by how the `b_coherent` and 
`b_incoherent2` properties for the atom types are specified. There are 
four default hydrogen atom types that can be used; the three isotopes 
H1, H2 and H3, and H which is an atom type with scattering lengths which 
depend on the natural abundances of the three isotopes. 

| Atom Type | $b_{\mathrm{coh}}$ / nm  | $b_{\mathrm{inc}}^2$ / nm$^2$ |
|-----------|--------------------------|-------------------------------|
| H1        | $-3.7406 \times 10^{-5}$ | $6.3878 \times 10^{-8}$       |
| H2        | $6.671 \times 10^{-5}$   | $1.6322 \times 10^{-9}$       |
| H3        | $4.792 \times 10^{-5}$   | $1.0816 \times 10^{-10}$      |
| H         | $-3.739 \times 10^{-5}$  | $6.3869 \times 10^{-8}$       |

For the isotopes H1, H2, and H3, $b_{\mathrm{coh}}$ and $b_{\mathrm{inc}}^2$ depend on 
their $b_{-}$ and $b_{+}$, and $p_{-}$ and $p_{+}$ values, which are the scattering lengths 
and occupation probabilities for the combined neutron plus nucleus system with 
spins $I-\frac{1}{2}$ and $I+\frac{1}{2}$. For example, H1 has a spin of $I = \frac{1}{2}$
and combined spin with the neutron of 0 and 1 with degeneracies of 1 and 3. The measured 
scattering lengths are $b_{-,\text{H1}} = -47.5 \times 10^{-5}$ and $b_{+,\text{H1}} = 10.85 \times 10^{-5}$. 
Therefore, the coherent and the squared incoherent scattering length will be

```math
b_{\mathrm{coh,H1}} = \frac{1}{4} (-47.5 \times 10^{-5}) + \frac{3}{4} (10.85 \times 10^{-5}) = -3.7406 \times 10^{-5}
```

and

```math
b_{\mathrm{inc,H1}}^2 = \frac{1}{4} (-47.5 \times 10^{-5})^2 + \frac{3}{4} (10.85 \times 10^{-5})^2 - b_{\mathrm{coh,H1}}^2  = 6.3878 \times 10^{-8}.
```

### Isotopic Incoherence

Let's compare the scattering lengths of hydrogen with argon.

| Atom Type | $b_{\mathrm{coh}}$ / nm | $b_{\mathrm{inc}}^2$ / nm$^2$ |
|-----------|-------------------------|-------------------------------|
| Ar36      | $24.9 \times 10^{-5}$   | $0.0$                         |
| Ar38      | $3.5 \times 10^{-5}$    | $0.0$                         |
| Ar40      | $1.83 \times 10^{-5}$   | $0.0$                         |
| Ar        | $1.909 \times 10^{-5}$  | $1.7956 \times 10^{-10}$      |

These isotopes all have zero spin nuclei which lead to zero 
$b_{\mathrm{inc}}^2$ values. Unlike the hydrogen atoms, there will be no
contribution to the incoherent scattering from spin incoherence. The $b_{\mathrm{inc}}^2$ 
for the Ar atom type arises from isotopic incoherence. By using the Ar 
atom type we specify to MDANSE that the isotopes of argon in our system 
are randomly distributed and follow their natural abundances.

Therefore, when we use the atom types which are not specific isotopes 
(e.g. H and Ar) the contribution to $b_{\mathrm{inc}}^2$ from spin and 
isotopic incoherence is made.
