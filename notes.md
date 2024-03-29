---
bibliography: bibliography.bib
link-citations: true
---

RF power is produced by a "thermionic" generator. What is that? Klystron?

# Stats

Branch A has a ~0.3 mm beam width.

Branch B has a new KB focus system

> Typically, the duration of a 25eV scan is ~20 minutes

CLS is a "third generation" source.

# Resolving power

VLS-PGM stands for Variable Line Spacing Plane Grating Monochromator.

#### What does that mean?

Amemiya 1996 -> Hettrick, Underwood, Batson & Eckart (1988) -> Hettrick, Underwood 1986, are the sources that describe why this configuration was chosen. 

Indeed the rule spacing is varied across the grating. Having a variable line spacing seems to be primarily just to simplify the mechanical movement of the gratings and mirrors. Rather than having to trace out a complex geometry, VLS means both gratings can just be rotated about their axis.







[@zuin2007early] describes the VLS-PGM beamline, and mentions that it has a "resolving power" of $10^4$. 

What does resolving power mean? [@XRay1991], page 311, chapter 9.5. 

> The angular dispersion is different from the *resolving power*, $\lambda / d\lambda$, or *resolution*.

$\lambda / d\lambda = E/|dE|$

I believe this means the energy setpoint divided by "the smallest FWHM seen in a spectrum".
one source stated a smallest FWHM of 1.5 milli-eV 

# Qs to be answered

#### what's the energy in this x-ray beam? 

Flux is between $10^12$ and $10^15$ photons/sec.

#### does the target get thermally damaged? 

The power on M1 after the undulator is almost 500 W! 

#### How can the intensity of the beam be adjusted?

SyLMAND beamline has a so-called "rotating disk intensity chopper".

## TODO

- Checklist
- Flowchart of strong suits of different techniques a la diffeq flowchart


#### Why are three gratings used to span the wavelength range rather than two on other light sources?

#### Shouldn't a grating monochromator have higher order modes, which would let the background bremnsstralung from distant bending dipole get through? How are these filtered out?

#### Standard file formats for XAFS?

X ray data interchange.


#### Is ionization damage/dislocation on the target a concern?

Yes! @close2015 calls for better reporting standardization, as total dose can affect results. I'm not sure that CLS mentioned total dose as a reporting variable - might perhaps be an interesting method. They also state that, since the beam spot size has decreased, increased. They also state that in Cryo EM, 

Radiation-induced dislocations don't seem to occur at these wavelengths. 

Possible research question: what effect does radiation dose have on <example study>, and how will these effects be increased with the new beamline?


##### Furthermore
   
Bokhoven spectrosocopy 2016 vol 2   
   
p. 627 

> However, Wilke and collaborators [54] have shown that beam-induced photo-reduction can severely affect those measurements (Figure 21.10). Therefore, the measurement of lower oxidations states around iron must be scrutinized with extreme care, particularly when using focused beams.
   
and later
   
>The Fourier transform of the Cu K-edge EXAFS spectra shows weak contributions from next-nearest neighbors, eliminating the possibility of spurious photoreduction processes induced by the beam.
   
   

#### Is the beam pulsed? Are XAS techniques ever pulsed?

I don't see any provisions on the control panel for pulsed operation. There is a provision for a basic kind of synchronization. The beam is split into bunches.

#### What detectors do the VLS-PGM beamlines have?

1. Si photodiode that monitors the flux.
2. QEPro USB4000 UV-Vis spectrometer (for luminescence [XEOL] measurement)
   


3. 
   > VLS-PGM's Toroidal Spectrometer apparatus measures the angle, energy, and relative drift time of ions and electrons generated by the ionization of molecules by soft X-rays.
   > @Recent2014 

    > The first is a *dual toroid electrostatic particle energy analyser*. Each toroid can (independently) measure the energy and angular distribution of charged particles emitted from the interaction region and can be set for either positive ions or electrons. This allows both photoelectron and ion kinetic energy spectra to be recorded. Recent results from this instrument will be presented including both high resolution photoelectron spectra and photoelectron asymmetry parameter (β) spectra. Coincidence circuitry exists to allow, in favourable circumstances,the measurement of molecular frame photoelectron angular distributions (MFPADs) where the detection of an ion fragment allows orientation of the parent molecule to be deduced. 
4.  
    > The second is a *Wiley-McLaren Time-of-Flight mass spectrometer* equipped with multihit electronics. This allows partial ion yield (PIY) spectra to be recorded as well as multi-ion coincidence spectra (PePIPICO). Again recent results will be presented looking at double ionisation in benzene like molecules.
    > @OPPORTUNITIES





#### What detector is usually used for XAS?


#### What is the most appropriate terminology?

XAFS [X-ray absorption fine structure] seems like a good catch-all. 

> The X-ray absorption fine structure (XAFS) is the general name which includes XAMES, XANES, WL and EXAFS.
> @XRay1991

#### What material is the VLS-PGM sample holder made of?

Carbon tape is used to affix the sample to the holder.

#### Are samples typically cooled?

In some beamlines there are provisions for cooling [which?].
   
The thermal contributions to resolution are discussed in Konegsberger. I believe the thermal contributions are, at this time, negligible compared to the other broadening effects.
   
#### Why use the VLS-PGM rather than 08D?

#### How does bremsstrahlung from the storage ring synchrotron radiation differ from that from electron-copper collision?

Cyclotron bremsstralung starts out as an accelerated charge. This creates an equivalent radiation pattern to a dipole oscillator. which creates a typical 

#### Why is an accelerating electron equivalent to a dipole?

   
#### What surface prep techniques are generally 
   


#### Why, intuitively, does the bremsstralung light from an orbiting electron form a cone?

@Properties1994 has a great paragraph on this.

> Physically, the time compression is due to the fact that a highly relativistic electron  follows very closely behind the signals it emitted at eralier times. Moreover, the strength of the electric field at the boserver is proportional to the apparent transverse acceleration of the electron as seen by the observer, which will be large when the time compression is large.

When the electron comes directly towards the observer, its relative speed is maximal, and so its time is shifted by $\gamma$, and so the acceleration "on the" electron as percieved by the observer is magnified. Bremsstralung is 

#### Why then does the electron not also emit a cone *backwards*, when $\omega = 180$?



#### Is the input to the monochromator to the VLS-PGM from an insertion device or from the storage ring bremmsstralung alone?

There are 12 straight sections in the beamline with dipole bending magnets at the corners. Wouldn't be any bremsstralung from the straight sections, presumably.



#### How does the undulator work? How is it different from a wiggler?

@VLSPGM2007a says it 

A wiggler and an undulator are apparently very similar in form and function. An undulator produces a sine wave: a wiggler produces a "chopped" sine, as the light-cone sweeps across the observer.

> Undulators and wigglers differ in the K parameter which can be interpreted as the ratio between the radiation divergence (∼ 1/γ)of adipole and the maximum deection angle of the charged particle (K/γ). For small K-values the light cones emitted at indivdual poles overlap and due to interference produce asharply peaked line spectrum with only afewharmonics. The harmonics are well separated and the on axis ux density isproportional to afactor between N and N 2 (depending on e-beam and beamline parameters), where Ndenotes the number of magnet periods. Wigglers havelar ge K-values. They produce hundreds to thousands of harmonics.
> @Insertion

> The frequency spread is $∼1/N_u%, due to the effect of truncated sinusoidal motion.

#### If undulators are coherent to the period between magnets, how are different spectra produced?

@Properties1994 eq. 12 discusses. 

$\lambda_u$ is the physical spacing of the undulator.

I'm not sure *why* this is, though. 

#### If the undulator uses fixed permanent magnets, how does it produce different wavelengths of x-rays as the input to the monochromator?


The gap width is adjusted. On electromagnet undulators this is done by altering the field strength. 

Intuitively, however, the period should have to be adjusted, I don't fully understand this yet.

The PPM undulator was replaced with an Elliptically Polarizing Undulator in 2019.

#### Why is the insertion device required? Why can't the SR bremmsstralung be used on its own?

> The vast majority of proposals for this new facility were based upon the radiation from insertion devices IDs and not from bending magnets.

#### How is light from the bending magnet before the undulator filtered out? 

It isn't! This is discussed in @properties.

#### For absorption measurements, how is fluroescence light from the sample filtered on the output photodiode?

#### Does the VLS even have provisions for "direct" (i.e. straight-through photodetector) absorption measurements?

Perhaps for gases

#### What's the 

   
#### 
   
In 
https://www.youtube.com/watch?v=kK5OBNJwnws&list=WL&index=62
he describes that monochromator is important because it improves resolution, fine, but also that it *decreases the background*. is that because
   of the x-ray tube bremmstralung? what background is he referring to?

#### What's the difference between RIXS and XAS?

Discussed by @XASa 

#### Why can't 'household' x-ray sources be used for XAS? Is XAS ever done in SEMs?

I have read that it is difficult to monochromate basic x-ray sources sufficiently to provide a good resolution. 

However,

> A conventional X-ray tube can be used as a source of X-rays for XAMES
> and XANES work because it provides a reliable energy calibration with the help
> of reference emission lines. When intense synchrotron radiation is used, the
> energy calibration of monochromators is a continuing problem due to heating
> of the dispersive crystals by the absorbed X-ray power.
> [@XRay1991, p.257]
> The EXAFS studies employ two sources for continuous X-ray: (1) the
> bremsstrahlung output from a laboratory X-ray tube (preferably with a rotating
> anode for high intensity), and (2) the (highly polarized) synchrotron radiation
> from electron storage rings or synchrotrons. These sources are compared in Fig.
> 7.16for intensity. In spite of the greater brightness of synchrotron radiation, for
> concentrated samples the bremsstrahlung from an X-ray tube (flux >- 106 to 108
> photons/s in a 10 eV bandwidth) is a satisfactory source [7.8, 151J for EXAFS
> work when a curved crystal (focusing type) spectrograph is used as the analyzer.
> [@XRay1991, p.269]

There's a brand of "metal-jet" x-ray sources that seem to have great flux properties nowadays.

#### If relativistic charges instead radiated parallel to the acceleration, rather than in the direction of the velocity, would synchrotrons still be possible?


#### How does the two-beam M1, M2 chicane work? 

   
#### What is the "injection septum photon absorber"?

#### Why does the VLS-PGM webpage say that TEY and FLY are "standard XAS"?

I am not sure if VLS-PGM has "straight-through" Beers law detector. TEY and FLY are both indirect methods of reading out the absorption spectrum, and might have different surface. 

> standard XAS measurements, where Total Electron Yield (TEY) and Total Fluorescence Yield (FLY) are recorded, the VLSPGM provide two alternative forms of data acquisition configurations: 

#### What's the difference between XAS and XPS?


#### 

https://xraydb.xrayabsorption.org/atten/

#### What are the steps to get a result from XANES?

   
   
#### Is surface charging an issue for FEL and TEL measurements?
   
here it is discussed that in XPS, the surface charge should be neutralized or else incorrect photoelectron energies will be obtained
   
https://www.youtube.com/watch?v=6XQOGS6CBkY
   
is that an issue for any XAS?
   
   
#### Some formulations use bras and kets. What does a basic quantum mechanical formulation of XAS with FLY look like?



#### What is "pink synchrotron light"?

#### Why are people allocated 8-hour blocks? What fraction of that 8 hours are samples in the load-lock and being analyzed? Does the 8-hours include time for sample prep?

Some experiments may require time- or condition- sensitive samples, e.g. without moisture. This would make it more reasonable to have block allocations of time.

#### Why are the M mirrors coated in carbon, and why is carbon tape used to fix samples?

In other situations, e.g. EXAFS, it's said that carbon contamination can be detrimental.

The mirrors operate in so-called "total external reflection" mode.

#### How is the photon flux adjusted?

In the manual for the TOF spectrometer, it is stated that the photon flux can be adjusted. How is this performed?

#### It is said that bremmstralung is quantized. This causes emittance growth in electron accelerators

Naturally; it is emitted in single photons. It is said that 

#### What is "the I0 mesh"?

A gold wire mesh of maybe 20 um can be placed before or after the sample; photoelectrons are emitted by the mesh. Can be affected by "carbon contamination" (?).

#### Which definition of emittance is most commonly used at the CLS?

Emittance is "conserved area in phase-space".

#### In [@VLSPGM2007a], a graph of photon energy vs intensity for Helium is shown, and named the "double excitation spectrum". The first peak is at about 63 eV. Why is this different from the second ionization energy of helium?


#### How does the energy compression system work?



#### Some XAFS and EXAFS are sensitive to the electric field. Can this be helpful to 

#### Why does X-ray luminescence depend on color of material?

https://youtu.be/YT4ZtCCP31s

At 20:47, that video also has a great intro to EXAFS.


#### What is bra-ket notation all about?

$\ket{\text{a}}$ is a vector in a vector space.

$\bra{\text{b}}$ is... a functional, outputting a complex number from a vector (?)

#### What is the Duane-Hunt limit?

The spectrum of bremmstralung can't exceed V.

#### What is the Rowland circle?

Described in Konegsberger, chapter 4.5.2.2.
   
#### Does spatial dependence 

In @L11, it is described that 

> We're going to be using our harmonic variation. We said in our harmonic variation, Hamiltonian delta h was 2h prime cosine of omega t, and we want this h prime to be simple enough. We want to think of this photon that is coming into the atom as a plane wave, something that doesn't have big spatial dependence in the atom. It hits the whole atom as with a uniform electric field. The electric field is changing in time. It's going up and down, but it's the same everywhere in the atom.
> 
> So for that, we need that-- if you have a wave, it has a wavelength, if you have an atom that is this big, you would have the different parts of the atom are experiencing different values of the electric field at the same time.
>
> On the other hand, if the wavelength is very big, the atom is experiencing the same spatially independent electric field at every instant of time. It's just varying up and down, but everywhere in the atom is all the same. So what we want for this is that lambda of the photon be much greater than a0. So that-- 1.
>
> So this means that the photon has to have sufficiently long wave, and you cannot be too energetic. If you're too energetic, the photon wave length is too little. By the time it becomes smaller than a0, your approximation is not going to be good enough. You're going to have to include the spatial dependence of the wave everywhere. It's going to make it much harder.


indeed, 

> The absorption for each X-ray level begins abruptly
> at the series limit and decreases roughly as the cube of the wavelength
> X. A general formula for this absorption is

$$ \sigma_n = \text{C}_n \text{Z}^a \lambda^b $$

> where cr^ 's the atomic absorption coefficient for each X-ray level K,
> Lj, L2f L3, M], M2, etc., and Cn I s a constant Involving the quantum
> numbers of each X-ray level and the threshold wavelength of the level
> and Z is the atomic number, a is roughly h and b ranges from 2.5 to 3.

#### What's the difference between the classical mechancis Hamiltonian and the QM one?

I CM, the hamiltonian is T = H+V, i.e the total energy of the system (kinetic and hamiltonian). In QM, 

#### The E in EXAFS doesn't mean *electron*, but Extended.

#### What's the difference between XRF and XAS?

XRF 

#### What's the "isotope linac"?

#### "Multiple scattering" is not what it sounds like.

I think EXAFS, even if disregarding "multiple scattering", still takes into account 

#### What is a fano resonance?
 
https://www.youtube.com/watch?v=YU151Kt6MMU
   
> I guess my view of the answer
is most what we're interested in but if
it's if they're if they're useful I mean
okay are we going to get some new
information out of them it's because
there is new information in the STM tip
position dependence on q and so you
must understand you can't use q just
as a fitting parameter which a lot of
solid-state people and a lot of the
solid-state applications you see out
there now people if they see in a
symmetric shape they they fit 
Fano shape using q as a parameter well
you can do that but it's not a- it
doesn't gain you any any new information
unless unless unless you understand the
physical content and Ned will I'm sure
talk a bit


#### What is an "apple II" undulator?

#### what is larch "happiness"?

#### What is XMCD?
   

   
https://www-ssrl.slac.stanford.edu/stohr/xmcd.htm

#### What is a xanes "standard"?

# Pitfalls and best practices, automated quality controls

Already we have our first issue. @close2015

Contamination of the gold mesh can lead to a decreased PE emission current.


In @Retraction2018, 

> The spectrum published in our PCCP paper is not consistent with backups of raw data from the beamline computer and it was thus modified while no specific data treatment is mentioned.


I've noticed that, because of the deadline & stuff associated with this project, I've stopped thinking in terms of "what do I feel like I need to learn" or "what can I do that will be genuinely useful or informative" to "what will be most impressive". Definitely something to avoid.

##### Position and definition of E0

The first peak of the first derivative is a common definition, but others can be used. might be nice to report which one.


# Resources

### @XRay1991

A good introduction

### @Modern2004

On perlego

I'm realizing that, by learning via these proprietary book sources, I might be making it harder for people, especially those in low-income countries, to verify quotes &c.

https://www.youtube.com/watch?v=bK2DQI7HSYo


### @Synchrotron2021

Great derivations of bremmstralung eqs.



# Bibliography

