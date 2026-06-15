# Showing new listings for Monday, 15 June 2026
Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.


阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送

See `Usage.md` for instructions on how to personalize the repo. 


Keyword list: ['star formation', 'molecular cloud', 'interstellar medium', 'dust', 'cloud', 'clump', 'core', 'filament', 'atomic gas', 'H$_2$', 'HI', 'N-PDF', 'bubble', 'shell', 'feedback', 'jet', 'outflow', 'protostar']


Excluded: ['galaxies', 'galaxy clusters', 'AGN', 'black hole', 'lensing', 'dark matter', 'dark energy', 'fast radio burst', 'pulsar', 'neutron star', 'white dwarf', 'AGB', ' z ', 'lightcurve']


### Today: 7papers 
#### Title:
          COUNTESS I: A Uniformly Vetted Catalog of Known and New Transiting Exoplanets in the TESS Northern Continuous Viewing Zone
 - **Authors:** Andrew Hotnisky, Rachel B. Fernandes, Kevin K. Hardegree-Ullman, Steven Giacalone, Kiersten M. Boley, Kristo Ment, Michelle Kunimoto, Galen J. Bergsten, Sakhee Bhure, Jessie L. Christiansen, Brandon Radzom, Suvrath Mahadevan
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP); Instrumentation and Methods for Astrophysics (astro-ph.IM); Solar and Stellar Astrophysics (astro-ph.SR)
- **Arxiv link:** [https://arxiv.org/abs/2606.13789](https://arxiv.org/abs/2606.13789)
- **Pdf link:** [https://arxiv.org/pdf/2606.13789.pdf](https://arxiv.org/pdf/2606.13789.pdf)
- **Abstract**
 The Transiting Exoplanet Survey Satellite (TESS) has transformed the study of nearby exoplanetary systems; however, its nominal observing strategy limits sensitivity to planets with orbital periods shorter than $\sim$10 days for most parts of the sky. The two TESS Continuous Viewing Zones (CVZs) provide extended temporal baselines that help overcome this limitation, enabling the detection of longer-period ($>$10 days) transiting planets around nearby stars. Here, we present COUNTESS, a transit-search pipeline optimized for long-baseline TESS observations that combines multi-sector light curves with heterogeneous cadences, and implements fast-folding BLS period detection, vetting, and statistical validation. As a first application of the pipeline, we conducted a search on the primary and first extended mission photometry in the TESS northern CVZ. For this analysis, we used Gaia DR3 and 2MASS photometry to homogeneously derive a stellar catalog of FGKM stars for the TESS northern CVZ, resulting in a sample of 391,059 stars. We used COUNTESS to search for transiting planets around 26,114 of these stars with TESS-SPOC light curves and assessed its performance, recovering 115 out of 159 known TESS Objects of Interest (TOIs; $0.85\ \text{days} < P <124.72\ \text{days}$; $1.03\ R_\oplus < R_p < 16.35\ R_\oplus$). Additionally, we identified 10 new exoplanet candidates ($1.20\ \text{days} < P <34.62\ \text{days}$; $1.73\ R_\oplus < R_p < 4.19\ R_\oplus$) that passed vetting tests, including two new statistically validated sub-Neptunes, TIC 219893931b and TIC 237254473b. COUNTESS enables extended-baseline TESS analyses and identification of longer-period planets, establishing a foundation for future exoplanet demographic studies, including comparisons with Kepler and K2.
#### Title:
          A novel data-driven approach to extract stellar population properties from galaxy spectra using absorption indices
 - **Authors:** Zahra Sharbaf, Ignacio Ferreras, Anna R. Gallazzi, Stefano Zibetti, Daniele Mattolini, Laura Scholz-Díaz
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
- **Arxiv link:** [https://arxiv.org/abs/2606.13791](https://arxiv.org/abs/2606.13791)
- **Pdf link:** [https://arxiv.org/pdf/2606.13791.pdf](https://arxiv.org/pdf/2606.13791.pdf)
- **Abstract**
 In an era of highly complex machine learning methods that often are informative but not straightforward to interpret, Principal Component Analysis (PCA) offers a simple, easily interpretable approach. With no fitting parameters, it extracts the most salient statistical trends in data without the need for training sets. In this paper, we explore a large range of composite stellar population models defined for detailed analyses of galaxy spectra from surveys. Six of the most prominent spectral indices are targeted to visualize a PCA-based latent space created by the model data. The age-metallicity degeneracy is broken in the 3-dimensional space spanned by the first three eigenvectors, but we emphasize that non-trivial combinations of all six absorption indices are needed for this. Moreover, the last eigenvector suggests an intriguing tug of war between two Balmer indices: H$\gamma_A$ and $H\delta_A$, that can help discern the presence of recent bursting behaviour, as it exploits the different behaviour of the two indices over timescales $\sim$0.5-1 Gyr. Comparisons can be made between SDSS and LEGA-C galaxy spectra based on the latent space created by the models. This method, based on pure data, produces excellent results in agreement with standard SPS model fitting techniques, allowing for the study of stellar populations in a variety of surveys or observational/synthetic databases on solid ground.
#### Title:
          A Scalable Fast Multipole Method Poisson Solver for the RAMSES code: I. Unigrid Algorithm
 - **Authors:** Jun-Young Lee, Romain Teyssier
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Astrophysics of Galaxies (astro-ph.GA); Computational Physics (physics.comp-ph)
- **Arxiv link:** [https://arxiv.org/abs/2606.13793](https://arxiv.org/abs/2606.13793)
- **Pdf link:** [https://arxiv.org/pdf/2606.13793.pdf](https://arxiv.org/pdf/2606.13793.pdf)
- **Abstract**
 We present a scalable Poisson solver with $O(N)$ complexity based on the fast multipole method (FMM) implemented in RAMSES. Our FMM constructs a hierarchy of FMM grids on top of the pre-existing Cartesian grid which is used to compute the force for hydrodynamics or particle-mesh simulations. In contrast to the $O(N)$ multigrid solver (MG) - an iterative method that requires multiple V-cycles through a multi-resolution hierarchy of Cartesian grids - the FMM algorithm performs just one upward pass through the same hierarchy, during which multipole expansions are accumulated and shifted, followed by a single downward pass, in which local expansions are propagated. Numerical tests indicate that FMM attains accuracy comparable to that of MG for smooth potentials and is particularly well-suited for problems with isolated boundary conditions, since it avoids the approximate Dirichlet boundary conditions required by MG schemes. Although in theory FMM requires around 30 times more floating-point operations than MG, its higher arithmetic intensity leads to comparable performance and better scalability relative to MG.
#### Title:
          Characterization of white-light enhancements under umbral conditions in one-dimensional simulations of solar flares
 - **Authors:** Sascha Ornig, Mats Carlsson
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
- **Arxiv link:** [https://arxiv.org/abs/2606.14282](https://arxiv.org/abs/2606.14282)
- **Pdf link:** [https://arxiv.org/pdf/2606.14282.pdf](https://arxiv.org/pdf/2606.14282.pdf)
- **Abstract**
 Solar flares with signatures in the optical continuum (white light, WL) pose a challenge to the standard flare model and to solar flare simulations. In particular, simulations are so far not able to convincingly reproduce observed WL enhancements. We investigate the effect of different electron beams on an umbral atmosphere and what the differences and similarities to the quiet-Sun response are. We characterized WL emission in one-dimensional simulations of solar flares using the radiation hydrodynamics code RADYN. We used a similar setup as the F-CHROMA grid, but with a starting atmosphere describing umbral conditions. We investigated the influence of different temporal profiles of an electron beam on this umbral atmosphere. Our simulations show maximum WL increases between 40 and 335%, which is comparable to observed values. The reduced umbral background is the main reason for these large increases. We identify hydrogen recombination in an optically thin chromosphere as the dominant process responsible for the increases, with the radiation from the heated photosphere becoming substantial in the later stages due to the longer timescale of the cooling of the photosphere compared to hydrogen recombination in the chromosphere. Shorter, more intense beams (i.e., beams with a higher maximum energy flux) lead to a faster and more dramatic atmospheric evolution. Such beams also cause larger WL enhancements due to a higher electron density in the relevant layers. Both the Balmer ratio and the Paschen ratio are substantially higher in our simulations compared to simulations with a quiet-Sun atmosphere. The detectability and amplitude of WL enhancements depends on the spectral and temporal structure of the electron beam as well as the underlying background radiation. The combination of a short, intense beam and an umbral atmosphere provides an excellent seed for substantial WL enhancements.
#### Title:
          Lensed hot stars with HST in the 2030s
 - **Authors:** J.M. Diego
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
- **Arxiv link:** [https://arxiv.org/abs/2606.14392](https://arxiv.org/abs/2606.14392)
- **Pdf link:** [https://arxiv.org/pdf/2606.14392.pdf](https://arxiv.org/pdf/2606.14392.pdf)
- **Abstract**
 In the late 20th century, the Hubble Space Telescope (HST) revolutionized astronomy, showing the Universe with a detail never seen before in the ultraviolet (UV), optical and infrared (IR) bands. In the early 2020s, the James Webb Space Telescope started a similar revolution in the IR. The launch of Roman in late 2026 challenges the reign of HST in the optical band, but even after Roman's launch, HST will remain as the only telescope capable of high-quality imaging in the UV band. In the optical bands, HST provides superior resolution than Roman for point sources. Although equipped with more sensitive MOS, Roman's sensors have a pixel size about 3 times larger than HST's CCDs, hence undersampling the point-spread-function, and resulting in a worse spatial resolution. The UV-capable and higher-resolution of HST in the UV and optical band, makes HST the best instrument for specific science cases. This paper responds to the "Building a Roadmap for Hubble science into the 2030s" call and focuses on science with lensed hot stars at $z>0.5$ in the UV and optical bands, exploiting the features that makes HST the best instrument in the UV/optical until the launch of the Habitable World Observatory in the 2040s.
#### Title:
          Morphokinematic structure of the Planetary Nebula NGC 6563
 - **Authors:** Zahra Al, Federico Soto-Badilla, Yüksel Karataş, Gerardo Ramos-Larios, Roberto Vázquez
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR); Astrophysics of Galaxies (astro-ph.GA)
- **Arxiv link:** [https://arxiv.org/abs/2606.14396](https://arxiv.org/abs/2606.14396)
- **Pdf link:** [https://arxiv.org/pdf/2606.14396.pdf](https://arxiv.org/pdf/2606.14396.pdf)
- **Abstract**
 We present a morphokinematic analysis based on high-resolution long-slit echelle spectroscopy of the \nii$\lambda6583$ line and narrowband imaging. Position-velocity diagrams reveal asymmetric expansion and localized kinematic features. We derive a systemic velocity of $V_{\rm sys}^{\rm LSR} = -25\pm1$\kms\ ($V_{\rm sys}^{\rm HEL} = -34 \pm 1$\kms) and a main shell expansion velocity of $V_{\rm exp} = 22 \pm 1$\kms. Three-dimensional modeling indicates an ellipsoidal main body surrounded by a thin shell, two ear-like protrusions, and additional small-scale structures. The corresponding kinematic ages are $3\,600 \pm 700$ yr for the ellipsoid and ring, and $7\,500 \pm 1\,000$ yr and $8\,800 \pm 1\,500$ yr for the two opposite ear-like protrusions, respectively, indicating that these outer structures predate the main nebular envelope. The kinematic asymmetry and enhanced emission regions suggest evolution within a non-uniform ambient medium. At the same time, the presence of collimated ear-like structures is consistent with shaping influenced by binary interaction, where earlier outflows preceded the ejection of the dense shell. NGC\,6563 therefore appears to be a dynamically evolved system shaped by the combined effects of episodic mass ejection and environmental interaction.
#### Title:
          Research on the Flat Field Measurement Method of Coronagraph
 - **Authors:** Yulong Feng, Xuefei Zhang, Hongfei Liang, Yu Liu, Mingzhe Sun, Tengfei Song, Mingyu Zhao
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
- **Arxiv link:** [https://arxiv.org/abs/2606.14569](https://arxiv.org/abs/2606.14569)
- **Pdf link:** [https://arxiv.org/pdf/2606.14569.pdf](https://arxiv.org/pdf/2606.14569.pdf)
- **Abstract**
 The solar corona has an extremely low density, and its brightness is only about one millionth of that of the photosphere. High-dynamic-range imaging of its faint structure is therefore essential for studying coronal heating, coronal mass ejections, and space weather. Quantitative coronagraph imaging requires flat-field measurement and calibration, which underpin intensity calibration, small-scale feature detection, and long-term cyclic analysis. This paper analyzes the coronagraph imaging chain and the origins of flat-field errors, including optical aberrations, stray light, and pixel-response non-uniformity, and summarizes the resulting calibration requirements of next-generation coronagraphs. On this basis, ground-based and space-based flat-fielding methods are systematically reviewed: the ground-based methods include integrating-sphere uniform light sources, opal glass/diffuser plates, clear-sky and thin-cloud backgrounds, and solar-disk scanning, while the space-based methods include internal light sources and diffuser plates, attitude-roll and off-corona offset observations, and multi-phase statistical self-consistent flat-fielding. Their accuracy, resource cost, and applicability are compared. The review shows that no single method is simultaneously high-precision, easy to update, and engineer-friendly; a hierarchical, multi-method calibration framework is therefore recommended. Finally, a new method is proposed in which lithographically generated structured light fields, combined with Fourier-optics and machine-learning inversion, are used to estimate the pixel-response function. Preliminary experiments show that this method achieves a lower residual error than the integrating-sphere and opal-glass methods, providing a high-precision reference for future wide-band, high-resolution coronagraph calibration.


by Al.Zn (Xin Lyu). 


2026-06-15
