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

| Atom Type | $b_{\mathrm{coh}}$ / nm  | $b_{\mathrm{inc}}^2$ / nm<sup>2</sup> |
|-----------|--------------------------|---------------------------------------|
| H1        | $-3.7406 \times 10^{-5}$ | $6.3878 \times 10^{-8}$               |
| H2        | $6.671 \times 10^{-5}$   | $1.6322 \times 10^{-9}$               |
| H3        | $4.792 \times 10^{-5}$   | $1.0816 \times 10^{-10}$              |
| H         | $-3.739 \times 10^{-5}$  | $6.3869 \times 10^{-8}$               |

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

| Atom Type | $b_{\mathrm{coh}}$ / nm | $b_{\mathrm{inc}}^2$ / nm<sup>2</sup> |
|-----------|-------------------------|---------------------------------------|
| Ar36      | $24.9 \times 10^{-5}$   | $0.0$                                 |
| Ar38      | $3.5 \times 10^{-5}$    | $0.0$                                 |
| Ar40      | $1.83 \times 10^{-5}$   | $0.0$                                 |
| Ar        | $1.909 \times 10^{-5}$  | $1.7956 \times 10^{-10}$              |

These isotopes all have zero spin nuclei which lead to zero 
$b_{\mathrm{inc}}^2$ values. Unlike the hydrogen atoms, there will be no
contribution to the incoherent scattering from spin incoherence. The $b_{\mathrm{inc}}^2$ 
for the Ar atom type arises from isotopic incoherence. The natural abundances
of the argon isotopes are 0.337%, 0.063%, and 99.6% for the Ar36, Ar38, and Ar40 
isotopes respectively, the coherent and the squared incoherent scattering length
of Ar is 

```math
b_{\mathrm{coh,Ar}} = 0.00337 (24.9 \times 10^{-5}) + 0.00063 (3.5 \times 10^{-5}) + 0.996 (1.83 \times 10^{-5}) = 1.909 \times 10^{-5}
```

and

```math
b_{\mathrm{inc,Ar}}^2 = 0.00337 (24.9 \times 10^{-5})^2 + 0.00063 (3.5 \times 10^{-5})^2 + 0.996 (1.83 \times 10^{-5})^2 - b_{\mathrm{coh,Ar}}^2  = 1.7956 \times 10^{-10}.
```

By using the Ar atom type we specify to MDANSE that the isotopes of argon 
in our system are randomly distributed and follow their natural abundances. 
When we use the atom types which are not specific isotopes 
(e.g. H and Ar) the contribution to $b_{\mathrm{inc}}^2$ from spin and 
isotopic incoherence is made.


### Chemical Incoherence

Incoherent scattering can arise from a system when two or more atoms with 
different scattering lengths which share similar trajectories and distributions 
across the system. Incoherent scattering from this source of randomness 
is known as *chemical incoherence* and is dependent on the system. Chemical 
incoherence is included in MDANSE but will turn up in the coherent signal,
(dynamic coherent structure factor) rather than the incohoerent (dynamic 
incoherent structure factor).

## Scenario of this tutorial

Using MDANSE we will create three new atom types (`Atm1`, `Atm2`, and `Atm1Atm2`), 
`Atm1Atm2` will be a combined atom type of Atm1 and Atm2. We will calculate 
the dynamic coherent structure factor (DCSF) and dynamic 
incoherent structure factor (DISF) for a 50/50 mixture of At1 and At2 
and a system of 100% Atm1Atm2. We will then combine the DCSF and DISF 
results using the neutron total dynamic structure factor (NTDSF) job.
We will them compare the coherent and incoherent signal between the two 
systems.

# Files

This tutorial contains the following files:

## mdanse_inputs
These are the scripts that, when run from the mdanse_inputs
directory, will produce the outputs of the mdanse runs
described in this tutorial.
* 

## mdanse_outputs
All the files created by MDANSE will be written here. We included some 
precalculated results using a longer Argon trajectory.
* 


# The actual tutorial, step by step.
In the text of the tutorial, we will concentrate on the
MDANSE GUI. However, the conversion and analysis jobs can
be run also without the GUI. The scripts for running all
the parts of the tutorial are provided in `md_inputs/script*`.


## Convert, edit and load the trajectory
This tutorial will use by using the trajectory files from tutorial 2, 
see **MDANSE Tutorial 2: the van Hove functions** for details. Alternatively 
use the `mdanse_inputs/script1_conversion.py` script, the converted 
trajectory will be in `mdanse_outputs/converted_trajectory.mdt`. This 
trajectory will be a trajectory containing Ar36 atom types. For this 
tutorial we will need to create two new trajectories from the argon one.

First lets create `Atm1`, `Atm2`, and `Atm1Atm2` atom types. Click the MDANSE 
Chemical Elements Database Editor button (next to the periodic table button) 
to load up the editor. Right-click on the table and add three new atoms 
`Atm1`, `Atm2`, and `Atm1Atm2`. Then set the `b_coherent` and `b_incoherent2`
properties as shown in the screenshot below.

<p align="center">
    <img width="800" src="pictures/atom_editor.png"/>
</p>

We defined `Atm1Atm2` to be formed from a 50/50 mixture of Atm1 and Atm2 
so that 

```math
b_{\mathrm{coh,Atm1Atm2}} = 0.5 (1 \times 10^{-5}) + 0.5 (2 \times 10^{-5}) = 1.5 \times 10^{-5}
```

and

```math
b_{\mathrm{inc,Atm1Atm2}}^2 = 0.5 (1 \times 10^{-5})^2 + 0.5 (2 \times 10^{-5})^2 - b_{\mathrm{coh,Atm1Atm2}}^2  = 1 \times 10^{-10}.
```

Now load up `converted_trajectory.mdt` and go to the TrajectoryEditor job in the 
Actions tab. Run the `mdanse_inputs/script2_random.py`, this will generate a 
transmutation setting string which tells MDANSE to transmute 128 atoms to 
`Atm1` and 128 to `Atm2` randomly. 
