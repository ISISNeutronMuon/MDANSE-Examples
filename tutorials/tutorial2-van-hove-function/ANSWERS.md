# Answers

## Question 1:

```math
n_0 g(r) 4 \pi r^2 \mathrm{d}r = \mathrm{d}N(r)
```

The function $N(r)$ is a sum of step functions so that $N(r)$
increases by one as $r$ increases each time it comes across an atom. 
Therefore, $\mathrm{d}N(r) = N(r + \mathrm{d}r) - N(r)$ and $\mathrm{d}N(r)$ 
will be the average number of particles in the shell volume between $r$ 
and $r + \mathrm{d}r$. The derivative of $N(r)$ will be the derivative 
of the step functions which are delta functions each centered on the 
distances from the other atoms.

```math
\frac{\mathrm{d}N(r)}{\mathrm{d}r} = \frac{1}{N} \sum_{k \neq j} \langle \delta (r - \vert \vec{r}_k - \vec{r}_j \vert) \rangle
```

where we have written the sum of delta functions inside the angle brackets
so that the positions are thermally averaged and also average the thermal 
average over all possible atom origins.

## Question 2:

For solid systems, atoms are fixed at specific sites so the 
distinct-part of the van Hove function does not change much. As 
$t \rightarrow \infty$, the van Hove function is more or less the same 
as it is for any other time. For liquid and gaseous systems the situation 
is quite different since atoms are free to move across the system, 
$G_{\mathrm{d}}(\vec{r}, t \rightarrow \infty) \sim n_0$ or $1$ in MDANSE 
since it has been normalized. In other words, these results tell us that 
there is no correlation between the configurations at $t=0$ and $t = \infty$.

## Question 3:

For a solid, each atom will be fixed at specific sites. They will oscillate 
around those sites so that the self-part of the van Hove function at large 
times will be a function which describes the probability of the atoms 
around the center of its site. For liquid and gaseous system all atoms 
are free to diffuse across the entire system. On average as 
$t \rightarrow \infty$ all possible distances will be explored. 
$G_{\mathrm{s}}(\vec{r}, t \rightarrow \infty) \sim V^{-1}$ or $N^{-1}$ 
in MDANSE since it has been normalized, in the thermodynamic 
limit $V \rightarrow \infty$ and $N \rightarrow \infty$.
