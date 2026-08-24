# ISM Literature Recommender v2.1 — Contrastive SPECTER2

Generated: 2026-08-22T15:39:54Z
Lookback: last 10 days

## Summary

- All recent astro-ph candidates: **495**
- Current production keyword baseline selected: **66**
- Contrastive Priority A: **8**
- Contrastive Priority B: **63**
- Contrastive Priority C: **104**
- Contrastive SKIP: **320**
- Semantic-margin quantiles: `{'0.05': -0.0424, '0.1': -0.0353, '0.25': -0.0224, '0.5': -0.0078, '0.75': 0.0046, '0.9': 0.0166, '0.95': 0.0229}`

## Method

For every paper, SPECTER2 computes similarity to both positive ISM/star-formation topic anchors and explicit negative anchors (solar physics, stellar atmospheres/evolution, planetary science, compact objects, galaxy evolution/AGN, cosmology, generic instrumentation).

The primary signal is `best positive cosine - best negative cosine`. Exact specialist terms provide secondary evidence. Raw cosine values are retained; there is **no per-topic min-max normalization** and the display score is not a probability.

## Highest-ranked A/B candidates

### [A] 79.4 — Impact of Upstream Clumpiness on Supernova Remnant Forward Shock Evolution in Molecular Cloud Environments
- **arXiv:** [2608.17477](https://arxiv.org/abs/2608.17477)
- **Primary category:** astro-ph.HE
- **Positive anchor:** turbulence = 0.7540
- **Negative anchor:** cosmology_large_scale_structure = 0.7017
- **Semantic margin:** +0.0524
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** turbulence (0.7540), massive_star_formation (0.7249), molecular_clouds (0.7218)
- **Current keyword baseline:** NO
- **Abstract:** Supernova remnants (SNRs) are widely considered to be the primary accelerators of Galactic cosmic rays. In recent years, detailed observations have significantly progressed for young SNRs interacting with molecular clouds, a prime example being RX J1713.7-3946. When molecular clouds are clumpy, their impact can affect not only radiation properties but also shock wave propagation. Therefore, a quantitative understanding linking observational quantities with the ambient medium structure is highly required. In this study, we perform three-dimensional hydrodynamic simulations to model a molecular cloud with an inhomogeneous density structure driven by supersonic turbulence and subsequent SNR formation. To investigate various pre-supernova environments, we systematically vary the medium clumpiness by replacing gas below a threshold number density with a low-density hot gas, quantifying the relationship between the forward shock velocity and the volume filling factor of the high-density clumps. As a result, we find that at an elapsed time of 1000 yr-a typical age for a young SNR-the forward shock can evolve consistently with the fast shock velocity measured in RX J1713.7-3946, provided that the clump volume filling factor is approximately 10% or less. Considering that hadronic gamma-ray emission originates exclusively from the clumpy, high-density gas, our findings suggest that the total energy of cosmic-ray protons in RX J1713.7-3946 is higher than previously estimated, amounting to at least several percent of the typical supernova explosion energy.

### [A] 79.1 — ALOHA IRDCs Molecular Line Follow-up: I. Gas properties and kinematics
- **arXiv:** [2608.20238](https://arxiv.org/abs/2608.20238)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7783
- **Negative anchor:** planetary_disks_exoplanets = 0.7266
- **Semantic margin:** +0.0517
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** astrochemistry (0.7783), massive_star_formation (0.7678), molecular_clouds (0.7565)
- **Current keyword baseline:** YES
- **Abstract:** Infrared Dark Clouds are ideal sites for investigating the initial conditions of massive star and cluster formation. The A Lei Of the Habitat and Assembly of Infrared Dark Clouds (ALOHA IRDCs), a James Clerk Maxwell Telescope (JCMT) Large Program, has mapped nearby IRDCs with SCUBA-2. Complementary molecular line observations are needed to characterise the physical, kinematic, and chemical properties of the dense gas. We aim to determine the thermal, kinematic, and chemical properties of clumps identified in the ALOHA IRDCs, and to assess their evolutionary status and level of star-forming activity. We performed single-pointing K-band and W-band observations towards 56 ALOHA IRDCs clumps using the Effelsberg 100-m and Yebes 40-m telescopes, respectively. We derived NH3 kinetic temperatures using the hyperfine group ratio (HFGR) method and identified infall and shock signatures from HCO+, H13CO+, SiO, and HNCO profiles. Water masers and NH2D emission were used as complementary tracers of chemical evolution and star formation. The clumps exhibit kinetic temperatures of 15-29 K. We detect NH2D emission towards 18 sources, with NH2D centroid velocities consistent with NH3, indicating both species trace the same dense gas component. More than half of the clumps display blue-asymmetric HCO+ profiles, identifying them as infall candidates. Water masers are detected in 22 sources, with prominent velocity ranges and variability. Broad SiO emission (>~20 km/s) indicates strong shocks, while narrower extents (<~6km/s) likely trace large-scale interactions or low-velocity shocks. The widespread infall signatures, shock tracers, masers, and NH2D emission suggest that relatively quiescent, chemically young material can coexist with dynamically active gas affected by early protostellar feedback, providing insight into the coupled physical and chemical evolution of massive IRDC clumps.

### [A] 78.2 — Collisionless Shock Driven by a Supersonic Velocity Shear
- **arXiv:** [2608.16656](https://arxiv.org/abs/2608.16656)
- **Primary category:** astro-ph.HE
- **Positive anchor:** turbulence = 0.7136
- **Negative anchor:** stellar_atmospheres_evolution = 0.6584
- **Semantic margin:** +0.0552
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** turbulence (0.7136), molecular_clouds (0.6740), magnetic_fields (0.6649)
- **Current keyword baseline:** NO
- **Abstract:** The long-term evolution of a relativistic collisionless velocity shear in an unmagnetized electron-positron plasma is investigated using a first-principle particle-in-cell simulation. The Alves instability converts the shear kinetic energy into thermal and magnetic field energy. The resulting pressures push the plasma, leading to the formation of collisionless shocks. The generated collisionless shocks would accelerate high energy particles, which is a possible solution to the injection problem of shear acceleration. In addition, the collisionless shocks generate a magnetic field turbulence that is required for the shear acceleration to work.

### [A] 75.6 — Outflows in steep density gradients: diversity of behavior and implications for tidal disruption events and luminous fast blue optical transients
- **arXiv:** [2608.19512](https://arxiv.org/abs/2608.19512)
- **Primary category:** astro-ph.HE
- **Positive anchor:** turbulence = 0.7726
- **Negative anchor:** planetary_disks_exoplanets = 0.7233
- **Semantic margin:** +0.0493
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** turbulence (0.7726), molecular_clouds (0.7485), massive_star_formation (0.7395)
- **Current keyword baseline:** NO
- **Abstract:** Powerful explosions may undergo sustained energy injection as a central engine launches a wind into the surrounding gas, generating a forward and a reverse shock separated by a contact discontinuity. During the adiabatic phase, the dynamics depend strongly on the wind-to-ambient density ratio $f \equiv ρ_{\rm w} / ρ_{\rm a}$. For $f << 1$, the reverse shock lies well inside the contact discontinuity, and the mechanical energy deposited by the wind is retained in a radially extended, approximately isobaric shocked-wind region whose pressure drives the swept-up ambient shell. For $f \gg 1$, the reverse shock remains close to the contact, and the expansion is governed by the ram-pressure interaction between the freely expanding wind and the swept-up ambient gas. We use analytic scalings and one-dimensional shock-capturing hydrodynamic simulations to determine how outflows in these two limits evolve in ambient density profiles $ρ_{\rm a} \propto r^{-n}$, where $2 \leq n \leq 3$, and whether their shock structures accelerate or coast at constant velocity. For $n > 2$, initially underdense outflows produce accelerating forward shocks whose radii evolve as $R_{\rm s} \propto t^{3/(5-n)}$. Because $ρ_{\rm w} \propto r^{-2}$, f increases with radius, causing the reverse-shocked wind region to contract relative to the contact position as the forward shock transitions toward constant-velocity expansion. This occurs when $f \sim$ a few at $t_{\rm dec} \propto f_0^{1/(2-n)}$, where $f_0$ is the initial wind-to-ambient density ratio. By contrast, outflows initialized with $f_0 \gg 1$ do not develop an extended accelerating phase and remain approximately coasting throughout their adiabatic evolution. We discuss applications to tidal disruption event outflows and luminous fast blue optical transients, whose environments are often inferred to have steep density profiles with $n > 2$.

### [A] 72.8 — CHANG-ES XL: Magnetic Field Structures in the Disk and Halo of NGC 891
- **arXiv:** [2608.12275](https://arxiv.org/abs/2608.12275)
- **Primary category:** astro-ph.GA
- **Positive anchor:** magnetic_fields = 0.7728
- **Negative anchor:** planetary_disks_exoplanets = 0.7352
- **Semantic margin:** +0.0376
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** magnetic_fields (0.7728), galactic_ism_surveys (0.7341), astrochemistry (0.7265)
- **Current keyword baseline:** NO
- **Abstract:** We present new Karl G. Jansky Very Large Array S-band (2-4 GHz) observations of the edge-on spiral galaxy NGC 891, complemented by C-band data, to investigate the structure of its radio continuum halo. Using rotation measure synthesis we detected an extended polarized halo, with most spatially extended polarized emission confined to Faraday depths within +/- 150 rad m-2. We identified a localized region in the north-east side of the galaxy that shows an enhancement in polarized intensity (not in percentage polarization). By combining the radio data with H-alpha and diffuse X-ray maps, we discuss a possible origin for this structure: a superbubble powered by clustered supernovae. Across the disk and halo, the percentage polarization decreases toward the midplane but shows a mild wavelength dependence, despite the edge-on orientation of NGC 891. This behavior implies that the depolarization cannot be dominated by small-scale Faraday rotation within the disk. Instead, it is possible that most of the observed polarized emission arises on the Earth-facing side of the galaxy. Our peak rotation measure (RM) map shows a smooth transition along the major axis, consistent with a large scale axisymmetric magnetic field. Using H-alpha and UV data, we analyzed the distribution of H II regions and found that they are parts of different spiral arms. We also identified a faint, isolated H II region at a galactocentric radius of 16.9 kpc, with both H-alpha and far-UV counterparts, indicating star formation outside the thin disk.

### [A] 69.3 — High Velocity Neutral Gas in the Fermi Bubbles: New Kinematic Limits and Spatial Structure
- **arXiv:** [2608.16754](https://arxiv.org/abs/2608.16754)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7479
- **Negative anchor:** galaxy_evolution_agn = 0.7180
- **Semantic margin:** +0.0299
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7479), turbulence (0.7359), astrochemistry (0.7267)
- **Current keyword baseline:** YES
- **Abstract:** We have detected hundreds of neutral clouds entrained in the Milky Way's nuclear wind using HI data from new surveys made with the Green Bank Telescope that cover about 500 sq-degrees around the Galactic center (GC). Galactic winds are common throughout the Universe, and these data at 9.1' angular resolution (22 pc at the GC) provide the most detailed analysis of the vertical profile of a neutral nuclear wind in any galaxy. A set of 228 of these Fermi Bubble clouds with the largest values of |VLSR| has been analyzed to examine the distribution and kinematics of the outflowing gas. The clouds span -335 km/s $\leq$ VLSR $\leq$ +438 km/s, the largest positive LSR velocities ever reported for neutral HI associated with the Milky Way disk. The highest velocities are found furthest from the GC, suggesting that clouds are accelerated from a low velocity near the nucleus to at least 500 km/s at a radial distance of $\lesssim 4$ kpc. Clouds appear disrupted as they are accelerated: their line brightness and NHI decreases steadily with distance from the GC, and the population becomes more uniform. There is an abrupt cutoff in the neutral clouds at a vertical distance of $\approx2$ kpc from the Galactic plane. Kinematic models of an outflowing cloud population that fills the FB volume are used to identify structure in the gas. The kinematics of the highest velocity, highest latitude clouds imply a past azimuthal asymmetry in the outflow.

### [B] 68.4 — Automated Assignment and Prediction of Molecules in Astronomical Line Surveys Using Machine-Learning-Based Chemical Embeddings
- **arXiv:** [2608.18221](https://arxiv.org/abs/2608.18221)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7611
- **Negative anchor:** planetary_disks_exoplanets = 0.7277
- **Semantic margin:** +0.0334
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7611), molecular_clouds (0.7466), turbulence (0.7454)
- **Current keyword baseline:** YES
- **Abstract:** Modern radio telescopes generate vast amounts of observational data, offering valuable insights into the molecular composition of interstellar sources. Identifying the molecules within these datasets typically involves time-consuming and labor-intensive manual analysis. This paper presents an automated method for assigning molecules in interstellar line surveys. The algorithm operates in two main stages. First, it automatically determines key parameters of the data, including excitation temperature, line width, and source velocity. Next, it assigns the observed spectral peaks by evaluating the spectroscopic match of the molecular candidates along with analyzing their chemical relevance to the interstellar source. The chemical relevance is determined by leveraging machine-learning-based molecular embedding techniques to analyze the regions of chemical space occupied by the observed species. Following the line assignment, this information is then used to generate new molecular candidates that occupy the same regions of chemical space. These newly generated species serve as promising targets for further investigation in the observational data. The algorithm was validated on spectral line surveys of the dark molecular cloud TMC-1 and the star-forming region IRAS 16293-2422B. In both cases, it identified at least 67 molecular species, accounting for over 90 percent of the analyzed line intensity, in 17 minutes or less while maintaining a high level of accuracy.

### [B] 68.3 — High-spectral-resolution Observations of the [S II] Emission-line Doublet in the Filamentary Nebula Surrounding NGC 1275
- **arXiv:** [2608.14888](https://arxiv.org/abs/2608.14888)
- **Primary category:** astro-ph.GA
- **Positive anchor:** turbulence = 0.7473
- **Negative anchor:** generic_instrumentation = 0.7141
- **Semantic margin:** +0.0332
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** turbulence (0.7473), astrochemistry (0.7326), galactic_ism_surveys (0.7316)
- **Current keyword baseline:** NO
- **Abstract:** We analyze new high-spectral resolution SITELLE observations (R = $λ/Δλ$ = 7000) of the filamentary nebula surrounding NGC 1275, central galaxy of the Perseus cluster. We present here analysis of the \sii$\lambda6716$ and \sii$\lambda6731$ emission line doublet, using its ratio to determine the electron density of the optically emitting filaments. We compare these measurements with electron densities derived from deep Chandra X-ray observations of the intra-cluster medium (ICM) to determine if any correlations in density can be found. We report the detection of a clear dichotomy between the outer filaments, displaying on average lower \sii\text{ }emission line ratio of $\sim 1.1$ and the inner filaments displaying higher ratios of $\sim 1.3$. These results indicate that most of the gaseous filaments lie close to the low-density threshold for the density measurement of $\sim 10^2\text{ cm}^{-3}$. Using radial profiles, we find that the inner filaments have a roughly constant density, whereas the ICM density decreases with radius. In the outer filaments, we observe hints of local connections between the densities of the ICM and optical filaments, but no clear correlation seems to be observed overall. We also combined these density measurements with cold molecular CO gas observations to derive a relationship between temperature, density and pressure for the multiphase environment surrounding NGC 1275. Finally, we investigated potential models to explain the observed density measurements and explored similar studies of filamentary nebula around other central galaxies of cool-core galaxy clusters.

### [B] 67.7 — Interpretations of the $10\%$ polarization observed in the early forward-shock afterglow of GRB 091208
- **arXiv:** [2608.15494](https://arxiv.org/abs/2608.15494)
- **Primary category:** astro-ph.HE
- **Positive anchor:** magnetic_fields = 0.7213
- **Negative anchor:** planetary_disks_exoplanets = 0.6896
- **Semantic margin:** +0.0318
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** magnetic_fields (0.7213), turbulence (0.7058), molecular_clouds (0.6835)
- **Current keyword baseline:** NO
- **Abstract:** The $\sim10\%$ optical polarization observed at the early stage of GRB 091208B comes from the forward shock emission, which is higher than the conventionally predicted value. Polarizations of the forward shock radiation would depend on the observational geometry and the post-shock magnetic field structure. This magnetic field could arise either from the compression of a pre-existing magnetic field (i.e., the magnetic field in the outer medium) or from the shock-generated instabilities. In this paper, we use a synchrotron radiation model to fit the light curve and polarization observations of GRB 091208B. Two scenarios are considered: one is the case of a slightly off-axis observer, and the other is with a large-scale ordered magnetic field component in the burst environment. We found both scenarios could interpret the observations of GRB 091208B. For the slightly off-axis observation scenario, the observational angle is restricted to be within the range of (1.02, 1.05) times the jet half-opening angle. For the large-scale ordered magnetic field component scenario, the ratio between the ordered component to the random component is constrained to be around 1.

### [B] 67.5 — Chromospheric heating and magnetic topology above the shared penumbra of a delta-spot: Multi-line inversions and multi-height magnetic-field extrapolations
- **arXiv:** [2608.19983](https://arxiv.org/abs/2608.19983)
- **Primary category:** astro-ph.SR
- **Positive anchor:** magnetic_fields = 0.7591
- **Negative anchor:** galaxy_evolution_agn = 0.7277
- **Semantic margin:** +0.0314
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** magnetic_fields (0.7591), galactic_ism_surveys (0.7470), astrochemistry (0.7384)
- **Current keyword baseline:** NO
- **Abstract:** We analysed observations of the Fe I 617.3 nm, Ca II 854.2 nm, and Ca II H lines obtained with CRISP and CHROMIS at the SST. Spatially coupled non-LTE inversions constrained the chromospheric atmosphere, while the WFA provided estimates of the chromospheric line-of-sight magnetic field. We combined these photospheric and chromospheric constraints with an HMI magnetogram as input to a multi-height field extrapolation. We characterised the reconstructed topology using the twist number, squashing factor, current density, and field-line connectivity. Results. The Ca II H magnetic signal is concentrated mainly above the strongest photospheric field concentrations, whereas Ca II 854.2 nm yields stronger and more spatially extended line-of-sight fields. The chromosphere above the shared penumbra is approximately 300 K hotter than nearby quiet regions. The selected brightening follows a chromospheric loop, with enhanced temperature and a transition from blueshift to redshift along the structure. The extrapolation recovers field strengths broadly consistent with the inversions and reveals a left-handed, flux-rope-like core following the polarity inversion line. Enhanced currents and connectivity gradients occur near parts of its boundary, where field lines connect the twisted structure to overarching loops. Conclusions. The temperature and velocity patterns and magnetic topology are consistent with reconnection between the twisted polarity-inversion-line field and the surrounding loops, depositing energy in the chromosphere and driving plasma along reconfigured field lines. These signatures do not uniquely establish reconnection, but show that combining high-resolution spectropolarimetric inversions with multi-height extrapolations can relate chromospheric energy release to the local three-dimensional magnetic structure.

### [B] 67.1 — Physics of Circular Polarized Ion-Scale Waves in Hybrid Simulations of Alfvénic Fluctuations
- **arXiv:** [2608.14151](https://arxiv.org/abs/2608.14151)
- **Primary category:** physics.plasm-ph
- **Positive anchor:** turbulence = 0.7444
- **Negative anchor:** planetary_disks_exoplanets = 0.7063
- **Semantic margin:** +0.0381
- **Lexical positive/negative:** 0.0000 / 0.0000
- **Top positive topics:** turbulence (0.7444), magnetic_fields (0.7194), molecular_clouds (0.7014)
- **Current keyword baseline:** NO
- **Abstract:** Ion cyclotron waves (ICW) and fast magnetosonic/whistler waves (FMW) are fundamental electromagnetic modes at ion kinetic scales, yet their generation mechanisms and roles in plasma evolution remain poorly understood. We analyze a 2.5D hybrid simulation of broadband Alfvénic fluctuations, where the proton velocity distribution is modeled as a sum of two bi-Maxwellian components: a thermal core and a drifting beam. Using wavelet-based wave identification, bi-Maxwellian VDF fitting, and the PLUME linear dispersion solver, we find that ICW behave as linear modes. Growth is intermittent, occurring when core temperature anisotropy builds up, and is driven mainly by the core (the beam contributes negligibly). Poynting flux analysis shows that ICW are predominantly forward-propagating, with a net energy flux ratio of $+1$ across all frequencies, consistent with the initial condition. FMW present a stark contrast: PLUME solutions often yield very small (near-zero) linear growth/damping rates. The species decomposition breaks down when $|γ/ω_r| \gtrsim 0.368$, indicating that linear theory predicts these waves to be strongly damped and not describable by linear eigenmodes. Nevertheless, FMW are clearly observed in the wavelet helicity spectrogram, indicating that they are generated by nonlinear processes (e.g., parametric decay or phase steepening) and persist despite linear damping. The net energy flux ratio for FMW is close to $+1$ at low frequencies but decreases at higher frequencies, yet never reaches zero (net energy flow remains forward). These results demonstrate that ICW are linear, core-driven waves that transfer energy to the plasma, while FMW are heavily damped, nonlinearly generated waves.

### [B] 66.5 — Infrared Spectroscopy of Cyanonaphthalenes under Interstellar Relevant Conditions and Their Potential Connection with Astronomical Aromatic Infrared Bands
- **arXiv:** [2608.14964](https://arxiv.org/abs/2608.14964)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7605
- **Negative anchor:** planetary_disks_exoplanets = 0.7239
- **Semantic margin:** +0.0367
- **Lexical positive/negative:** 0.0000 / 0.0000
- **Top positive topics:** astrochemistry (0.7605), molecular_clouds (0.7322), atomic_ism (0.7314)
- **Current keyword baseline:** YES
- **Abstract:** Context. Aromatic infrared bands (AIBs) are widely observed in diverse astrophysical environments and are generally attributed to vibrational emission from polycyclic aromatic hydrocarbons (PAHs). The recent interstellar detection of 1-cyanonaphthalene (1-CNN) and 2-cyanonaphthalene (2-CNN) has motivated detailed infrared spectroscopic studies of cyano-substituted PAHs. Aims. We aim to characterize the infrared spectra and vibrational modes of neutral 1-CNN and 2-CNN under cold and gas-phase conditions and to assess their possible spectroscopic relevance to the astronomical AIBs. Methods. The gas-phase infrared spectra of neutral 1-CNN and 2-CNN were measured in a cold molecular beam using ion-dip spectroscopy. The observed bands were assigned with the aid of harmonic and anharmonic calculations at the B3LYP/N07D level. Infrared emission spectra were subsequently simulated from the experimental spectra within a single-photon approximation framework. Results. We report the infrared spectra of neutral 1-CNN and 2-CNN measured under cold and gas-phase conditions relevant to the interstellar medium. Their vibrational features were assigned in detail, including fundamental vibrations as well as overtone and combination bands. The simulated emission spectra exhibit features in several wavelength regions associated with prominent AIBs, including the aromatic CH stretching region near 3.3 micron, the CC stretching region near 6.2 micron, the mixed CH in-plane bending and CC stretching region at 8.6-8.9 microns, and the CH out-of-plane bending region between 10 and 15 microns. Conclusions. The present spectra provide laboratory reference data for small cyano-substituted PAHs and offer useful clues for interpreting selected AIB regions. These results suggest that cyanonaphthalene molecules are promising contributors to the aromatic infrared bands.

### [B] 65.4 — Diffuse HI emission in the circumgalactic medium of NGC891 and NGC4565 - III: azimuthal profiles
- **arXiv:** [2608.19186](https://arxiv.org/abs/2608.19186)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7573
- **Negative anchor:** stellar_atmospheres_evolution = 0.7307
- **Semantic margin:** +0.0266
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7573), astrochemistry (0.7376), magnetic_fields (0.7256)
- **Current keyword baseline:** NO
- **Abstract:** Diffuse HI emission in the circumgalactic medium (CGM) of NGC891 and NGC4565 has been previously shown to trace an inflow along minor axes pointings and to co-rotate with the HI disk along major axes pointings out to ~100 kpc (Das2020b,Das2024a). To obtain a 360$^\circ$ view of the inner neutral CGM ($\rm < 25 kpc$ for NGC891, $\rm < 30 kpc$ for NGC4565), we perform deep stare observations with the Green Bank Telescope (GBT) along the off-axes, 45$^\circ$ between principal axes, achieving a 5$σ$ column density sensitivity of $1.1-1.2 x 10^{17} \rm cm^{-2}$ over a 20 kms$^{-1}$ velocity width. While detecting HI emission in the inner CGM with single-dish telescopes is common, separating the true CGM emission from disk contamination is extremely challenging and has so far been largely unsuccessful. To achieve that, we compare our single-dish detections to deep interferometric maps from the Westerbork Synthesis Radio Telescope (WSRT) HALOGAS survey, and improve upon our previous methods by incorporating velocity offset corrections and channel-wise brightness-temperature scaling. We find that $30-38$ % and $18-28$ % of the emission detected by the GBT cannot be explained by WSRT in NGC891 and NGC4565, respectively, implying a true CGM detection. There is $4-6$ ($3-7$) times more HI along the off-axes than major (minor) axes, nullifying the common assumption of azimuthal symmetry of the neutral CGM. The velocity profile of the diffuse inner CGM suggests a lagged co-rotation with the HI disk in both galaxies. This exercise illustrates the power of deep observation and careful cross-instrument comparisons to characterize the diffuse HI in the CGM.

### [B] 64.8 — Strangeness Transport in Binary Neutron Star Mergers
- **arXiv:** [2608.15527](https://arxiv.org/abs/2608.15527)
- **Primary category:** astro-ph.HE
- **Positive anchor:** turbulence = 0.7256
- **Negative anchor:** cosmology_large_scale_structure = 0.6851
- **Semantic margin:** +0.0405
- **Lexical positive/negative:** 0.0000 / 0.2835
- **Top positive topics:** turbulence (0.7256), astrochemistry (0.6897), feedback_bubbles (0.6832)
- **Current keyword baseline:** NO
- **Abstract:** The presence of hyperons in the cores of neutron stars opens fast strangeness equilibration channels that can produce bulk-viscous dissipation during binary inspiral. Because these reactions coexist with electron $β$-equilibration, tidal compression can drive the two coupled chemical imbalances far beyond linear response. We construct the first reaction network that self-consistently evolves the electron and strangeness fractions with a four-dimensional strangeness-dependent chiral mean-field (CMF) equation of state, including nucleonic and hyperonic Urca processes and non-leptonic hyperon reactions. For periodic density perturbations, representative of inspiral oscillations, we find that rapid strangeness conversion can generate a large $β$-imbalance, after which slow $β$-equilibration bottlenecks strangeness relaxation. Rather than decaying exponentially, the coupled system consequently exhibits dynamically important algebraic decay in a far-from-equilibrium regime. At the $\rm keV$ temperatures expected during inspiral, this nonlinear response produces a broad enhancement of the effective bulk viscosity, reaching $\sim10^{31}\,\mathrm{g\,cm^{-1}\,s^{-1}}$ for $320$ Hz oscillations. A phenomenological estimate of continuous inspiral dissipation yields gravitational-wave phase shifts up to $\sim0.14$ rad for neutron stars with hyperonic cores. Self-consistent, far-from-equilibrium strangeness transport may therefore provide a dynamical probe of hyperons in neutron-star interiors.

### [B] 64.5 — Complex morphology and kinematics at the heart of the very low luminosity object IRAM 04191+1522
- **arXiv:** [2608.17593](https://arxiv.org/abs/2608.17593)
- **Primary category:** astro-ph.SR
- **Positive anchor:** molecular_clouds = 0.7678
- **Negative anchor:** planetary_disks_exoplanets = 0.7571
- **Semantic margin:** +0.0107
- **Lexical positive/negative:** 0.8111 / 0.0000
- **Top positive topics:** molecular_clouds (0.7678), astrochemistry (0.7543), massive_star_formation (0.7372)
- **Current keyword baseline:** YES
- **Abstract:** The formation of the majority of brown dwarfs (BDs) remains uncertain. They may form in molecular cloud cores in a process akin to low mass star formation, or via fragmentation in circumstellar discs. Studying the youngest, most embedded sources is crucial for distinguishing these scenarios. We investigate molecular gas morphology and kinematics around one young & embedded very low luminosity object (VeLLO), IRAM 04191+1522, utilising archival ALMA observations of 13CO, C18O, and SO. We trace gas on scales of a few 10s to 100s of au around the source to search for outflowing and/or infalling structures. The red and blueshifted 13CO (3-2) emission show distinct morphologies and kinematics. The blueshifted emission to the north-west may trace shocked material oriented differently from the previously reported approx. 0.1 pc CO outflow. Redshifted emission mainly to the south-east and south-west may trace the base of an outflow cavity. The position angle of this cavity suggests the presence of a second outflow, which supports the possible binary nature of this VeLLO. The C18O (2-1) emission is highly complex, comprising structures at different spatial scales and distances from the source. These may trace a mix of molecular outflow, outflow cavity, and disc emission. SO 65-54 reveals evidence for anticlockwise rotation around the central source, together with a northern structure of uncertain origin. We have identified a complex set of 13CO (3-2) and C18O (2-1) structures alongside evidence of a new outflow cavity at a distinct position angle from previously detected outflows. This supports the scenario that IRAM 04191+1522 is a binary system. The northern SO gas structure remains unexplained. Higher spectral resolution observations at intermediate scales are needed to characterise these substructures, their connection to larger scale structures, and to determine this system's final fate.

### [B] 63.8 — Aromatics and Aliphatics in Local Star-Forming Galaxies as Probed by AKARI
- **arXiv:** [2608.14989](https://arxiv.org/abs/2608.14989)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7795
- **Negative anchor:** planetary_disks_exoplanets = 0.7489
- **Semantic margin:** +0.0307
- **Lexical positive/negative:** 0.2835 / 0.2835
- **Top positive topics:** astrochemistry (0.7795), massive_star_formation (0.7529), atomic_ism (0.7458)
- **Current keyword baseline:** NO
- **Abstract:** Polycyclic aromatic hydrocarbon (PAH) molecules are abundant and widespread in galaxies and their infrared (IR) emission traces star formation. PAH molecules in astronomical environments often have aliphatic contents as revealed by the detection of the 3.4 micron aliphatic C--H stretch, a weak satellite feature accompanying the 3.3 micron aromatic C--H stretch. Here, we selected 102 local star-forming galaxies from the AKARI archive, including 66 galaxies each of which hosts an active galactic nucleus (AGN). We analyzed their AKARI near-IR spectra, which exhibit pronounced 3.3 micron aromatic and 3.4 micron aliphatic C--H emission. We also compiled their multi-wavelength photometric data and performed a decompositional analysis of their spectral energy distributions (SEDs) from the ultraviolet (UV) to the far-IR to derive the star formation rates (SFRs), stellar masses, metallicities, and luminosity of the galaxies. We explored the 3.3 micron PAH emission luminosity ($L_{3.3}$) as a calibrator of the SFR and found a close agreement with previous studies. We also found that $L_{3.3}/L_{\rm IR}$ and $L_{3.4}/L_{\rm IR}$ exhibit a strong dependence on metallicity, but remain nearly constant above 12+log(O/H)$\sim\,$8.5, where $L_{\rm IR}$ is the total luminosity emitted by dust, and $L_{3.4}$ is the luminosity of the 3.4 micron aliphatic emission. We derived from $L_{3.4}/L_{3.3}$ the PAH aliphatic fractions, defined as the fractions of carbon atoms in aliphatic units, to be in the range of $\sim\,$0.38%--6.8%, with a median fraction of $\sim\,$3.1%. The PAH aliphatic fractions are lower in AGN hosts and show a weak negative correlation with the SFR and $L_{\rm IR}$, suggesting that UV photons in regions with AGN or strong star formation activities may photodissociate the aliphatic structures associated with PAH molecules.

### [B] 63.7 — The CMZ Asymmetries: Feeding or Feedback?
- **arXiv:** [2608.13734](https://arxiv.org/abs/2608.13734)
- **Primary category:** astro-ph.GA
- **Positive anchor:** molecular_clouds = 0.7210
- **Negative anchor:** cosmology_large_scale_structure = 0.7034
- **Semantic margin:** +0.0176
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** molecular_clouds (0.7210), galactic_ism_surveys (0.7126), astrochemistry (0.7074)
- **Current keyword baseline:** YES
- **Abstract:** Three-fourths of the dense gas and dust in the CMZ is located at positive longitudes and positive radial velocities. The majority of compact 24 micrometer wavelength sources are at negative longitudes. These two asymmetries indicate either a recent asymmetric injection of gas along the bar dust lanes, or that most of the molecular gas is contained in a small number of massive, gravitationally bound clouds, or a major feedback episode which dissociated an entire sector of the CMZ's dense gas.

### [B] 63.7 — ALMA observations of pre-JWST z ~ 10 galaxy candidates: A CO(J = 9-8) line from a ULIRG at z = 2.54 and revisit of the photometric redshifts with JWST photometry
- **arXiv:** [2608.12708](https://arxiv.org/abs/2608.12708)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7709
- **Negative anchor:** galaxy_evolution_agn = 0.7480
- **Semantic margin:** +0.0229
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7709), atomic_ism (0.7616), massive_star_formation (0.7596)
- **Current keyword baseline:** NO
- **Abstract:** We present Atacama Large Millimetre/submillimetre Array (ALMA) observations targeting the [OIII]$88\,μ$m line for six $z\sim10$ galaxy candidates selected with the Hubble Space Telescope and the Spitzer Space Telescope. We detect a line ($4.5σ$) and dust continuum emission ($30σ$) in UDS_18697, while detecting neither robust line nor continuum emission in the remaining five objects. The detected line in UDS_18697 is identified as CO($J=9-8$), because follow-up James Webb Space Telescope (JWST) NIRSpec observations have confirmed the redshift as $z=2.54$. UDS_18697 is classified as an ultra luminous infrared galaxy (ULIRG) with far-infrared (FIR) luminosity of $L_\mathrm{FIR}\approx1.1\times10^{12}\,L_\odot$, assuming a dust temperature of $T_\mathrm{d}\approx42\,$K, estimated using a physically-motivated method. We find that UDS_18697 follows the $L_\mathrm{FIR}-L'_\mathrm{CO}$ relation for local and $z>2$ galaxies, albeit being slightly brighter in CO($J=9-8$). Also, based on the follow-up NIRSpec observations and spectral energy distribution fitting using JWST/NIRCam photometry, we found that most of our targets are suggested to be low-$z$ interlopers. Motivated by these redshift misclassifications, we investigate colour--colour selection criteria for high-$z$ galaxies using JWST spectroscopic survey catalogues. We find that elevating a colour threshold tracing the Lyman break is crucial for constructing a robust high-$z$ sample, particularly for wide field surveys such as Euclid Deep Fields and Roman High-Latitude Wide-Area Survey.

### [B] 63.5 — The efficient star-forming regions of stripped-envelope supernovae
- **arXiv:** [2608.18897](https://arxiv.org/abs/2608.18897)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7478
- **Negative anchor:** galaxy_evolution_agn = 0.7307
- **Semantic margin:** +0.0170
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** astrochemistry (0.7478), galactic_ism_surveys (0.7445), massive_star_formation (0.7359)
- **Current keyword baseline:** NO
- **Abstract:** Massive stars ($> 8~\rm{M}_{\odot}$) play a key role in shaping the interstellar medium of galaxies through stellar feedback. However, how these stars form and evolve before exploding as core-collapse supernovae (SNe) remains elusive. We compute for the first time the star-formation efficiencies (SFEs) at the locations of hydrogen-rich (H-rich) SNe and stripped-envelope SNe (SESNe) to constrain their progenitor properties. We used VLT/MUSE and ALMA observations of H$α$/H$β$ and CO(2-1) emission lines to trace the components of the warm ionised gas and cold molecular gas, respectively. Both observations resolve individual H II regions and giant molecular clouds at spatial resolutions on cloud-scales ($\sim$100 pc). This combined data allows us to compute the SFE from the star formation rate (SFR) and the molecular gas mass (M$_{\rm{mol}}$) as SFE = SFR/M$_{\rm{mol}}$. We find that SESNe explode in environments that are currently forming stars eight times more efficiently than those of H-rich SNe (higher SFR for SESNe with similar M$_{\rm{mol}}$). On one hand, this is consistent with the scenario in which the majority of SESNe are produced from very massive stars ($> 20~\rm{M}_{\odot}$) if the initial mass function is top-heavy. On the other hand, most of SESN progenitor channels are formed from interacting binaries ($< 20~\rm{M}_{\odot}$) if an increased binary system formation rate is connected with turbulences and, in turn, with the boost to SFE. Then, an increased binary fraction could explain the enhanced H$α$ luminosities. In summary, SESNe preferentially occur in regions of intense, efficient star formation rather than simply higher gas content.

### [B] 63.4 — A self-consistent solar coronal heating model by Alfvenic waves
- **arXiv:** [2608.15221](https://arxiv.org/abs/2608.15221)
- **Primary category:** astro-ph.SR
- **Positive anchor:** magnetic_fields = 0.7320
- **Negative anchor:** solar_physics = 0.7190
- **Semantic margin:** +0.0130
- **Lexical positive/negative:** 0.6321 / 0.0000
- **Top positive topics:** magnetic_fields (0.7320), turbulence (0.7225), astrochemistry (0.7020)
- **Current keyword baseline:** NO
- **Abstract:** Alfvenic waves are prevalent throughout the solar atmosphere and are believed to play an essential role in coronal heating, classified as alternating current (AC) heating in contrast to direct current (DC) heating associated with quasi-static magnetic field line braiding. The relative importance of AC versus DC heating depends on the details of the photospheric driver and on the configuration of the magnetic field. Moreover, even if AC heating prevails, several wave dissipation mechanisms have been proposed, and which of them dominates remains unclear, as its efficiency depends on plasma compressibility and density inhomogeneity. We address these issues by performing three-dimensional radiative magnetohydrodynamic (MHD) simulations of a coronal loop spanning from the upper convection zone to the corona, which self-consistently capture many relevant physical processes. We find that the corona is predominantly heated by AC heating, with Alfven wave turbulence providing the primary contribution, accounting for at least 80% of the entire coronal heating in the present simulation. Our results strongly support the use of Alfven wave turbulence-based models employed in space weather and stellar activity research, such as the Alfven Wave Solar Model (AWSoM) and the Magnetohydrodynamic Algorithm outside a Sphere (MAS).

### [B] 62.8 — The Nearby Star Formation and Supernova Histories Reconstructed from Young Star Clusters
- **arXiv:** [2608.20307](https://arxiv.org/abs/2608.20307)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7447
- **Negative anchor:** planetary_disks_exoplanets = 0.7292
- **Semantic margin:** +0.0155
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** astrochemistry (0.7447), massive_star_formation (0.7261), galactic_ism_surveys (0.7255)
- **Current keyword baseline:** YES
- **Abstract:** We reconstruct the recent star formation and core-collapse supernova (ccSN) histories of the Solar Neighborhood from the past trajectories of young star clusters. Using a \textit{Gaia}-based cluster sample with newly derived ages, masses, and bulk 3D velocities, we integrate orbits backward in an assumed axisymmetric Galactic potential and combine the trajectories with IMF sampling and stellar lifetimes to infer ccSN times and locations over the past 50 Myr. The result is an all-sky, 3D, time-resolved map of nearby ccSN activity for comparison with high-resolution 3D views of the local interstellar medium. The 0--15 Myr map shows strong enhancements toward Orion, Vela, Sco--Cen, and Cepheus, many within present-day cavities and shells. At earlier times, the dominant enhancements trace the Collinder 135, Messier 6, and Alpha Persei cluster families, showing how the remnants of massive star-forming complexes have shaped the recent local feedback history. We recover a bursty star formation history followed by a delayed, smoother ccSN history. Over the last 40 Myr, the mean star formation and ccSN rates are \(823~M_\odot~\mathrm{Myr}^{-1}\) and \(7.7~\mathrm{Myr}^{-1}\), respectively, corresponding to a Milky Way rate of \(0.55\pm0.03~\mathrm{century}^{-1}\). Present-day OB-star catalogs yield rates ranging from agreement with the cluster reconstruction to several times higher. Because the catalogs overlap weakly and require different corrections, we do not rescale the ccSN map. Our reconstruction provides an empirical framework for connecting the recent history of massive-star feedback to the 3D structure and life cycle of gas in the nearby Milky Way.

### [A] 62.2 — Large-Scale Dynamos Driven by Shear-Flow-Induced Jets
- **arXiv:** [2608.12530](https://arxiv.org/abs/2608.12530)
- **Primary category:** astro-ph.SR
- **Positive anchor:** turbulence = 0.7375
- **Negative anchor:** cosmology_large_scale_structure = 0.7157
- **Semantic margin:** +0.0217
- **Lexical positive/negative:** 0.4866 / 0.2835
- **Top positive topics:** turbulence (0.7375), magnetic_fields (0.7196), molecular_clouds (0.7068)
- **Current keyword baseline:** NO
- **Abstract:** At every scale they occupy, magnetic fields affect various phenomena, including star formation, cosmic ray transport, charged particle acceleration, space weather, transport in planetary atmospheres, and laboratory plasmas. These fields are often generated and sustained by turbulent flows in a process called the dynamo. In 1955, E. N. Parker parameterized the effects of small-scale turbulence to propose a mean-field dynamo theory. The widely used theory reproduces observed large-scale fields but suffers from difficulty in tuning parameters as they are not justified from first principles: Studies of turbulent flows show tangled magnetic fields, which are folded and fragmented into small-scale structures due to shear-flow straining. Here, considering a shear flow that is unstable and driven, we develop analytic theory and perform three-dimensional (3D), advanced computer simulations of turbulence with up to 4096 x 4096 x 8192 grid points, showing ab initio generation of quasi-periodic, large-scale magnetic fields. The generation occurs via the mean-vorticity effect---an additional mean-field dynamo process postulated in 1990. Crucial to this dynamo is the prior generation of large-scale 3D jets, robustly produced as topologically protected and exact nonlinear solutions of the magnetohydrodynamic equations. The jet-driven dynamo applies to shear-driven laboratory and astrophysical systems. These include binary neutron star mergers, where the reported dynamo likely operates on microsecond timescales to produce in milliseconds some of the strongest magnetic fields in the Universe, providing signals for multimessenger astronomy.

### [A] 62.1 — Star Formation in the H II Region Sh 2-205: 3D Morphology and Kinematics from Young Stars and Molecular Gas
- **arXiv:** [2608.16179](https://arxiv.org/abs/2608.16179)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7679
- **Negative anchor:** planetary_disks_exoplanets = 0.7464
- **Semantic margin:** +0.0214
- **Lexical positive/negative:** 0.4866 / 0.2835
- **Top positive topics:** astrochemistry (0.7679), galactic_ism_surveys (0.7504), molecular_clouds (0.7346)
- **Current keyword baseline:** NO
- **Abstract:** Using Gaia astrometry of young stars combined with CO observations, we present the first systematic three-dimensional (3D) analysis of the structure, kinematics, and evolutionary history of the star-forming regions in the environs of the H II region Sh 2-205 (S205). S205 exhibits a complex morphology and coherent expansion on both global and subregional scales. We identify several O9-B1 stars and a 0.56 Myr old pulsar that are likely associated with the region. A momentum estimate suggests that feedback from these objects may account for the observed overall expansion. Trace-back analysis of the expansion, combined with color-magnitude diagram fitting for young star clusters, indicates at least two episodes of star formation. These results reveal a complex star-formation history of S205 and provide new insights into its 3D evolution.

### [B] 61.9 — Confining density functional approach to the QCD phase diagram at low temperatures and thermal twin stars
- **arXiv:** [2608.18038](https://arxiv.org/abs/2608.18038)
- **Primary category:** nucl-th
- **Positive anchor:** turbulence = 0.7002
- **Negative anchor:** cosmology_large_scale_structure = 0.6737
- **Semantic margin:** +0.0265
- **Lexical positive/negative:** 0.2835 / 0.2835
- **Top positive topics:** turbulence (0.7002), astrochemistry (0.6858), star_formation (0.6689)
- **Current keyword baseline:** NO
- **Abstract:** We present a density functional-based equation of state for warm, dense nuclear matter with a transition to deconfined quark matter for applications to simulations of supernova explosions and neutron star mergers, but also for the cosmological evolution of Q-balls. For the quark matter equation of state, we employ a recently developed confining density functional approach while nuclear matter is described within a relativistic density functional model of the DD2 class. The phase transition is obtained by a Maxwell construction at constant entropy per baryon. We discuss the solutions of TOV equations for isentropic hybrid stars for the hybrid equation of state model DDf-SFM (DD2-$χ$CDF) without (with) color superconductivity and find that at finite temperatures above a critical value of entropy per baryon sequences of disconnected third family branches ("thermal twin stars") may appear for the DDf-SFM model, while they are absent for the color superconducting model and at $T=0$. We discuss the relation of this critical entropy per baryon to the Seidov criterion of gravitational instability for $T=0$ and find that it is a good guide. We suggest that the presence of thermal twin stars may be regarded as an indicator for the core-collapse supernova explodability of massive blue supergiant stars and thus serve as a new criterion for the reliability of hybrid equation of state models. By this argument, strong color superconductivity shall be excluded and it remains to be shown whether models with moderate diquark pairing could fulfill the thermal twin constraint. For the case of symmetric matter, we compare the resulting hybrid EOS with the flow constraint by Danielewicz et al. and find a a sensitivity of the onset density for deconfinement on the presence or absence of color superconductivity.

### [B] 61.9 — Massive cold hybrid stars in a modified Polyakov-Nambu-Jona-Lasinio model
- **arXiv:** [2608.12653](https://arxiv.org/abs/2608.12653)
- **Primary category:** hep-ph
- **Positive anchor:** turbulence = 0.7279
- **Negative anchor:** cosmology_large_scale_structure = 0.7016
- **Semantic margin:** +0.0264
- **Lexical positive/negative:** 0.0000 / 0.0000
- **Top positive topics:** turbulence (0.7279), astrochemistry (0.6956), magnetic_fields (0.6909)
- **Current keyword baseline:** NO
- **Abstract:** We propose a modified Polyakov-loop Nambu--Jona-Lasinio (mPNJL) model in which the Polyakov potential is given by an explicit dependence on the quark chemical potential, allowing it to remain finite at zero temperature and thus to describe the confinement-deconfinement transition in cold dense matter. Combining this modified quark sector with hadronic equations of state via a Maxwell construction, we find that, depending on the model parameters, the equation of state can exhibit either two phase transitions, from hadronic matter to confined (quarkyonic) quark matter and subsequently to deconfined quark matter, or a single transition directly from hadronic to deconfined quark matter or from hadronic to quarkyonic quark matter. Stable massive cold hybrid stars with only quarkyonic and/or deconfined quark phase are obtained. We systematically examine how the parameters of the modified Polyakov potential and the quark vector interactions control the location of these transitions, and find that repulsive vector interactions are essential to obtain a stable quark core. Hybrid stars with quarkyonic and/or a deconfined core can reach maximum masses above $2M_\odot$, provided a sufficiently stiff hadronic equation of state is used at low density. In the core of the maximum-mass configurations, the speed of sound exceeds the conformal limit, $c_s^2 = 1/3$, for the quarkyonic core stars. This work establishes the qualitative role of each model parameter in shaping hybrid-star structure.

### [B] 61.7 — Multiphase turbulence as the origin of OH+, H2O+ and H3+ column density scatter in the local ISM
- **arXiv:** [2608.15633](https://arxiv.org/abs/2608.15633)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7647
- **Negative anchor:** galaxy_evolution_agn = 0.7515
- **Semantic margin:** +0.0131
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** astrochemistry (0.7647), turbulence (0.7535), galactic_ism_surveys (0.7477)
- **Current keyword baseline:** NO
- **Abstract:** Observations of the reactive ions OH+, H2O+ and H3+ in the Galactic interstellar medium reveal large sight-line-to-sight-line scatter in their column densities, commonly interpreted as evidence for substantial variations in the cosmic-ray ionization rate (CRIR). We revisit this interpretation using high-resolution three-dimensional magneto-hydrodynamic simulations of the multiphase ISM with time-dependent chemistry for H, H2, H+ and electrons, building on the fiducial model of Godard et al. (2023). We find that a single CRIR of ~2 10^{-16} s^{-1}, together with standard Galactic-scale parameters, naturally produces broad column-density distributions for all three tracers in good agreement with the observed medians and percentile widths, with no fine tuning. Reaching this match requires that the post-processing of OH+, H2O+ and H3+ retain the time-dependent H2 field generated by the turbulent flow rather than assume chemical equilibrium: turbulence drives long-lived H2 enhancements in the unstable neutral medium where OH+ and H2O+ predominantly reside, and an equilibrium treatment under-predicts their columns substantially. H3+, which receives most of its column from denser CNM gas closer to equilibrium, is much less affected. Our results caution against interpreting sight-line-to-sight-line scatter as direct evidence for large CRIR fluctuations, and motivate a shift from independent 1D equilibrium analyses toward 3D dynamical frameworks when inferring ionization conditions in the ISM.

### [B] 61.4 — Radio Properties of RS Canum Venaticorum Variables in VLASS and RACS
- **arXiv:** [2608.13653](https://arxiv.org/abs/2608.13653)
- **Primary category:** astro-ph.SR
- **Positive anchor:** astrochemistry = 0.7516
- **Negative anchor:** planetary_disks_exoplanets = 0.7188
- **Semantic margin:** +0.0328
- **Lexical positive/negative:** 0.0000 / 0.2835
- **Top positive topics:** astrochemistry (0.7516), massive_star_formation (0.7235), ism_methods_data (0.7232)
- **Current keyword baseline:** NO
- **Abstract:** We performed a systematic search for radio emission from RS Canum Venaticorum (RS CVn) binaries, selected from the International Variable Star Index (VSX) catalog, in the Very Large Array Sky Survey (VLASS; three epochs) and Rapid ASKAP Continuum Survey (RACS; two epochs) data. We detected 108 candidate radio-emitting RS CVn in at least one epoch. Several of these systems rank among the most radio-luminous RS CVn binaries reported to date. The radio and X-ray luminosities, obtained from cross-matching with the eROSITA and ROSAT X-ray catalogs, are consistent with the Guedel-Benz relation for magnetically active stars, but are also comparable to radio-luminous quiescent black hole X-ray binaries, indicating a potential for misidentification between these two classes. Analysis of optical, radio, and stellar properties indicates that optically bright RS CVn (i.e., those with at least one giant component) are radio-quieter and have periods that are consistent with lower coronal activity. However, two of these optically bright RS CVn systems show persistent and unusually high radio specific luminosities (>2e17 erg/s/Hz) across all observed epochs, showing that stellar activity can produce relatively persistent radio signals as bright as quiescent black hole binaries.

### [B] 61.3 — Correlations with Magnetic Activity in the Solar Near-Surface Shear Layer. I. Rotation
- **arXiv:** [2608.19438](https://arxiv.org/abs/2608.19438)
- **Primary category:** astro-ph.SR
- **Positive anchor:** magnetic_fields = 0.7066
- **Negative anchor:** cosmology_large_scale_structure = 0.6891
- **Semantic margin:** +0.0175
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** magnetic_fields (0.7066), galactic_ism_surveys (0.6987), astrochemistry (0.6882)
- **Current keyword baseline:** NO
- **Abstract:** We used data from the Helioseismic and Magnetic Imager to determine the rotation rate of the near-surface shear layer and its time variation. We applied the ring-diagram analysis technique allowing us to probe the layer between the depths of 1 Mm and 17 Mm. We find that the rotation rate increases inwards; it reaches values consistent with those inferred from global helioseismic analyses in the deeper layers, however, there are differences in the rotation rate of the northern and southern hemispheres. We show that the time variation of the rotation rate can be determined even without subtracting the time-averaged rotation rate from each epoch; however, such a subtraction is needed to get the canonical ``torsional oscillation'' signal. We find that even at depths as shallow as 1 Mm, the rotation rate shows the typical torsional oscillation pattern. The cumulative zonal displacement inferred from the residual flows exhibits a pronounced high-latitude hemispheric asymmetry and varies on solar-cycle timescales; at $75^\circ$ it shows an apparent temporal association with the polar magnetic field. We find significant correlations between the cumulative displacement and magnetic activity at a subset of latitudes, with multi-year lags: the displacement leads activity by ~5 years near $15^\circ$, whereas at higher latitudes activity leads by ~4 years. At mid to high latitudes, the inferred lags show a hemispheric dependence, with activity tending to lead in the north and lag in the south, suggesting possible hemispheric differences in the timing of cycle evolution and motivating longer time series to test cycle-to-cycle variation.

### [B] 61.2 — Why is GN-z11 Bright, Compact, and Nitrogen Enhanced? Insights from UV Absorption and Emission Diagnostics
- **arXiv:** [2608.12466](https://arxiv.org/abs/2608.12466)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7657
- **Negative anchor:** stellar_atmospheres_evolution = 0.7408
- **Semantic margin:** +0.0248
- **Lexical positive/negative:** 0.2835 / 0.2835
- **Top positive topics:** astrochemistry (0.7657), massive_star_formation (0.7459), turbulence (0.7335)
- **Current keyword baseline:** NO
- **Abstract:** We investigate the UV spectrum of GN-z11, a luminous, compact galaxy with strong nitrogen lines, at $z=10.60$, using deep JWST/NIRSpec high-resolution IFU and medium-resolution MSA spectra assembled from the JADES, SPURS, and GO programs. After optimized reduction and extraction of the IFU data including an evaluation of statistical and systematic uncertainties, we obtain mutually consistent spectra from the high- and medium-resolution observations. After carefully accounting for the data quality limitations, we identify prominent P-Cygni profiles in NV$λ\lambda1238,1243$, SiIV$λ\lambda1394,1403$, and CIV$λ\lambda1548,1550$, together with broad NIV]$λ\lambda1483,1486$ emission (FWHM $\sim1600$ km s$^{-1}$). The P-Cygni profiles resemble those of massive stars such as O-type stars and luminous blue variables (LBVs), while the broad NIV] emission resembles that of nitrogen-sequence Wolf-Rayet (WN) stars. We fit stellar and active galactic nuclei (AGN) UV spectral models and find that the stellar models are strongly preferred over the AGN models ($Δ$WAIC $=-25$), with the preference driven primarily by the NV P-Cygni profile. These results indicate that the luminous, compact UV continuum of GN-z11 is dominated by massive stars. We derive electron densities from CIII]$λ\lambda1907,1909$, NIII]$λ\lambda1747-1754$, and NIV], with the nitrogen diagnostics extending well beyond the CIII]-based limit and reaching densities of $\gtrsim10^{6.5}$ cm$^{-3}$ for NIV], indicating physically distinct carbon- and nitrogen-emitting nebular components. These findings suggest that the apparent nitrogen enhancement inferred for GN-z11 as a whole may arise when strong narrow nitrogen emission originates from dense gas locally enriched in nitrogen by WN stellar winds and photoionized by nearby massive stars within the same star-forming region.

### [B] 61.0 — pynucastro 3: A community library for nuclear astrophysics
- **arXiv:** [2608.17049](https://arxiv.org/abs/2608.17049)
- **Primary category:** astro-ph.IM
- **Positive anchor:** astrochemistry = 0.7325
- **Negative anchor:** stellar_atmospheres_evolution = 0.7079
- **Semantic margin:** +0.0245
- **Lexical positive/negative:** 0.0000 / 0.0000
- **Top positive topics:** astrochemistry (0.7325), turbulence (0.7318), ism_methods_data (0.7199)
- **Current keyword baseline:** NO
- **Abstract:** We describe the latest release of pynucastro: a community python library for nuclear astrophysics. The goal of the pynucastro project is to build the tools needed to interactively explore nuclear properties, reaction rates, and networks, and to export these networks to a variety of simulation codes. Major changes in pynucastro since the last major release include new rate approximations, a stellar equation of state, support for the StarLib library and rate uncertainties, and new tools for exploring networks.

### [B] 61.0 — Two domains of extended Lyman-alpha emission around galaxies: from local radiation to environmental regulation
- **arXiv:** [2608.16665](https://arxiv.org/abs/2608.16665)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7510
- **Negative anchor:** galaxy_evolution_agn = 0.7341
- **Semantic margin:** +0.0169
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7510), atomic_ism (0.7313), astrochemistry (0.7276)
- **Current keyword baseline:** NO
- **Abstract:** We examine the relation between extended Ly$α$ halos around high-redshift galaxies and the main factors responsible for driving the emission in such halos, in particular at distances around and beyond one virial radius $r_\mathrm{vir}$. To reach the required surface brightness sensitivity we take advantage of the MUSE eXtremely Deep Field (MXDF) survey, allowing us to probe levels as faint as $\sim 10^{-20}$ erg cm$^{-2}$ s$^{-1}$ arcsec$^{-2}$ in individual Ly$α$ halos. Our sample consists of the 21 apparently core- and halo-brightest (yet intrinsically low luminosity $\log_{10}$L$_{\mathrm{Ly}α} < 42.3$ erg s$^{-1}$) Ly$α$ emitters (LAEs) in the MXDF at $3<z<4$, with typical virial radii around 20 kpc. We measure their radial surface brightness profiles out to 50 kpc (more than $2r_{\mathrm{vir}}$) and investigate the correlations between surface brightness and internal (star formation rates of the host galaxies, SFR) or external influences (environmental density, $δ+1$). We find a clear break in these correlations at radii around or just below $1r_{\mathrm{vir}}$. Below this break the emission correlates tightly with SFR (as expected) and not at all with $δ+1$. Beyond $\sim 1r_\mathrm{vir}$(20 kpc) we observe the opposite trend with no dependence on SFR, but an emerging correlation with $δ+1$. We compare our measurements with the expected integrated surface brightness from ultrafaint, individually undetected LAEs and find that the latter is insufficient to drive the observed correlation. We conclude that Ly$α$ emission from the outer halos is regulated by the surrounding environment, but originates mostly from diffuse gas rather than discrete sources.

### [B] 60.9 — The deepest color-magnitude diagrams for the benchmark open cluster NGC 2437 from Gaia and VVVX
- **arXiv:** [2608.14514](https://arxiv.org/abs/2608.14514)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7510
- **Negative anchor:** planetary_disks_exoplanets = 0.7343
- **Semantic margin:** +0.0167
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7510), astrochemistry (0.7400), massive_star_formation (0.7306)
- **Current keyword baseline:** NO
- **Abstract:** Deep photometry of Galactic star clusters provides one of the most powerful tools for determining their physical properties. In particular, in low Galactic latitude regions that suffer from heavy extinction and crowding. NGC2437 is the most extended star cluster in the near-IR footprint of the VVV Extended Survey (VVVX), covering more than one degree on the sky. We aim to characterize its physical properties using Gaia DR3 in the optical and the VVVX in the near-IR. We use Gaia DR3 proper motions to select NGC2437 members in order to make optical and near-IR color-magnitude and color-color diagrams. We further exploited the newly constructed VVVX deep stack images to obtain the deepest near-IR color-magnitude diagram currently available for this cluster. We estimate the main physical parameters for NGC2437, including the mean parallax of 0.608 mas and PMs (-3.85, 0.41) mas/yr. The mean reddening E(J-Ks) = 0.059 mag and extinction of A_k = 0.034 mag for the cluster field, with no significant differential reddening spread. A distance modulus of 11.08 mag is estimated, equivalent to a distance of 1644 pc. This places NGC2437 at z=115 pc above the Galactic plane and at a galactocentric distance of 9.24 kpc. We measure the cluster structural parameters, obtaining a core radius of 10.79 arcmin. The estimated total absolute magnitudes are Mk = -4.91 mag and Mv = -3.70 mag. The cluster mean age is 350 Myr, using PARSEC-COLIBRI isochrones for solar metallicity. We measure a binary fraction of 28.6%. We also discuss the implications of the revised cluster parameters for the nearby open cluster NGC2425, the planetary nebula NGC2438, and the evolved OH/IR source OH231.8+04.2. The VVVX deep stacks increase the Ks photometric depth by 1.6 mag, nearly doubling the detected point sources and enabling significantly improved studies of stellar populations throughout the southern Galactic plane.

### [B] 60.8 — Catalytic formation of H_2 on carbonaceous dust grains - implications for interstellar observations
- **arXiv:** [2608.16149](https://arxiv.org/abs/2608.16149)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7424
- **Negative anchor:** planetary_disks_exoplanets = 0.7259
- **Semantic margin:** +0.0165
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7424), galactic_ism_surveys (0.7392), molecular_clouds (0.7311)
- **Current keyword baseline:** YES
- **Abstract:** We use kinetic Monte Carlo (KMC) simulations to study molecular hydrogen formation on carbonaceous dust grain surfaces, validated against recent laboratory measurements of H$_2$ formation on coronene films at temperatures from 10 to 250 K. The model uses a three-dimensional amorphous carbon lattice with heterogeneous physisorption ($45 \pm 5$ meV) and chemisorption ($1.75 \pm 0.25$ eV) sites, and tracks both Langmuir--Hinshelwood (LH) and Eley--Rideal (ER) formation channels within a stochastic Gillespie event-driven framework. The model reproduces the measured efficiency curve within the experimental uncertainties, including the isothermal (constant surface temperature) measurements at 100 - 250 K. The simulations correctly describe the phase boundary between the LH and ER driven processes as functions of grain temperature and the observed crossover. Under interstellar medium conditions, 10 - 250 K and n = 10 - 10$^4$ cm$^3$, the model predicts three distinct regimes for the formation efficiency $ε$, the fraction of impinging H atoms released as H$_2$. At 10 K diffusion is slow and $ε\approx 0.06$. Between 20 K and 80 K, LH dominates and $ε\approx 0.28$. Above 150 K, an ER plateau at $ε= 0.19$ is sustained by chemisorption-trapped H atoms. The LH-to-ER crossover occurs between 100 and 120 K. At 100 K we observe a 16\% density-dependent stochastic enhancement, which rate-equation models cannot capture. At T$_{dust}$ = 60 K, n = 10$^3$ cm$^3$ we find the ratio of H$_2$ formation to free-fall time $t_{{\rm H}_2}/t_{\rm ff} \approx 0.93$, so dust-catalysed H$_2$ chemistry can keep pace with gravitational collapse in high-redshift star-forming environments.

### [B] 60.6 — Modelling mountains on accreting magnetized neutron stars
- **arXiv:** [2608.17508](https://arxiv.org/abs/2608.17508)
- **Primary category:** astro-ph.HE
- **Positive anchor:** magnetic_fields = 0.7235
- **Negative anchor:** cosmology_large_scale_structure = 0.7000
- **Semantic margin:** +0.0235
- **Lexical positive/negative:** 0.2835 / 0.2835
- **Top positive topics:** magnetic_fields (0.7235), turbulence (0.6907), feedback_bubbles (0.6826)
- **Current keyword baseline:** NO
- **Abstract:** Continuous gravitational waves from accreting neutron stars in Low Mass X-ray Binaries are one of the main targets for current and next generation ground based detectors. In order to select the most promising astrophysical sources, however, reliable predictions for the signals are required, and it is therefore necessary to develop models that consistently account for the combined effects of magnetic stresses, accretion-induced heating, and the elastic response of the crust.}{We present a model for computing the quadrupolar deformation, incorporating for the first time the coupled effects of a poloidal magnetic field, deep crustal heating, and crustal elasticity. Perturbations to the star's structure driven by the Lorentz force density and by thermally-induced density variations are computed by solving a system of linearised deformation equations in the crust, for which we consider the full elastic response, while the ocean and core treated as barotropic fluids. We identify a threshold accretion rate whose value depends on crustal microphysics and the superfluid gaps in the core, above which magnetic stresses and asymmetric accretion drive deformations of opposite sign, while below this threshold their roles are reversed. The predicted eccentricities reach magnitudes up to $\varepsilon\sim 10^{-11}$, corresponding to characteristic gravitational-wave strains accessible to next-generation detectors such as the Einstein Telescope or Cosmic Explorer, but generally below the sensitivity of current LIGO, Virgo and KAGRA interferometers. These results are consistent with the non-detection of continuous gravitational waves from accreting neutron stars in Low Mass X-ray Binaries in recent observational campaigns, but highlight the need of reliable models to understand the impact of gravitational wave emission in these systems and select relevant targets for future searches.

### [B] 60.6 — SPURS: Massive Stars, Dense Gas, and Ly$α$ Escape in GN-z11 at $z = 10.6$
- **arXiv:** [2608.12699](https://arxiv.org/abs/2608.12699)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7630
- **Negative anchor:** stellar_atmospheres_evolution = 0.7396
- **Semantic margin:** +0.0234
- **Lexical positive/negative:** 0.2835 / 0.2835
- **Top positive topics:** astrochemistry (0.7630), molecular_clouds (0.7393), massive_star_formation (0.7388)
- **Current keyword baseline:** NO
- **Abstract:** We present ultra-deep {\it JWST} spectroscopy of GN-z11 ($z=10.6$) obtained through the SPURS Cycle 4 Large Program, providing the deepest rest-UV view yet obtained of a galaxy at $z>10$. GN-z11 was previously found to be nitrogen-enhanced with detectable Ly$α$. The SPURS spectrum reveals P-Cygni stellar wind features and broad He II emission that are jointly reproduced by stellar population models incorporating very massive stars (VMS; $>100\,M_\odot$) at low metallicity and young ages ($\lesssim3$ Myr). We also detect a broad ($\rm FWHM=1670$ km s$^{-1}$) component to N IV] $\lambda1486$, now seen in several nitrogen emitters, potentially arising from dense WN-like winds or LBV-like outbursts associated with a population of VMS in a dense environment, though an AGN-driven wind cannot be excluded. In either scenario, this broad component may trace the gas producing GN-z11's nitrogen enhancement. Rest-UV absorption lines reveal a fast ($\sim500$~km~s$^{-1}$), highly ionized outflow and a negligible neutral gas covering fraction. We resolve the weak Ly$α$ emission (EW=5.6 Å, $f_{\rm esc,Lyα}=2.7$\%), finding a broad red wing (44\% of flux at $>500$ km s$^{-1}$) that should experience reduced IGM damping wing suppression and help explain Ly$α$ visibility at $z>10$. Fine-structure O I* $\lambda1304$ emission indicates dense neutral gas near a subset of the ionizing sources, which may also scatter Ly$α$ to the large observed velocities. The weak low-ionization absorption favors a picture in which this dense neutral gas is confined to a compact nuclear region. Together, these results are consistent with a rapid burst of star formation building up the dense nuclear regions and surrounding clusters in GN-z11.

### [B] 60.4 — Large eROSITA X-ray sources as 2MRS galaxy groups
- **arXiv:** [2608.17732](https://arxiv.org/abs/2608.17732)
- **Primary category:** astro-ph.CO
- **Positive anchor:** galactic_ism_surveys = 0.7528
- **Negative anchor:** cosmology_large_scale_structure = 0.7297
- **Semantic margin:** +0.0230
- **Lexical positive/negative:** 0.0000 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7528), astrochemistry (0.7359), massive_star_formation (0.7351)
- **Current keyword baseline:** NO
- **Abstract:** We aim to exploit the large area coverage, good sensitivity, and low instrumental background of eROSITA to detect the faint surface brightness emission of galaxy groups from the Two Micron All Sky Survey Redshift Survey (2MRS). Using the data from eROSITA-DE Data Release 1, including images, exposure maps, and local background maps, we performed a wavelet decomposition of image mosaics in the 0.6--2.3 keV band at angular scales of 1/8-16'. We adopted 8-16' scales for source detection and 2-4' scales to improve catalog purity. A novel identification method based on the ranked partial Hausdorff distance fully exploits the X-ray image and group membership information. Random catalogs were used to control match purity, and the identification threshold was chosen to maximize the catalog size at a fixed purity. {We present a catalog of 619 X-ray galaxy groups with 80% purity, and define subsamples with 90% and 97% purity. Bright sources closely match the AXES-2MRS catalog (which is based on ROSAT All Sky Survey data analysis on spatial scales of 12-24'). The X-ray luminosity function of our groups agrees with previous studies down to 5.e41 erg/s. Using dynamical mass estimates, we find that the X-ray counterpart completeness for groups with >=4 members exceeds 60% for masses >2e13 Msun. We modeled the 2MRS group catalog and justify the inclusion of two-member groups in the identification. This study demonstrates that large X-ray sources on spatial scales relevant for cosmological studies of baryonic distributions can be reliably detected and identified using nearby galaxy group catalogs.

### [B] 60.3 — Beyond Idealized PAHs: Infrared Signatures of Carbon-Chain Defects from Shock Synthesis
- **arXiv:** [2608.18505](https://arxiv.org/abs/2608.18505)
- **Primary category:** astro-ph.GA
- **Positive anchor:** turbulence = 0.7493
- **Negative anchor:** planetary_disks_exoplanets = 0.7265
- **Semantic margin:** +0.0229
- **Lexical positive/negative:** 0.0000 / 0.0000
- **Top positive topics:** turbulence (0.7493), molecular_clouds (0.7426), massive_star_formation (0.7384)
- **Current keyword baseline:** YES
- **Abstract:** Polycyclic aromatic hydrocarbons (PAHs) are widely recognized as carriers of the aromatic infrared bands (AIBs). However, most spectral models rely on idealized structures that fail to capture the energetic environments of interstellar PAH formation. This work investigates the infrared (IR) signatures of PAHs formed under shock conditions and explores whether produced defective structures can explain observational features unpredicted by standard, idealized models. We combine two-stage reactive molecular dynamics simulations of PAH formation via condensation and shock processing with density functional theory spectral calculations, and compare our theoretical results with James Webb Space Telescope (JWST) observations of NGC 7023 and MRK 1066. Shock processing produces PAHs featuring fullerene-like carbon skeletons and linear carbon-chain attachments. These structural defects yield distinct IR signatures, including prominent carbon-chain stretching features at 4.6-5.5 micron that is absent in ideal PAHs, and significantly enhanced out-of-plane skeletal modes in the 14.5-20 micron regime. Our findings attribute the observed 5.2 micron band in NGC 7023 and MRK 1066 to carbon-chain vibrations and the 15-18 micron emission to curved skeletal modes, providing observational support for the prevalence of defective, shock-formed PAHs in the interstellar medium.

### [B] 60.3 — The Galactic Centre G+0.633-0.0604 Molecular Cloud: A New Gold Mine for Astrochemistry
- **arXiv:** [2608.14381](https://arxiv.org/abs/2608.14381)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7769
- **Negative anchor:** planetary_disks_exoplanets = 0.7615
- **Semantic margin:** +0.0154
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7769), molecular_clouds (0.7550), massive_star_formation (0.7486)
- **Current keyword baseline:** YES
- **Abstract:** Astrochemistry is living a golden age, with more than a quarter of the ~350 molecules in the current interstellar census having been detected over the last three years. One of the sources driving this progress is the G+0.693-0.027 cloud, located in the northern part of the Galactic Centre Sgr B2 complex. In this contribution, we present the astrochemical characterisation of G+0.633-0.0604, a newly discovered chemically rich molecular cloud at the southern edge of Sgr B2. With an inventory of >120 species, G+0.633 provides robust second detections of several prebiotic molecules only reported towards G+0.693, establishing it as the first confirmed astrochemical twin of G+0.693 while demonstrating that the extraordinary chemistry of this cloud is not unique. Furthermore, G+0.633 offers an observational advantage over G+0.693 since it displays half narrower linewidths. Together, G+0.633 and G+0.693 form a unique benchmark pair for unveiling molecular complexity and prebiotic chemistry in the interstellar medium.

### [B] 60.3 — Cosmography with DESI-DR1 Cosmic Chronometers: Direct H(z) measurements from Luminous Red Galaxy ages
- **arXiv:** [2608.13178](https://arxiv.org/abs/2608.13178)
- **Primary category:** astro-ph.CO
- **Positive anchor:** astrochemistry = 0.7751
- **Negative anchor:** galaxy_evolution_agn = 0.7522
- **Semantic margin:** +0.0229
- **Lexical positive/negative:** 0.2835 / 0.2835
- **Top positive topics:** astrochemistry (0.7751), galactic_ism_surveys (0.7493), massive_star_formation (0.7276)
- **Current keyword baseline:** NO
- **Abstract:** Providing robust redshift estimates for almost 3 million luminous red galaxies (LRGs), the Dark Energy Spectroscopic Instrument (DESI) offers a unique opportunity to test the expansion rate of the Universe with independent approaches. We apply the cosmic chronometer method to derive new, independent constraints on the Hubble parameter at 0.3<z<1.2 from the differential age evolution of DESI LRGs. We select spectra applying spectroscopic cuts to ensure sample purity and remove contamination by star-forming objects, then build a robust sample of cosmic chronometers (CCs) by stacking to obtain stable, high signal-to-noise (S/N) spectra, which also serves as a democratic binning choice for the $t-z$ plane. Ages are estimated by measuring Lick indices on the stacked spectra and fitting them with a theoretical stellar population model. We obtain $t-z$ relations from which we derive $H(z)$ constraints via two independent approaches: a fit with a pivotal-redshift cosmography, and a direct estimate from the original CC method. The cosmographic fit yields posteriors for the kinematic parameters $\{H_{z_0}, q_{z_0}, j_{z_0}\}$ compatible with currently considered cosmologies, giving a precision-level estimate of $H(z)$. We provide the maximum-a-posteriori (MAP) $H(z)$ estimate, an array of the median confidence region in the $H-z$ plane, and its covariance matrix. We also leverage the redshift distributions of the $t-z$ relation for different velocity dispersion groups to obtain two independent local measurements using the discrete approximation $H(z) \approx -Δz/[Δt (1+z)]$; the one from the reddest envelope of CCs gives $H(z \approx 0.61) = 88.5^{+6.7}_{-12.6}$ (stat.) $\pm 8.1$ (syst.) km s$^{-1}$ Mpc$^{-1}$. Systematic uncertainties for both the cosmographic and discrete $H(z)$ measurements come from a comprehensive analysis of all methodological choices in the data treatment.

### [B] 60.2 — The Production of Electron-Capture Elements in Thermonuclear Supernovae: Theory vs. Observations
- **arXiv:** [2608.13432](https://arxiv.org/abs/2608.13432)
- **Primary category:** astro-ph.SR
- **Positive anchor:** turbulence = 0.7248
- **Negative anchor:** cosmology_large_scale_structure = 0.7077
- **Semantic margin:** +0.0171
- **Lexical positive/negative:** 0.4866 / 0.2835
- **Top positive topics:** turbulence (0.7248), astrochemistry (0.7124), massive_star_formation (0.7081)
- **Current keyword baseline:** NO
- **Abstract:** Type Ia supernovae (SNe Ia) explosively destroy carbon-oxygen white dwarfs (WDs) in multiple stellar systems. They produce approximately 50% of the iron-group elements in the Universe, synthesize electron-capture (EC) elements, drive nuclear physics experiments, and underpin high-precision cosmology. To first order, the outcome is governed by nuclear physics, a property often described as stellar amnesia. Recently, this stellar amnesia has begun to be broken by the nearly universal detection of EC elements with JWST. These elements trace high-density burning, largely ruling out the currently popular helium-triggered, sub-Mch detonation models as the dominant channel. Instead, the ubiquitous presence of EC is shifting back the focus to dynamical and secular mergers, and near-Mch explosions similar to the deflagration model W7, but in which the nuclear flame undergoes a deflagration-to-detonation transition. The early deflagration phase is especially important because spherical simulations identify the central WD density, and thus the WD mass, as a key parameter governing the explosion. Here, we present detailed magneto-hydrodynamical simulations. We find that small-scale, pre-existing turbulence expected from the pre-explosion smoldering phase is essential for overcoming the fundamental challenges imposed by the intrinsic 3D physics. This turbulence systematically reduces the production of EC elements by about a factor of two, implying the need for WD central densities closer to those associated with accretion-induced collapse to a neutron star. We also demonstrate the effect of magnetic fields near the saturation field strength and highlight the need for higher-precision EC rates at low Ye.

### [B] 60.1 — $\texttt{Aether.jl}$ : A High-Performance 3D MHD and Multifluid Dust Code Written in a Dynamic Language with an Interactive Human-AI Development Framework
- **arXiv:** [2608.14048](https://arxiv.org/abs/2608.14048)
- **Primary category:** astro-ph.IM
- **Positive anchor:** turbulence = 0.7422
- **Negative anchor:** planetary_disks_exoplanets = 0.7273
- **Semantic margin:** +0.0149
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** turbulence (0.7422), astrochemistry (0.7268), galactic_ism_surveys (0.7261)
- **Current keyword baseline:** NO
- **Abstract:** We present $\texttt{Aether}$, a new finite-volume code for compressible hydrodynamics and magnetohydrodynamics, written in Julia and primarily designed for GPU systems. The code solves the MHD equations with constrained transport in Cartesian, cylindrical, and spherical-polar coordinates, using standard high-order Godunov methods. An arbitrary number of dust fluids can be coupled to the gas through stiff mutual drag. It was developed from scratch with interactive Human-coding agent workflow; the paper documents the framework of this workflow alongside the numerical methods. Performance-critical kernel is written through $\texttt{KernelAbstractions}$, and supports runs on CPUs and GPUs from multiple vendors. $\texttt{Aether}$ can be ran either from an interactive notebook or batch scripts, keeping prototyping, production runs, and analysis in a single language. We verify the implementation through a series of hydrodynamic, MHD, and dust tests. Although written in a dynamic language, $\texttt{Aether}$ achieves comparable or even higher single-GPU throughput than C++ code on the same hardware. In weak scaling on Frontier, parallel efficiency stays above $93\%$S on 4096 GCDs. These results show that a dynamic language now supports production astrophysical MHD simulations on exascale systems. $\texttt{Aether}$ and its Jupyter notebook example suite are publicly available.

### [B] 59.7 — Evolution of lunar wake potentials: structure, energy conversion, and their imprints on velocity distributions
- **arXiv:** [2608.18383](https://arxiv.org/abs/2608.18383)
- **Primary category:** physics.space-ph
- **Positive anchor:** turbulence = 0.7498
- **Negative anchor:** cosmology_large_scale_structure = 0.7207
- **Semantic margin:** +0.0291
- **Lexical positive/negative:** 0.0000 / 0.2835
- **Top positive topics:** turbulence (0.7498), molecular_clouds (0.7213), magnetic_fields (0.7103)
- **Current keyword baseline:** NO
- **Abstract:** We study the evolution of electric potentials in the lunar wake. The wake potential exhibits two distinct spatial scales. The macroscopic scale arises from solar wind expansion into the vacuum, with a potential length-scale growing with distance from the Moon; the microscopic scales arises from ion acoustic shocks near the wake center, with transition layers spanning tens of local Debye lengths. This two-scale potential mediates energy conversion between ions and electrons during wake refilling. The macroscale potential retards electrons and accelerates ions to supersonic velocities, converting electron thermal energy to ion kinetic energy. The microscale potential then decelerates ions to subsonic velocities and heats both species, converting ion kinetic energy back to thermal energy. Together, the two-scale potential imprints distinct signatures on velocity distributions, including ion beams and electron flat-top distributions, consistent with ARTEMIS observations.

### [B] 59.6 — Observing Co-Located Neutral and Ionized Gas-Phase Iron Depletion in the Magellanic Clouds
- **arXiv:** [2608.12557](https://arxiv.org/abs/2608.12557)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7663
- **Negative anchor:** planetary_disks_exoplanets = 0.7580
- **Semantic margin:** +0.0083
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** astrochemistry (0.7663), galactic_ism_surveys (0.7381), molecular_clouds (0.7366)
- **Current keyword baseline:** YES
- **Abstract:** Depletion is the observed phenomenon where gas-phase elemental abundances are reduced through accretion onto dust grains. We measure neutral gas-phase elemental abundances (S, Fe) in the Magellanic Clouds along 33 sightlines using high-resolution UV spectroscopy (HST/COS and HST/STIS), and compare them to ionized gas-phase abundances (S, Fe) adopted from the literature for six co-located H\,\textsc{ii} regions (with the furthest separation of $\lesssim3'$, 50 pc). Comparing S abundances show that S is minimally depleted in the H\,\textsc{ii} regions and surrounding diffuse ISM. However, we find that the gas-phase Fe abundances in H\,\textsc{ii} regions can be lower than those of the neighboring neutral ISM by 0.3 to 2 dex. This difference is likely an offset in the amount of Fe depleted into dust grains. As accretion of gas-phase Fe is likely not effective at the temperatures of the H\,\textsc{ii} regions, Fe depletion into solid form would have occurred in the dense atomic or molecular clouds prior to star formation. Stronger depletion in the H\,\textsc{ii} regions shows that Fe-bearing grains survive destruction in the first few million years following ionization. Our observations highlight that Fe depletion in H\,\textsc{ii} regions can be a useful tracer of Fe depletion in dense molecular clouds, which are challenging to observe directly via UV absorption.

### [B] 59.3 — Diffuse Dwarf Galaxies in Galaxy Clusters: I. Stellar Populations and Radial Gradients
- **arXiv:** [2608.17375](https://arxiv.org/abs/2608.17375)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7487
- **Negative anchor:** galaxy_evolution_agn = 0.7355
- **Semantic margin:** +0.0132
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7487), massive_star_formation (0.7365), galactic_ism_surveys (0.7147)
- **Current keyword baseline:** NO
- **Abstract:** We use Keck/KCWI spectroscopy to study one ultra-diffuse galaxy (UDG) and five Nearly-UDGs (NUDGEs) in the Perseus cluster, together with an additional UDG in the Coma cluster. As the first paper in a series, we focus on the global and radial stellar population properties of our sample. We find that these galaxies host intermediate-to old stellar populations, with typical ages of ~7 Gyr, low metallicities ([M/H]$\simeq$ -0.9 dex), and enhanced [Mg/Fe] abundances (~0.3 dex), consistent with previous studies. Six galaxies lie within the scatter of the present-day mass-metallicity relation (MZR), whereas the Coma UDG (DF11) is more consistent with the MZR of high-z galaxies (z ~ 2). We find no strong correlation between global stellar population properties and cluster infall parameters, suggesting that any environmental impact is not easily traceable through integrated stellar populations. We go one step further and measure radial gradients for three galaxies. Two show flat age and mildly negative metallicity gradients, similar to classical dwarfs, while one shows a rising metallicity profile as recently found in other UDGs. Comparing with classical dwarfs, we find a continuous correlation between metallicity gradient and globular cluster (GC) richness, where more GC-rich systems tend to show rising profiles. We propose that preferential tidal disruption of GCs in the inner regions of galaxies naturally produces rising metallicity profiles, unlike GC-poor classical dwarfs. This mechanism, potentially coupled with strong stellar feedback from early concentrated star formation, may explain the unusual rising metallicity profiles observed in GC-rich UDGs/NUDGEs.

### [B] 59.2 — Measuring Simulated Circumgalactic Medium Turbulence with Emission-Weighted Projected Velocity Structure Functions in FOGGIE
- **arXiv:** [2608.17013](https://arxiv.org/abs/2608.17013)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7435
- **Negative anchor:** galaxy_evolution_agn = 0.7286
- **Semantic margin:** +0.0149
- **Lexical positive/negative:** 0.4866 / 0.2835
- **Top positive topics:** galactic_ism_surveys (0.7435), turbulence (0.7353), molecular_clouds (0.7052)
- **Current keyword baseline:** YES
- **Abstract:** The spatially-resolved kinematics of line emission from the circumgalactic medium (CGM) of a galaxy can contain information about the CGM turbulence, which may play an important role in galaxy evolution. Due to the region's diffuse nature, there have been limited observations of low-redshift CGM emission until recent efforts that use spatially-resolved emission line kinematics to probe CGM turbulence. We use velocity structure functions (VSFs) as a measure for the properties of turbulence using the high-resolution cosmological zoom-in FOGGIE simulations. We focus on the location of the "turnover" in the VSF slope, often used as a measurement of the turbulence driving scale, and study how resolution, measurement area size, projection effects, and gas temperature influence the inferred CGM turbulence driving scale. We find that projection significantly lowers the VSF normalization but we do not find significant differences in the slope between 3D VSFs and emission-weighted projected 2D VSFs. We find that the size of the area used to measure the VSF, which can be thought of as the size of the emission nebula for a given instrument sensitivity, correlates directly with the turnover location in the VSF. These dependencies should be considered when using VSFs to interpret CGM turbulence from emission data, as projection, resolution and sensitivity constraints, and the temperature of the gas probed will all have a measurable effect on the VSF structure and the corresponding inferred turbulent properties.

### [B] 59.1 — The Total and Polarized Radio Emission from the Innermost Jets of a High-Redshift Quasar and a Candidate at Parsec-Scale Resolution
- **arXiv:** [2608.18691](https://arxiv.org/abs/2608.18691)
- **Primary category:** astro-ph.GA
- **Positive anchor:** turbulence = 0.7526
- **Negative anchor:** galaxy_evolution_agn = 0.7323
- **Semantic margin:** +0.0203
- **Lexical positive/negative:** 0.0000 / 0.0000
- **Top positive topics:** turbulence (0.7526), molecular_clouds (0.7465), magnetic_fields (0.7370)
- **Current keyword baseline:** NO
- **Abstract:** High-frequency very long baseline interferometry (VLBI) polarimetry probes synchrotron-emitting plasma closer to the central engines of radio-loud active galactic nuclei (AGNs), but observations above 43 GHz are technically demanding. We present 22-GHz European VLBI Network observations of the $z=4.31$ quasar J1510+5702 and J1606+3124, whose published spectroscopic redshift, $z=4.56$, is uncertain; a photometric estimate gives $z_{\rm phot}=0.9\pm0.1$. For the published $z>4$ redshifts, 22 GHz corresponds to rest-frame frequencies above 118 GHz. Polarized emission is detected in J1510+5702, and a low-level polarized signal is recovered from the brightest feature of J1606+3124. Adopting $z=4.56$, that feature has a brightness temperature of $T_{\mathrm{b,VLBI}}=(7.4\pm0.8)\cdot10^{10}$ K, allowing a mildly Doppler-boosted interpretation, while the young compact-source scenario also remains viable. The core of J1510+5702 has $T_{\mathrm{b,VLBI}}=(1.08\pm0.15) \cdot10^{12}$ K, implying a Doppler factor of ${\sim}22$ under the equipartition assumption. This component has a ${\sim}3.5$ % fractional polarization. These observations show that cm-wavelength VLBI can access rest-frame millimeter-band polarization in bright $z>4$ jets.

### [B] 59.1 — OH Line Detections in Southern Galaxies of the IRAS Revised Bright Galaxy Sample
- **arXiv:** [2608.14473](https://arxiv.org/abs/2608.14473)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7474
- **Negative anchor:** generic_instrumentation = 0.7347
- **Semantic margin:** +0.0127
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7474), astrochemistry (0.7434), massive_star_formation (0.7291)
- **Current keyword baseline:** NO
- **Abstract:** We present a systematic study of OH main-line emission and absorption in 186 southern galaxies from the IRAS Revised Bright Galaxy Sample, using archival MeerKAT snapshot data. OH features are detected in 38 galaxies, including eight with OH maser emission (three new) and 30 showing OH absorption, mostly unreported previously. Four absorption systems exhibit weak OH emission superposed on strong absorption. OH-emitting regions are generally more compact than the associated radio continuum. Most absorption profiles are well fit by two Gaussian components (1667 and 1665 MHz), with an average integrated line ratio of $\sim$1.5. LIRGs show an OH emission detection rate of ~13\%, versus significantly lower rates in non-LIRGs. For sources with radio continuum flux densities >20 mJy, OH absorption detection rates reach ~36\% (LIRGs) and ~27\% (non-LIRGs), while no OH absorption features were detected among sources with lower radio continuum flux densities. This suggests that sufficient background continuum is likely an important factor for the detection of OH absorption. Detected OH emitters follow the empirical $L_{\rm OH}$--$L_{\rm FIR}$ relation, consistent with far-infrared pumping, while non-detections show upper limits below the relation. No significant differences are found between OH absorbers and non-detections in infrared luminosity or radio continuum compactness. Stacked spectra of non-detections reveal no significant OH features, suggesting that sensitivity and orientation alone do not fully explain the absence of absorption. In contrast, mid-infrared colors (e.g., W2--W3) and q_TIR differ between the two populations. OH absorption galaxies occupy an intermediate regime in L_HCN/L_CO between OH megamasers and non-detections, implying that OH absorption detectability is linked to dense molecular gas conditions, with extreme star formation potentially suppressing its occurrence.

### [B] 59.0 — The segmented spiral structure of the Solar neighbourhood traced by young clustered populations
- **arXiv:** [2608.17887](https://arxiv.org/abs/2608.17887)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7379
- **Negative anchor:** galaxy_evolution_agn = 0.7308
- **Semantic margin:** +0.0071
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7379), astrochemistry (0.7232), molecular_clouds (0.7098)
- **Current keyword baseline:** NO
- **Abstract:** The Milky Way spiral pattern remains poorly constrained, and the youngest tracers in the solar neighbourhood do not always follow a few smooth, continuous logarithmic arms. We analyse young open clusters, both independently and combined with young stellar object (YSO)-based groups, to test whether they define continuous spiral-arm ridges or shorter, partially connected structures. In the (theta_G, ln R_G) plane, we identify local overdensities using a density-supported Bayesian Gaussian Mixture Model (BGMM), introducing published Perseus, Local, Sagittarius, and Scutum arm tracks only afterwards as reference curves. We then apply a Minimum Spanning Tree (MST) analysis in the heliocentric (X,Y) plane to examine spatial connectivity. The open-cluster sample already resolves into several local components, while the addition of YSO-based groups highlights branches and intermediate regions without producing continuous arms. The MST likewise shows distinct local branches at small pruning scales that progressively merge as the linking scale increases. The Local--Sagittarius region provides the clearest agreement between both diagnostics: the BGMM identifies an intermediate component between the reference arms, while the MST connects neighbouring branches through the same region. Overall, young structures near the Sun appear as fragmented, spiral-like segments with partial links rather than smooth continuations of a few grand-design arms. Determining whether this morphology reflects spiral-arm formation mechanisms or subsequent evolution will require additional age, vertical, and kinematic information.

### [B] 59.0 — Revised $^{45}$V($p,γ$)$^{46}$Cr reaction rate and its impact on the production of $^{44}$Ti in core-collapse supernovae
- **arXiv:** [2608.17757](https://arxiv.org/abs/2608.17757)
- **Primary category:** nucl-ex
- **Positive anchor:** astrochemistry = 0.7458
- **Negative anchor:** stellar_atmospheres_evolution = 0.7335
- **Semantic margin:** +0.0123
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7458), turbulence (0.7305), ism_methods_data (0.7168)
- **Current keyword baseline:** YES
- **Abstract:** The thermonuclear $^{45}$V($p,γ$)$^{46}$Cr reaction is the primary leakage pathway from the $^{44}$Ti--$^{45}$V quasi-equilibrium cluster during $α$-rich freeze-out in core-collapse supernovae (CCSN), governing the final abundance of the $γ$-ray-emitting isotope $^{44}$Ti. A recent high-resolution $γ$-ray study [C. Cousins \textit{et al.}, Phys. Rev. Lett. 136, 252701 (2026)] identified ten previously unknown low-spin proton-unbound states in $^{46}$Cr, enabling the first experimentally constrained $^{45}$V($p,γ$)$^{46}$Cr reaction rate using the AME2020 mass excess, $\text{ME}(^{46}\text{Cr}) = -29472(11)$~keV. Here, we adopt the four-fold more precise CSRe mass excess $\text{ME}(^{46}\text{Cr}) = -29477.2(2.6)$~keV [M.~Wang \textit{et al.}, Phys. Rev. C \textbf{106}, L051301 (2022)] to recalculate the reaction rate. Including proton capture on the ground and first two excited states of $^{45}$V alongside new shell-model proton spectroscopic factors, we reduce mass-related rate uncertainties to a subdominant level. The revised rate is up to 69% higher than that of Cousins \textit{et al.} at $α$-rich freeze-out temperatures ($T \simeq 1.5$--$2$~GK). CCSN nucleosynthesis calculations show this revised rate increases the ejected $^{44}$Ti yield by $\sim$26% in a $20\,M_\odot$ model compared to The \textit{et al.} [ApJ \textbf{504}, 500 (1998)], while causing negligible changes for the SN~1987A trajectory. We demonstrate that $^{44}$Ti production sensitivity is dictated by the ejecta electron fraction ($Y_e$): the reaction significantly affects proton-rich ejecta ($Y_e \approx 0.50$) but has little impact on neutron-rich ejecta ($Y_e \approx 0.496$), where lower free-proton abundances suppress reaction flow. This reconciles conflicting results from past sensitivity studies.

### [B] 58.7 — Hemispheric Asymmetry of Solar Active Regions Arises from a Nested Population
- **arXiv:** [2608.12263](https://arxiv.org/abs/2608.12263)
- **Primary category:** astro-ph.SR
- **Positive anchor:** astrochemistry = 0.7229
- **Negative anchor:** cosmology_large_scale_structure = 0.7112
- **Semantic margin:** +0.0117
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7229), magnetic_fields (0.7204), galactic_ism_surveys (0.7063)
- **Current keyword baseline:** NO
- **Abstract:** We investigate the longitude--time distribution of NOAA active regions (ARs) during Solar Cycles 22--24 and find statistically significant North--South asymmetry in AR emergence. Using an activity-nest identification algorithm, we show that this asymmetry is concentrated in the subset of ARs that participate in nests. Nest-member ARs exhibit substantially larger hemispheric asymmetry than either the full AR population or the non-nest population, and the asymmetry is largely removed when nest-member ARs are excluded. Monte Carlo tests with randomized longitudes and temporal perturbations show that the observed nesting and asymmetry exceed random expectations, implying that $\sim$6--18\% of ARs participate in a non-random, hemispherically asymmetric nesting component. This asymmetry is associated with temporally offset bursts of activity and distinct longitudinal clustering between the hemispheres, leading to reduced cross-equatorial coherence in the longitude--time distribution of solar ARs. Intervals of enhanced nesting activity and hemispheric asymmetry broadly coincide with enhanced hemispheric quasi-biennial variability and temporal evolution of the large-scale solar magnetic field, suggesting a possible connection between intermediate-timescale dynamo variability and the hemispheric organization of solar activity.

### [B] 58.3 — JWST Whirlpool Galaxy Treasury: Mid-Infrared Emission in M51 and its Relation to Gas Column and Star Formation
- **arXiv:** [2608.16802](https://arxiv.org/abs/2608.16802)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7553
- **Negative anchor:** galaxy_evolution_agn = 0.7498
- **Semantic margin:** +0.0055
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** astrochemistry (0.7553), galactic_ism_surveys (0.7534), turbulence (0.7486)
- **Current keyword baseline:** YES
- **Abstract:** Using JWST/MIRI imaging of M51 in eight broadband filters, we investigate correlations of mid-infrared emission from polycyclic aromatic hydrocarbons (PAHs) and dust continuum with molecular, atomic, and ionized gas traced by CO(1-0), HI, and Pa-alpha, respectively. In molecular gas-dominated regions, PAH-dominated filters (F560W, F770W, F1130W, F1280W) exhibit near-linear correlations with CO(1-0) at 40 pc scale, indicating that PAHs are well-mixed with gas and experience relatively constant radiation field intensities. The F1500W, F1800W, and F2100W dust continuum-dominated filters show shallower slopes with CO(1-0), reflecting contributions from star-forming regions with high radiation field intensities. This is reinforced by the near-linear scaling between F2100W and Pa-alpha. PAH-dominated bands do not show this linear trend with Pa-alpha, likely due to their destruction in ionized regions. F1000W behaves similarly to PAH bands in its correlations with CO(1-0) and Pa-alpha. Modeling mid-infrared emission with an empirical decomposition into gas- and star-formation-associated components shows that PAH-dominated filters receive comparable contributions from both, while the relative contribution associated with the Pa-alpha template increases toward longer wavelengths, reaching $\sim$75% in F2100W. These results demonstrate that mid-infrared simultaneously traces the gas column and star formation, but with a systematic wavelength-dependent shift in what drives the correlations: PAHs being more gas-tracing and dust-continuum reflecting star formation. Lastly, considering both HI and H$_2$ at 440 pc resolution, we find a tight, linear relation between $Σ_{HI+H_2}$ and PAH-dominated filters. Although most of our coverage is in H$_2$-dominated regions, we note similar observations with HI, suggesting that PAHs are also well-mixed with atomic gas.

### [B] 58.1 — The X-Ray Continuum Emission Region in the Lensed Quasar SDSS J133907.23+131038.6 is Much Smaller than the Accretion Disk
- **arXiv:** [2608.17041](https://arxiv.org/abs/2608.17041)
- **Primary category:** astro-ph.HE
- **Positive anchor:** galactic_ism_surveys = 0.7470
- **Negative anchor:** galaxy_evolution_agn = 0.7236
- **Semantic margin:** +0.0234
- **Lexical positive/negative:** 0.2835 / 0.4866
- **Top positive topics:** galactic_ism_surveys (0.7470), astrochemistry (0.7258), ism_methods_data (0.7177)
- **Current keyword baseline:** NO
- **Abstract:** We analyze microlensing variability in 15 seasons of optical monitoring data and 4 epochs of new X-ray observations of the doubly-imaged gravitationally lensed quasar SDSS J133907.23+131038.6 to place empirical constraints on the size and structure of that system's X-ray and optical continuum emission regions. Employing a Bayesian Monte Carlo method, we analyzed ground-based optical light curves to constrain the half-light radius of the far-UV source $\log(r_{\rm 1/2, FUV}/{\rm cm})=15.78^{+0.26}_{-0.28}$ at 193 nm, the rest-frame center of the {\it r}-band, assuming a $60^\circ$ inclination angle. This size corresponds to $\sim100\,{\it r}_{\rm g}$ for a $4.0 \times 10^{8} \: {\rm M_{\odot}}$ black hole. We measured the half-light radius of the full band ($0.2-8.0 \: {\rm keV}$) X-ray continuum emission region $\log(r_{\rm 1/2, X_{full}}/{\rm cm})=14.32^{+0.23}_{-0.31}$, a size measurement that is consistent with the radius of the innermost stable circular orbit (ISCO) in the Schwarzschild metric.Two shifted Fe K$α$ lines caused by microlensing are detected in the stacked spectrum of image A at 5.9 and 8.9~keV at $>99\%$ significance.

### [B] 58.0 — Kinematics and Dynamics of the Open Cluster NGC 2302
- **arXiv:** [2608.18550](https://arxiv.org/abs/2608.18550)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7355
- **Negative anchor:** stellar_atmospheres_evolution = 0.7253
- **Semantic margin:** +0.0102
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7355), turbulence (0.7249), galactic_ism_surveys (0.7165)
- **Current keyword baseline:** NO
- **Abstract:** Open clusters are ideal observational testbeds to understand the dynamics of stellar systems. We present a dynamical study of the young open cluster NGC 2302. The latest Gaia data and $UBVIJHK_s$ photometric data are used in this study. A total of 117 stars are selected as the genuine members using the Gaia data. This cluster is, on average, reddened by $<E(B-V)> = 0.24 \pm 0.06$ (s.d.). The ratio of total-to-selective extinction ($R_V$) in the direction of NGC 2302 is $2.8 \pm 0.1$. The cluster distance is determined to be $1.16 \pm 0.08$ kpc using Gaia parallaxes. Theoretical isochrone fitting for $Z = 0.008$ on color-magnitude diagrams yields an age of $80 \pm 20$ Myr. The relative proper motions of individual members show no significant radial expansion or contraction. NGC 2302 contains a total stellar mass of $333 \pm 48 M_{\odot}$. The one-dimensional velocity dispersion is approximately 0.26 km s$^{-1}$, which is comparable to the viral velocity dispersion of 0.27 km s$^{-1}$ derived from its total mass. Its relaxation time is estimated to be approximately 90 Myr, which is similar to the age of the cluster within the uncertainty in age estimation. Finally, we report a pattern of mass segregation in the radial distribution of stellar masses. Our results suggest that NGC 2302 is virialized and currently approaching a state of dynamical relaxation. However, because no definitive evidence of kinetic energy equipartition is found, the possibility of the in-situ formation of high-mass stars within the central region should be carefully considered.

### [B] 57.7 — Accurately simulating gain and clock-induced charge production in the EMCCD gain register
- **arXiv:** [2608.17842](https://arxiv.org/abs/2608.17842)
- **Primary category:** astro-ph.IM
- **Positive anchor:** astrochemistry = 0.7211
- **Negative anchor:** generic_instrumentation = 0.7116
- **Semantic margin:** +0.0095
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7211), molecular_clouds (0.7081), massive_star_formation (0.7066)
- **Current keyword baseline:** NO
- **Abstract:** An electron-multiplying charge-coupled device (EMCCD) is capable of precise detections in low-signal environments, able to detect a single photon through electron multiplication. It has many applications, such as faint-target astronomy, quantum optics, molecule tracing, and others, and it will be used for faint companion detection in the Roman Telescope's coronagraph instrument. In an EMCCD, photons hit the pixels, and photo-electrons are created; these are multiplied via impact ionization as they travel through the gain register from one gain stage to the next. A high gain means a high multiplication factor, and this is achieved through a high voltage difference across a gain stage. If the gain is high enough, the chance of clock-induced charge (CIC) production in the gain register increases. The probability distribution function governing the gain process typically used only accounts for charge multiplication if one or more electrons enter the gain register. I discuss my implementation of the simulation of this effect and its customization in emccd_detect, the EMCCD detector simulator used for the Roman Telescope. In addition, the simulator has been updated to use the exact binomial distribution for EM gain instead of the approximate Gamma distribution usually used in the literature, which is only valid for large counts. I also examine some EMCCD data and show through maximum likelihood estimation with CIC_gain_register that the data conform better to the binomial distribution versus the approximate Gamma/Erlang distribution. The use of the modified distribution would in principle improve the fidelity of Roman's testing and lead to better EMCCD calibration and more accurate signal extraction from a frame.

### [B] 57.0 — Multi-zone Modeling of Blazar Jets: Constraints from GeV-Optical Correlation and Short-Timescale Variability
- **arXiv:** [2608.18707](https://arxiv.org/abs/2608.18707)
- **Primary category:** astro-ph.HE
- **Positive anchor:** galactic_ism_surveys = 0.7236
- **Negative anchor:** cosmology_large_scale_structure = 0.7156
- **Semantic margin:** +0.0081
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7236), turbulence (0.7058), magnetic_fields (0.7043)
- **Current keyword baseline:** NO
- **Abstract:** We have developed a multi-zone model of blazar jet emission, in which the emission region contains many cells with individual magnetic fields and electron energy distributions. Nonthermal emission from radio to $γ$-rays is generated by electrons accelerated by shocks passing through the region via synchrotron and inverse-Compton (IC) processes. The optical and GeV variability at days-to-months time-scale simulated from our model are strongly correlated with no significant time lag, as observed in most blazars and indicated by the standard shock-in-jet model. However, the mechanism of the shorter time-scale variability has been less explored, although such fluctuations at X-rays, $γ$-rays and optical bands have been observed regularly in recent years. In our model, the hr time-scale variability of the synchrotron radiation is due to the spatial fluctuation of the magnetic field in the emission region. We found that to reproduce the short-timescale variability of the observed synchrotron emission in blazars, the required fluctuations of the magnetic field are in the range $1-2\%$ to $25-30\%$. Similar variability of the IC emission, which does not depend on the magnetic field, may be reproduced in our model by implementing equipartition of energy between the magnetic field and particles. We found that orphan flares in the optical or GeV band, or optical-GeV correlation with a significant time delay, as observed occasionally, may be reproduced in certain special conditions related to the orientation of the magnetic field in the cells.

### [B] 57.0 — Local Interstellar Flow Parameters from the First Intersection of IMAP-Lo's Parameter Tubes
- **arXiv:** [2608.14939](https://arxiv.org/abs/2608.14939)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7454
- **Negative anchor:** cosmology_large_scale_structure = 0.7374
- **Semantic margin:** +0.0081
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7454), galactic_ism_surveys (0.7401), turbulence (0.7384)
- **Current keyword baseline:** YES
- **Abstract:** The Sun's motion through the interstellar medium creates a flow of interstellar neutral (ISN) atoms through the heliosphere. ISN He, due to its high universal abundance and relatively low ionization rate, is the most abundant of the interstellar species near 1 au and ideal for flow parameter determination. The Interstellar Boundary Explorer (IBEX) measurements of ISN He flow parameters (speed, temperature, and direction) yielded a tube in 4D parameter space -- narrow in cross-section but highly extended along one parameter axis (e.g., ecliptic longitude direction). This ``4D parameter tube'' results in large systematic uncertainties, a direct consequence of IBEX-Lo's fixed viewing orientation on the spacecraft. On the Interstellar Mapping and Acceleration Probe (IMAP), the articulation of the IMAP-Lo boresight using its pivot platform enables multiple viewing orientations of the ISN flow for significant systematic uncertainty reduction. We provide first results that definitively intersect ISN parameter tubes for elongation angles $79^\circ$, 94$^\circ$, and 109$^\circ$, resulting in precise interstellar parameters: speed $26.37 \pm 0.82$ km s$^{-1}$, ecliptic longitude direction $74.85^\circ \pm 0.96^\circ$, ecliptic latitude direction $-5.212^\circ \pm 0.035^\circ$, and temperature $7740^{+770}_{-730}$ K. The inferred flow of the Very Local Interstellar Medium is not consistent with either the Local Interstellar Cloud or the G-Cloud, but rather an intermediate state. IMAP is now positioned to study the detailed physics of this complex, nearby interstellar region. By resolving and understanding its physics, we determine how the heliosphere responds to the local interstellar flow, and how it may evolve in time

### [B] 56.9 — Differential Reddening and Extinction Law Analyses of Galactic Open Clusters
- **arXiv:** [2608.13313](https://arxiv.org/abs/2608.13313)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7629
- **Negative anchor:** stellar_atmospheres_evolution = 0.7606
- **Semantic margin:** +0.0023
- **Lexical positive/negative:** 0.4866 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7629), astrochemistry (0.7576), massive_star_formation (0.7467)
- **Current keyword baseline:** NO
- **Abstract:** Extinction significantly affects open cluster parameters and their use in studies of Galactic structure, yet homogeneous large sample measurements of open cluster extinction properties remain limited. Using Gaia-era open cluster member samples combined with multi-band photometry and stellar parameters, we derive color excesses of member stars and provide the homogeneous characterization of the mean reddening, differential reddening, and color excess ratio (CER) at the cluster scale. Differential reddening increases systematically with mean reddening, with highly reddened clusters near the Galactic plane showing stronger extinction variations. Star-by-star reddening corrections narrow color--magnitude diagram (CMD) sequences in 369 of 435 clusters (85%) with reliable CMD-width measurements, and cluster color excess maps reveal small-scale extinction structures. The median CER is compatible with the standard diffuse interstellar medium extinction curve, while the broad CER distribution and its large-scale variations across the Galactic disk likely reflect differences in the dominant dust environments sampled along different Galactic sight lines.

### [B] 56.5 — Revisiting the Growth Rate of the Relativistic Tearing Instability: The Role of the Non-ideal MHD Structure
- **arXiv:** [2608.19645](https://arxiv.org/abs/2608.19645)
- **Primary category:** physics.plasm-ph
- **Positive anchor:** magnetic_fields = 0.7177
- **Negative anchor:** planetary_disks_exoplanets = 0.7109
- **Semantic margin:** +0.0068
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** magnetic_fields (0.7177), turbulence (0.7141), galactic_ism_surveys (0.6952)
- **Current keyword baseline:** NO
- **Abstract:** Magnetic reconnection in magnetically dominated pair plasmas is a key process in high-energy astrophysical systems. We revisit the relativistic tearing instability in a Harris current sheet and derive an improved analytical expression for its linear growth rate and the most unstable wavenumber. The key modification is the treatment of the vector potential perturbation in the non-ideal magnetohydrodynamic (MHD) region. Instead of the conventional constant-A approximation, we use an extrapolated-A approximation, in which the ideal-MHD solution is linearly extrapolated into the non-ideal region. Comparison with two-dimensional particle-in-cell simulations shows that the revised theory improves the prediction of the most unstable wavenumber. The improvement is most pronounced at low particle drift velocities, where the particle gyroradius is smaller than the current-sheet thickness and the fastest-growing mode shifts to longer wavelength. The resulting analytical expressions provide an updated benchmark for magnetically dominated reconnection and its applications to high-energy astrophysical plasmas, including gamma-ray bursts and fast radio bursts.

### [B] 55.9 — No Evidence for Nearby Circumstellar Material in the Type Ia Supernova 2025rbs
- **arXiv:** [2608.13655](https://arxiv.org/abs/2608.13655)
- **Primary category:** astro-ph.HE
- **Positive anchor:** astrochemistry = 0.7604
- **Negative anchor:** planetary_disks_exoplanets = 0.7549
- **Semantic margin:** +0.0055
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7604), galactic_ism_surveys (0.7306), turbulence (0.7290)
- **Current keyword baseline:** NO
- **Abstract:** We present a high-resolution spectral time series of the Type Ia supernova (SN) 2025rbs discovered in the nearby galaxy NGC 7331. The Automated Planet Finder (APF) at Lick Observatory and the MAROON-X/IGRINS-2 at Gemini North were used to obtain echelle spectra between -5 and 15 days with respect to the epoch of maximum light. Several unsaturated NaID absorption components along the line of sight are identified, but there is no evidence of time variance in any of them. We measure the equivalent width of the observed diffuse interstellar band around 5780 A and constrain the extinction along the line of sight to SN 2025rbs as $A_V = 0.64\,\pm\,0.32$ mag, corresponding to a moderate reddening of $E(B-V) = 0.21\,\pm\,0.10$ mag (assuming $R_\mathrm{V}$ = 3.1). The observed Ca II H & K interstellar absorption roughly traces NaID in velocity space, suggesting a common origin. Quantitative comparisons between the column densities of Na and Ca gas in these host clouds ($N_{NaID}$ / $N_{Ca II}$ of order unity) argue against their origin in the Galactic halo gas and instead support absorption due to the interstellar gas of NGC 7331. Time invariance of all the observed absorption features suggests a lack of nearby circumstellar material ($\lesssim$ 10$^{16}$ cm) around the progenitor system of SN 2025rbs. This supports a progenitor scenario for SN 2025rbs with minimal ambient circumstellar gas, consistent with a double-degenerate CO white dwarf binary system.

### [B] 55.6 — Asteroseismic analysis of red giants in eclipsing binaries using two methods: implications for scaling relations and chemical composition
- **arXiv:** [2608.18250](https://arxiv.org/abs/2608.18250)
- **Primary category:** astro-ph.SR
- **Positive anchor:** astrochemistry = 0.7318
- **Negative anchor:** planetary_disks_exoplanets = 0.7269
- **Semantic margin:** +0.0049
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7318), magnetic_fields (0.6959), massive_star_formation (0.6885)
- **Current keyword baseline:** YES
- **Abstract:** The study of solar-like oscillating red giants in eclipsing binaries (EBs) provides a unique opportunity to advance stellar astrophysics by combining dynamical mass and radius measurements with asteroseismic constraints. EBs provide precise fundamental parameters (e.g. mass, radius, and luminosity) independent of distance, while solar-like oscillations probe stellar interiors and enable tests of asteroseismic scaling relations used to determine stellar masses and radii. {We apply two different methods to estimate the initial chemical composition of the systems. In Method I, the initial helium abundance ($Y_0$) is treated as the free parameter, whereas in Method II the free parameter is the initial metallicity ($Z_0$), assuming a relation between $Y_0$ and $Z_0$. We construct interior models individually for the components of 11 EBs and obtain coeval solutions for eight systems.} The ages and chemical compositions derived from the two methods are generally consistent with each other. Our results provide important clues about the chemical evolution of a part of the Galactic disk. Moreover, using the parameters obtained for two oscillating stars, Tek Ayak (KIC 8410637) and KIC 9970396, instead of solar reference values in the scaling relations yields masses and radii that are in much better agreement with the dynamical solutions without requiring additional corrections.

### [B] 55.6 — Nuclear Drip Line and the Composition of Supernova Matter
- **arXiv:** [2608.16778](https://arxiv.org/abs/2608.16778)
- **Primary category:** nucl-th
- **Positive anchor:** turbulence = 0.7210
- **Negative anchor:** stellar_atmospheres_evolution = 0.7161
- **Semantic margin:** +0.0049
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** turbulence (0.7210), astrochemistry (0.7197), massive_star_formation (0.6965)
- **Current keyword baseline:** YES
- **Abstract:** The nuclear drip line plays a crucial role in determining the composition of matter under extreme astrophysical conditions. In core-collapse supernovae and neutron-star crusts, matter is driven far from saturation density and nuclear stability; nuclei coexist with a sea of free neutrons, an effect that is present even at zero temperature in neutron-star crusts and becomes more pronounced in the hotter, neutron-rich supernova environment. This makes a careful treatment of drip-line physics essential for a realistic description of the equation of state and composition. In this work, the influence of the nuclear drip line on the baryonic composition of supernova matter is investigated within the framework of nuclear statistical equilibrium (NSE). The composition is evaluated in terms of free nucleons, light clusters, and heavy nuclei at finite temperature and global sub-saturation densities. The results indicate that, at low proton fractions and higher densities, the inclusion of nuclei beyond the drip line enhances the formation of extremely neutron-rich light clusters, leading to a significant reduction in the free-neutron density and the charge fraction of heavy nuclei. These findings demonstrate that drip-line physics has a significant impact on the composition of supernova matter and should be carefully incorporated in supernova modeling and nucleosynthesis studies.

### [B] 55.6 — X-ray thread/Nonthermal Radio Filament associations: Evidence for Interstellar Magnetic Reconnection
- **arXiv:** [2608.14830](https://arxiv.org/abs/2608.14830)
- **Primary category:** astro-ph.HE
- **Positive anchor:** molecular_clouds = 0.7414
- **Negative anchor:** planetary_disks_exoplanets = 0.7364
- **Semantic margin:** +0.0050
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** molecular_clouds (0.7414), magnetic_fields (0.7395), galactic_ism_surveys (0.7346)
- **Current keyword baseline:** NO
- **Abstract:** Nonthermal radio filaments (NTFs), first discovered at 20-centimeter wavelength more than four decades ago, are among the most enigmatic structures at the Galactic Center. They still defy a clear explanation. These striking narrow features trace intense magnetic fields and often stand in bold contrast to the Galactic plane. Recent discoveries have revealed surprising associations: some NTFs align well with X-ray threads that seem to exhibit Fe He-$α$ emission. Here, I present preliminary results from an ongoing, collaborative, multi-wavelength study aimed at understanding the origins of these filaments, focusing on testing the magnetic reconnection scenario of these associations and shedding new light on the high-energy processes and magnetic phenomena operating under extreme conditions at the heart of our Galaxy.

### [B] 55.3 — Sr and Ba yields of the First Generation(s) of stars: Constraints from metal-poor stars
- **arXiv:** [2608.17001](https://arxiv.org/abs/2608.17001)
- **Primary category:** astro-ph.SR
- **Positive anchor:** astrochemistry = 0.7624
- **Negative anchor:** stellar_atmospheres_evolution = 0.7581
- **Semantic margin:** +0.0043
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7624), massive_star_formation (0.7295), galactic_ism_surveys (0.7292)
- **Current keyword baseline:** NO
- **Abstract:** We present our chemical abundance analysis of ten new extremely metal-poor stars with $-4.05\leq\mbox{[Fe/H]}\leq-2.33$, based on high-resolution (R $\sim28,000$) Magellan/MIKE spectra. Eight of our stars have low heavy-element abundances of $\mbox{[Sr/H]}<-4.5$ and $\mbox{[Ba/H]}<-4.0$, making them Small Accreted Stellar System (SASS) stars. Four are hyper neutron-capture-element poor with $\mbox{[Sr/H]}<-5.0$, including Gaia DR3 5729400267359655680, which sets a new record for the lowest detected Sr abundance of $\mbox{[Sr/H]} =-6.4$. We identify four distinct [Sr/Ba] groups within the wider SASS star population which span a large range from $\mbox{[Sr/Ba]} =-2.0$ to +1.6, pointing to multiple types of progenitor events and different nucleosynthesis processes/sites. To explore the origins of this large [Sr/Ba] range, we adopt site-agnostic Sr yields of $\mbox{[Sr/H]}=-6$, $-5.75$, $-5.42$, and $-4.93$ for the four groups. Applying those yields suggests that the majority of SASS stars formed from gas enriched by $\sim$1-10 progenitor events, consistent with expectations from their extremely metal-poor nature. We thus attribute the [Sr/H] abundance scatter to intrinsic variations in the Sr yield per nucleosynthesis site/event. Our proposed Sr yields for each [Sr/Ba] group and associated nucleosynthesis origin are a reasonable and representative approximation, good to within a factor of a few, and can constrain future theoretical heavy element nucleosynthesis calculations in early core-collapse supernovae.

### [B] 55.2 — A stochastic forward model for the intergalactic dispersion-measure distribution of Fast Radio Bursts
- **arXiv:** [2608.17658](https://arxiv.org/abs/2608.17658)
- **Primary category:** astro-ph.CO
- **Positive anchor:** galactic_ism_surveys = 0.7348
- **Negative anchor:** galaxy_evolution_agn = 0.7309
- **Semantic margin:** +0.0039
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7348), turbulence (0.7266), ism_methods_data (0.7098)
- **Current keyword baseline:** NO
- **Abstract:** Fast Radio Bursts probe ionised baryons through their observed dispersion measures. We present \turbofrb, a semi-analytic stochastic forward model for the intergalactic dispersion-measure distribution, $P({\rm DM}_{\rm IGM}\mid z)$, that resolves the diffuse IGM, halo, and filament contributions as explicit physical channels, with the halo and filament encounter rates coupled by a latent line-of-sight environmental variable. Only four effective parameters are calibrated against hydrodynamical ray-traced IllustrisTNG benchmark. The model matches the benchmark mean DM to the percent level and yields a per-redshift Jensen-Shannon divergence of at most $5\times10^{-3}$ across $z = 0.5$-$2.5$. The per-sightline channel decomposition makes explicit what closed-form parametric descriptions cannot show: the diffuse IGM sets the body of the distribution, while halos and filaments populate the high-DM tail. Applied to representative localised FRBs, the forward likelihood quantifies host-excess events independently of their astrophysical signatures and recovers the injected $H_0$ within $1σ$ in a closed-loop consistency test. The \turbofrb package is available at \href{https://github.com/jefersonfortunato/turbofrb}{github.com/jefersonfortunato/turbofrb}.

### [B] 55.1 — The initial evolution of SN 2011dh: The importance of inhomogeneities
- **arXiv:** [2608.17736](https://arxiv.org/abs/2608.17736)
- **Primary category:** astro-ph.HE
- **Positive anchor:** magnetic_fields = 0.7190
- **Negative anchor:** cosmology_large_scale_structure = 0.7153
- **Semantic margin:** +0.0037
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** magnetic_fields (0.7190), turbulence (0.7187), astrochemistry (0.7057)
- **Current keyword baseline:** NO
- **Abstract:** SN 2011dh is rather unique in that it offered detailed observations of the initial phase in the radio as well as optical regimes. This makes possible a comparison between models used to deduce properties of the outer envelope of the supernova ejecta. It is shown that a consistent description suggests the forward shock to have started in the piston phase with constant velocity, and only later, around 50 days, transitioned to the standard model, which is independent of initial conditions. In addition, observations imply that the radio source is inhomogeneous with a covering factor of, approximately, 50%. It is emphasised that the deduced properties of the synchrotron source are very sensitive to the presence of inhomogeneities; for example, a covering factor of 50% increases the ratio of the energy densities of relativistic electrons and magnetic field by several orders of magnitude as compared to a homogeneous source. The shallow density gradient in the envelope causes substantial deceleration of the forward shock. This is used to argue that the magnetic field strength scales inversely with radius rather than inversely with time; this is similar to SN 1993J. Attention is also drawn to the similarities between the flat spectra of compact, extragalatic radio sources and the evolution of radio supernovae; e.g., the scaling of the magnetic field and the constant brightness temperature.

### [B] 55.1 — Radio Properties of Narrow-Line and Broad-Line Seyfert 1 Galaxies
- **arXiv:** [2608.13303](https://arxiv.org/abs/2608.13303)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7222
- **Negative anchor:** galaxy_evolution_agn = 0.7162
- **Semantic margin:** +0.0060
- **Lexical positive/negative:** 0.4866 / 0.2835
- **Top positive topics:** galactic_ism_surveys (0.7222), turbulence (0.7103), astrochemistry (0.7028)
- **Current keyword baseline:** NO
- **Abstract:** Narrow-line Seyfert 1 (NLS1) galaxies host active galactic nuclei (AGN) with narrow optical emission lines of the broad-line region. This is often explained with a relatively lower mass of the central supermassive black hole and super-Eddington accretion. We compared the radio properties of large samples of NLS1 and broad-line Seyfert 1 (BLS1) galaxies compiled from the Sloan Digital Sky Survey. We cross-matched the NLS1 and BLS1 samples with the Faint Images of the Radio Sky at Twenty-Centimeters (FIRST) sky survey at 1.4 GHz and the first and second epoch data of the Very Large Array Sky Survey (VLASS) at 3 GHz. We calculated the radio spectral indices, the 1.4-GHz radio power, and the radio loudness. We found lower 1.4-GHz radio detection rates for the NLS1 galaxies. The median radio loudness values, the fraction of radio-loud AGN, and the median 1.4-GHz radio power are also lower for the NLS1 sample. The median spectral indices imply a slightly steeper radio spectrum for the NLS1 sample than for the BLS1 sample. Comparison of the star formation rates estimated from the radio data and the infrared measurements of the Wide-field Infrared Survey Explorer satellite indicated that more than half of the FIRST- and VLASS-detected NLS1 and BLS1 galaxies contain radio-emitting AGN.

### [B] 54.9 — Broadband emission of microquasar remnants
- **arXiv:** [2608.17000](https://arxiv.org/abs/2608.17000)
- **Primary category:** astro-ph.HE
- **Positive anchor:** turbulence = 0.6976
- **Negative anchor:** cosmology_large_scale_structure = 0.6944
- **Semantic margin:** +0.0032
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** turbulence (0.6976), ism_methods_data (0.6758), galactic_ism_surveys (0.6736)
- **Current keyword baseline:** NO
- **Abstract:** Microquasar remnants (MQRs), the long-lived cocoons inflated by extinct microquasar jets, have recently been proposed as hidden Galactic PeVatrons capable of producing ultra-high-energy gamma rays without an active central engine. While hadronic interactions can account for bright gamma-ray emission from nearby clouds, the direct detection of MQRs remains challenging because their intrinsic emission is expected to be extended and of low surface brightness. In this work, we explore the broadband emission of MQRs by focusing on the leptonic component confined within the cocoon and on particle interactions in the shocked shell surrounding it. We model the injection and time-dependent transport of relativistic particles, including stochastic re-acceleration driven by internal turbulence, treated as a second-order Fermi process. We consider sub-Eddington and super-Eddington microquasar systems and compute the resulting non-thermal emission from radio to gamma-ray energies, together with the thermal soft X-ray emission produced in the shocked shell. In the super-Eddington case, the intrinsic emission reaches peak values of $νL_ν\sim 10^{35}-10^{36}\,{\rm erg\,s^{-1}}$, whereas sub-Eddington remnants are typically several orders of magnitude fainter. At 1.3 GHz, the modeled cocoon surface brightness is of order $Σ_ν\sim 10^{-19}\,{\rm W\,m^{-2}\,Hz^{-1}\,sr^{-1}}$ for young powerful remnants and decreases rapidly as the remnant evolves. We find that the direct detectability of MQRs is therefore controlled mainly by surface brightness rather than by integrated luminosity. Powerful remnants may be detectable as extended synchrotron radio cocoons and shell-dominated soft X-ray structures, whereas sub-Eddington remnants are expected to be much harder to identify directly. Our results suggest that MQRs may constitute a hidden population of extended Galactic non-thermal sources.

### [B] 54.9 — Diverse ionized gas conditions in a dynamically hot, interacting galaxy at $z = 9.31$ revealed by JWST/NIRSpec IFU
- **arXiv:** [2608.16996](https://arxiv.org/abs/2608.16996)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7572
- **Negative anchor:** planetary_disks_exoplanets = 0.7538
- **Semantic margin:** +0.0033
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7572), galactic_ism_surveys (0.7334), massive_star_formation (0.7323)
- **Current keyword baseline:** YES
- **Abstract:** We present a spatially and spectrally resolved study of an interacting galaxy, Gz9p3 at $z=9.31$, using the James Webb Space Telescope NIRSpec/G395H IFU observation with high-spectral resolution ($R\approx 2700$) mode. Gz9p3 consists of two sub-regions (`core' and `tail'), which show stark contrast in their physical properties. The HII regions in the core are characterized by high electron density ($n_{e}\gtrsim2900$ cm$^{-3}$), low gas-phase metallicity ($0.25$ dex below the mass-metallicity relation), and yet relatively low specific star formation rate (sSFR) among the system. On the other hand, the tail exhibits low electron density ($n_{e}<70$ cm$^{-3}$), relatively high gas-phase metallicity that is consistent with the mass-metallicity relation, and high sSFR. The integrated spectrum thus shows the properties inbetween these two regions. No evidence of ordered rotation in ionized gas is found, suggesting that Gz9p3 is a dynamically hot system. Finally, we find ionized gas outflows characterized by the secondary [OIII]5007 line component throughout most of the system. The outflow velocity is below the escape velocity, making Gz9p3 one of the first galactic systems experiencing a galactic fountain. Overall, our findings indicate that this system is in a phase in which the pristine gas is falling efficiently into the core, diluting the gas metallicity, and enhancing star formation and outflows after the galaxy interaction.

### [B] 54.9 — The Low-Mass Baryon Cycle in QUEST Dwarf Galaxies I: Sample definition and first results
- **arXiv:** [2608.15782](https://arxiv.org/abs/2608.15782)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7636
- **Negative anchor:** galaxy_evolution_agn = 0.7603
- **Semantic margin:** +0.0034
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7636), galactic_ism_surveys (0.7485), massive_star_formation (0.7433)
- **Current keyword baseline:** NO
- **Abstract:** We introduce the QUEST Dwarfs program, which connects low-mass galaxies' stellar populations, interstellar medium, and circumgalactic medium in a large and coherently analyzed sample using a combination of optical spectroscopy, broadband imaging, and FUV absorption spectra of bright background sources .We present initial results from the first-release sample, comprising 14 galaxies with stellar mass $M_\mathrm{star} \leq 10^9 M_\odot$ at $z\approx0.001-0.017$, each with at least one CGM absorption probe at projected distances $d_\mathrm{proj}\lesssim 100$ kpc. This representative sample triples the number of available probes within 1/3 of the halo radius of dwarf galaxies outside of the Local Group. We find that the total silicon column density declines much more rapidly with projected distance than \textsc{Hi}, implying that chemically enriched cool gas is preferentially concentrated in the inner CGM, while the increasing ionization fraction of hydrogen with radius likely enhances this contrast. Accounting for unobserved silicon in higher ionization stages, we infer total metal masses of $\log M_Z/M_\odot\approx4.8$ and $6.5$ in the cool CGM within $0.3 R_\mathrm{vir}$ for dwarfs with median $\log M_\mathrm{star}/M_\odot=7.6$ and 8.6, respectively. These reservoirs correspond to $\approx3$% and $\approx16$% of the total metals produced over the galaxies' lifetimes. More massive galaxies also exhibit systematically stronger metal absorption, suggesting that projected distance governs the radial decline of metal absorption while stellar mass sets the normalization of the CGM metal profile. Individual ions reveal a multiphase structure, with low-ionization species concentrated in the inner halo and higher-ionization species extending farther. The full QUEST Dwarfs survey will provide the statistical power needed to isolate the dominant drivers of CGM enrichment in low-mass halos.

### [B] 54.8 — The SAMI Galaxy Survey: Linking Tidal Features and Orbit Populations Using Schwarzschild Modelling
- **arXiv:** [2608.14012](https://arxiv.org/abs/2608.14012)
- **Primary category:** astro-ph.GA
- **Positive anchor:** astrochemistry = 0.7161
- **Negative anchor:** stellar_atmospheres_evolution = 0.7129
- **Semantic margin:** +0.0032
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** astrochemistry (0.7161), galactic_ism_surveys (0.7127), ism_methods_data (0.7086)
- **Current keyword baseline:** NO
- **Abstract:** The evolution of angular momentum in galaxies is shaped by a combination of internal secular processes and external mechanisms such as mergers. Orbit-superposition based dynamical modelling provides a powerful means of linking the intrinsic orbital structures of galaxies to their global properties and merger histories. We construct Schwarzschild orbit-superposition models of massive ($\log(M/M_{\odot})>10$) SAMI galaxies using the DYNAMITE code, utilising deep KiDS photometry to accurately reproduce each galaxy's luminosity distribution. We find that the fractions of hot, cold, warm, and counter-rotating orbits all show significant correlations with the spin parameter proxy $λ_{R_e}$, with the strongest correlation arising from the combined hot plus counter-rotating fraction. When controlling for stellar mass and environment, we find that the fraction of hot and cold orbits show significant correlations with stellar age, whereas warm orbits do not. We further find that the lower values of $λ_{R_e}$ for young galaxies with shell merger features as compared to the full sample is driven by an excess of hot orbits and a deficit of cold orbits, with no dependence on warm orbits. We suggest that the kinematic transformation in this SAMI sample proceeds through stars transitioning directly from cold to hot orbits. As warm orbits are expected to arise from secular heating processes, these findings indicate that merger-driven heating is the dominant mechanism governing the redistribution of angular momentum and the reduction of rotational support in massive galaxies.

### [B] 53.5 — Diversity of Ionized Gas Structures in Nearby Metal-poor Dwarf Galaxies
- **arXiv:** [2608.19667](https://arxiv.org/abs/2608.19667)
- **Primary category:** astro-ph.GA
- **Positive anchor:** galactic_ism_surveys = 0.7525
- **Negative anchor:** planetary_disks_exoplanets = 0.7522
- **Semantic margin:** +0.0002
- **Lexical positive/negative:** 0.2835 / 0.0000
- **Top positive topics:** galactic_ism_surveys (0.7525), astrochemistry (0.7518), massive_star_formation (0.7319)
- **Current keyword baseline:** NO
- **Abstract:** We investigate whether optical and far-infrared [O III] emission from nearby metal-poor dwarf galaxies can be represented by a homogeneous one-zone ionized-gas model with a single electron temperature and density. Our sample comprises five galaxies from the Herschel Dwarf Galaxy Survey: HS1222+3741, SBS0335-052E, POX186, Haro11, and IZw18. We combine galaxy-integrated or nearly galaxy-integrated [O III] 4363 and 5007 measurements from Seimei/KOOLS-IFU observations and published or archival spectroscopy with Herschel/PACS [O III] 88um measurements. Because [O III] 4363 is not detected in HS1222+3741, the analysis is based on the remaining four galaxies. SBS0335-052E and Haro11 lie near or slightly beyond the low-density boundary of the one-zone diagnostic. Their nominal line ratios favor effective densities of ne<1cm-3, while conservative treatment of the uncertainties allows values up to 40 and 10cm-3, respectively. These remain substantially below densities inferred from independent diagnostics. By contrast, POX186 and IZw18 show no significant discrepancy between the optical--far-infrared [O III] and low-ionization optical diagnostics. Additional optical and ultraviolet diagnostics show that inferred densities can span several orders of magnitude within a galaxy. Representative two-zone models reproduce the [O III] 4363, 5007, and 88um emission in SBS0335-052E and Haro11 by combining relatively dense gas with cooler, low-density gas. The low-density component contributes approximately 61% and 72% of the 88um luminosity, but only 14% and 23% of the 5007 luminosity, respectively. These solutions are not unique and may represent a broader unresolved distribution of gas conditions. Our results show that temperatures and densities inferred from integrated one-zone analyses are effective quantities and that similar diagnostic discrepancies can arise in nearby metal-poor galaxies.

## Disagreement: old keyword selected, contrastive SKIP

- **TomoSphero: Fast Differentiable Projector for Planetary and Solar Tomography on Spherical Grids** — margin -0.0046, negative `planetary_disks_exoplanets` — [2608.16960](https://arxiv.org/abs/2608.16960)
- **A comprehensive cluster census of Orion. An application of the Significance Mode Analysis (SigMA) algorithm** — margin -0.0061, negative `planetary_disks_exoplanets` — [2608.16989](https://arxiv.org/abs/2608.16989)
- **Panchromatic JWST Observations and Models of the Dim Type Iax Supernova 2024vjm at 200 days** — margin -0.0082, negative `planetary_disks_exoplanets` — [2608.15040](https://arxiv.org/abs/2608.15040)
- **From Variability to SED Modeling: A Multiwavelength Study of the Neutrino Blazar TXS 0506+056** — margin -0.0086, negative `galaxy_evolution_agn` — [2608.17526](https://arxiv.org/abs/2608.17526)
- **Concerns regarding recurrent fluorescence's impact on smaller diffuse ISM aromatics** — margin -0.0022, negative `planetary_disks_exoplanets` — [2608.17886](https://arxiv.org/abs/2608.17886)
- **The instantaneous mass accretion rate of novae in quiescence: - an archival ultraviolet optical spectral analysis** — margin -0.0024, negative `planetary_disks_exoplanets` — [2608.18037](https://arxiv.org/abs/2608.18037)
- **Recurrent Multi-year Mg II BAL Variability in SDSS J1333+0012** — margin -0.0129, negative `stellar_atmospheres_evolution` — [2608.18211](https://arxiv.org/abs/2608.18211)
- **Asteroseismology of the multiperiodic field SX Phe pulsator BL Camelopardalis** — margin -0.0073, negative `planetary_disks_exoplanets` — [2608.19076](https://arxiv.org/abs/2608.19076)
- **Nascent Embedded-protostar Survey in Taurus (NEST) I: Protostellar Multiplicity** — margin -0.0223, negative `planetary_disks_exoplanets` — [2608.12186](https://arxiv.org/abs/2608.12186)
- **ALMA high resolution observations of Betelgeuse: Persistent structure spanning the inner atmosphere** — margin -0.0007, negative `planetary_disks_exoplanets` — [2608.19339](https://arxiv.org/abs/2608.19339)
- **Gaia DR3 Limits on Stellar Engine Technosignatures in Nearby Stars** — margin -0.0114, negative `stellar_atmospheres_evolution` — [2608.16060](https://arxiv.org/abs/2608.16060)
- **Machine Learning in Application to Automatic Noise Processing of Solar Spectrograms** — margin -0.0049, negative `generic_instrumentation` — [2608.16392](https://arxiv.org/abs/2608.16392)
- **Eta Carinae's historical light curve: evidence for cyclic Roche lobe overflow from the primary star** — margin -0.0137, negative `planetary_disks_exoplanets` — [2608.16818](https://arxiv.org/abs/2608.16818)
- **Radiation damage to the Hubble Space Telescope has been several years out of phase with the Solar cycle** — margin -0.0143, negative `planetary_disks_exoplanets` — [2608.18214](https://arxiv.org/abs/2608.18214)
- **TIC 433545934: The first 2+2 type doubly eclipsing binary with extra, mutual eclipses** — margin -0.0156, negative `planetary_disks_exoplanets` — [2608.13034](https://arxiv.org/abs/2608.13034)
- **The Roman Coronagraph Community Participation Program: pre-launch reference star list and impact of reference star properties on post-processing performance** — margin -0.0175, negative `planetary_disks_exoplanets` — [2608.17057](https://arxiv.org/abs/2608.17057)
- **From the Earth to the Sun** — margin -0.0183, negative `planetary_disks_exoplanets` — [2608.13635](https://arxiv.org/abs/2608.13635)
- **Responses of the X-ray spectrometer/imager STIX onboard Solar Orbiter** — margin -0.0112, negative `planetary_disks_exoplanets` — [2608.19420](https://arxiv.org/abs/2608.19420)
- **Astronomical Cardiology II: A Search For Heartbeat Stars Using APOGEE and TESS** — margin -0.0189, negative `planetary_disks_exoplanets` — [2608.12474](https://arxiv.org/abs/2608.12474)
- **Could John Ellard Gore have pre-empted the Hertzsprung-Russell diagram?** — margin -0.0209, negative `stellar_atmospheres_evolution` — [2608.18799](https://arxiv.org/abs/2608.18799)
- **JWST-MIRI's multi-dimensional view of mass loss in the irradiated disks of NGC 1977** — margin -0.0222, negative `planetary_disks_exoplanets` — [2608.17226](https://arxiv.org/abs/2608.17226)
- **Early Planet Formation in Embedded Disks (eDisk). XXIV: Systematic Investigation of Disk Structures based on Visibility Analysis** — margin -0.0240, negative `planetary_disks_exoplanets` — [2608.19364](https://arxiv.org/abs/2608.19364)
- **Are Hot Jupiters Tidally Disrupted During Stellar Main Sequence?** — margin -0.0322, negative `planetary_disks_exoplanets` — [2608.12790](https://arxiv.org/abs/2608.12790)
- **Hydrodynamics modeling of the water snow line in young protoplanetary disks with dust-size-dependent opacities** — margin -0.0262, negative `planetary_disks_exoplanets` — [2608.17921](https://arxiv.org/abs/2608.17921)
- **A Catalog of Homogeneously Derived Stellar Parameters for Spectroscopic Survey Stars** — margin -0.0191, negative `planetary_disks_exoplanets` — [2608.17734](https://arxiv.org/abs/2608.17734)
- **SN 2023gfo: A Peculiar Type IIP Supernova with High Luminosity and Normal Plateau Duration** — margin -0.0267, negative `planetary_disks_exoplanets` — [2608.16006](https://arxiv.org/abs/2608.16006)
- **Stellar tidal systematics in apsidal-motion searches for circumbinary planets: CH Ind and SW CMa** — margin -0.0270, negative `planetary_disks_exoplanets` — [2608.13269](https://arxiv.org/abs/2608.13269)
- **Stability of circumbinary orbits in misaligned triple star systems** — margin -0.0304, negative `planetary_disks_exoplanets` — [2608.15316](https://arxiv.org/abs/2608.15316)
- **A metallicity sweet spot for disc fragmentation and planet formation** — margin -0.0235, negative `planetary_disks_exoplanets` — [2608.18830](https://arxiv.org/abs/2608.18830)
- **Planetary systems in the light of asteroseismology: metallicity threshold for the planetary systems and age-metallicity relation** — margin -0.0314, negative `planetary_disks_exoplanets` — [2608.15849](https://arxiv.org/abs/2608.15849)
- **Are Near Resonant Multiple-planet Systems from Kepler Young?** — margin -0.0421, negative `planetary_disks_exoplanets` — [2608.12786](https://arxiv.org/abs/2608.12786)
- **Toward Operational Solar Flare Peak Flux Nowcasting: A Strategy Combining Real-Time Data, Machine Learning, and NOAA Flare Detection Criteria** — margin -0.0225, negative `solar_physics` — [2608.20062](https://arxiv.org/abs/2608.20062)
- **Revisiting gravitational instability in protostellar discs with improved radiative cooling models** — margin -0.0362, negative `planetary_disks_exoplanets` — [2608.13058](https://arxiv.org/abs/2608.13058)
- **Stellar Abundances as Probes of Rocky Exoplanet Interiors: The Mantle Composition and Mineralogy of GJ 486b** — margin -0.0317, negative `planetary_disks_exoplanets` — [2608.18457](https://arxiv.org/abs/2608.18457)
- **Substructure evolution from protoplanetary to debris disks driven by mutually gravitating planetesimals and implications on Kepler resonances and free-floating planets** — margin -0.0556, negative `planetary_disks_exoplanets` — [2608.19329](https://arxiv.org/abs/2608.19329)

## Disagreement: contrastive A/B, old keyword missed

- **[A] 79.4 — Impact of Upstream Clumpiness on Supernova Remnant Forward Shock Evolution in Molecular Cloud Environments** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0524 — [2608.17477](https://arxiv.org/abs/2608.17477)
- **[A] 78.2 — Collisionless Shock Driven by a Supersonic Velocity Shear** — `turbulence` vs `stellar_atmospheres_evolution`, margin +0.0552 — [2608.16656](https://arxiv.org/abs/2608.16656)
- **[A] 75.6 — Outflows in steep density gradients: diversity of behavior and implications for tidal disruption events and luminous fast blue optical transients** — `turbulence` vs `planetary_disks_exoplanets`, margin +0.0493 — [2608.19512](https://arxiv.org/abs/2608.19512)
- **[A] 72.8 — CHANG-ES XL: Magnetic Field Structures in the Disk and Halo of NGC 891** — `magnetic_fields` vs `planetary_disks_exoplanets`, margin +0.0376 — [2608.12275](https://arxiv.org/abs/2608.12275)
- **[B] 68.3 — High-spectral-resolution Observations of the [S II] Emission-line Doublet in the Filamentary Nebula Surrounding NGC 1275** — `turbulence` vs `generic_instrumentation`, margin +0.0332 — [2608.14888](https://arxiv.org/abs/2608.14888)
- **[B] 67.7 — Interpretations of the $10\%$ polarization observed in the early forward-shock afterglow of GRB 091208** — `magnetic_fields` vs `planetary_disks_exoplanets`, margin +0.0318 — [2608.15494](https://arxiv.org/abs/2608.15494)
- **[B] 67.5 — Chromospheric heating and magnetic topology above the shared penumbra of a delta-spot: Multi-line inversions and multi-height magnetic-field extrapolations** — `magnetic_fields` vs `galaxy_evolution_agn`, margin +0.0314 — [2608.19983](https://arxiv.org/abs/2608.19983)
- **[B] 67.1 — Physics of Circular Polarized Ion-Scale Waves in Hybrid Simulations of Alfvénic Fluctuations** — `turbulence` vs `planetary_disks_exoplanets`, margin +0.0381 — [2608.14151](https://arxiv.org/abs/2608.14151)
- **[B] 65.4 — Diffuse HI emission in the circumgalactic medium of NGC891 and NGC4565 - III: azimuthal profiles** — `galactic_ism_surveys` vs `stellar_atmospheres_evolution`, margin +0.0266 — [2608.19186](https://arxiv.org/abs/2608.19186)
- **[B] 64.8 — Strangeness Transport in Binary Neutron Star Mergers** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0405 — [2608.15527](https://arxiv.org/abs/2608.15527)
- **[B] 63.8 — Aromatics and Aliphatics in Local Star-Forming Galaxies as Probed by AKARI** — `astrochemistry` vs `planetary_disks_exoplanets`, margin +0.0307 — [2608.14989](https://arxiv.org/abs/2608.14989)
- **[B] 63.7 — ALMA observations of pre-JWST z ~ 10 galaxy candidates: A CO(J = 9-8) line from a ULIRG at z = 2.54 and revisit of the photometric redshifts with JWST photometry** — `astrochemistry` vs `galaxy_evolution_agn`, margin +0.0229 — [2608.12708](https://arxiv.org/abs/2608.12708)
- **[B] 63.5 — The efficient star-forming regions of stripped-envelope supernovae** — `astrochemistry` vs `galaxy_evolution_agn`, margin +0.0170 — [2608.18897](https://arxiv.org/abs/2608.18897)
- **[B] 63.4 — A self-consistent solar coronal heating model by Alfvenic waves** — `magnetic_fields` vs `solar_physics`, margin +0.0130 — [2608.15221](https://arxiv.org/abs/2608.15221)
- **[A] 62.2 — Large-Scale Dynamos Driven by Shear-Flow-Induced Jets** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0217 — [2608.12530](https://arxiv.org/abs/2608.12530)
- **[A] 62.1 — Star Formation in the H II Region Sh 2-205: 3D Morphology and Kinematics from Young Stars and Molecular Gas** — `astrochemistry` vs `planetary_disks_exoplanets`, margin +0.0214 — [2608.16179](https://arxiv.org/abs/2608.16179)
- **[B] 61.9 — Confining density functional approach to the QCD phase diagram at low temperatures and thermal twin stars** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0265 — [2608.18038](https://arxiv.org/abs/2608.18038)
- **[B] 61.9 — Massive cold hybrid stars in a modified Polyakov-Nambu-Jona-Lasinio model** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0264 — [2608.12653](https://arxiv.org/abs/2608.12653)
- **[B] 61.7 — Multiphase turbulence as the origin of OH+, H2O+ and H3+ column density scatter in the local ISM** — `astrochemistry` vs `galaxy_evolution_agn`, margin +0.0131 — [2608.15633](https://arxiv.org/abs/2608.15633)
- **[B] 61.4 — Radio Properties of RS Canum Venaticorum Variables in VLASS and RACS** — `astrochemistry` vs `planetary_disks_exoplanets`, margin +0.0328 — [2608.13653](https://arxiv.org/abs/2608.13653)
- **[B] 61.3 — Correlations with Magnetic Activity in the Solar Near-Surface Shear Layer. I. Rotation** — `magnetic_fields` vs `cosmology_large_scale_structure`, margin +0.0175 — [2608.19438](https://arxiv.org/abs/2608.19438)
- **[B] 61.2 — Why is GN-z11 Bright, Compact, and Nitrogen Enhanced? Insights from UV Absorption and Emission Diagnostics** — `astrochemistry` vs `stellar_atmospheres_evolution`, margin +0.0248 — [2608.12466](https://arxiv.org/abs/2608.12466)
- **[B] 61.0 — pynucastro 3: A community library for nuclear astrophysics** — `astrochemistry` vs `stellar_atmospheres_evolution`, margin +0.0245 — [2608.17049](https://arxiv.org/abs/2608.17049)
- **[B] 61.0 — Two domains of extended Lyman-alpha emission around galaxies: from local radiation to environmental regulation** — `galactic_ism_surveys` vs `galaxy_evolution_agn`, margin +0.0169 — [2608.16665](https://arxiv.org/abs/2608.16665)
- **[B] 60.9 — The deepest color-magnitude diagrams for the benchmark open cluster NGC 2437 from Gaia and VVVX** — `galactic_ism_surveys` vs `planetary_disks_exoplanets`, margin +0.0167 — [2608.14514](https://arxiv.org/abs/2608.14514)
- **[B] 60.6 — Modelling mountains on accreting magnetized neutron stars** — `magnetic_fields` vs `cosmology_large_scale_structure`, margin +0.0235 — [2608.17508](https://arxiv.org/abs/2608.17508)
- **[B] 60.6 — SPURS: Massive Stars, Dense Gas, and Ly$α$ Escape in GN-z11 at $z = 10.6$** — `astrochemistry` vs `stellar_atmospheres_evolution`, margin +0.0234 — [2608.12699](https://arxiv.org/abs/2608.12699)
- **[B] 60.4 — Large eROSITA X-ray sources as 2MRS galaxy groups** — `galactic_ism_surveys` vs `cosmology_large_scale_structure`, margin +0.0230 — [2608.17732](https://arxiv.org/abs/2608.17732)
- **[B] 60.3 — Cosmography with DESI-DR1 Cosmic Chronometers: Direct H(z) measurements from Luminous Red Galaxy ages** — `astrochemistry` vs `galaxy_evolution_agn`, margin +0.0229 — [2608.13178](https://arxiv.org/abs/2608.13178)
- **[B] 60.2 — The Production of Electron-Capture Elements in Thermonuclear Supernovae: Theory vs. Observations** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0171 — [2608.13432](https://arxiv.org/abs/2608.13432)
- **[B] 60.1 — $\texttt{Aether.jl}$ : A High-Performance 3D MHD and Multifluid Dust Code Written in a Dynamic Language with an Interactive Human-AI Development Framework** — `turbulence` vs `planetary_disks_exoplanets`, margin +0.0149 — [2608.14048](https://arxiv.org/abs/2608.14048)
- **[B] 59.7 — Evolution of lunar wake potentials: structure, energy conversion, and their imprints on velocity distributions** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0291 — [2608.18383](https://arxiv.org/abs/2608.18383)
- **[B] 59.3 — Diffuse Dwarf Galaxies in Galaxy Clusters: I. Stellar Populations and Radial Gradients** — `astrochemistry` vs `galaxy_evolution_agn`, margin +0.0132 — [2608.17375](https://arxiv.org/abs/2608.17375)
- **[B] 59.1 — The Total and Polarized Radio Emission from the Innermost Jets of a High-Redshift Quasar and a Candidate at Parsec-Scale Resolution** — `turbulence` vs `galaxy_evolution_agn`, margin +0.0203 — [2608.18691](https://arxiv.org/abs/2608.18691)
- **[B] 59.1 — OH Line Detections in Southern Galaxies of the IRAS Revised Bright Galaxy Sample** — `galactic_ism_surveys` vs `generic_instrumentation`, margin +0.0127 — [2608.14473](https://arxiv.org/abs/2608.14473)
- **[B] 59.0 — The segmented spiral structure of the Solar neighbourhood traced by young clustered populations** — `galactic_ism_surveys` vs `galaxy_evolution_agn`, margin +0.0071 — [2608.17887](https://arxiv.org/abs/2608.17887)
- **[B] 58.7 — Hemispheric Asymmetry of Solar Active Regions Arises from a Nested Population** — `astrochemistry` vs `cosmology_large_scale_structure`, margin +0.0117 — [2608.12263](https://arxiv.org/abs/2608.12263)
- **[B] 58.1 — The X-Ray Continuum Emission Region in the Lensed Quasar SDSS J133907.23+131038.6 is Much Smaller than the Accretion Disk** — `galactic_ism_surveys` vs `galaxy_evolution_agn`, margin +0.0234 — [2608.17041](https://arxiv.org/abs/2608.17041)
- **[B] 58.0 — Kinematics and Dynamics of the Open Cluster NGC 2302** — `astrochemistry` vs `stellar_atmospheres_evolution`, margin +0.0102 — [2608.18550](https://arxiv.org/abs/2608.18550)
- **[B] 57.7 — Accurately simulating gain and clock-induced charge production in the EMCCD gain register** — `astrochemistry` vs `generic_instrumentation`, margin +0.0095 — [2608.17842](https://arxiv.org/abs/2608.17842)
- **[B] 57.0 — Multi-zone Modeling of Blazar Jets: Constraints from GeV-Optical Correlation and Short-Timescale Variability** — `galactic_ism_surveys` vs `cosmology_large_scale_structure`, margin +0.0081 — [2608.18707](https://arxiv.org/abs/2608.18707)
- **[B] 56.9 — Differential Reddening and Extinction Law Analyses of Galactic Open Clusters** — `galactic_ism_surveys` vs `stellar_atmospheres_evolution`, margin +0.0023 — [2608.13313](https://arxiv.org/abs/2608.13313)
- **[B] 56.5 — Revisiting the Growth Rate of the Relativistic Tearing Instability: The Role of the Non-ideal MHD Structure** — `magnetic_fields` vs `planetary_disks_exoplanets`, margin +0.0068 — [2608.19645](https://arxiv.org/abs/2608.19645)
- **[B] 55.9 — No Evidence for Nearby Circumstellar Material in the Type Ia Supernova 2025rbs** — `astrochemistry` vs `planetary_disks_exoplanets`, margin +0.0055 — [2608.13655](https://arxiv.org/abs/2608.13655)
- **[B] 55.6 — X-ray thread/Nonthermal Radio Filament associations: Evidence for Interstellar Magnetic Reconnection** — `molecular_clouds` vs `planetary_disks_exoplanets`, margin +0.0050 — [2608.14830](https://arxiv.org/abs/2608.14830)
- **[B] 55.3 — Sr and Ba yields of the First Generation(s) of stars: Constraints from metal-poor stars** — `astrochemistry` vs `stellar_atmospheres_evolution`, margin +0.0043 — [2608.17001](https://arxiv.org/abs/2608.17001)
- **[B] 55.2 — A stochastic forward model for the intergalactic dispersion-measure distribution of Fast Radio Bursts** — `galactic_ism_surveys` vs `galaxy_evolution_agn`, margin +0.0039 — [2608.17658](https://arxiv.org/abs/2608.17658)
- **[B] 55.1 — The initial evolution of SN 2011dh: The importance of inhomogeneities** — `magnetic_fields` vs `cosmology_large_scale_structure`, margin +0.0037 — [2608.17736](https://arxiv.org/abs/2608.17736)
- **[B] 55.1 — Radio Properties of Narrow-Line and Broad-Line Seyfert 1 Galaxies** — `galactic_ism_surveys` vs `galaxy_evolution_agn`, margin +0.0060 — [2608.13303](https://arxiv.org/abs/2608.13303)
- **[B] 54.9 — Broadband emission of microquasar remnants** — `turbulence` vs `cosmology_large_scale_structure`, margin +0.0032 — [2608.17000](https://arxiv.org/abs/2608.17000)
- **[B] 54.9 — The Low-Mass Baryon Cycle in QUEST Dwarf Galaxies I: Sample definition and first results** — `astrochemistry` vs `galaxy_evolution_agn`, margin +0.0034 — [2608.15782](https://arxiv.org/abs/2608.15782)
- **[B] 54.8 — The SAMI Galaxy Survey: Linking Tidal Features and Orbit Populations Using Schwarzschild Modelling** — `astrochemistry` vs `stellar_atmospheres_evolution`, margin +0.0032 — [2608.14012](https://arxiv.org/abs/2608.14012)
- **[B] 53.5 — Diversity of Ionized Gas Structures in Nearby Metal-poor Dwarf Galaxies** — `galactic_ism_surveys` vs `planetary_disks_exoplanets`, margin +0.0002 — [2608.19667](https://arxiv.org/abs/2608.19667)
