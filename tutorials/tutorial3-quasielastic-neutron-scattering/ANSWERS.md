# Answers

## Question 1:

For an isotropic monoatomic system of free particles
```math
\langle d^{2}(t) \rangle = \frac{1}{3} \langle \vert \vec{r}(t) - \vec{r}(0) \vert^2 \rangle.
```
Since free particles move in a straight line, 
$\vert \vec{r}(t) - \vec{r}(0) \vert^2 = (v t)^2$ where $v$ is the speed for a given
particle. We can then integrate $(v t)^2$ over the Maxwell-Boltzmann distribution so that
```math
\langle d^{2}(t) \rangle = \frac{t^2}{3} \int_{0}^{\infty} \mathrm{d}v \: v^2 f(v)
```
where
```math
f(v) = \left( \frac{m}{2\pi k_{\mathrm{B}} T}\right)^{3 / 2} 4 \pi v^2 \exp\left(- \frac{m v^2}{2 k_{\mathrm{B}} T} \right)
```
is the Maxwell-Boltzmann distribution. Solving the above we obtain the following result
```math
\langle d^{2}(t) \rangle = \frac{1}{2} (v_{\mathrm{p}} t)^2
```
where $v_{\mathrm{p}} = \sqrt{2k_{\mathrm{B}} T / m}$ is the most probable 
speed and $m$ is the mass of the particles.

We can now plug this result into the Gaussian approximation of the intermediate 
function and Fourier transform to obtain the van Hove and dynamic structure 
factor for a system of free particles.
```math
G_{\mathrm{s}}(\vec{r}, t) = \left( \frac{1}{\pi v_{\mathrm{p}}^2 t^2} \right)^{3/2} \exp\left[ - \left(\frac{r}{v_{\mathrm{p}} t}\right)^2 \right]
```
```math
F_{\mathrm{inc}}(\vec{q}, t) =  \exp\left[ - \frac{1}{2} (q v_{\mathrm{p}} t)^2 \right]
```
```math
S_{\mathrm{inc}}(\vec{q}, \omega) = \frac{1}{\sqrt{2 \pi} q v_{\mathrm{p}}} \exp\left[ \frac{1}{2}\left(\frac{\omega}{q v_{\mathrm{p}}}\right)^2 \right]
```

## Question 2:

As explained earlier the Gaussian approximation is exact for system of 
free particles and a system of particles undergoing brownian motion.
At short time scales the atoms in the liquid Argon trajectory behaves 
like a free particle while at long time scales it will behave like a 
particle undergoing brownian motion. Since these time scales correspond 
to short (large $q$) and long (small $q$) wavelength dynamics we should 
expect good agreements between the GDISF and DISF results at these limits.
At intermediate values of $q$ this is where so called nongaussian effects 
occur which results in deviations between the GDISF and DISF results.

## Question 3:

Here are the results for the GDISF and DISF plots of the QENS peak HWHM 
against $q^2$ with a line of best fit with the intercept set to run 
through the origin.

<p align="center">
    <img width="400" src="pictures/gdisf_diffusion_plot.png"/>
</p>
<p align="center">
    <img width="400" src="pictures/disf_diffusion_plot.png"/>
</p>


From the linear fits the diffusion constant from the GDISF and DISF is
$2.46 \times 10^{-5}$ and $2.08 \times 10^{-5}$ $\mathrm{cm}^2\mathrm{s}^{-1}$
respectively. Calculating the diffusion 
constant from the MSD using $D = \mathrm{MSD}(t) / 6t$ with $t=60000$ fs
gives a diffusion constant of $1.96 \times 10^{-5}$ $\mathrm{cm}^2\mathrm{s}^{-1}$. 

We should expect some differences from all three results; 
it is only at specific limits where they will agree with each other. 
This occurs when the MSD is calculated at large $t$ and the 
diffusion is calculated from QENS peaks at small $q$. Small $q$ values 
are required as this is where the nongaussian effects in the DISF are 
small and also where the main contribution to the QENS peak for both GDISF and DISF 
are from long wavelength dynamics.

Since our linear fits were made over a range of $q$, our calculations 
for the diffusion constant will be inaccurate due to the effects mentioned 
above. Try refitting the data using only the smaller values of $q$. You 
should see closer agreements with the MSD results.
