


# A few notes on deconvolution of XAFS spectra

Daniel Correia

> An ostensibly more noise-tolerant deconvolution algorithm is (poorly) implemented in Larch; results are not clearly superior. Real-world results from the VLS-PGM are re-processed and yield useable fidelity. An interface to the existing inverse filtering deconvolution is added to demeter/Athena. Non-stationary kernels are discussed.




![](Zn_Cu_output.png)

@Highresolution2007 perform XANES on a variety of ZnS sphalerite samples and compare to a nifty ab initio model. They find limited correspondence between theory and experiment unless the predicted spectra are filtered and broadened by 1 eV, accounting for all the sources of line uncertainty in the experiment, in which case an excellent fit is found.

In this figure, two deconvolution algorithms (bottom, solid) are used to pare off a gaussian with $\pm\sigma=0.5 \text{ eV}$ from the experimental data (top), the reverse procedure to that used in the paper.

Very surprisingly, the small inflection point near 166 eV <sup>(what is this feature?)</sup> predicted by theory is accurately reconstructed by the L-R algorithm, even though no corresponding feature is obviously present in the input data. On the other hand, a poor showing is consistenly seen in the ripple near 170 eV.

A relatively wide slit width of 100 um was used for this experiment, which may have contributed to the success of deconvolution. The 


### Introduction

*(note: this paper was written by someone who has perhaps an hour's experience in XAS. All statements are almost certainly false.)*

In papers describing the VLS-PGM[@zuin2007early][@VLSPGM2007a] and similar beamlines, the "resolving power" of the system is often a key point of comparison. However, this resolving power does not perhaps seem to represent an ultimate "information-theoretic" limit, but rather seems to mostly reflect the quality of the output spectrum of the monochromator[see, @XRay1991, chapter 9.5, "Plane crystal spectrograph"] $$

Purely for amusement, the question arose of what the ultimate resolving power would be if the effect of  and how corrections can be implemented.



With modern detectors, circumstances are probably rather rare in which deconvolution is a good experimental design. @High2021, for instance, discuss a HERFD-XAS technique that can natively probe at sub-linewidth resolutions.

Tt seems more episemologically robust to use an inherently higher-resolution technique then to try to extract. 


An X-ray spectrum observed from experiment represents the convolution of many different sources of error, tabulated by 

For argon this is perhaps 1 eV, and can reach 

Excellent discussion can be found in [@XRay1991], particularly chapters 4.5.3, Chapter 4.7, X-ray line width

These widths vary 

In terms of the intrinsic 

In a machine with a resolving power of 0.025

(Note: a )


# Non-stationary, or varying, 

One impediement to deconvolving to the resolution, especially in the case of the VLS-PGM, is the significant non-flatness of the spectrum across the energy window. 

In practice, segments of spectrum requiring  ultra-high-resolution are probably unlikely to be very much wider than a few tens of eV, so the variation in spectrum seems likely to be negligible




note that these experimental spectra were determined via fluorescnces yield XANES. the discussion above 


access to original data and the analysis scripts are quite rarely provided, even though the same pitfalls can be encountered.



![](stretch.png)
