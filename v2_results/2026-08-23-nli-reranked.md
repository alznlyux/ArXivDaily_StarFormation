# ISM Literature Recommender v2.3 — SPECTER2 + NLI

Generated: 2026-08-23T04:37:32Z
Source: `2026-08-23-domain-gated.json`

## Summary

- Candidates: **455**
- NLI evaluated: **91**
- A: **3**
- B: **8**
- C: **48**
- SKIP: **396**
- Promoted by NLI: **0**
- Downgraded by NLI: **19**
- NLI model: `cross-encoder/nli-deberta-v3-xsmall`

## A/B candidates

### [A] 76.8 — ALOHA IRDCs Molecular Line Follow-up: I. Gas properties and kinematics
- **arXiv:** [2608.20238](https://arxiv.org/abs/2608.20238)
- **Primary:** astro-ph.GA
- **SPECTER2:** `astrochemistry` 0.7783 vs `planetary_disks_exoplanets` 0.7266 (margin +0.0517)
- **Domain evidence:** 14.0 — `contrastive`
- **NLI:** pos 0.009 / neg 0.003 / margin +0.006
- **Decision:** A → A — NLI consistent or protected by direct object evidence
- **Abstract:** Infrared Dark Clouds are ideal sites for investigating the initial conditions of massive star and cluster formation. The A Lei Of the Habitat and Assembly of Infrared Dark Clouds (ALOHA IRDCs), a James Clerk Maxwell Telescope (JCMT) Large Program, has mapped nearby IRDCs with SCUBA-2. Complementary molecular line observations are needed to characterise the physical, kinematic, and chemical properties of the dense gas. We aim to determine the thermal, kinematic, and chemical properties of clumps identified in the ALOHA IRDCs, and to assess their evolutionary status and level of star-forming activity. We performed single-pointing K-band and W-band observations towards 56 ALOHA IRDCs clumps using the Effelsberg 100-m and Yebes 40-m telescopes, respectively. We derived NH3 kinetic temperatures using the hyperfine group ratio (HFGR) method and identified infall and shock signatures from HCO+, H13CO+, SiO, and HNCO profiles. Water masers and NH2D emission were used as complementary tracers of chemical evolution and star formation. The clumps exhibit kinetic temperatures of 15-29 K. We detect NH2D emission towards 18 sources, with NH2D centroid velocities consistent with NH3, indicating both species trace the same dense gas component. More than half of the clumps display blue-asymmetric HCO+ profiles, identifying them as infall candidates. Water masers are detected in 22 sources, with prominent velocity ranges and variability. Broad SiO emission (>~20 km/s) indicates strong shocks, while narrower extents (<~6km/s) likely trace large-scale interactions or low-velocity shocks. The widespread infall signatures, shock tracers, masers, and NH2D emission suggest that relatively quiescent, chemically young material can coexist with dynamically active gas affected by early protostellar feedback, providing insight into the coupled physical and chemical evolution of massive IRDC clumps.

### [A] 66.9 — Impact of Upstream Clumpiness on Supernova Remnant Forward Shock Evolution in Molecular Cloud Environments
- **arXiv:** [2608.17477](https://arxiv.org/abs/2608.17477)
- **Primary:** astro-ph.HE
- **SPECTER2:** `turbulence` 0.754 vs `relativistic_plasma_transients` 0.7285 (margin +0.0255)
- **Domain evidence:** 4.5 — `contrastive`
- **NLI:** pos 0.003 / neg 0.002 / margin +0.002
- **Decision:** A → A — NLI consistent or protected by direct object evidence
- **Abstract:** Supernova remnants (SNRs) are widely considered to be the primary accelerators of Galactic cosmic rays. In recent years, detailed observations have significantly progressed for young SNRs interacting with molecular clouds, a prime example being RX J1713.7-3946. When molecular clouds are clumpy, their impact can affect not only radiation properties but also shock wave propagation. Therefore, a quantitative understanding linking observational quantities with the ambient medium structure is highly required. In this study, we perform three-dimensional hydrodynamic simulations to model a molecular cloud with an inhomogeneous density structure driven by supersonic turbulence and subsequent SNR formation. To investigate various pre-supernova environments, we systematically vary the medium clumpiness by replacing gas below a threshold number density with a low-density hot gas, quantifying the relationship between the forward shock velocity and the volume filling factor of the high-density clumps. As a result, we find that at an elapsed time of 1000 yr-a typical age for a young SNR-the forward shock can evolve consistently with the fast shock velocity measured in RX J1713.7-3946, provided that the clump volume filling factor is approximately 10% or less. Considering that hadronic gamma-ray emission originates exclusively from the clumpy, high-density gas, our findings suggest that the total energy of cosmic-ray protons in RX J1713.7-3946 is higher than previously estimated, amounting to at least several percent of the typical supernova explosion energy.

### [A] 64.8 — Star Formation in the H II Region Sh 2-205: 3D Morphology and Kinematics from Young Stars and Molecular Gas
- **arXiv:** [2608.16179](https://arxiv.org/abs/2608.16179)
- **Primary:** astro-ph.GA
- **SPECTER2:** `astrochemistry` 0.7679 vs `planetary_disks_exoplanets` 0.7464 (margin +0.0214)
- **Domain evidence:** 12.25 — `contrastive`
- **NLI:** pos 0.007 / neg 0.002 / margin +0.005
- **Decision:** A → A — NLI consistent or protected by direct object evidence
- **Abstract:** Using Gaia astrometry of young stars combined with CO observations, we present the first systematic three-dimensional (3D) analysis of the structure, kinematics, and evolutionary history of the star-forming regions in the environs of the H II region Sh 2-205 (S205). S205 exhibits a complex morphology and coherent expansion on both global and subregional scales. We identify several O9-B1 stars and a 0.56 Myr old pulsar that are likely associated with the region. A momentum estimate suggests that feedback from these objects may account for the observed overall expansion. Trace-back analysis of the expansion, combined with color-magnitude diagram fitting for young star clusters, indicates at least two episodes of star formation. These results reveal a complex star-formation history of S205 and provide new insights into its 3D evolution.

### [B] 69.3 — Complex morphology and kinematics at the heart of the very low luminosity object IRAM 04191+1522
- **arXiv:** [2608.17593](https://arxiv.org/abs/2608.17593)
- **Primary:** astro-ph.SR
- **SPECTER2:** `molecular_clouds` 0.7678 vs `planetary_disks_exoplanets` 0.7571 (margin +0.0107)
- **Domain evidence:** 10.0 — `contrastive`
- **NLI:** pos 0.430 / neg 0.243 / margin +0.187
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** The formation of the majority of brown dwarfs (BDs) remains uncertain. They may form in molecular cloud cores in a process akin to low mass star formation, or via fragmentation in circumstellar discs. Studying the youngest, most embedded sources is crucial for distinguishing these scenarios. We investigate molecular gas morphology and kinematics around one young & embedded very low luminosity object (VeLLO), IRAM 04191+1522, utilising archival ALMA observations of 13CO, C18O, and SO. We trace gas on scales of a few 10s to 100s of au around the source to search for outflowing and/or infalling structures. The red and blueshifted 13CO (3-2) emission show distinct morphologies and kinematics. The blueshifted emission to the north-west may trace shocked material oriented differently from the previously reported approx. 0.1 pc CO outflow. Redshifted emission mainly to the south-east and south-west may trace the base of an outflow cavity. The position angle of this cavity suggests the presence of a second outflow, which supports the possible binary nature of this VeLLO. The C18O (2-1) emission is highly complex, comprising structures at different spatial scales and distances from the source. These may trace a mix of molecular outflow, outflow cavity, and disc emission. SO 65-54 reveals evidence for anticlockwise rotation around the central source, together with a northern structure of uncertain origin. We have identified a complex set of 13CO (3-2) and C18O (2-1) structures alongside evidence of a new outflow cavity at a distinct position angle from previously detected outflows. This supports the scenario that IRAM 04191+1522 is a binary system. The northern SO gas structure remains unexplained. Higher spectral resolution observations at intermediate scales are needed to characterise these substructures, their connection to larger scale structures, and to determine this system's final fate.

### [B] 65.8 — The efficient star-forming regions of stripped-envelope supernovae
- **arXiv:** [2608.18897](https://arxiv.org/abs/2608.18897)
- **Primary:** astro-ph.GA
- **SPECTER2:** `astrochemistry` 0.7478 vs `galaxy_evolution_agn` 0.7307 (margin +0.0170)
- **Domain evidence:** 18.75 — `contrastive`
- **NLI:** pos 0.006 / neg 0.002 / margin +0.004
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** Massive stars ($> 8~\rm{M}_{\odot}$) play a key role in shaping the interstellar medium of galaxies through stellar feedback. However, how these stars form and evolve before exploding as core-collapse supernovae (SNe) remains elusive. We compute for the first time the star-formation efficiencies (SFEs) at the locations of hydrogen-rich (H-rich) SNe and stripped-envelope SNe (SESNe) to constrain their progenitor properties. We used VLT/MUSE and ALMA observations of H$α$/H$β$ and CO(2-1) emission lines to trace the components of the warm ionised gas and cold molecular gas, respectively. Both observations resolve individual H II regions and giant molecular clouds at spatial resolutions on cloud-scales ($\sim$100 pc). This combined data allows us to compute the SFE from the star formation rate (SFR) and the molecular gas mass (M$_{\rm{mol}}$) as SFE = SFR/M$_{\rm{mol}}$. We find that SESNe explode in environments that are currently forming stars eight times more efficiently than those of H-rich SNe (higher SFR for SESNe with similar M$_{\rm{mol}}$). On one hand, this is consistent with the scenario in which the majority of SESNe are produced from very massive stars ($> 20~\rm{M}_{\odot}$) if the initial mass function is top-heavy. On the other hand, most of SESN progenitor channels are formed from interacting binaries ($< 20~\rm{M}_{\odot}$) if an increased binary system formation rate is connected with turbulences and, in turn, with the boost to SFE. Then, an increased binary fraction could explain the enhanced H$α$ luminosities. In summary, SESNe preferentially occur in regions of intense, efficient star formation rather than simply higher gas content.

### [B] 65.5 — Diffuse HI emission in the circumgalactic medium of NGC891 and NGC4565 - III: azimuthal profiles
- **arXiv:** [2608.19186](https://arxiv.org/abs/2608.19186)
- **Primary:** astro-ph.GA
- **SPECTER2:** `galactic_ism_surveys` 0.7573 vs `stellar_atmospheres_evolution` 0.7307 (margin +0.0266)
- **Domain evidence:** 4.5 — `contrastive`
- **NLI:** pos 0.006 / neg 0.002 / margin +0.004
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** Diffuse HI emission in the circumgalactic medium (CGM) of NGC891 and NGC4565 has been previously shown to trace an inflow along minor axes pointings and to co-rotate with the HI disk along major axes pointings out to ~100 kpc (Das2020b,Das2024a). To obtain a 360$^\circ$ view of the inner neutral CGM ($\rm < 25 kpc$ for NGC891, $\rm < 30 kpc$ for NGC4565), we perform deep stare observations with the Green Bank Telescope (GBT) along the off-axes, 45$^\circ$ between principal axes, achieving a 5$σ$ column density sensitivity of $1.1-1.2 x 10^{17} \rm cm^{-2}$ over a 20 kms$^{-1}$ velocity width. While detecting HI emission in the inner CGM with single-dish telescopes is common, separating the true CGM emission from disk contamination is extremely challenging and has so far been largely unsuccessful. To achieve that, we compare our single-dish detections to deep interferometric maps from the Westerbork Synthesis Radio Telescope (WSRT) HALOGAS survey, and improve upon our previous methods by incorporating velocity offset corrections and channel-wise brightness-temperature scaling. We find that $30-38$ % and $18-28$ % of the emission detected by the GBT cannot be explained by WSRT in NGC891 and NGC4565, respectively, implying a true CGM detection. There is $4-6$ ($3-7$) times more HI along the off-axes than major (minor) axes, nullifying the common assumption of azimuthal symmetry of the neutral CGM. The velocity profile of the diffuse inner CGM suggests a lagged co-rotation with the HI disk in both galaxies. This exercise illustrates the power of deep observation and careful cross-instrument comparisons to characterize the diffuse HI in the CGM.

### [B] 64.7 — Multiphase turbulence as the origin of OH+, H2O+ and H3+ column density scatter in the local ISM
- **arXiv:** [2608.15633](https://arxiv.org/abs/2608.15633)
- **Primary:** astro-ph.GA
- **SPECTER2:** `astrochemistry` 0.7647 vs `galaxy_evolution_agn` 0.7515 (margin +0.0131)
- **Domain evidence:** 7.5 — `contrastive`
- **NLI:** pos 0.015 / neg 0.004 / margin +0.011
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** Observations of the reactive ions OH+, H2O+ and H3+ in the Galactic interstellar medium reveal large sight-line-to-sight-line scatter in their column densities, commonly interpreted as evidence for substantial variations in the cosmic-ray ionization rate (CRIR). We revisit this interpretation using high-resolution three-dimensional magneto-hydrodynamic simulations of the multiphase ISM with time-dependent chemistry for H, H2, H+ and electrons, building on the fiducial model of Godard et al. (2023). We find that a single CRIR of ~2 10^{-16} s^{-1}, together with standard Galactic-scale parameters, naturally produces broad column-density distributions for all three tracers in good agreement with the observed medians and percentile widths, with no fine tuning. Reaching this match requires that the post-processing of OH+, H2O+ and H3+ retain the time-dependent H2 field generated by the turbulent flow rather than assume chemical equilibrium: turbulence drives long-lived H2 enhancements in the unstable neutral medium where OH+ and H2O+ predominantly reside, and an equilibrium treatment under-predicts their columns substantially. H3+, which receives most of its column from denser CNM gas closer to equilibrium, is much less affected. Our results caution against interpreting sight-line-to-sight-line scatter as direct evidence for large CRIR fluctuations, and motivate a shift from independent 1D equilibrium analyses toward 3D dynamical frameworks when inferring ionization conditions in the ISM.

### [B] 63.7 — The Galactic Centre G+0.633-0.0604 Molecular Cloud: A New Gold Mine for Astrochemistry
- **arXiv:** [2608.14381](https://arxiv.org/abs/2608.14381)
- **Primary:** astro-ph.GA
- **SPECTER2:** `astrochemistry` 0.7769 vs `planetary_disks_exoplanets` 0.7615 (margin +0.0154)
- **Domain evidence:** 7.0 — `contrastive`
- **NLI:** pos 0.025 / neg 0.011 / margin +0.014
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** Astrochemistry is living a golden age, with more than a quarter of the ~350 molecules in the current interstellar census having been detected over the last three years. One of the sources driving this progress is the G+0.693-0.027 cloud, located in the northern part of the Galactic Centre Sgr B2 complex. In this contribution, we present the astrochemical characterisation of G+0.633-0.0604, a newly discovered chemically rich molecular cloud at the southern edge of Sgr B2. With an inventory of >120 species, G+0.633 provides robust second detections of several prebiotic molecules only reported towards G+0.693, establishing it as the first confirmed astrochemical twin of G+0.693 while demonstrating that the extraordinary chemistry of this cloud is not unique. Furthermore, G+0.633 offers an observational advantage over G+0.693 since it displays half narrower linewidths. Together, G+0.633 and G+0.693 form a unique benchmark pair for unveiling molecular complexity and prebiotic chemistry in the interstellar medium.

### [B] 62.3 — JWST Whirlpool Galaxy Treasury: Mid-Infrared Emission in M51 and its Relation to Gas Column and Star Formation
- **arXiv:** [2608.16802](https://arxiv.org/abs/2608.16802)
- **Primary:** astro-ph.GA
- **SPECTER2:** `astrochemistry` 0.7553 vs `galaxy_evolution_agn` 0.7498 (margin +0.0055)
- **Domain evidence:** 7.25 — `contrastive`
- **NLI:** pos 0.014 / neg 0.004 / margin +0.010
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** Using JWST/MIRI imaging of M51 in eight broadband filters, we investigate correlations of mid-infrared emission from polycyclic aromatic hydrocarbons (PAHs) and dust continuum with molecular, atomic, and ionized gas traced by CO(1-0), HI, and Pa-alpha, respectively. In molecular gas-dominated regions, PAH-dominated filters (F560W, F770W, F1130W, F1280W) exhibit near-linear correlations with CO(1-0) at 40 pc scale, indicating that PAHs are well-mixed with gas and experience relatively constant radiation field intensities. The F1500W, F1800W, and F2100W dust continuum-dominated filters show shallower slopes with CO(1-0), reflecting contributions from star-forming regions with high radiation field intensities. This is reinforced by the near-linear scaling between F2100W and Pa-alpha. PAH-dominated bands do not show this linear trend with Pa-alpha, likely due to their destruction in ionized regions. F1000W behaves similarly to PAH bands in its correlations with CO(1-0) and Pa-alpha. Modeling mid-infrared emission with an empirical decomposition into gas- and star-formation-associated components shows that PAH-dominated filters receive comparable contributions from both, while the relative contribution associated with the Pa-alpha template increases toward longer wavelengths, reaching $\sim$75% in F2100W. These results demonstrate that mid-infrared simultaneously traces the gas column and star formation, but with a systematic wavelength-dependent shift in what drives the correlations: PAHs being more gas-tracing and dust-continuum reflecting star formation. Lastly, considering both HI and H$_2$ at 440 pc resolution, we find a tight, linear relation between $Σ_{HI+H_2}$ and PAH-dominated filters. Although most of our coverage is in H$_2$-dominated regions, we note similar observations with HI, suggesting that PAHs are also well-mixed with atomic gas.

### [B] 62.2 — The THESAN-ZOOM project: clumpiness of high-redshift galaxies and its connection to bursty star formation
- **arXiv:** [2608.19308](https://arxiv.org/abs/2608.19308)
- **Primary:** astro-ph.GA
- **SPECTER2:** `massive_star_formation` 0.7502 vs `galaxy_evolution_agn` 0.7328 (margin +0.0174)
- **Domain evidence:** 6.75 — `rescued by direct ISM/star-formation title evidence`
- **NLI:** pos 0.043 / neg 0.013 / margin +0.030
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** Recent JWST observations have revealed diverse high-redshift galaxy morphologies, including a population with irregular and clumpy structures. The physical origin of these structures, and the extent to which observational biases shape their appearance, remain uncertain. We present a power-spectrum-based method for quantifying galaxy clumpiness across spatial scales, using the radiation-hydrodynamic simulation suite THESAN-ZOOM, which employs a state-of-the-art galaxy formation model that resolves the multiphase interstellar medium (ISM). Although the total stellar mass distributions in THESAN-ZOOM galaxies are usually smooth, clumpy structures appear in the H$α$, far-ultraviolet (FUV), and optical light distributions. Tracers sensitive to shorter-timescale star formation exhibit more pronounced small-scale structure ($\sim10^{2}$--$10^{3}{\rm pc}$). The corresponding projected light spectra follow $P(k)\propto k^{-1}$ to $k^{-2}$, with progressively shallower slopes for tracers sensitive to more recent star formation, reflecting enhanced small-scale power and greater spatial intermittency in young stellar populations. This behaviour is consistent with a highly compressible, shock-dominated ISM in which stellar feedback and outflows reorganise dense gas into filamentary and clumpy structures. We also find that galaxy clumpiness depends on the treatment of stellar feedback. Weaker early stellar feedback enhances small-scale power in both the mass and light distributions. Clumpiness also varies strongly over the bursty star formation cycle, implying that observed samples may be biased towards galaxies caught in phases of elevated star formation. Galaxy clumpiness, therefore, could provide a complementary probe of the bursty star formation in the early Universe.

### [B] 59.8 — Diverse ionized gas conditions in a dynamically hot, interacting galaxy at $z = 9.31$ revealed by JWST/NIRSpec IFU
- **arXiv:** [2608.16996](https://arxiv.org/abs/2608.16996)
- **Primary:** astro-ph.GA
- **SPECTER2:** `astrochemistry` 0.7572 vs `planetary_disks_exoplanets` 0.7538 (margin +0.0033)
- **Domain evidence:** 6.5 — `contrastive`
- **NLI:** pos 0.029 / neg 0.023 / margin +0.007
- **Decision:** B → B — NLI consistent or protected by direct object evidence
- **Abstract:** We present a spatially and spectrally resolved study of an interacting galaxy, Gz9p3 at $z=9.31$, using the James Webb Space Telescope NIRSpec/G395H IFU observation with high-spectral resolution ($R\approx 2700$) mode. Gz9p3 consists of two sub-regions (`core' and `tail'), which show stark contrast in their physical properties. The HII regions in the core are characterized by high electron density ($n_{e}\gtrsim2900$ cm$^{-3}$), low gas-phase metallicity ($0.25$ dex below the mass-metallicity relation), and yet relatively low specific star formation rate (sSFR) among the system. On the other hand, the tail exhibits low electron density ($n_{e}<70$ cm$^{-3}$), relatively high gas-phase metallicity that is consistent with the mass-metallicity relation, and high sSFR. The integrated spectrum thus shows the properties inbetween these two regions. No evidence of ordered rotation in ionized gas is found, suggesting that Gz9p3 is a dynamically hot system. Finally, we find ionized gas outflows characterized by the secondary [OIII]5007 line component throughout most of the system. The outflow velocity is below the escape velocity, making Gz9p3 one of the first galactic systems experiencing a galactic fountain. Overall, our findings indicate that this system is in a phase in which the pristine gas is falling efficiently into the core, diluting the gas metallicity, and enhancing star formation and outflows after the galaxy interaction.

## NLI downgraded

- **B → C** — Automated Assignment and Prediction of Molecules in Astronomical Line Surveys Using Machine-Learning-Based Chemical Embeddings — NLI 0.002/0.001 — [2608.18221](https://arxiv.org/abs/2608.18221)
- **B → C** — Infrared Spectroscopy of Cyanonaphthalenes under Interstellar Relevant Conditions and Their Potential Connection with Astronomical Aromatic Infrared Bands — NLI 0.103/0.036 — [2608.14964](https://arxiv.org/abs/2608.14964)
- **B → C** — The Nearby Star Formation and Supernova Histories Reconstructed from Young Star Clusters — NLI 0.078/0.029 — [2608.20307](https://arxiv.org/abs/2608.20307)
- **B → C** — High-spectral-resolution Observations of the [S II] Emission-line Doublet in the Filamentary Nebula Surrounding NGC 1275 — NLI 0.005/0.004 — [2608.14888](https://arxiv.org/abs/2608.14888)
- **B → C** — Chromospheric heating and magnetic topology above the shared penumbra of a delta-spot: Multi-line inversions and multi-height magnetic-field extrapolations — NLI 0.021/0.017 — [2608.19983](https://arxiv.org/abs/2608.19983)
- **B → C** — The CMZ Asymmetries: Feeding or Feedback? — NLI 0.005/0.001 — [2608.13734](https://arxiv.org/abs/2608.13734)
- **B → C** — Aromatics and Aliphatics in Local Star-Forming Galaxies as Probed by AKARI — NLI 0.022/0.008 — [2608.14989](https://arxiv.org/abs/2608.14989)
- **B → C** — Beyond Idealized PAHs: Infrared Signatures of Carbon-Chain Defects from Shock Synthesis — NLI 0.118/0.030 — [2608.18505](https://arxiv.org/abs/2608.18505)
- **B → C** — OH Line Detections in Southern Galaxies of the IRAS Revised Bright Galaxy Sample — NLI 0.048/0.045 — [2608.14473](https://arxiv.org/abs/2608.14473)
- **B → C** — The segmented spiral structure of the Solar neighbourhood traced by young clustered populations — NLI 0.007/0.004 — [2608.17887](https://arxiv.org/abs/2608.17887)
- **B → C** — Catalytic formation of H_2 on carbonaceous dust grains - implications for interstellar observations — NLI 0.029/0.011 — [2608.16149](https://arxiv.org/abs/2608.16149)
- **B → C** — Two domains of extended Lyman-alpha emission around galaxies: from local radiation to environmental regulation — NLI 0.012/0.001 — [2608.16665](https://arxiv.org/abs/2608.16665)
- **B → C** — Differential Reddening and Extinction Law Analyses of Galactic Open Clusters — NLI 0.007/0.004 — [2608.13313](https://arxiv.org/abs/2608.13313)
- **B → C** — Diffuse Dwarf Galaxies in Galaxy Clusters: I. Stellar Populations and Radial Gradients — NLI 0.000/0.000 — [2608.17375](https://arxiv.org/abs/2608.17375)
- **B → C** — Radio Properties of RS Canum Venaticorum Variables in VLASS and RACS — NLI 0.002/0.002 — [2608.13653](https://arxiv.org/abs/2608.13653)
- **B → C** — Local Interstellar Flow Parameters from the First Intersection of IMAP-Lo's Parameter Tubes — NLI 0.001/0.001 — [2608.14939](https://arxiv.org/abs/2608.14939)
- **B → C** — Measuring Simulated Circumgalactic Medium Turbulence with Emission-Weighted Projected Velocity Structure Functions in FOGGIE — NLI 0.048/0.013 — [2608.17013](https://arxiv.org/abs/2608.17013)
- **B → C** — The Low-Mass Baryon Cycle in QUEST Dwarf Galaxies I: Sample definition and first results — NLI 0.020/0.035 — [2608.15782](https://arxiv.org/abs/2608.15782)
- **B → C** — Radio Properties of Narrow-Line and Broad-Line Seyfert 1 Galaxies — NLI 0.003/0.002 — [2608.13303](https://arxiv.org/abs/2608.13303)

## NLI promoted / rescued

- None

## NLI uncertain boundary cases

- **[A] ALOHA IRDCs Molecular Line Follow-up: I. Gas properties and kinematics** — margin +0.006, domain 14.0 — [2608.20238](https://arxiv.org/abs/2608.20238)
- **[A] Impact of Upstream Clumpiness on Supernova Remnant Forward Shock Evolution in Molecular Cloud Environments** — margin +0.002, domain 4.5 — [2608.17477](https://arxiv.org/abs/2608.17477)
- **[A] Star Formation in the H II Region Sh 2-205: 3D Morphology and Kinematics from Young Stars and Molecular Gas** — margin +0.005, domain 12.25 — [2608.16179](https://arxiv.org/abs/2608.16179)
- **[B] The efficient star-forming regions of stripped-envelope supernovae** — margin +0.004, domain 18.75 — [2608.18897](https://arxiv.org/abs/2608.18897)
- **[B] Diffuse HI emission in the circumgalactic medium of NGC891 and NGC4565 - III: azimuthal profiles** — margin +0.004, domain 4.5 — [2608.19186](https://arxiv.org/abs/2608.19186)
- **[B] Multiphase turbulence as the origin of OH+, H2O+ and H3+ column density scatter in the local ISM** — margin +0.011, domain 7.5 — [2608.15633](https://arxiv.org/abs/2608.15633)
- **[B] The Galactic Centre G+0.633-0.0604 Molecular Cloud: A New Gold Mine for Astrochemistry** — margin +0.014, domain 7.0 — [2608.14381](https://arxiv.org/abs/2608.14381)
- **[B] JWST Whirlpool Galaxy Treasury: Mid-Infrared Emission in M51 and its Relation to Gas Column and Star Formation** — margin +0.010, domain 7.25 — [2608.16802](https://arxiv.org/abs/2608.16802)
- **[B] The THESAN-ZOOM project: clumpiness of high-redshift galaxies and its connection to bursty star formation** — margin +0.030, domain 6.75 — [2608.19308](https://arxiv.org/abs/2608.19308)
- **[B] Diverse ionized gas conditions in a dynamically hot, interacting galaxy at $z = 9.31$ revealed by JWST/NIRSpec IFU** — margin +0.007, domain 6.5 — [2608.16996](https://arxiv.org/abs/2608.16996)
- **[C] Automated Assignment and Prediction of Molecules in Astronomical Line Surveys Using Machine-Learning-Based Chemical Embeddings** — margin +0.001, domain 5.5 — [2608.18221](https://arxiv.org/abs/2608.18221)
- **[C] Infrared Spectroscopy of Cyanonaphthalenes under Interstellar Relevant Conditions and Their Potential Connection with Astronomical Aromatic Infrared Bands** — margin +0.066, domain 2.5 — [2608.14964](https://arxiv.org/abs/2608.14964)
- **[C] The Nearby Star Formation and Supernova Histories Reconstructed from Young Star Clusters** — margin +0.048, domain 4.75 — [2608.20307](https://arxiv.org/abs/2608.20307)
- **[C] High Velocity Neutral Gas in the Fermi Bubbles: New Kinematic Limits and Spatial Structure** — margin +0.002, domain 1.0 — [2608.16754](https://arxiv.org/abs/2608.16754)
- **[C] High-spectral-resolution Observations of the [S II] Emission-line Doublet in the Filamentary Nebula Surrounding NGC 1275** — margin +0.001, domain 0.0 — [2608.14888](https://arxiv.org/abs/2608.14888)
- **[C] Chromospheric heating and magnetic topology above the shared penumbra of a delta-spot: Multi-line inversions and multi-height magnetic-field extrapolations** — margin +0.004, domain 0.0 — [2608.19983](https://arxiv.org/abs/2608.19983)
- **[C] The CMZ Asymmetries: Feeding or Feedback?** — margin +0.004, domain 2.5 — [2608.13734](https://arxiv.org/abs/2608.13734)
- **[C] Aromatics and Aliphatics in Local Star-Forming Galaxies as Probed by AKARI** — margin +0.014, domain 1.5 — [2608.14989](https://arxiv.org/abs/2608.14989)
- **[C] OH Line Detections in Southern Galaxies of the IRAS Revised Bright Galaxy Sample** — margin +0.002, domain 4.0 — [2608.14473](https://arxiv.org/abs/2608.14473)
- **[C] The segmented spiral structure of the Solar neighbourhood traced by young clustered populations** — margin +0.002, domain 4.0 — [2608.17887](https://arxiv.org/abs/2608.17887)
- **[C] Catalytic formation of H_2 on carbonaceous dust grains - implications for interstellar observations** — margin +0.019, domain 2.5 — [2608.16149](https://arxiv.org/abs/2608.16149)
- **[C] Two domains of extended Lyman-alpha emission around galaxies: from local radiation to environmental regulation** — margin +0.011, domain 1.5 — [2608.16665](https://arxiv.org/abs/2608.16665)
- **[C] Theoretical emission lines and metallicity calibrations of H II regions in ASTRID simulation** — margin +0.001, domain 5.75 — [2608.15572](https://arxiv.org/abs/2608.15572)
- **[C] Differential Reddening and Extinction Law Analyses of Galactic Open Clusters** — margin +0.003, domain 3.5 — [2608.13313](https://arxiv.org/abs/2608.13313)
- **[C] RIOJA. Environmental Effects on Stellar Populations and Ionized Gas in a Protocluster at $z=7.88$** — margin +0.005, domain 3.0 — [2608.16343](https://arxiv.org/abs/2608.16343)
- **[C] Diffuse Dwarf Galaxies in Galaxy Clusters: I. Stellar Populations and Radial Gradients** — margin +0.000, domain 1.5 — [2608.17375](https://arxiv.org/abs/2608.17375)
- **[C] Radio Properties of RS Canum Venaticorum Variables in VLASS and RACS** — margin +0.001, domain 0.0 — [2608.13653](https://arxiv.org/abs/2608.13653)
- **[C] Local Interstellar Flow Parameters from the First Intersection of IMAP-Lo's Parameter Tubes** — margin -0.000, domain 2.5 — [2608.14939](https://arxiv.org/abs/2608.14939)
- **[C] Abundant Heavy Black Hole Seeds from Moderate Lyman-Werner Radiation** — margin +0.002, domain 3.5 — [2608.13656](https://arxiv.org/abs/2608.13656)
- **[C] Measuring Simulated Circumgalactic Medium Turbulence with Emission-Weighted Projected Velocity Structure Functions in FOGGIE** — margin +0.035, domain 0.0 — [2608.17013](https://arxiv.org/abs/2608.17013)
- **[C] A comprehensive cluster census of Orion. An application of the Significance Mode Analysis (SigMA) algorithm** — margin +0.004, domain 6.0 — [2608.16989](https://arxiv.org/abs/2608.16989)
- **[C] An ALMA view of the Jet-Arc CO clouds toward the TeV $γ$-ray source HESS J1023-575 and Westerlund 2; Evidence for the footprints of microquasar jets, the very powerful cosmic-ray accelerator in the Galactic disk** — margin +0.035, domain 3.0 — [2608.14988](https://arxiv.org/abs/2608.14988)
- **[C] The Low-Mass Baryon Cycle in QUEST Dwarf Galaxies I: Sample definition and first results** — margin -0.014, domain 2.5 — [2608.15782](https://arxiv.org/abs/2608.15782)
- **[C] High-Redshift Type Ia Supernovae Exhibit Enhanced Calcium Abundances** — margin +0.002, domain 0.0 — [2608.18342](https://arxiv.org/abs/2608.18342)
- **[C] How mergers shape galaxy morphology in the IllustrisTNG simulation** — margin +0.001, domain 1.5 — [2608.13996](https://arxiv.org/abs/2608.13996)
- **[C] Radio Properties of Narrow-Line and Broad-Line Seyfert 1 Galaxies** — margin +0.001, domain 1.5 — [2608.13303](https://arxiv.org/abs/2608.13303)
- **[C] Numerical Model Simulation of the Carruthers GCI Images** — margin +0.012, domain 0.0 — [2608.13516](https://arxiv.org/abs/2608.13516)
- **[C] The Stellar Population of NGC 346 in the Small Magellanic Cloud with JWST** — margin +0.010, domain 8.0 — [2608.17875](https://arxiv.org/abs/2608.17875)
- **[C] Energy Partitioning in Dust-catalyzed $\mathrm{H_2}$ and HD Formation Revealed by Molecular Simulations Considering Nuclear Quantum Effects** — margin +0.023, domain 2.5 — [2608.13843](https://arxiv.org/abs/2608.13843)
- **[C] How X-rays heat the IGM in different 21-cm simulation codes: a comparison between Licorice and Beorn** — margin +0.001, domain 3.0 — [2608.14423](https://arxiv.org/abs/2608.14423)
- **[C] Enhancing the performance and capabilities of the MIRI instrument on JWST** — margin -0.000, domain 0.0 — [2608.13873](https://arxiv.org/abs/2608.13873)
- **[C] The reddening of NGC 7469 and evidence for variable extinction** — margin +0.001, domain 0.0 — [2608.15663](https://arxiv.org/abs/2608.15663)
- **[C] Widefield Arecibo Virgo Extragalactic Survey: II. Characterizing the HI properties and environment of the WAVES South region** — margin +0.010, domain 3.0 — [2608.13411](https://arxiv.org/abs/2608.13411)
- **[C] Gal3D: Superellipsoid Modeling of Radial 3D Galaxy Structure in IllustrisTNG and EAGLE Simulations** — margin +0.045, domain 0.0 — [2608.12933](https://arxiv.org/abs/2608.12933)
- **[C] Cosmic Ray Diffusion and the Origin of Very High Energy Gamma-Ray Emission in Young Massive Stellar Clusters** — margin +0.006, domain 0.0 — [2608.14547](https://arxiv.org/abs/2608.14547)
- **[C] Old Disks Die Hard: How Does AGN Feedback Suppress Disk Formation in Milky Way Mass Galaxies?** — margin +0.009, domain 1.5 — [2608.13718](https://arxiv.org/abs/2608.13718)
- **[C] Coronal gas excitation as a tracer of supermassive black hole mass: on the mid-IR coronal [Ne v] lines** — margin -0.001, domain 0.0 — [2608.16304](https://arxiv.org/abs/2608.16304)
- **[C] A JWST/MIRI Study of Dust in a Sample of Normal Type IIP Core Collapse Supernovae** — margin +0.001, domain 0.0 — [2608.16979](https://arxiv.org/abs/2608.16979)
- **[C] Forecast for the detectability of patchy hydrogen reionization in WEAVE-QSO measurements of the Lyman-$α$ forest power spectrum at redshift $z \geq 4$** — margin +0.003, domain 0.0 — [2608.13153](https://arxiv.org/abs/2608.13153)
- **[C] Nonlinear velocity power spectrum: modeling the cosmological dependence on the Hubble constant and cold dark matter density** — margin -0.000, domain 0.0 — [2608.16489](https://arxiv.org/abs/2608.16489)
- **[C] Evidence for Dynamical Filtering: High Binary Fraction, Hard-binary Excess, and Unresolved Triples in the Surviving Core of NGC 6791** — margin +0.028, domain 0.0 — [2608.13955](https://arxiv.org/abs/2608.13955)
- **[C] Orbital Migration of Interacting Stellar Mass Black Holes in Disks around Supermassive Black Holes. III. Mass Distribution of Hierarchical Mergers** — margin +0.004, domain 0.0 — [2608.13641](https://arxiv.org/abs/2608.13641)
- **[C] Optical Spectroscopy of TeV-emitting BL Lac Candidates** — margin -0.000, domain 0.0 — [2608.14412](https://arxiv.org/abs/2608.14412)
- **[C] Improved Cosmological Constraints from Morphology-Based Marked Correlation Functions** — margin -0.000, domain 0.0 — [2608.15083](https://arxiv.org/abs/2608.15083)
- **[C] Accretion of AGN Stars under Influence of Disk Geometry II: The Adiabatic Regime and Runaway Collapse Induced by Self-gravity** — margin +0.012, domain 0.0 — [2608.18249](https://arxiv.org/abs/2608.18249)
- **[C] A Radio-Bright Local Little Red Dot Analog** — margin -0.007, domain 0.0 — [2608.16200](https://arxiv.org/abs/2608.16200)
- **[C] The H$α$ specific angular momentum of dwarf galaxies** — margin +0.001, domain 0.0 — [2608.16089](https://arxiv.org/abs/2608.16089)
- **[SKIP] Physics of Circular Polarized Ion-Scale Waves in Hybrid Simulations of Alfvénic Fluctuations** — margin -0.006, domain 0.0 — [2608.14151](https://arxiv.org/abs/2608.14151)
- **[SKIP] Outflows in steep density gradients: diversity of behavior and implications for tidal disruption events and luminous fast blue optical transients** — margin +0.028, domain 0.0 — [2608.19512](https://arxiv.org/abs/2608.19512)
- **[SKIP] The deepest color-magnitude diagrams for the benchmark open cluster NGC 2437 from Gaia and VVVX** — margin +0.004, domain 1.0 — [2608.14514](https://arxiv.org/abs/2608.14514)
- **[SKIP] Cosmography with DESI-DR1 Cosmic Chronometers: Direct H(z) measurements from Luminous Red Galaxy ages** — margin +0.000, domain 0.0 — [2608.13178](https://arxiv.org/abs/2608.13178)
- **[SKIP] $\texttt{Aether.jl}$ : A High-Performance 3D MHD and Multifluid Dust Code Written in a Dynamic Language with an Interactive Human-AI Development Framework** — margin +0.001, domain 0.0 — [2608.14048](https://arxiv.org/abs/2608.14048)
- **[SKIP] Evolution of lunar wake potentials: structure, energy conversion, and their imprints on velocity distributions** — margin +0.003, domain 0.0 — [2608.18383](https://arxiv.org/abs/2608.18383)
- **[SKIP] A self-consistent solar coronal heating model by Alfvenic waves** — margin +0.000, domain 0.0 — [2608.15221](https://arxiv.org/abs/2608.15221)
- **[SKIP] Revised $^{45}$V($p,γ$)$^{46}$Cr reaction rate and its impact on the production of $^{44}$Ti in core-collapse supernovae** — margin +0.007, domain 0.0 — [2608.17757](https://arxiv.org/abs/2608.17757)
- **[SKIP] The X-Ray Continuum Emission Region in the Lensed Quasar SDSS J133907.23+131038.6 is Much Smaller than the Accretion Disk** — margin +0.002, domain 0.0 — [2608.17041](https://arxiv.org/abs/2608.17041)
- **[SKIP] Interpretations of the $10\%$ polarization observed in the early forward-shock afterglow of GRB 091208** — margin -0.007, domain 0.0 — [2608.15494](https://arxiv.org/abs/2608.15494)
- **[SKIP] Accurately simulating gain and clock-induced charge production in the EMCCD gain register** — margin +0.001, domain 0.0 — [2608.17842](https://arxiv.org/abs/2608.17842)
- **[SKIP] X-ray thread/Nonthermal Radio Filament associations: Evidence for Interstellar Magnetic Reconnection** — margin +0.009, domain 1.0 — [2608.14830](https://arxiv.org/abs/2608.14830)
- **[SKIP] Kinematics and Dynamics of the Open Cluster NGC 2302** — margin -0.038, domain 0.0 — [2608.18550](https://arxiv.org/abs/2608.18550)
- **[SKIP] No Evidence for Nearby Circumstellar Material in the Type Ia Supernova 2025rbs** — margin +0.028, domain 0.0 — [2608.13655](https://arxiv.org/abs/2608.13655)
- **[SKIP] Multi-zone Modeling of Blazar Jets: Constraints from GeV-Optical Correlation and Short-Timescale Variability** — margin +0.001, domain 0.0 — [2608.18707](https://arxiv.org/abs/2608.18707)
- **[SKIP] Correlations with Magnetic Activity in the Solar Near-Surface Shear Layer. I. Rotation** — margin +0.007, domain 0.0 — [2608.19438](https://arxiv.org/abs/2608.19438)
- **[SKIP] Asteroseismic analysis of red giants in eclipsing binaries using two methods: implications for scaling relations and chemical composition** — margin +0.001, domain 0.0 — [2608.18250](https://arxiv.org/abs/2608.18250)
- **[SKIP] Sr and Ba yields of the First Generation(s) of stars: Constraints from metal-poor stars** — margin +0.011, domain 0.0 — [2608.17001](https://arxiv.org/abs/2608.17001)
- **[SKIP] Broadband emission of microquasar remnants** — margin +0.035, domain 0.0 — [2608.17000](https://arxiv.org/abs/2608.17000)
- **[SKIP] Non-ideal MHD and protostellar feedback effects on disc formation and evolution in numerical simulations of star cluster formation** — margin +0.007, domain 7.5 — [2608.19518](https://arxiv.org/abs/2608.19518)
- **[SKIP] A stochastic forward model for the intergalactic dispersion-measure distribution of Fast Radio Bursts** — margin +0.001, domain 0.0 — [2608.17658](https://arxiv.org/abs/2608.17658)
- **[SKIP] The initial evolution of SN 2011dh: The importance of inhomogeneities** — margin +0.000, domain 0.0 — [2608.17736](https://arxiv.org/abs/2608.17736)
- **[SKIP] The SAMI Galaxy Survey: Linking Tidal Features and Orbit Populations Using Schwarzschild Modelling** — margin +0.008, domain 0.0 — [2608.14012](https://arxiv.org/abs/2608.14012)
