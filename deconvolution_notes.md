

# Things to read

1. lifetime broadening, especially "core-hole"

Discussed in @XRay1991, 3.2 Form and Width of Lines





#### Is it possible to get a better idea of the monochromator output spectrum 

Lacking a solid foundation in quantum mechanics, and disenfranchised by how many EXAFS codes there are, 

The "resolution" of the thing is limited by the narrowness of the monochromator bandwidth.

In many of the CLS' calibration datasets (like @VLSPGM2007a), a narrow peak in the helium spectrum is used to compute the resolving power. 
A graph of simulated resolving power versus energy is also provided.

The question is, the helium peak has a finite width in reality. This width and the monochromator width are convolved to produce the output.

if we deconvolve, we can compare to the same spectrum on a better machine, etc.
or, assuming emittance / acceptance angle / through the beam-path is the largest factor (doubtful), try to replicate the cls's simulation.

Based on this, 

Larch already includes a simple deconvolution function, 
https://xraypy.github.io/xraylarch/xafs_preedge.html

but this has not been pulled out into the api for demeter.
https://bruceravel.github.io/demeter/documents/DPG/mue/deconvolve.html
people have actually asked for it!
https://millenia.cars.aps.anl.gov/pipermail/ifeffit/2019-April/009784.html

indeed it's on demeter's to-do list https://bruceravel.github.io/demeter/todo.html. Cool!

> Remove experimental and lifetime broadening from your data.
> A deconvolution algorithm is one of the most important things
>	   in :demeter:`demeter` that has not yet been started.

it sounds like he wants something more than just larch's deconv. 

need to stress care and pitfalls.

can probably compare to larch's own deconv. unit tests

on the other hand, experimental stuff might contribute to this.

@Extraction2000 suggest a quite exceptionally complex Baesian statistical deconvolution.

@Curve1988 is a much simpler paper on a similar topic. Has an equation describing all the different components represented in the signal.

xraypy has a "darwin width" function for monocromator width
https://xraypy.github.io/XrayDB/examples.html#darwin-widths-of-monochromator-crystals

Deconvolution can maybe be done in a fourier-transform way, like 
or using a transfer-function

can prototype with python first then translate into demeter's perl

##### Does Larch's deconv algorithm do $\lambda / \text{d}\lambda$ or a fixed energy spread?




##### What is core-hole lifetime broadening: are there any systems that do not exhbit it, or where the broadening is much smaller than the  (He gas calibration)?

larch has a function to get the core-hole broadening.
"easy mode" would be to do 




In practice, resolving power varies enormously with energy. A deconvolution with a constant spectral width won't work.
Use resolving power equation from agarwal as an approximation?





#### Deconvolution is perhaps not, in practice, a very robust way to obtain these data.

@Curve1988 mentions a bunch of great ways to get rid of the monochromator spectra besides deconvolution: divide or subtract a "clean surface" signal, etc, etc.

Fits to experimental data are already some form of "deconvolution".

> X-ray absorption spectroscopy (XAS) provides a powerful tool for in situ chemical speciation but is severely limited by poor spectroscopic resolution arising from core-hole lifetime broadening.

https://pubmed.ncbi.nlm.nih.gov/34164981/



larch's documentation on the topic is pretty great.
https://millenia.cars.aps.anl.gov/xraylarch/xafs_preedge.html#spectral-deconvolution

> For a large fraction of XAFS data, the energy resolution is dominated by the intrinsic width of the excited core level and by the resolution of a silicon (111) double crystal monochromator, and so does not vary appreciably between spectra taken at different facilities or at different times.
> 
> Whereas a Gaussian most closely reflects broadening from the X-ray source, broadening due to the natural energy width of the core levels is better described by a Lorentzian. Therefore, to try to reduce the influence of the core level in order better mimic high-resolution fluorescence data, de-convolving with a Lorentzian is often better.

The PLEIADES beamline is about 1 order of magnitude more spectrally pure than 

https://www.wayforlight.eu/en/beamline/20876

note the larch sample lifetime broadening equation for hydrogen




@Deconvolving2007 blammo! I love you guys. okay. this seems more straightforward than the other paper. 
first implement this in Python.
actually really really simple.

looks like this ended up as a physical review paper by Fister et al.

however, this seems to use a non-energy-varying gaussian, whereas the true gaussian of the experimental system changes by many orders of magnitude over the eneryg.
maybe at each grid point a different-sized gaussian width parameter could be used...

actually, it doesn't even need to be gaussian. the input there could be the true "undulator and monochromator" output, since it's just going to be convolved
with the core-hole gaussian.

# that's key




In fact, this technique flat-out *won't work* with much of the data from the VLS-PGM. 
maybe a second grid (or just break into small segments) on a much coarser grid can be used to implement a variable PSF.
Fister et al don't need this because they're only working with small segments of a spectrum.



use a high-order polynomial to approximate the instrument response

their technique does mandate a filtering step, so very sharp information may be lost....

honestly the dependence of the output on the filtering intensity is quite troubling. Definitely something to note.

> Here, the deconvolved estimate is not able to fully resolve features with
> widths below ~2 eV

after this is done, should see what the latest data is on this R-L technique.
it seems like this is powerful enough, but not quite the best.


demeter comms with larch via the "larch server". 


oh, varying is also called "nonstationary".


larch uses scipy diconvolve, "inverse filtering" - divides the frequency domain of one signal by the otther.

https://www.ft.unicamp.br/docentes/magic/khoros/html-dip/c7/s1/front-page.html


use monochromator equation as example spectrum or something

https://github.com/xraypy/xraylarch/blob/a02840b3ce0cf9c24461e5a000f28f2034601e4c/larch/xafs/deconvolve.py

#### What advantages does the iterative richardson-lucy algo have over deconvolve?

For one, the Fister technique has

0. provisions for both the core-hole and the experimental subtraction

The convolution of two gaussian distributions is a gaussian: so strictly speaking it's possible to incorporate this now.

https://jeremy9959.net/Math-5800-Spring-2020/notebooks/convolution_of_gaussians.html

> If $F$ is gaussian with mean $\mu$ and variance $\sigma$, and $G$ is the gaussian with mean $\nu$ and variance $\tau$, then $F\star G$ 

however: if the two distributions are different (which seems likely to be the case)

1. noise tolerance compared to basic inverse filtering

also hopefully:

2. adjustable width with energy (maybe)

actually, I was reading the wrong graph: the resolving power only varies by about a factor of 4 across the frequency range.
it really isn't all that helpful to have a variable graph unless you can extract the monochrom. output spectrum in situ. 

1. not assuming gaussian distribution (maybe)


an even more advanced deconv could be implemented using either https://en.wikipedia.org/wiki/Wiener_filter 
or that other paper's baesian

##### Test cases



some datasets for metals can be found at https://github.com/XraySpectroscopy/XASDataLibrary/tree/master/data

argon k-edge is at https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z18.html ,  but not very high resolution

fister use Ag k-edge: this is availabel in the xasdl.

http://skuld.bmsc.washington.edu/scatter/AS_periodic.html
has some generated data for each of the elements

same here https://henke.lbl.gov/optical_constants/asf.html but there's no data on how it was collected

- low core-hole broadened elements, no 
- 


- Compare CLS VLS-PGM data to PLEIADES

look into other deconvolution validation


#### Varying spread-function tests

convolve a bunch of different gaussians with a sawtooth square function.

since L-R uses forward convolution, as long as you can convolve a variable function, 
https://stackoverflow.com/questions/62955273/convolve-array-with-kernel-of-variable-standard-deviation

https://math.stackexchange.com/questions/2423597/can-i-apply-the-convolution-theorem-with-an-adaptive-kernel
then it is extended to an "integral transform" 


#### The Richardson-Lucy Algorithm


need to note that "fano profile analysis" and "curve fitting" was done (what is that?) by He when characterizing the VLS, they're not going blind



> Currently, the best citation for Larch is M. Newville, Larch: An Analysis Package For XAFS And Related Spectroscopies. Journal of Physics: Conference Series, 430:012007 (2013). [Newville (2013)]


> The algorithm is based on a PSF (Point Spread Function), where PSF is described as the impulse response of the optical system. 

oh neat

https://github.com/sheliak/varconvolve has a variable convolution - uses an interesting technique, warping the signal first. GPL license, probably not compatible.

scikit has a richardson-lucy implementation 
https://scikit-image.org/docs/dev/auto_examples/filters/plot_deconvolution.html
not sure if we can use that, since we need to filter, too.



is there a way we can extract the PSF / monochromator output distribution from the plot?
one risk would be that, in more complex situations, we might subtract some unknown 


the call signiture should be

psf_function() can be 'lorentzian', 'gaussian', return a 1d interpolation function (for constant but weirdly-shaped functions)
or maybe the PCA thing ? 
deconvolution(mode= psf=psf_function



'athena' uses LARCH here:

> In ATHENA's implementation of peak fitting, a Levenberg-Marquardt non-linear least-squares minimization is used. (To be specific, IFEFFIT's minimize command is used after constructing an array with a sum of line shapes or LARCH's minimize function is using an objective function which contructs an array with a sum of the line shapes.)

> An obviously useful function are not available in the current version of ATHENA is a broadened Cromer-Lieberman calculation of the bare atomic edge step (which might better approximate the shape of the XANES data).



can probably just directly copy the convolution athena program to add deconv.


man, athena is *such* a well-documented program. the preferences section is really good too.

#### Starting demeter with larch backend. 

one way to tell is if more options are added to peak fit types.

DEMETER_BACKEND env var is not documented. should add to 

okay, got it to work. entered into conda and ran dathena, still worked despite different perl; dmeter seems to need larch on the path
might be nice to have an env var to skip that check and just do a remote connection to the port.

## WARNING 
this means I need to switch back and forth to compile dathena - cannot compile in the same window.

https://millenia.cars.aps.anl.gov/pipermail/ifeffit/2017-August/009222.html





TODO:

add env var override to dathena to connect to existing larch server