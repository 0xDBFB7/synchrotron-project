

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


larch uses scipy diconvolve, "inverse filtering". 

https://www.ft.unicamp.br/docentes/magic/khoros/html-dip/c7/s1/front-page.html


use monochromator equation as example spectrum or something

#### What advantages does the iterative richardson-lucy algo have over deconvolve?

For one, the Fister technique has

0. provisions for both the core-hole and the 
1. noise tolerance compared to basic inverse filtering

also hopefully:

2. adjustable width with energy (maybe)
3. not assuming gaussian distribution (maybe)


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


#### Varying spread-function tests

convolve a gaussian 




#### The Richardson-Lucy Algorithm


need to note that "fano profile analysis" and "curve fitting" was done (what is that?) by He when characterizing the VLS, they're not going blind

