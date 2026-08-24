# ISM Literature Recommender v2 — Experiment

Generated: 2026-08-22T13:25:01Z
Lookback: last 10 days

## Candidate summary

- All recent astro-ph candidates: **503**
- Current production keyword baseline selected: **68**
- Hybrid Priority A: **59**
- Hybrid Priority B: **230**
- Hybrid Priority C: **160**

## Scoring design

- **Current baseline**: exact reproduction of the production `GA/SR + keyword include/exclude` logic.
- **BM25**: independent lexical ranking against each group-topic description.
- **Hybrid**: 80% SPECTER2 semantic similarity + 20% exact specialist-term signal.
- Topic scores are relative ranking scores within this experiment, not calibrated probabilities.

## Group topics

- **atomic_ism** — Cold and warm atomic interstellar gas in the Milky Way and nearby star-forming environments, including H I 21 cm emission and absorption, HISA, HINSA, CNM and WNM, and the atomic-to-molecular transition.
- **molecular_clouds** — Molecular clouds and molecular gas: cloud formation, structure, evolution, kinematics, CO and other molecular-line observations, dense gas, filaments, clumps, and cores.
- **star_formation** — Star formation from cloud to core and young stellar object, including gravitational collapse, protostars, protostellar envelopes, accretion, clusters, and the interaction between young stars and their natal clouds.
- **feedback_bubbles** — Stellar feedback in the interstellar medium, including H II regions, ionized bubbles and cavities, shells, stellar winds, supernova feedback, expanding structures, triggered star formation, and interactions with molecular clouds.
- **turbulence** — Turbulence and gas dynamics in the interstellar medium and molecular clouds, including velocity statistics, power spectra, structure functions, linewidths, density and column-density PDFs, and turbulent driving.
- **magnetic_fields** — Magnetic fields in the interstellar medium and star-forming clouds, including polarization, Zeeman measurements, MHD, magnetic support, field morphology, and the role of magnetic fields in cloud and core evolution.
- **astrochemistry** — Astrochemistry and molecular tracers in interstellar and star-forming gas, including chemical evolution, abundances, deuteration, ionization, cosmic-ray chemistry, and diagnostic molecular species.
- **massive_star_formation** — Massive star and cluster formation in dense molecular environments, including infrared dark clouds, massive clumps, high-mass protostars, hot cores, massive young stellar objects, and clustered star formation.
- **galactic_ism_surveys** — Galactic interstellar medium on large scales, including Milky Way gas and dust surveys, Galactic structure, H I and molecular-line surveys, three-dimensional dust and gas mapping, and new observational datasets useful for ISM science.
- **ism_methods_data** — Observational, statistical, computational, and radiative-transfer methods directly applicable to interstellar-medium and star-formation research, including spectral decomposition, tomography, map reconstruction, line analysis, and new surveys or instruments.

## Highest-ranked hybrid candidates

### [A] 96.2 — Complex morphology and kinematics at the heart of the very low luminosity object IRAM 04191+1522
- **arXiv:** [2608.17593](https://arxiv.org/abs/2608.17593)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** molecular_clouds (96.2), star_formation (79.7), astrochemistry (69.1)
- **Current keyword baseline:** YES
- **BM25 max:** 100.0
- **Semantic max:** 100.0
- **Abstract:** The formation of the majority of brown dwarfs (BDs) remains uncertain. They may form in molecular cloud cores in a process akin to low mass star formation, or via fragmentation in circumstellar discs. Studying the youngest, most embedded sources is crucial for distinguishing these scenarios. We investigate molecular gas morphology and kinematics around one young & embedded very low luminosity object (VeLLO), IRAM 04191+1522, utilising archival ALMA observations of 13CO, C18O, and SO. We trace gas on scales of a few 10s to 100s of au around the source to search for outflowing and/or infalling structures. The red and blueshifted 13CO (3-2) emission show distinct morphologies and kinematics. The blueshifted emission to the north-west may trace shocked material oriented differently from the previously reported approx. 0.1 pc CO outflow. Redshifted emission mainly to the south-east and south-west may trace the base of an outflow cavity. The position angle of this cavity suggests the presence of a second outflow, which supports the possible binary nature of this VeLLO. The C18O (2-1) emission is highly complex, comprising structures at different spatial scales and distances from the source. These may trace a mix of molecular outflow, outflow cavity, and disc emission. SO 65-54 reveals evidence for anticlockwise rotation around the central source, together with a northern structure of uncertain origin. We have identified a complex set of 13CO (3-2) and C18O (2-1) structures alongside evidence of a new outflow cavity at a distinct position angle from previously detected outflows. This supports the scenario that IRAM 04191+1522 is a binary system. The northern SO gas structure remains unexplained. Higher spectral resolution observations at intermediate scales are needed to characterise these substructures, their connection to larger scale structures, and to determine this system's final fate.

### [A] 89.7 — CHANG-ES XL: Magnetic Field Structures in the Disk and Halo of NGC 891
- **arXiv:** [2608.12275](https://arxiv.org/abs/2608.12275)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** magnetic_fields (89.7), feedback_bubbles (66.5), galactic_ism_surveys (64.5)
- **Current keyword baseline:** NO
- **BM25 max:** 70.4
- **Semantic max:** 100.0
- **Abstract:** We present new Karl G. Jansky Very Large Array S-band (2-4 GHz) observations of the edge-on spiral galaxy NGC 891, complemented by C-band data, to investigate the structure of its radio continuum halo. Using rotation measure synthesis we detected an extended polarized halo, with most spatially extended polarized emission confined to Faraday depths within +/- 150 rad m-2. We identified a localized region in the north-east side of the galaxy that shows an enhancement in polarized intensity (not in percentage polarization). By combining the radio data with H-alpha and diffuse X-ray maps, we discuss a possible origin for this structure: a superbubble powered by clustered supernovae. Across the disk and halo, the percentage polarization decreases toward the midplane but shows a mild wavelength dependence, despite the edge-on orientation of NGC 891. This behavior implies that the depolarization cannot be dominated by small-scale Faraday rotation within the disk. Instead, it is possible that most of the observed polarized emission arises on the Earth-facing side of the galaxy. Our peak rotation measure (RM) map shows a smooth transition along the major axis, consistent with a large scale axisymmetric magnetic field. Using H-alpha and UV data, we analyzed the distribution of H II regions and found that they are parts of different spiral arms. We also identified a faint, isolated H II region at a galactocentric radius of 16.9 kpc, with both H-alpha and far-UV counterparts, indicating star formation outside the thin disk.

### [A] 88.5 — Theoretical emission lines and metallicity calibrations of H II regions in ASTRID simulation
- **arXiv:** [2608.15572](https://arxiv.org/abs/2608.15572)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (88.5), astrochemistry (86.2), galactic_ism_surveys (72.4)
- **Current keyword baseline:** NO
- **BM25 max:** 96.7
- **Semantic max:** 98.5
- **Abstract:** We present a theoretical framework to derive redshift-dependent metallicity calibrations for galaxies at $z$=2-7. The ionization parameter ($U$) and gas pressure ($P$) in our approach are not assumed, but are predicted self-consistently. By combining the ASTRID cosmological simulation with stellar population synthesis (SPS) and MAPPINGS V photoionization modeling, we evolve young star clusters under an analytic wind-driven bubble model. This directly couples stellar feedback to the local ISM density, allowing \hii{} region properties to emerge from the underlying physics rather than being treated as free parameters. The emission-line predictions are validated against observed star-formation rate indicators (deviation <0.05 dex) and the \oiii{} luminosity function. We derive calibrations for common optical (e.g. R23, O3N2, N2, O32) and UV (e.g. C3O3, N3O3) diagnostics. We find significant redshift evolution in these relations, driven primarily by changing ionization conditions. A Bayesian analysis quantifies calibration performance under varying signal-to-noise, enabling diagnostic recommendations as a function of redshift and data quality. The R23 calibration performs well at all redshifts with minimal error in our model, while nitrogen- and carbon-based calibrations are highly sensitive to the abundance enrichment process and should be used with caution. These results provide a practical framework for interpreting JWST spectroscopy and tracing chemical evolution from cosmic noon to the epoch of reionization.

### [A] 87.3 — Differential Reddening and Extinction Law Analyses of Galactic Open Clusters
- **arXiv:** [2608.13313](https://arxiv.org/abs/2608.13313)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** galactic_ism_surveys (87.3), astrochemistry (69.3), massive_star_formation (68.8)
- **Current keyword baseline:** NO
- **BM25 max:** 76.2
- **Semantic max:** 96.9
- **Abstract:** Extinction significantly affects open cluster parameters and their use in studies of Galactic structure, yet homogeneous large sample measurements of open cluster extinction properties remain limited. Using Gaia-era open cluster member samples combined with multi-band photometry and stellar parameters, we derive color excesses of member stars and provide the homogeneous characterization of the mean reddening, differential reddening, and color excess ratio (CER) at the cluster scale. Differential reddening increases systematically with mean reddening, with highly reddened clusters near the Galactic plane showing stronger extinction variations. Star-by-star reddening corrections narrow color--magnitude diagram (CMD) sequences in 369 of 435 clusters (85%) with reliable CMD-width measurements, and cluster color excess maps reveal small-scale extinction structures. The median CER is compatible with the standard diffuse interstellar medium extinction curve, while the broad CER distribution and its large-scale variations across the Galactic disk likely reflect differences in the dominant dust environments sampled along different Galactic sight lines.

### [A] 85.8 — The Nearby Star Formation and Supernova Histories Reconstructed from Young Star Clusters
- **arXiv:** [2608.20307](https://arxiv.org/abs/2608.20307)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (85.8), feedback_bubbles (68.2), galactic_ism_surveys (63.8)
- **Current keyword baseline:** YES
- **BM25 max:** 96.7
- **Semantic max:** 95.1
- **Abstract:** We reconstruct the recent star formation and core-collapse supernova (ccSN) histories of the Solar Neighborhood from the past trajectories of young star clusters. Using a \textit{Gaia}-based cluster sample with newly derived ages, masses, and bulk 3D velocities, we integrate orbits backward in an assumed axisymmetric Galactic potential and combine the trajectories with IMF sampling and stellar lifetimes to infer ccSN times and locations over the past 50 Myr. The result is an all-sky, 3D, time-resolved map of nearby ccSN activity for comparison with high-resolution 3D views of the local interstellar medium. The 0--15 Myr map shows strong enhancements toward Orion, Vela, Sco--Cen, and Cepheus, many within present-day cavities and shells. At earlier times, the dominant enhancements trace the Collinder 135, Messier 6, and Alpha Persei cluster families, showing how the remnants of massive star-forming complexes have shaped the recent local feedback history. We recover a bursty star formation history followed by a delayed, smoother ccSN history. Over the last 40 Myr, the mean star formation and ccSN rates are \(823~M_\odot~\mathrm{Myr}^{-1}\) and \(7.7~\mathrm{Myr}^{-1}\), respectively, corresponding to a Milky Way rate of \(0.55\pm0.03~\mathrm{century}^{-1}\). Present-day OB-star catalogs yield rates ranging from agreement with the cluster reconstruction to several times higher. Because the catalogs overlap weakly and require different corrections, we do not rescale the ccSN map. Our reconstruction provides an empirical framework for connecting the recent history of massive-star feedback to the 3D structure and life cycle of gas in the nearby Milky Way.

### [A] 85.7 — ALOHA IRDCs Molecular Line Follow-up: I. Gas properties and kinematics
- **arXiv:** [2608.20238](https://arxiv.org/abs/2608.20238)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** massive_star_formation (85.7), astrochemistry (84.1), molecular_clouds (80.8)
- **Current keyword baseline:** YES
- **BM25 max:** 100.0
- **Semantic max:** 100.0
- **Abstract:** Infrared Dark Clouds are ideal sites for investigating the initial conditions of massive star and cluster formation. The A Lei Of the Habitat and Assembly of Infrared Dark Clouds (ALOHA IRDCs), a James Clerk Maxwell Telescope (JCMT) Large Program, has mapped nearby IRDCs with SCUBA-2. Complementary molecular line observations are needed to characterise the physical, kinematic, and chemical properties of the dense gas. We aim to determine the thermal, kinematic, and chemical properties of clumps identified in the ALOHA IRDCs, and to assess their evolutionary status and level of star-forming activity. We performed single-pointing K-band and W-band observations towards 56 ALOHA IRDCs clumps using the Effelsberg 100-m and Yebes 40-m telescopes, respectively. We derived NH3 kinetic temperatures using the hyperfine group ratio (HFGR) method and identified infall and shock signatures from HCO+, H13CO+, SiO, and HNCO profiles. Water masers and NH2D emission were used as complementary tracers of chemical evolution and star formation. The clumps exhibit kinetic temperatures of 15-29 K. We detect NH2D emission towards 18 sources, with NH2D centroid velocities consistent with NH3, indicating both species trace the same dense gas component. More than half of the clumps display blue-asymmetric HCO+ profiles, identifying them as infall candidates. Water masers are detected in 22 sources, with prominent velocity ranges and variability. Broad SiO emission (>~20 km/s) indicates strong shocks, while narrower extents (<~6km/s) likely trace large-scale interactions or low-velocity shocks. The widespread infall signatures, shock tracers, masers, and NH2D emission suggest that relatively quiescent, chemically young material can coexist with dynamically active gas affected by early protostellar feedback, providing insight into the coupled physical and chemical evolution of massive IRDC clumps.

### [A] 85.7 — Wide field Slitless Spectroscopy with JWST's MIRI
- **arXiv:** [2608.15430](https://arxiv.org/abs/2608.15430)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (85.7), galactic_ism_surveys (70.8), feedback_bubbles (69.1)
- **Current keyword baseline:** NO
- **BM25 max:** 34.3
- **Semantic max:** 100.0
- **Abstract:** We present a snapshot of the ongoing efforts to obtain background-subtracted, wavelength-, and flux-calibrated spectra taken with the new Wide-Field Slitless Spectroscopy (WFSS) mode for the MIRI instrument on the James Webb Space Telescope (JWST), offered for the first time in JWST Cycle 5 (starting July 2026). We describe here the capabilities of the new mode, the operational concept, and an overview of the calibration and pipeline development activities that are currently ongoing.

### [A] 85.0 — The Galactic Centre G+0.633-0.0604 Molecular Cloud: A New Gold Mine for Astrochemistry
- **arXiv:** [2608.14381](https://arxiv.org/abs/2608.14381)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** astrochemistry (85.0), molecular_clouds (80.1), feedback_bubbles (74.0)
- **Current keyword baseline:** YES
- **BM25 max:** 94.8
- **Semantic max:** 99.1
- **Abstract:** Astrochemistry is living a golden age, with more than a quarter of the ~350 molecules in the current interstellar census having been detected over the last three years. One of the sources driving this progress is the G+0.693-0.027 cloud, located in the northern part of the Galactic Centre Sgr B2 complex. In this contribution, we present the astrochemical characterisation of G+0.633-0.0604, a newly discovered chemically rich molecular cloud at the southern edge of Sgr B2. With an inventory of >120 species, G+0.633 provides robust second detections of several prebiotic molecules only reported towards G+0.693, establishing it as the first confirmed astrochemical twin of G+0.693 while demonstrating that the extraordinary chemistry of this cloud is not unique. Furthermore, G+0.633 offers an observational advantage over G+0.693 since it displays half narrower linewidths. Together, G+0.633 and G+0.693 form a unique benchmark pair for unveiling molecular complexity and prebiotic chemistry in the interstellar medium.

### [A] 83.9 — A comprehensive cluster census of Orion. An application of the Significance Mode Analysis (SigMA) algorithm
- **arXiv:** [2608.16989](https://arxiv.org/abs/2608.16989)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** star_formation (83.9), astrochemistry (70.1), massive_star_formation (69.5)
- **Current keyword baseline:** YES
- **BM25 max:** 62.0
- **Semantic max:** 97.8
- **Abstract:** Precise astrometric surveys and modern clustering algorithms are working in step to transform our view of star-forming regions. By revealing a much richer substructure than previously accessible, they pave the way for reconstructing star formation histories by accurately resolving and age-dating individual sub-populations. The Orion star-forming complex is the best-studied stellar nursery in the solar neighborhood and the nearest one currently forming massive stars. Even so, a comprehensive characterization of its substructure, including a homogeneous age mapping and extinction analysis, is still incomplete. Here, we present the most complete census of stellar populations across the Orion complex from the newest version of the SigMA algorithm and outline our additions and improvements to the algorithm that have extended its usage to distant (>300 pc) regions. We separate the Orion complex into 47 co-spatial and co-moving stellar groups comprising 11,996 reliable members, with ages ranging from 1.5 to 25 Myr. To evaluate the statistical robustness of each group, we derive cluster persistence values and individual membership probabilities for each source from 10 independent clustering repetitions. Our group memberships agree well with the literature, but SigMA consistently finds a factor of ~2-3 more members. In particular, it resolves more very young populations, such as NGC 2024, RV Orionis, B30, NGC 1977, NGC 2068, and NGC 2071, than previous algorithms. In addition to recovering 28 known clusters and three groups previously classified as substructures, we present 16 new co-eval substructure candidates of the Orion star-forming complex. This work builds up a new high-resolution time-resolved picture of Orion. This spatio-temporal map allows us to relate its stellar content to the surrounding ISM and paves the way for a detailed analysis of its star formation history in the future.

### [A] 83.8 — Star Formation in the H II Region Sh 2-205: 3D Morphology and Kinematics from Young Stars and Molecular Gas
- **arXiv:** [2608.16179](https://arxiv.org/abs/2608.16179)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (83.8), feedback_bubbles (81.9), molecular_clouds (75.3)
- **Current keyword baseline:** NO
- **BM25 max:** 100.0
- **Semantic max:** 97.6
- **Abstract:** Using Gaia astrometry of young stars combined with CO observations, we present the first systematic three-dimensional (3D) analysis of the structure, kinematics, and evolutionary history of the star-forming regions in the environs of the H II region Sh 2-205 (S205). S205 exhibits a complex morphology and coherent expansion on both global and subregional scales. We identify several O9-B1 stars and a 0.56 Myr old pulsar that are likely associated with the region. A momentum estimate suggests that feedback from these objects may account for the observed overall expansion. Trace-back analysis of the expansion, combined with color-magnitude diagram fitting for young star clusters, indicates at least two episodes of star formation. These results reveal a complex star-formation history of S205 and provide new insights into its 3D evolution.

### [A] 82.9 — Trace the Self-Gravitating Gas Using CO Isotopologues
- **arXiv:** [2608.12473](https://arxiv.org/abs/2608.12473)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (82.9), galactic_ism_surveys (77.0), ism_methods_data (76.3)
- **Current keyword baseline:** NO
- **BM25 max:** 88.1
- **Semantic max:** 96.5
- **Abstract:** Recent studies have shown that the star formation rate (SFR) correlates tightly and linearly with the mass of gravitationally bound gas, which can be delineated from the power-law tail of the column-density probability distribution function ($N$-PDF) derived from dust emission observations. This relationship holds across four orders of magnitude within the Milky Way--spanning low-mass to high-mass star-forming regions and encompassing the extreme environment of the Central Molecular Zone. Building on this framework, we present a new approach for estimating the mass of gravitationally bound gas in molecular clouds using multi-line CO isotopologue observations. Our sample includes 16 molecular clouds with robust detections in $^{12}$CO, $^{13}$CO, and C$^{18}$O $J$ = 1-0, spanning both massive inner Galaxy clouds and nearby star-forming regions. We find that the $N$-PDFs derived from combined CO isotopologue data recover the characteristic log-normal plus power-law profiles seen in dust-based studies. The mass and spatial distribution of the self-gravitating structures estimated from both dust-based and CO-based methods agree well throughout the sample. This indicates that the CO isotopologue combination can robustly trace the self-gravitating component via the $N$-PDF method and provides a reliable, scalable, and velocity-resolved alternative to dust emission for identifying the star-forming gas in molecular clouds.

### [A] 82.7 — ALMA observations of pre-JWST z ~ 10 galaxy candidates: A CO(J = 9-8) line from a ULIRG at z = 2.54 and revisit of the photometric redshifts with JWST photometry
- **arXiv:** [2608.12708](https://arxiv.org/abs/2608.12708)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (82.7), galactic_ism_surveys (80.0), atomic_ism (80.0)
- **Current keyword baseline:** NO
- **BM25 max:** 73.1
- **Semantic max:** 100.0
- **Abstract:** We present Atacama Large Millimetre/submillimetre Array (ALMA) observations targeting the [OIII]$88\,μ$m line for six $z\sim10$ galaxy candidates selected with the Hubble Space Telescope and the Spitzer Space Telescope. We detect a line ($4.5σ$) and dust continuum emission ($30σ$) in UDS_18697, while detecting neither robust line nor continuum emission in the remaining five objects. The detected line in UDS_18697 is identified as CO($J=9-8$), because follow-up James Webb Space Telescope (JWST) NIRSpec observations have confirmed the redshift as $z=2.54$. UDS_18697 is classified as an ultra luminous infrared galaxy (ULIRG) with far-infrared (FIR) luminosity of $L_\mathrm{FIR}\approx1.1\times10^{12}\,L_\odot$, assuming a dust temperature of $T_\mathrm{d}\approx42\,$K, estimated using a physically-motivated method. We find that UDS_18697 follows the $L_\mathrm{FIR}-L'_\mathrm{CO}$ relation for local and $z>2$ galaxies, albeit being slightly brighter in CO($J=9-8$). Also, based on the follow-up NIRSpec observations and spectral energy distribution fitting using JWST/NIRCam photometry, we found that most of our targets are suggested to be low-$z$ interlopers. Motivated by these redshift misclassifications, we investigate colour--colour selection criteria for high-$z$ galaxies using JWST spectroscopic survey catalogues. We find that elevating a colour threshold tracing the Lyman break is crucial for constructing a robust high-$z$ sample, particularly for wide field surveys such as Euclid Deep Fields and Roman High-Latitude Wide-Area Survey.

### [A] 81.3 — OutThere Survey: Addressing $\mathrm{ξ_{ion}}$ and $\mathrm{f_{esc}}$ with a population of average galaxies at z$\sim$2
- **arXiv:** [2608.19687](https://arxiv.org/abs/2608.19687)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (81.3), atomic_ism (74.5), galactic_ism_surveys (70.8)
- **Current keyword baseline:** NO
- **BM25 max:** 49.5
- **Semantic max:** 94.5
- **Abstract:** Constraining the major contributors to the ionisation of the early universe is an ongoing endeavour of high-redshift galaxy research. We measure the ionising photon production efficiency and Lyman Continuum escape fraction for a sample of 230 intermediate redshift ($1.3<z<2.6$) sources observed as a part of the \textit{OutThere survey}; a pure-parallel, wide-area JWST/NIRISS survey with accompanying JWST/NIRCam, NIRISS and HST photometry. The low threshold emission selection criteria for this sample makes for a large and robust control, against which other works may be contrasted, particularly for low-mass galaxies above z$>$5. This control sample allows us to verify the correlations between ionising and spectral/physical properties suggested by previous studies. We find no significant correlations between the ionising photon production efficiency ($\mathrm{ξ_{ion}}$) with the UV slope, $\mathrm{M_{UV}}$, M$_*$ or sSFR. We do find that $\mathrm{ξ_{ion}}$ correlates with [OIII]5007Å\, equivalent width (EW) (Spearman coefficient $ρ$ =0.24; p$< 4\times10^{-4}$) and H$α$ EW ($ρ$ =0.63; p$<< 1\times10^{-6}$) hold even at low EW albeit with more scatter. We also find that our novel approach to determining the ionising photon escape fraction $\mathrm{f_{esc}}$ results in values within theoretical ranges (0-10\%) though vary substantially in comparison to the empirical results (median $\mathrm{f_{esc}} = 0.9\%^{+1.1}_{-0.5}$ including non-detections, median $\mathrm{f_{esc}} = 1.9\%^{+8.9}_{-1.8}$ above a $0.01\%$ threshold). We find that this escape fraction method has consistently significant correlations with the redshift, SFR and M$_{UV}$ and sample-dependent correlations with [OIII]5007Å\,EW,H$α$ EW and stellar mass.

### [A] 81.2 — High-Redshift Type Ia Supernovae Exhibit Enhanced Calcium Abundances
- **arXiv:** [2608.18342](https://arxiv.org/abs/2608.18342)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (81.2), astrochemistry (75.7), ism_methods_data (73.8)
- **Current keyword baseline:** NO
- **BM25 max:** 54.9
- **Semantic max:** 94.7
- **Abstract:** Type Ia supernovae (SNe Ia) are major contributors to cosmic chemical enrichment, and their elemental abundances provide a probe of progenitor properties and explosion physics across cosmic time. We employ an artificial intelligence-assisted inversion technique to analyze spectra of high-redshift SNe Ia from the Supernova Legacy Survey and of gravitationally lensed SNe Ia observed by the James Webb Space Telescope, extending the sample to redshift 2.05. We find a positive correlation between SN Ia calcium abundance and redshift. The redshift-dependent variation in calcium abundance exceeds that predicted by SN Ia nucleosynthesis simulations with varying progenitor metallicities, suggesting that high-redshift SNe Ia may undergo different explosion mechanisms from nearby SNe Ia.

### [A] 81.2 — CO rotational line emission in very red carbon stars in the Magellanic Clouds
- **arXiv:** [2608.16456](https://arxiv.org/abs/2608.16456)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** molecular_clouds (81.2), star_formation (73.6), astrochemistry (71.3)
- **Current keyword baseline:** NO
- **BM25 max:** 79.4
- **Semantic max:** 94.4
- **Abstract:** Stars of low and intermediate initial mass lose most of their stellar mass at the end of their lives during the asymptotic giant branch (AGB) phase. Determining their gas and dust mass-loss rates (MLRs) is crucial for quantifying the contribution of evolved stars to the life cycle of dust and gas in the Universe. The Atacama Large Millimeter/submillimeter Array was used to observe 38 carbon stars (C stars) in the large Magellanic cloud (LMC) and three C stars in the small Magellanic cloud (SMC) in the CO J= 2-1 line. Line profiles were fitted to derive stellar velocities and wind-expansion velocities (Vexp). CO emission is detected in two C stars in the SMC and 33 C stars in the LMC. This is the first detection of carbon monoxide around an AGB star in the SMC. One object in the LMC shows emission in $^{13}$CO. The wind-expansion velocity ranges from \sim7.5 to \sim30 km/s. Archival data were used to determine the pulsation periods as well as construct and model the spectral energy distributions using two dust radiative transfer codes. Mass-loss rates were independently derived from these two codes as well as from the intensity of the CO line, using a simple formula. On average, the dust-based MLRs higher than the MLRs based on the CO line by a factor of 1.6. Additional CO data in other transitions, combined with proper modelling, is required to further investigate this possible discrepancy. Mass-loss rates, pulsation periods, and expansion velocities were compared to a sample of Galactic C stars. There is a strong bias, as the Magellanic Cloud targets sample the highest MLRs and luminosities, yet they represent only a minority of stars in a Galactic sample. Comparing this sample with a similarly extreme set of Galactic stars with periods longer than 500 days, we identify no correlation between metallicity and either the MLR or Vexp.

### [A] 81.0 — TomoSphero: Fast Differentiable Projector for Planetary and Solar Tomography on Spherical Grids
- **arXiv:** [2608.16960](https://arxiv.org/abs/2608.16960)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP, astro-ph.SR
- **Top topics:** ism_methods_data (81.0), star_formation (60.9), molecular_clouds (53.1)
- **Current keyword baseline:** YES
- **BM25 max:** 100.0
- **Semantic max:** 94.2
- **Abstract:** Computational tomography is a tool for determining the internal structure of objects from a set of projections, typically taken along some regular path. In recent years, methods and GPU-accelerated libraries have emerged that allow for fast reconstruction from projections along more complicated paths. Most of these libraries rely on a Cartesian discretization of the object, which is not appropriate for all scenarios. We present TomoSphero, a differentiable tomographic projector over spherical grids which are often used in planetary and solar tomography. TomoSphero is designed to be used as a building block in reconstruction algorithms and includes common projection types such as cone-beam and parallel-beam, but is flexible enough to accommodate arbitrary projections. TomoSphero is implemented in PyTorch which allows for fast projection computation on GPUs, easy access to modern machine learning optimizers, and automatic differentiation for rapid prototyping of parametric models.

### [A] 80.9 — High Velocity Neutral Gas in the Fermi Bubbles: New Kinematic Limits and Spatial Structure
- **arXiv:** [2608.16754](https://arxiv.org/abs/2608.16754)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (80.9), feedback_bubbles (68.3), molecular_clouds (62.1)
- **Current keyword baseline:** YES
- **BM25 max:** 91.7
- **Semantic max:** 89.0
- **Abstract:** We have detected hundreds of neutral clouds entrained in the Milky Way's nuclear wind using HI data from new surveys made with the Green Bank Telescope that cover about 500 sq-degrees around the Galactic center (GC). Galactic winds are common throughout the Universe, and these data at 9.1' angular resolution (22 pc at the GC) provide the most detailed analysis of the vertical profile of a neutral nuclear wind in any galaxy. A set of 228 of these Fermi Bubble clouds with the largest values of |VLSR| has been analyzed to examine the distribution and kinematics of the outflowing gas. The clouds span -335 km/s $\leq$ VLSR $\leq$ +438 km/s, the largest positive LSR velocities ever reported for neutral HI associated with the Milky Way disk. The highest velocities are found furthest from the GC, suggesting that clouds are accelerated from a low velocity near the nucleus to at least 500 km/s at a radial distance of $\lesssim 4$ kpc. Clouds appear disrupted as they are accelerated: their line brightness and NHI decreases steadily with distance from the GC, and the population becomes more uniform. There is an abrupt cutoff in the neutral clouds at a vertical distance of $\approx2$ kpc from the Galactic plane. Kinematic models of an outflowing cloud population that fills the FB volume are used to identify structure in the gas. The kinematics of the highest velocity, highest latitude clouds imply a past azimuthal asymmetry in the outflow.

### [A] 80.7 — Abundant Heavy Black Hole Seeds from Moderate Lyman-Werner Radiation
- **arXiv:** [2608.13656](https://arxiv.org/abs/2608.13656)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** star_formation (80.7), massive_star_formation (73.4), galactic_ism_surveys (70.7)
- **Current keyword baseline:** NO
- **BM25 max:** 75.5
- **Semantic max:** 91.7
- **Abstract:** The existence of high-redshift quasars may indicate that massive black hole seeds formed via supermassive Population III stars in atomic-cooling halos with large gas inflow rates; however, the dependence of this process on halo assembly rate and radiative background remains poorly constrained. We present a large suite of 65 high-resolution cosmological zoom-in simulations of 15 pristine halos spanning a wide range of Lyman-Werner radiation backgrounds and halo assembly histories. We introduce a novel method to estimate the final Population III stellar mass from radial gas infall profiles at the onset of runaway collapse and validate it against simulations from the literature that explicitly follow protostellar accretion with sink particles, reproducing protostellar masses to within a factor of $\sim2$. We find a clear transition in gas inflow rates between halos exposed to $J_{\rm 21} \lesssim 1$ and $J_{\rm 21} \gtrsim 10$, with the latter frequently sustaining inflow rates above the adopted threshold for supermassive star formation and producing estimated stellar masses up to $10^{5} \, M_{\odot}$. In contrast, the halo assembly timescale, $M_{\rm Halo}$/$\dot{M}_{\rm Halo}$, shows no statistically significant correlation with predicted stellar mass, despite halo assembly rates spanning $0.01$-$7 \, M_{\rm \odot} \, {\rm yr}^{-1}$. The Lyman-Werner radiation field therefore is a stronger predictor of sustained high accretion within our parameter space. Finally, a semi-analytic model applied to cosmological volumes shows that halos exposed to intermediate Lyman-Werner backgrounds ($1 \lesssim J_{\rm 21} < 10$) are orders of magnitude more common than those in the high-$J_{\rm 21}$ tail. If sustained high accretion extends into this intermediate regime, heavy black hole seeds may form in substantially more common environments than required by classical direct-collapse scenarios.

### [A] 80.4 — The Roman Coronagraph Community Participation Program: calibration strategy for the Mueller matrix using on-sky sources
- **arXiv:** [2608.17369](https://arxiv.org/abs/2608.17369)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** ism_methods_data (80.4), magnetic_fields (67.3), astrochemistry (59.8)
- **Current keyword baseline:** NO
- **BM25 max:** 55.1
- **Semantic max:** 93.4
- **Abstract:** The Nancy Grace Roman Space Telescope Coronagraph Instrument will provide space-based polarimetric observations of circumstellar disks and exoplanetary systems. Accurate reconstruction of the linear polarization fraction requires calibration of the instrumental Mueller matrix using polarized and weakly polarized standard stars. We constructed a candidate catalog by combining published optical polarimetry with Gaia DR3 astrometry and photometry and selected separate samples for coronagraphic calibration observations and observations using a neutral-density filter. Precursor $VRI$-band polarimetry of 18 faint candidates was obtained with HONIR on the 1.5-m Kanata telescope. The wavelength dependence of their normalized Stokes parameters was modeled using the Serkowski law to predict their polarization properties in \cgi\ Bands~1 and 4, and 2 sets of 3 calibrators were selected for the 2 calibration scenarios. We then estimated the achievable LPF reconstruction accuracy using Monte Carlo simulations that include uncertainties in the calibrator polarization properties, photometric noise, and residual detector-response errors. A dithered observing configuration was also simulated to reduce differential detector-response errors among the calibrators. The current estimates indicate LPF reconstruction errors at the few-percentage-point level, with a small bias arising from treating a weakly polarized calibrator as unpolarized. Finally, we present progress toward an end-to-end test using \texttt{corgisim} and \texttt{corgiDRP}, including successful processing of simulated datasets from Level~1 through Level~2b.

### [A] 80.0 — Outflows in steep density gradients: diversity of behavior and implications for tidal disruption events and luminous fast blue optical transients
- **arXiv:** [2608.19512](https://arxiv.org/abs/2608.19512)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** turbulence (80.0), feedback_bubbles (78.9), molecular_clouds (71.6)
- **Current keyword baseline:** NO
- **BM25 max:** 58.5
- **Semantic max:** 100.0
- **Abstract:** Powerful explosions may undergo sustained energy injection as a central engine launches a wind into the surrounding gas, generating a forward and a reverse shock separated by a contact discontinuity. During the adiabatic phase, the dynamics depend strongly on the wind-to-ambient density ratio $f \equiv ρ_{\rm w} / ρ_{\rm a}$. For $f << 1$, the reverse shock lies well inside the contact discontinuity, and the mechanical energy deposited by the wind is retained in a radially extended, approximately isobaric shocked-wind region whose pressure drives the swept-up ambient shell. For $f \gg 1$, the reverse shock remains close to the contact, and the expansion is governed by the ram-pressure interaction between the freely expanding wind and the swept-up ambient gas. We use analytic scalings and one-dimensional shock-capturing hydrodynamic simulations to determine how outflows in these two limits evolve in ambient density profiles $ρ_{\rm a} \propto r^{-n}$, where $2 \leq n \leq 3$, and whether their shock structures accelerate or coast at constant velocity. For $n > 2$, initially underdense outflows produce accelerating forward shocks whose radii evolve as $R_{\rm s} \propto t^{3/(5-n)}$. Because $ρ_{\rm w} \propto r^{-2}$, f increases with radius, causing the reverse-shocked wind region to contract relative to the contact position as the forward shock transitions toward constant-velocity expansion. This occurs when $f \sim$ a few at $t_{\rm dec} \propto f_0^{1/(2-n)}$, where $f_0$ is the initial wind-to-ambient density ratio. By contrast, outflows initialized with $f_0 \gg 1$ do not develop an extended accelerating phase and remain approximately coasting throughout their adiabatic evolution. We discuss applications to tidal disruption event outflows and luminous fast blue optical transients, whose environments are often inferred to have steep density profiles with $n > 2$.

### [A] 80.0 — Generalized Non-linear Bayesian Pulsar Timing with Enterprise
- **arXiv:** [2608.18047](https://arxiv.org/abs/2608.18047)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (80.0), ism_methods_data (77.2), turbulence (62.2)
- **Current keyword baseline:** NO
- **BM25 max:** 32.9
- **Semantic max:** 100.0
- **Abstract:** In this study, we use the Bayesian methods in the Enterprise package to examine the fully general parameterization of pulsar timing models in tandem with noise. We investigate four pulsars, PSR J1600$-$3053, PSR J2043+1711, PSR J0740+6620, and PSR J1640+2224, through the lens of Bayesian timing. These four are selected as they are well-studied, but exhibit interesting characteristics under the lens of Bayesian timing. Our new pulsar mass constraints (medians and 68\% confidence intervals) for our fully general non-linear Bayesian timing models are $m_{\mathrm{p}}=1.6(1)~\mathrm{M}_{\odot}$ for PSR J2043+1711 and $m_{\mathrm{p}}=2.3^{+0.9}_{-0.7}~\mathrm{M}_{\odot}$ for PSR J1600$-$3053 both using the NANOGrav 12.5-yr data release, and $m_{\mathrm{p}}=2.06(6)~\mathrm{M}_{\odot}$ for PSR J0740+6620 using the data from Fonseca, et al., 2021. We investigate the effects on placing physical priors on timing model parameters, including restricting the upper limit on the pulsar mass for PSR J1640+2224, which has a mass often estimated to be greater than $3~\mathrm{M}_{\odot}$. We find \ark{that restricting the allowed sampling space of the pulsar mass for PSR J1640+2224 to} $m_{\mathrm{p}}<3~\mathrm{M}_{\odot}$ results in a pulsar mass of $m_{\mathrm{p}}=2.2(5)~\mathrm{M}_{\odot}$ for PSR J1640+2224 using the NANOGrav 12.5-yr data release. For the first time, we find evidence for intrinsic red noise in PSR J2043+1711. We show how fully general Bayesian timing can better model the interplay of the intrinsic noise and the timing parameters.

### [A] 80.0 — Aromatics and Aliphatics in Local Star-Forming Galaxies as Probed by AKARI
- **arXiv:** [2608.14989](https://arxiv.org/abs/2608.14989)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (80.0), massive_star_formation (72.1), atomic_ism (71.9)
- **Current keyword baseline:** NO
- **BM25 max:** 59.4
- **Semantic max:** 100.0
- **Abstract:** Polycyclic aromatic hydrocarbon (PAH) molecules are abundant and widespread in galaxies and their infrared (IR) emission traces star formation. PAH molecules in astronomical environments often have aliphatic contents as revealed by the detection of the 3.4 micron aliphatic C--H stretch, a weak satellite feature accompanying the 3.3 micron aromatic C--H stretch. Here, we selected 102 local star-forming galaxies from the AKARI archive, including 66 galaxies each of which hosts an active galactic nucleus (AGN). We analyzed their AKARI near-IR spectra, which exhibit pronounced 3.3 micron aromatic and 3.4 micron aliphatic C--H emission. We also compiled their multi-wavelength photometric data and performed a decompositional analysis of their spectral energy distributions (SEDs) from the ultraviolet (UV) to the far-IR to derive the star formation rates (SFRs), stellar masses, metallicities, and luminosity of the galaxies. We explored the 3.3 micron PAH emission luminosity ($L_{3.3}$) as a calibrator of the SFR and found a close agreement with previous studies. We also found that $L_{3.3}/L_{\rm IR}$ and $L_{3.4}/L_{\rm IR}$ exhibit a strong dependence on metallicity, but remain nearly constant above 12+log(O/H)$\sim\,$8.5, where $L_{\rm IR}$ is the total luminosity emitted by dust, and $L_{3.4}$ is the luminosity of the 3.4 micron aliphatic emission. We derived from $L_{3.4}/L_{3.3}$ the PAH aliphatic fractions, defined as the fractions of carbon atoms in aliphatic units, to be in the range of $\sim\,$0.38%--6.8%, with a median fraction of $\sim\,$3.1%. The PAH aliphatic fractions are lower in AGN hosts and show a weak negative correlation with the SFR and $L_{\rm IR}$, suggesting that UV photons in regions with AGN or strong star formation activities may photodissociate the aliphatic structures associated with PAH molecules.

### [A] 80.0 — JWST/NIRSpec Spectra for Three Ultracool Brown Dwarfs Detected in Extragalactic Surveys: Further Evidence for Phosphine Absorption
- **arXiv:** [2608.14786](https://arxiv.org/abs/2608.14786)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** feedback_bubbles (80.0), ism_methods_data (78.4), massive_star_formation (78.3)
- **Current keyword baseline:** YES
- **BM25 max:** 53.4
- **Semantic max:** 100.0
- **Abstract:** We present JWST NIRSpec prism spectra for three ultracool brown dwarfs discovered in extragalactic survey data, two from the JWST Advanced Deep Extragalactic Survey (JADES), and one from Public Release IMaging for Extragalactic Research (PRIMER) survey observed as part of the Mirage or Miracle (MoM) program. The spectra for these sources indicate that one is a T6 dwarf (JADES-GS-BD-11, T$_{\mathrm{eff}} = \sim 700$ K) and two are Y0-Y1 dwarfs (JADES-GS-BD-5, T$_{\mathrm{eff}} = \sim 400$ K, and MoM-239450, T$_{\mathrm{eff}} = \sim 500$ K). Model atmospheric fits with $\texttt{NIFTY}$ to the spectra are consistent with this classification, and indicate that JADES-GS-BD-5 is only $\sim 150$ pc from the Sun, MoM-239450 is $\sim 700 - 800$ pc from the Sun, and JADES-GS-BD-11 is $\sim 1$ kpc from the Sun, with these latter two more distant sources being best fit at sub-solar metallicities. JADES-GS-BD-5 has an observed spectrum with significantly weaker J and H band emission than Y dwarf atmospheric models, potentially indicating the presence of water ice clouds in the brown dwarf. The spectrum for JADES-GS-BD-11 has a feature at 4.3$μ$m consistent with absorption from the rarely seen phosphine molecule at $2.6σ$ confidence. Given the low metallicity for this source ([M/H] $ = -0.7$), our finding supports the theory that detecting phosphine in brown dwarf atmospheres is tied to atmospheric metallicity. JWST/NIRSpec spectroscopy continues to be a powerful tool for understanding the properties of these distant, and very cold brown dwarfs.

### [A] 79.8 — Chromospheric heating and magnetic topology above the shared penumbra of a delta-spot: Multi-line inversions and multi-height magnetic-field extrapolations
- **arXiv:** [2608.19983](https://arxiv.org/abs/2608.19983)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** magnetic_fields (79.8), galactic_ism_surveys (69.0), astrochemistry (60.3)
- **Current keyword baseline:** NO
- **BM25 max:** 76.3
- **Semantic max:** 92.7
- **Abstract:** We analysed observations of the Fe I 617.3 nm, Ca II 854.2 nm, and Ca II H lines obtained with CRISP and CHROMIS at the SST. Spatially coupled non-LTE inversions constrained the chromospheric atmosphere, while the WFA provided estimates of the chromospheric line-of-sight magnetic field. We combined these photospheric and chromospheric constraints with an HMI magnetogram as input to a multi-height field extrapolation. We characterised the reconstructed topology using the twist number, squashing factor, current density, and field-line connectivity. Results. The Ca II H magnetic signal is concentrated mainly above the strongest photospheric field concentrations, whereas Ca II 854.2 nm yields stronger and more spatially extended line-of-sight fields. The chromosphere above the shared penumbra is approximately 300 K hotter than nearby quiet regions. The selected brightening follows a chromospheric loop, with enhanced temperature and a transition from blueshift to redshift along the structure. The extrapolation recovers field strengths broadly consistent with the inversions and reveals a left-handed, flux-rope-like core following the polarity inversion line. Enhanced currents and connectivity gradients occur near parts of its boundary, where field lines connect the twisted structure to overarching loops. Conclusions. The temperature and velocity patterns and magnetic topology are consistent with reconnection between the twisted polarity-inversion-line field and the surrounding loops, depositing energy in the chromosphere and driving plasma along reconfigured field lines. These signatures do not uniquely establish reconnection, but show that combining high-resolution spectropolarimetric inversions with multi-height extrapolations can relate chromospheric energy release to the local three-dimensional magnetic structure.

### [A] 79.7 — A Cross-Band (X-ray $\times$ Optical) Periodicity Search for Supermassive Black Hole Binaries: A Null Result and the First Completeness-Corrected Constraint
- **arXiv:** [2608.16787](https://arxiv.org/abs/2608.16787)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA, astro-ph.IM
- **Top topics:** star_formation (79.7), ism_methods_data (71.3), molecular_clouds (70.3)
- **Current keyword baseline:** NO
- **BM25 max:** 34.7
- **Semantic max:** 99.6
- **Abstract:** We present the first sample-level search for supermassive black hole binaries (SMBHBs) requiring coherent quasi-periodicity at a common period in the X-ray and optical bands, over 1194 Swift-BAT hard X-ray AGN (Stage 1) and 175 4XMM-DR14 AGN (Stage 2). No source is a co-periodic candidate. Each light curve is modelled as a damped random walk (DRW) and searched with a Lomb-Scargle periodogram and a look-elsewhere-corrected Monte-Carlo significance. Because DRW red noise is largely independent between corona and disc, we require both bands individually significant with periods coincident within 5%, and gate the survivors with the model-independent null-signal-template test of Robnik et al. (2024). Over $P=100$-$900$ d the completeness-corrected 95% upper limit on the co-periodic fraction is amplitude-dependent: $\lesssim 3\%$ for hard-X-ray fractional modulation $\gtrsim 0.3$, $\approx 15\%$ (precision-limited) at 0.2, and uninformative below $\sim 0.15$ (the $ε=1$ floor is 0.25%). The sensitivity is set by the hard X-ray monitoring, not the optical photometry or the statistics, the opposite of the usual assumption. Daily MAXI and RXTE/ASM monitoring of the brightest AGN raises the X-ray completeness 5-8-fold, and the search remains null. Integrated over the BAT black-hole mass function, the expected all-amplitude co-periodic fraction is $\sim 3\times10^{-2}\, f_{\rm bin}\, δ_{\rm mod}$ (modulo a factor $g<1$), with $f_{\rm bin}$ the sub-pc binary fraction, $δ_{\rm mod}$ the modulating duty cycle, and $g$ the fraction reaching recoverable hard-X-ray amplitude, so a null is expected. We deliver a validated cross-band framework and the first completeness-corrected constraint on the co-periodic fraction, ready for the denser X-ray monitoring of Einstein Probe and eROSITA.

### [A] 79.7 — Elemental Composition Evolution during the 2024 September 30 Solar Eruption: A Comparison of Hot and Cool Plasma Components with Solar Orbiter/SPICE, Hinode/EIS, and Chandrayaan-2/XSM
- **arXiv:** [2608.12881](https://arxiv.org/abs/2608.12881)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** astrochemistry (79.7), feedback_bubbles (64.1), molecular_clouds (56.0)
- **Current keyword baseline:** NO
- **BM25 max:** 58.8
- **Semantic max:** 92.5
- **Abstract:** Solar plasma composition differs between the photosphere and corona over a range of timescales, with preferential enhancement of elements with low first ionization potential (FIP). However, the physical origin of the FIP fractionation remains incompletely understood. Furthermore, during flares, the FIP bias also exhibits rapid changes, associated with fast transport of material with different FIP biases. We present novel observations from Solar Orbiter SPICE and EUI, Hinode/EIS, and Chandrayaan-2 XSM instruments, finding rapid abundance changes in the emitting plasma, on timescales of minutes, during the eruptive M7.6-class solar flare observed on 2024 Sept 30. These instruments have wide temperature coverage and find contrasting abundance-evolution patterns between the hotter and cooler plasma components. 3D reconstruction of the active region and additional observations from the Solar Orbiter STIX X-ray telescope show how the hot and cool plasma components, emitting in different spectral regions and observed with the various instruments, sample the plasma composition evolution in distinct locations within the observed flaring plasma. The bright post-flare loop tops observed by SPICE show coronal FIP bias, while the hot plasma observed with XSM exhibits FIP-bias decreasing from coronal to photospheric during the impulsive phase. We interpret these observations as evidence of the X-ray diagnostics seeing hot coronal reconnection outflows mixing with chromospheric plasma as flare loops sequentially energize and relax, explaining why the FIP bias decreases from coronal to a hybrid; and the cool loop tops seen with SPICE show coronal abundances due to coronal material deposited near the looptops.

### [A] 79.5 — Eta Carinae's historical light curve: evidence for cyclic Roche lobe overflow from the primary star
- **arXiv:** [2608.16818](https://arxiv.org/abs/2608.16818)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** star_formation (79.5), astrochemistry (67.8), feedback_bubbles (66.1)
- **Current keyword baseline:** YES
- **BM25 max:** 45.3
- **Semantic max:** 99.3
- **Abstract:** The large amount of ground-based photometric measurements of $η$ Carinae obtained since 1940 have remained problematic for quantitative modeling due to the blending of flux from the stellar core and the surrounding circumstellar nebula. In the era of the Hubble Space Telescope, spatially resolved imaging & spectrophotometry have enabled disentanglement of these components, allowing recovery of the stellar core $V$-band brightness from ground-based observations. We isolate the $V$-band fluxes of the stellar core and nebula using 1999--2020 HST (ACS and STIS) observations, and use these to calibrate coeval ground-based photometry. The main finding is an orbital light curve with an amplitude $Δm \approx \pm 0.2\,$mag, many times higher than that modeled by ellipsoidal deformation of the primary. The observations suggest that Roche lobe overflow starts at $- 75$ days before periastron in coincidence with the start of rising in the orbital light curve, and remains for 150 days. An expanding (and afterwards dissipating) gas cloud reflecting the light from the primary would explain the observed large amplitude of the orbital light curve. A sharp periodic photometric peak occurs at $\sim -18$ days from the periastron. It is followed by a broad minimum around the superior conjunction of the secondary (T$_0+5.2$ days), which we interpret as a partial eclipse of the ejected material, in coincidence with the \emph{shallow minimum} in X-rays, which also has been attributed to an eclipse.

### [A] 79.4 — The efficient star-forming regions of stripped-envelope supernovae
- **arXiv:** [2608.18897](https://arxiv.org/abs/2608.18897)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.HE
- **Top topics:** feedback_bubbles (79.4), galactic_ism_surveys (70.5), astrochemistry (64.3)
- **Current keyword baseline:** NO
- **BM25 max:** 97.2
- **Semantic max:** 92.2
- **Abstract:** Massive stars ($> 8~\rm{M}_{\odot}$) play a key role in shaping the interstellar medium of galaxies through stellar feedback. However, how these stars form and evolve before exploding as core-collapse supernovae (SNe) remains elusive. We compute for the first time the star-formation efficiencies (SFEs) at the locations of hydrogen-rich (H-rich) SNe and stripped-envelope SNe (SESNe) to constrain their progenitor properties. We used VLT/MUSE and ALMA observations of H$α$/H$β$ and CO(2-1) emission lines to trace the components of the warm ionised gas and cold molecular gas, respectively. Both observations resolve individual H II regions and giant molecular clouds at spatial resolutions on cloud-scales ($\sim$100 pc). This combined data allows us to compute the SFE from the star formation rate (SFR) and the molecular gas mass (M$_{\rm{mol}}$) as SFE = SFR/M$_{\rm{mol}}$. We find that SESNe explode in environments that are currently forming stars eight times more efficiently than those of H-rich SNe (higher SFR for SESNe with similar M$_{\rm{mol}}$). On one hand, this is consistent with the scenario in which the majority of SESNe are produced from very massive stars ($> 20~\rm{M}_{\odot}$) if the initial mass function is top-heavy. On the other hand, most of SESN progenitor channels are formed from interacting binaries ($< 20~\rm{M}_{\odot}$) if an increased binary system formation rate is connected with turbulences and, in turn, with the boost to SFE. Then, an increased binary fraction could explain the enhanced H$α$ luminosities. In summary, SESNe preferentially occur in regions of intense, efficient star formation rather than simply higher gas content.

### [A] 79.2 — Enhancing the performance and capabilities of the MIRI instrument on JWST
- **arXiv:** [2608.13873](https://arxiv.org/abs/2608.13873)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** galactic_ism_surveys (79.2), feedback_bubbles (74.8), ism_methods_data (70.2)
- **Current keyword baseline:** NO
- **BM25 max:** 43.2
- **Semantic max:** 98.9
- **Abstract:** MIRI, the Mid-Infrared Instrument on the James Webb Space Telescope, is the only instrument sensitive to wavelengths longward of 5 um on the observatory. In this regime, MIRI brings order-of-magnitude improvements over past instruments and missions in a wavelength range that is challenging or impossible to access from the ground. As such, MIRI occupies a unique parameter space, offering unparalleled capabilities in all areas of astrophysics, from the Solar System to the most distant galaxies in the Universe. We continue to make operational improvements to MIRI, four years into its operational lifetime, to create new observing opportunities, improve performance, and enhance its scientific return. In this paper we will describe several such improvements, and their anticipated impact on MIRI and JWST science.

### [A] 79.1 — The Roman Coronagraph Community Participation Program: target database and tools
- **arXiv:** [2608.17152](https://arxiv.org/abs/2608.17152)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** molecular_clouds (79.1), star_formation (78.1), ism_methods_data (76.8)
- **Current keyword baseline:** NO
- **BM25 max:** 37.8
- **Semantic max:** 98.9
- **Abstract:** The Nancy Grace Roman Space Telescope, set to launch in Fall 2026, will carry the Coronagraph Instrument, which will, for the first time, demonstrate high-contrast imaging with active wavefront control in visible wavelengths from space. In preparation for execution of the Coronagraph's commissioning and observing programs, the Roman Coronagraph Community Participation Program (CPP) has developed a target database and associated ecosystem of publicly accessible tools for observation planning and scheduling. The target database includes both stars and known sub-stellar companions and disks that may be observed by the Coronagraph instrument during its primary mission. Targets in the database include planet and disk hosts as well as calibration stars, reference stars, and engineering program targets. The database is designed to operate in conjunction with a variety of tools, including an exposure time calculator, a pointing and keepout calculator, and a reference star selection tool. Here, we describe the current schema and contents of the database and demonstrate how it and its associated tools are being used for observation planning.

### [A] 79.1 — The Low-Mass Baryon Cycle in QUEST Dwarf Galaxies I: Sample definition and first results
- **arXiv:** [2608.15782](https://arxiv.org/abs/2608.15782)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (79.1), galactic_ism_surveys (69.8), massive_star_formation (67.0)
- **Current keyword baseline:** NO
- **BM25 max:** 69.9
- **Semantic max:** 91.8
- **Abstract:** We introduce the QUEST Dwarfs program, which connects low-mass galaxies' stellar populations, interstellar medium, and circumgalactic medium in a large and coherently analyzed sample using a combination of optical spectroscopy, broadband imaging, and FUV absorption spectra of bright background sources .We present initial results from the first-release sample, comprising 14 galaxies with stellar mass $M_\mathrm{star} \leq 10^9 M_\odot$ at $z\approx0.001-0.017$, each with at least one CGM absorption probe at projected distances $d_\mathrm{proj}\lesssim 100$ kpc. This representative sample triples the number of available probes within 1/3 of the halo radius of dwarf galaxies outside of the Local Group. We find that the total silicon column density declines much more rapidly with projected distance than \textsc{Hi}, implying that chemically enriched cool gas is preferentially concentrated in the inner CGM, while the increasing ionization fraction of hydrogen with radius likely enhances this contrast. Accounting for unobserved silicon in higher ionization stages, we infer total metal masses of $\log M_Z/M_\odot\approx4.8$ and $6.5$ in the cool CGM within $0.3 R_\mathrm{vir}$ for dwarfs with median $\log M_\mathrm{star}/M_\odot=7.6$ and 8.6, respectively. These reservoirs correspond to $\approx3$% and $\approx16$% of the total metals produced over the galaxies' lifetimes. More massive galaxies also exhibit systematically stronger metal absorption, suggesting that projected distance governs the radial decline of metal absorption while stellar mass sets the normalization of the CGM metal profile. Individual ions reveal a multiphase structure, with low-ionization species concentrated in the inner halo and higher-ionization species extending farther. The full QUEST Dwarfs survey will provide the statistical power needed to isolate the dominant drivers of CGM enrichment in low-mass halos.

### [A] 78.9 — JWST-MIRI's multi-dimensional view of mass loss in the irradiated disks of NGC 1977
- **arXiv:** [2608.17226](https://arxiv.org/abs/2608.17226)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** feedback_bubbles (78.9), astrochemistry (63.4), galactic_ism_surveys (62.1)
- **Current keyword baseline:** YES
- **BM25 max:** 88.0
- **Semantic max:** 91.6
- **Abstract:** The evolution of protoplanetary disks, and consequently the outcomes of planet formation, are thought to be significantly altered in regions containing massive stars. Extreme cases in the Orion Nebula Cluster (ONC) demonstrate the impact of external irradiation (FUV$\gtrsim10^{4}$ G$_{0}$) on disk evolution, but intermediate environments remain less observationally constrained. We present JWST/MIRI Medium Resolution Spectroscopy (MRS) observations of seven proplyds in NGC 1977 exposed to an external FUV field of $10^{3}-10^{5}$ G$_{0}$ from the B1V star 42 Orionis (42 Ori). We characterize emission from molecular (H$_{2}$) and atomic (e.g., [Ne II], [Ar II], HI) species, and in some cases, MIRI reveals extended emission tracing the proplyd ionization front and wind. The closest disk to 42 Ori, KCFF#1, is undergoing extreme mass loss, traced by a 1000s-of-au-long dusty tail, and lacks clear H$_{2}$ or HI emission, indicating an advanced stage of dispersal. The remaining six disks exhibit two-temperature components of H$_{2}$ emission (500--700 K and 1000--1500 K), likely tracing the disk molecular layer and a photoevaporative wind, alongside HI lines which are used to estimate mass accretion rates. When comparing KCFF#2 and #6, which have similar host stars, KCFF#2 (closer to 42 Ori) is dominated by externally driven mass loss, with extended molecular and atomic emission, whereas KCFF#6 only shows extended H$_{2}$ emission, with roughly equal contributions from accretion and external mass loss. While the sample is small, this work demonstrates how JWST/MIRI can assess environmental impacts on disk evolution, with NGC 1977 bridging strongly irradiated disks in the ONC and the more local population.

### [A] 78.6 — Old Disks Die Hard: How Does AGN Feedback Suppress Disk Formation in Milky Way Mass Galaxies?
- **arXiv:** [2608.13718](https://arxiv.org/abs/2608.13718)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (78.6), feedback_bubbles (74.5), star_formation (67.1)
- **Current keyword baseline:** NO
- **BM25 max:** 67.1
- **Semantic max:** 91.2
- **Abstract:** The connection between a galaxy's visual shape and its star formation rate is one of the oldest established trends in galaxy evolution, yet the origin of this trend remains unsettled. We analyze two Milky-Way mass halos simulated with FIRE-2 galaxy formation physics, each run without AGN and with up to three implementations of AGN feedback. We use them to study how and why AGN star formation suppression affects morphological evolution over cosmic time. Both runs without AGN feedback produce prominent, thin, star-forming spiral disks at $z=0$. Each of the AGN runs has less late-time star formation, and ends up with a higher spheroid fraction and a lower thin-disk mass fraction. In two instances, the AGN runs produce quenched lenticular galaxies with no cool gas at $z=0$. The main reason for these morphological differences is that AGN feedback becomes effective {\em just after} the onset of disk formation, at ``spin up," in every run. This time-differentiated impact suppresses the formation of disk stars, especially thin-disk stars, preferentially because thin-disk formation occurs late. The spheroidal components are assembled early in all runs, before AGN feedback is effective, and are therefore similar in mass and size across runs.

### [A] 78.5 — Cosmography with DESI-DR1 Cosmic Chronometers: Direct H(z) measurements from Luminous Red Galaxy ages
- **arXiv:** [2608.13178](https://arxiv.org/abs/2608.13178)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, astro-ph.GA
- **Top topics:** astrochemistry (78.5), galactic_ism_surveys (70.8), ism_methods_data (63.1)
- **Current keyword baseline:** NO
- **BM25 max:** 46.4
- **Semantic max:** 98.2
- **Abstract:** Providing robust redshift estimates for almost 3 million luminous red galaxies (LRGs), the Dark Energy Spectroscopic Instrument (DESI) offers a unique opportunity to test the expansion rate of the Universe with independent approaches. We apply the cosmic chronometer method to derive new, independent constraints on the Hubble parameter at 0.3<z<1.2 from the differential age evolution of DESI LRGs. We select spectra applying spectroscopic cuts to ensure sample purity and remove contamination by star-forming objects, then build a robust sample of cosmic chronometers (CCs) by stacking to obtain stable, high signal-to-noise (S/N) spectra, which also serves as a democratic binning choice for the $t-z$ plane. Ages are estimated by measuring Lick indices on the stacked spectra and fitting them with a theoretical stellar population model. We obtain $t-z$ relations from which we derive $H(z)$ constraints via two independent approaches: a fit with a pivotal-redshift cosmography, and a direct estimate from the original CC method. The cosmographic fit yields posteriors for the kinematic parameters $\{H_{z_0}, q_{z_0}, j_{z_0}\}$ compatible with currently considered cosmologies, giving a precision-level estimate of $H(z)$. We provide the maximum-a-posteriori (MAP) $H(z)$ estimate, an array of the median confidence region in the $H-z$ plane, and its covariance matrix. We also leverage the redshift distributions of the $t-z$ relation for different velocity dispersion groups to obtain two independent local measurements using the discrete approximation $H(z) \approx -Δz/[Δt (1+z)]$; the one from the reddest envelope of CCs gives $H(z \approx 0.61) = 88.5^{+6.7}_{-12.6}$ (stat.) $\pm 8.1$ (syst.) km s$^{-1}$ Mpc$^{-1}$. Systematic uncertainties for both the cosmographic and discrete $H(z)$ measurements come from a comprehensive analysis of all methodological choices in the data treatment.

### [A] 78.4 — Multiphase turbulence as the origin of OH+, H2O+ and H3+ column density scatter in the local ISM
- **arXiv:** [2608.15633](https://arxiv.org/abs/2608.15633)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** turbulence (78.4), astrochemistry (77.0), galactic_ism_surveys (67.9)
- **Current keyword baseline:** NO
- **BM25 max:** 91.3
- **Semantic max:** 89.1
- **Abstract:** Observations of the reactive ions OH+, H2O+ and H3+ in the Galactic interstellar medium reveal large sight-line-to-sight-line scatter in their column densities, commonly interpreted as evidence for substantial variations in the cosmic-ray ionization rate (CRIR). We revisit this interpretation using high-resolution three-dimensional magneto-hydrodynamic simulations of the multiphase ISM with time-dependent chemistry for H, H2, H+ and electrons, building on the fiducial model of Godard et al. (2023). We find that a single CRIR of ~2 10^{-16} s^{-1}, together with standard Galactic-scale parameters, naturally produces broad column-density distributions for all three tracers in good agreement with the observed medians and percentile widths, with no fine tuning. Reaching this match requires that the post-processing of OH+, H2O+ and H3+ retain the time-dependent H2 field generated by the turbulent flow rather than assume chemical equilibrium: turbulence drives long-lived H2 enhancements in the unstable neutral medium where OH+ and H2O+ predominantly reside, and an equilibrium treatment under-predicts their columns substantially. H3+, which receives most of its column from denser CNM gas closer to equilibrium, is much less affected. Our results caution against interpreting sight-line-to-sight-line scatter as direct evidence for large CRIR fluctuations, and motivate a shift from independent 1D equilibrium analyses toward 3D dynamical frameworks when inferring ionization conditions in the ISM.

### [A] 78.3 — Observing Co-Located Neutral and Ionized Gas-Phase Iron Depletion in the Magellanic Clouds
- **arXiv:** [2608.12557](https://arxiv.org/abs/2608.12557)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (78.3), molecular_clouds (72.1), feedback_bubbles (65.1)
- **Current keyword baseline:** YES
- **BM25 max:** 93.7
- **Semantic max:** 90.7
- **Abstract:** Depletion is the observed phenomenon where gas-phase elemental abundances are reduced through accretion onto dust grains. We measure neutral gas-phase elemental abundances (S, Fe) in the Magellanic Clouds along 33 sightlines using high-resolution UV spectroscopy (HST/COS and HST/STIS), and compare them to ionized gas-phase abundances (S, Fe) adopted from the literature for six co-located H\,\textsc{ii} regions (with the furthest separation of $\lesssim3'$, 50 pc). Comparing S abundances show that S is minimally depleted in the H\,\textsc{ii} regions and surrounding diffuse ISM. However, we find that the gas-phase Fe abundances in H\,\textsc{ii} regions can be lower than those of the neighboring neutral ISM by 0.3 to 2 dex. This difference is likely an offset in the amount of Fe depleted into dust grains. As accretion of gas-phase Fe is likely not effective at the temperatures of the H\,\textsc{ii} regions, Fe depletion into solid form would have occurred in the dense atomic or molecular clouds prior to star formation. Stronger depletion in the H\,\textsc{ii} regions shows that Fe-bearing grains survive destruction in the first few million years following ionization. Our observations highlight that Fe depletion in H\,\textsc{ii} regions can be a useful tracer of Fe depletion in dense molecular clouds, which are challenging to observe directly via UV absorption.

### [A] 78.2 — VAPOLA - A multiyear, multiband polarization survey of AGNs and Sgr A* at millimeter wavelengths with ALMA II. Spectropolarimetric properties and their evolution from 2017 to 2023
- **arXiv:** [2608.14900](https://arxiv.org/abs/2608.14900)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (78.2), magnetic_fields (74.9), star_formation (70.3)
- **Current keyword baseline:** NO
- **BM25 max:** 60.8
- **Semantic max:** 90.7
- **Abstract:** We present a systematic analysis of the spectropolarimetric properties of a sample of 39 active galactic nuclei and Sagittarius A* observed with the Atacama Large Millimeter/submillimeter Array during five VLBI campaigns between 2017 and 2023. We characterize the compact cores in total intensity and polarization, focusing on the behavior or the linear polarization fraction (LP), electric vector position angle (EVPA), and Faraday rotation measure (RM) over time and spectral domains. We investigate both individual objects--such as M87, Sgr A*, 3C273, and 3C279--and ensemble properties of different source classes, including flat-spectrum radio quasars, BLLac objects, and other active galaxies. While total intensity and spectral index are generally stable on weekly timescales, polarization properties often exhibit strong variability, with significant day-to-day changes in LP, EVPA, and RM. Several sources display large EVPA rotations accompanied by variations in LP and RM, in some cases coinciding with flaring activity. We observe that the magnitude of RM increases with observing frequency for all sources for which we have reliable multi-band measurements, consistent with Faraday rotation arising in a magnetized sheath surrounding the relativistic jet, although an origin in the accretion flow--particularly in the case of Sgr A*--cannot be ruled out.

### [A] 78.1 — The Cross-Survey Decade: A Call to Action
- **arXiv:** [2608.19272](https://arxiv.org/abs/2608.19272)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.CO, astro-ph.GA
- **Top topics:** ism_methods_data (78.1), galactic_ism_surveys (67.8), star_formation (60.7)
- **Current keyword baseline:** NO
- **BM25 max:** 58.2
- **Semantic max:** 90.5
- **Abstract:** By 2027, three flagship wide-field surveys will be operating simultaneously from ground and space, observing overlapping sky and representing more than $6 billion in US and European public investment. Together they will produce overlapping petabyte-scale datasets across thousands of square degrees. This is a different class of challenge: the observations are no longer the bottleneck; realizing their joint scientific return now depends on shared computational infrastructure and coordination. Decades of community studies show that combining these datasets does more than improve precision. For science ranging from weak lensing to transient discovery and Galactic-plane astronomy, joint processing and analysis can unlock capabilities no single survey provides alone. Yet the required infrastructure -- joint pixel-level processing, cross-calibration and validation, interoperable data access, and the people to build and sustain it -- falls outside any single mission or institution's mandate. We issue a call to action for cross-survey science infrastructure, built around four pillars: (1) joint pixel-level processing and validation; (2) an AI-ready data substrate for scientific foundation models; (3) standardized, interoperable data access across surveys, democratizing participation in astrophysical discovery; and (4) dedicated personnel and career pathways. We outline concrete steps for policymakers, agencies, observatories, universities, the research community, and philanthropy, and argue that the moment to act is now, while foundational technical choices can still be aligned at a fraction of the cost of reconciling them later.

### [A] 78.1 — Radio Monitoring of Classical Novae using the ASKAP Variable and Slow Transients Survey
- **arXiv:** [2608.13330](https://arxiv.org/abs/2608.13330)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.SR
- **Top topics:** ism_methods_data (78.1), star_formation (70.8), feedback_bubbles (63.1)
- **Current keyword baseline:** YES
- **BM25 max:** 62.7
- **Semantic max:** 90.5
- **Abstract:** We present a search for radio emission from classical novae at 887.5 MHz using data from the Australian SKA Pathfinder Variable And Slow Transient (VAST) survey. We cross-matched 43 optically discovered classical novae that erupted between 2021 September and 2025 November within the 1200-square-degree Galactic survey footprint, and found three which show significant radio emission: V6598 Sgr, V1716 Sco, and V1723 Sco. To analyse their radio light curves, we use both thermal free-free and non-thermal synchrotron emission models. We fit the data using the Markov chain Monte Carlo (MCMC) method to constrain parameters, including the ejected mass and ejecta velocities for the thermal models, and mass-loss rate, explosion energy, wind velocity, and filling factor for the non-thermal model. All three novae show evidence of non-thermal synchrotron emission as the dominant emission mechanism at this frequency. We use a broken power law to describe the radial density structure of a non-uniform circumbinary material, which provides a better fit than a standard wind density profile. This strong early-time synchrotron emission is strong evidence of shock-driven particle acceleration, which may be related to detections of gamma-rays from all three novae as well. In contrast to earlier studies that used multi-frequency data to distinguish between emission models, our analysis is based on single-frequency radio light curves, which can still provide useful constraints on the dominant emission mechanism when interpreted with physically motivated models

### [A] 77.8 — Towards Quantum-Dot Detectors as Barcodes for Dark Matter Interactions
- **arXiv:** [2608.18204](https://arxiv.org/abs/2608.18204)
- **Primary category:** hep-ph
- **Categories:** hep-ph, astro-ph.CO, cond-mat.mes-hall, hep-ex, quant-ph
- **Top topics:** ism_methods_data (77.8), turbulence (54.0), star_formation (53.3)
- **Current keyword baseline:** NO
- **BM25 max:** 35.4
- **Semantic max:** 97.2
- **Abstract:** Quantum dots are tunable semiconductor nanocrystals that can be produced at industrial scales. We present the first ab initio calculation of the scattering of dark matter on electrons bound in quantum dots. The momentum-dependence of a quantum dot's electronic response depends on its morphology and on the dark matter mass, interaction operator, mediator coupling, and mediator mass. Therefore, the relative rates across an array of distinct quantum dot targets form a ``barcode'' that carries information about the nature of the dark matter interaction. We project the sensitivity of a detector concept in which a collection of independent target subunits, each loaded with silicon quantum dots of a particular morphology, are read out by Skipper CCDs. Given a future signal, this barcode could discriminate between interaction operators and mediator types. We quantify the discrimination power for a benchmark pair of models as a function of readout noise and exposure.

### [A] 77.4 — From Cluster Cores to the Low-Density Field: Strong Environmental Quenching of Galaxy Star Formation at Low Redshift
- **arXiv:** [2608.12301](https://arxiv.org/abs/2608.12301)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (77.4), feedback_bubbles (68.6), galactic_ism_surveys (63.7)
- **Current keyword baseline:** NO
- **BM25 max:** 57.9
- **Semantic max:** 89.6
- **Abstract:** We investigate how galaxy star formation activity depends on environment using a sample of 81,647 SDSS galaxies selected over $0.03\leq z\leq0.075$ and $9.7\leq\log_{10}(M_\star/h^{-2}M_\odot)\leq11.0$, including 18,426 members from 572 clusters in the \texttt{GalWCat19} catalog. We characterize environment in two complementary ways: (1) nearest-neighbor density for the full sample, and (2) clustercentric radius and host halo mass for \texttt{GalWCat19}. The sSFR distribution remains bimodal across all environments, with distinct quenched and star-forming components. As local density increases, the quenched component becomes more prominent, while the characteristic sSFR of the star-forming component decreases by approximately $0.29$--$0.35$ dex from the lowest- to highest-density classes. Within clusters, the quenched fraction decreases with increasing projected clustercentric radius, while the star-forming peak shifts by approximately $0.42$ dex toward lower sSFR from the outskirts to the inner cluster region. This extends the picture from previous studies, in which environmental trends are primarily associated with changes in the quenched fraction, by showing that galaxies remaining in the star-forming population also exhibit systematically suppressed sSFR in denser environments. The dependence on host halo mass is weaker and is most apparent among lower-stellar-mass galaxies in the inner cluster regions. By measuring the environmental quenching efficiency at fixed stellar mass, we find excess quenching in cluster environments beyond that expected from stellar-mass quenching alone. These results show that environment is associated not only with an increased probability of quenching, but also with suppressed star formation among galaxies that remain star forming, with local density and clustercentric radius showing the strongest associations.

### [A] 77.1 — A Radio-Bright Local Little Red Dot Analog
- **arXiv:** [2608.16200](https://arxiv.org/abs/2608.16200)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (77.1), galactic_ism_surveys (71.6), massive_star_formation (62.4)
- **Current keyword baseline:** NO
- **BM25 max:** 28.4
- **Semantic max:** 89.5
- **Abstract:** The James Webb Space Telescope revealed the existence in the early Universe ($z >$ 4) of large populations of little red dots (LRDs), compact red luminous sources that host rapidly growing supermassive black holes (SMBHs) surrounded by coeval nuclear starbursts. LRDs have defining properties, one of which is the absence of radio detections. LRDs could be radio-undetected because of their large distances. A way to investigate the radio properties of LRDs is to search for radio emission in their local analogs, the Local Little Red Dot (LLRD) galaxies at $z <$ 1 with analogous properties to LRDs. We report the radio continuum detection of the LLRD analog J204837.26${-}$002437.2 ($z$ = 0.4332, hereinafter J2048). This adds to the previous radio detection of two other LLRDs. However, with a flux density of 3.0$\pm$0.2 mJy at 3.0 GHz, J2048 is two orders of magnitude more radio luminous than the previous detections. The spectral index of $α$ = -0.39$\pm$0.04 is consistent with moderately optically-thick synchrotron emission. The radio luminosity of J2048 is $1.2 \times 10^{41}~ \mathrm{erg ~s^{-1}}$, in the lower end of the range defined by radio-loud giant elliptical galaxies and quasars of $L_R$ = $10^{41-46} ~\mathrm{erg ~s^{-1}}$. The expected radio luminosity of the SMBH associated with J2048 is estimated to be about an order of magnitude larger, suggesting that its radio luminosity could potentially be strongly dimmed. A cosmological ($z >$ 4) LRD with radio luminosity similar to that of J2048 would be detectable using the VLA with moderately long integrations.

### [A] 77.1 — Improved Cosmological Constraints from Morphology-Based Marked Correlation Functions
- **arXiv:** [2608.15083](https://arxiv.org/abs/2608.15083)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (77.1), turbulence (73.1), ism_methods_data (69.9)
- **Current keyword baseline:** NO
- **BM25 max:** 42.3
- **Semantic max:** 96.4
- **Abstract:** The cosmic web contains morphology-dependent information that is not fully captured by standard two-point statistics. We construct morphology-based marked correlation functions (MCFs) by assigning marks to halos according to the cosmic-web morphology identified with the \textsc{Nexus} algorithm. Using the \textsc{Kun} simulation suite, which spans 129 $w_0w_a$CDM cosmologies, we build Gaussian-process emulators for the MCFs as functions of cosmological parameters and tracer bias. We then apply the emulators to mock halo catalogues from the independent \textsc{Jiutian} simulation and perform a joint likelihood analysis to quantify the resulting cosmological constraints. We consider two marker choices: a discrete morphology marker and a continuous morphology strength marker. The continuous marker improves the Figure of Merit (FoM) by a factor of $\sim 8.6$ relative to the standard 2PCF and reduces the $1σ$ uncertainty on $σ_8$ by a factor of $\sim 5$. The discrete marker gives a more modest FoM improvement of $\sim 17\%$. We further test the impact of tracer selection by varying the halo mass threshold by a factor of $\sim 4.5$. Even for the lowest mass threshold, the continuous marker remains unbiased and achieves a FoM about $\sim 3.4$ times higher than that of the 2PCF alone. These results show that morphology-based MCFs, combined with simulation-based emulation, provide a useful framework for extracting additional cosmological information from large-scale structure surveys.

### [A] 76.9 — A NuSTAR Reflection-Spectroscopy Survey of Cygnus X-1
- **arXiv:** [2608.15902](https://arxiv.org/abs/2608.15902)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (76.9), astrochemistry (65.2), molecular_clouds (60.8)
- **Current keyword baseline:** NO
- **BM25 max:** 45.7
- **Semantic max:** 89.0
- **Abstract:** Relativistic-reflection measurements of Cygnus X-1 disagree on the extent of disk truncation and commonly infer supersolar iron abundances. We analyze a selected sample of 26 archival NuSTAR observations obtained between 2012 and 2024 using two configurations from one reflection-model family, with posterior modes sampled by preconditioned sequential Monte Carlo. In the baseline recovered modes, disk-surface ionization increases with photon index (Pearson r = +0.59), with state medians rising from log xi approximately 3.3 in the hard state to approximately 3.9 in the soft state. The corresponding free-emissivity fits give median inner radii of 6.6, 4.4, and 4.0 R_ISCO in the hard, intermediate, and soft states. Fixing q = 3 moves three of eight soft-state observations to the ISCO and one to 2.4 R_ISCO; four fixed-q fits have lower chi^2 than the sampled free-q solutions, showing that those runs missed higher-likelihood regions. The inferred radii are therefore model- and mode-dependent, and the spectra neither require nor exclude an ISCO disk or R_in greater than or approximately 20 R_ISCO. Baseline fitted abundances span A_Fe = 1.6-8.6, with a median of 4.9. Two observations separated by 7.2 hr yield A_Fe = 1.9 +/- 0.2 and 4.5 +/- 1.0, indicating that fitted abundance is not a direct composition measurement. Fixing A_Fe = 1.6 drives some densities toward the grid boundary and worsens the fits relative to A_Fe = 4.5. The wind parameters remain sensitive to the continuum, abundance, and orbital-phase sampling.

### [A] 76.6 — The VariableTNG project: mass-dependent regulation of galaxy morphology by baryonic feedback
- **arXiv:** [2608.19543](https://arxiv.org/abs/2608.19543)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (76.6), star_formation (63.1), galactic_ism_surveys (62.1)
- **Current keyword baseline:** NO
- **BM25 max:** 81.3
- **Semantic max:** 83.6
- **Abstract:** Galaxy morphology is shaped by both assembly history and baryonic processes, but their relative roles remain uncertain. We use the VariableTNG (VTNG) simulation suite to investigate how variations in baryonic feedback regulate galaxy morphology while keeping the initial conditions fixed. VTNG consists of cosmological magnetohydrodynamic simulations performed with the moving-mesh code {\sc AREPO}, varying eight parameters governing stellar and AGN feedback. At $z=1$, we characterize morphology using $κ_{\rm co}$, $v/σ$, and the axis ratio $c/a$. We find substantial morphological diversity across feedback models, with the dominant mechanism strongly dependent on stellar mass. For $M_\ast \lesssim 10^{11}\,{\rm M_\odot}$, morphology is primarily controlled by the supernova temperature $T_{\rm SN}$: larger $T_{\rm SN}$ delays early star formation, promotes a denser and more rotationally supported gas reservoir, and favours subsequent disc growth through in-situ star formation. At higher masses, morphology becomes increasingly sensitive to AGN feedback, particularly the quasar-mode coupling efficiency $ε_{\rm f,high}$. Higher $ε_{\rm f,high}$ suppresses early black hole growth, thereby weakening subsequent radio-mode feedback associated with gas depletion and loss of rotational support. The resulting morphology--mass relation is non-monotonic, with maximum rotational support at intermediate stellar masses. Our results demonstrate that baryonic feedback regulates galaxy morphology through distinct mass-dependent pathways, with stellar feedback dominating at lower masses and AGN self-regulation becoming increasingly important at the massive end.

### [A] 76.6 — Deep Earth imaging through neutrino and seismic tomography
- **arXiv:** [2608.15231](https://arxiv.org/abs/2608.15231)
- **Primary category:** hep-ex
- **Categories:** hep-ex, astro-ph.EP, hep-ph, physics.geo-ph
- **Top topics:** ism_methods_data (76.6), galactic_ism_surveys (61.5), feedback_bubbles (54.3)
- **Current keyword baseline:** NO
- **BM25 max:** 65.9
- **Semantic max:** 88.7
- **Abstract:** This article is a report on the Deep Earth Neutrino + Seismic Imaging and TomographY (DENSITY 2026) mini-workshop, held on 23--24 February 2026 in the Department of Earth and Climate Science at the Indian Institute of Science Education and Research (IISER), Pune. The workshop was jointly organised by IISER Pune and the Institute of Physics (IOP), Bhubaneswar. Researchers from Earth Sciences and Neutrino Physics participated in the workshop to explore multipronged approaches for studying the deep interior of the Earth. Since the participants came from diverse scientific disciplines (seismology, geochemistry, mineral physics, and neutrino physics), the programme featured a series of overview talks introducing all participants to the basic concepts of each field and highlighting how these concepts may be applied to the study of the deep Earth.

### [A] 76.5 — Automated Assignment and Prediction of Molecules in Astronomical Line Surveys Using Machine-Learning-Based Chemical Embeddings
- **arXiv:** [2608.18221](https://arxiv.org/abs/2608.18221)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (76.5), astrochemistry (73.5), ism_methods_data (73.2)
- **Current keyword baseline:** YES
- **BM25 max:** 100.0
- **Semantic max:** 91.9
- **Abstract:** Modern radio telescopes generate vast amounts of observational data, offering valuable insights into the molecular composition of interstellar sources. Identifying the molecules within these datasets typically involves time-consuming and labor-intensive manual analysis. This paper presents an automated method for assigning molecules in interstellar line surveys. The algorithm operates in two main stages. First, it automatically determines key parameters of the data, including excitation temperature, line width, and source velocity. Next, it assigns the observed spectral peaks by evaluating the spectroscopic match of the molecular candidates along with analyzing their chemical relevance to the interstellar source. The chemical relevance is determined by leveraging machine-learning-based molecular embedding techniques to analyze the regions of chemical space occupied by the observed species. Following the line assignment, this information is then used to generate new molecular candidates that occupy the same regions of chemical space. These newly generated species serve as promising targets for further investigation in the observational data. The algorithm was validated on spectral line surveys of the dark molecular cloud TMC-1 and the star-forming region IRAS 16293-2422B. In both cases, it identified at least 67 molecular species, accounting for over 90 percent of the analyzed line intensity, in 17 minutes or less while maintaining a high level of accuracy.

### [A] 76.5 — CLASSY. XV. Kinematics and Spatial Distributions of Outflows in Local Highly Star-Forming Galaxies
- **arXiv:** [2608.12482](https://arxiv.org/abs/2608.12482)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (76.5), astrochemistry (74.0), star_formation (70.3)
- **Current keyword baseline:** NO
- **BM25 max:** 77.0
- **Semantic max:** 88.5
- **Abstract:** Star-forming galaxies drive massive outflows that play an important role in galaxy evolution by regulating feedback and influencing the dynamics of surrounding media. Measuring galactic outflow rates is essential for quantifying feedback efficiency and the amount of mass, momentum, and energy deposited into the circumgalactic medium. In this paper, we examine 17 galactic outflows from the CLASSY survey with radiative transfer modeling of UV absorption lines presented in M. Huberty et al. (2024), to study their spatial distributions and kinematic properties. We study the SiII, SiIII, and SiIV ionization states that trace the cool and warm phases of the outflows and find that SiII traced winds generally behave differently than the warmer SiIII and SiIV traced winds. We derive the mass, momentum, and energy loading factors, which we find scale inversely proportional to stellar mass. We find that our measurements of the mass and momentum loading factors are in agreement with the hydrodynamic FIRE-2 simulations. We model the velocity profiles of the winds, with profiles reaching a maximum velocity of 620 km/s on average, in agreement with hydrodynamic simulations from CGOLS. We also investigate the relationship between outflow properties and the age of the stellar population from SED fitting. We find that outflows associated with young star forming regions are more likely to have a column density dominated by cooler gas and have mass outflow rates which decrease with radius.

### [A] 76.4 — The Stellar Population of NGC 346 in the Small Magellanic Cloud with JWST
- **arXiv:** [2608.17875](https://arxiv.org/abs/2608.17875)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (76.4), feedback_bubbles (66.9), massive_star_formation (65.6)
- **Current keyword baseline:** NO
- **BM25 max:** 84.1
- **Semantic max:** 83.6
- **Abstract:** NGC 346 is a massive star-forming region located at a distance of $\sim$62 kpc, in the Small Magellanic Cloud (SMC). Due to its low metallicity (Z $\sim$1/5 Z$_{\odot}$), it is an ideal environment to study star formation and stellar population analogues to those at Cosmic Noon. In this work, we produce a combined JWST NIRCam and MIRI photometric catalogue of NGC 346. We characterise different stellar populations in the region: the upper main sequence (UMS), red giant branch (RGB), and red clump (RC), as well as pre-main sequence (pre-MS) stars and young stellar objects (YSOs). We performed point-spread function (PSF) weighted photometry in 11 wavelength bands across NIRCam and MIRI and utilised multiple colour-magnitude-diagrams to identify the various stellar populations in the field. Our final photometric catalogue of NGC 346 comprises 249,519 unique sources, including 2,024 UMS stars, 2,755 RGB stars and 742 RC stars. In addition, we identified 6,274 candidate pre-MS stars, 7,350 candidate YSOs and 23,819 IR-excess sources. Combining these three categories, we characterised 1,583 strong and 3,761 likely pre-MS/YSO candidates. By utilising the F115W-F200W vs F115W-F187N colour-colour diagram, we found 239 non-spurious sources with Pa$α$ excess, indicating accretion and star formation in NGC 346. Using JWST NIRCam and MIRI observations, we produced the deepest catalogue to date of the star formation region NGC 346 in the near- and mid-IR range (1-21$~μ$m). Our catalogue and characterisations of the young and old populations will provide the basis for detailed follow-up studies.

### [A] 76.4 — JWST Whirlpool Galaxy Treasury: Mid-Infrared Emission in M51 and its Relation to Gas Column and Star Formation
- **arXiv:** [2608.16802](https://arxiv.org/abs/2608.16802)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** atomic_ism (76.4), galactic_ism_surveys (75.3), molecular_clouds (73.6)
- **Current keyword baseline:** YES
- **BM25 max:** 97.2
- **Semantic max:** 94.2
- **Abstract:** Using JWST/MIRI imaging of M51 in eight broadband filters, we investigate correlations of mid-infrared emission from polycyclic aromatic hydrocarbons (PAHs) and dust continuum with molecular, atomic, and ionized gas traced by CO(1-0), HI, and Pa-alpha, respectively. In molecular gas-dominated regions, PAH-dominated filters (F560W, F770W, F1130W, F1280W) exhibit near-linear correlations with CO(1-0) at 40 pc scale, indicating that PAHs are well-mixed with gas and experience relatively constant radiation field intensities. The F1500W, F1800W, and F2100W dust continuum-dominated filters show shallower slopes with CO(1-0), reflecting contributions from star-forming regions with high radiation field intensities. This is reinforced by the near-linear scaling between F2100W and Pa-alpha. PAH-dominated bands do not show this linear trend with Pa-alpha, likely due to their destruction in ionized regions. F1000W behaves similarly to PAH bands in its correlations with CO(1-0) and Pa-alpha. Modeling mid-infrared emission with an empirical decomposition into gas- and star-formation-associated components shows that PAH-dominated filters receive comparable contributions from both, while the relative contribution associated with the Pa-alpha template increases toward longer wavelengths, reaching $\sim$75% in F2100W. These results demonstrate that mid-infrared simultaneously traces the gas column and star formation, but with a systematic wavelength-dependent shift in what drives the correlations: PAHs being more gas-tracing and dust-continuum reflecting star formation. Lastly, considering both HI and H$_2$ at 440 pc resolution, we find a tight, linear relation between $Σ_{HI+H_2}$ and PAH-dominated filters. Although most of our coverage is in H$_2$-dominated regions, we note similar observations with HI, suggesting that PAHs are also well-mixed with atomic gas.

### [A] 76.2 — SPURS: Massive Stars, Dense Gas, and Ly$α$ Escape in GN-z11 at $z = 10.6$
- **arXiv:** [2608.12699](https://arxiv.org/abs/2608.12699)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (76.2), molecular_clouds (73.3), feedback_bubbles (70.9)
- **Current keyword baseline:** NO
- **BM25 max:** 68.9
- **Semantic max:** 88.2
- **Abstract:** We present ultra-deep {\it JWST} spectroscopy of GN-z11 ($z=10.6$) obtained through the SPURS Cycle 4 Large Program, providing the deepest rest-UV view yet obtained of a galaxy at $z>10$. GN-z11 was previously found to be nitrogen-enhanced with detectable Ly$α$. The SPURS spectrum reveals P-Cygni stellar wind features and broad He II emission that are jointly reproduced by stellar population models incorporating very massive stars (VMS; $>100\,M_\odot$) at low metallicity and young ages ($\lesssim3$ Myr). We also detect a broad ($\rm FWHM=1670$ km s$^{-1}$) component to N IV] $\lambda1486$, now seen in several nitrogen emitters, potentially arising from dense WN-like winds or LBV-like outbursts associated with a population of VMS in a dense environment, though an AGN-driven wind cannot be excluded. In either scenario, this broad component may trace the gas producing GN-z11's nitrogen enhancement. Rest-UV absorption lines reveal a fast ($\sim500$~km~s$^{-1}$), highly ionized outflow and a negligible neutral gas covering fraction. We resolve the weak Ly$α$ emission (EW=5.6 Å, $f_{\rm esc,Lyα}=2.7$\%), finding a broad red wing (44\% of flux at $>500$ km s$^{-1}$) that should experience reduced IGM damping wing suppression and help explain Ly$α$ visibility at $z>10$. Fine-structure O I* $\lambda1304$ emission indicates dense neutral gas near a subset of the ionizing sources, which may also scatter Ly$α$ to the large observed velocities. The weak low-ionization absorption favors a picture in which this dense neutral gas is confined to a compact nuclear region. Together, these results are consistent with a rapid burst of star formation building up the dense nuclear regions and surrounding clusters in GN-z11.

### [A] 75.8 — The first comprehensive spectral and timing study of the ultra-compact X-ray binary 4U 1812-12 with NICER and NuSTAR
- **arXiv:** [2608.16841](https://arxiv.org/abs/2608.16841)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (75.8), ism_methods_data (67.1), molecular_clouds (64.1)
- **Current keyword baseline:** NO
- **BM25 max:** 47.8
- **Semantic max:** 87.7
- **Abstract:** The source 4U 1812-12 is a persistent, weakly variable low-mass X-ray binary containing a neutron star. The source was observed by NICER between 2019 and 2021 and, more recently, by NuSTAR in 2025. During the NICER and NuSTAR observations, the source was detected in a hard spectral state with a bolometric luminosity of $\sim 1.90\times 10^{36}$ ergs s$^{-1}$. Its $3-70$ keV NuSTAR spectrum is characterized by a soft thermal emission from the disc, a hard Comptonized emission from the corona, and its reflection from the accretion disc. The NuSTAR energy spectrum exhibits the clear presence of disc reflection features, fitted using a self-consistent relativistic reflection model {\tt relxill}. Our reflection modeling indicates a moderately ionized accretion disc (log\:$ξ\sim2.72$) extending close to the neutron star surface ($R_{in}\lesssim 1.72\:R_{ISCO}$), and viewed through a small inclination angle ($i\sim 25$ degrees). Assuming that the magnetic field ($B$) truncates the disc, we found $B\lesssim 2.54\times 10^{8}$ G, comparable to the typical values observed for NS LMXBs. The $1.0-9.5$ keV NICER spectra are also characterized by a soft thermal component and a dominant hard Comptonized component. During NICER observations, the disc temperature exhibits a small variation within $\sim 0.69-0.84$ keV. In contrast, the power law photon index, $Γ$, exhibits a large variation of $\sim 0.8-1.5$, implying a substantial change in the Comptonized emission. Moreover, NICER timing analysis reveals broadband aperiodic variability with significant QPO-like features at $0.379\pm 0.008$ Hz and $0.724\pm 0.025$ Hz, having fractional rms amplitudes of $2.9\pm 0.6\%$ and $4.1\pm 0.5\%$, respectively.

### [A] 75.8 — 3D Radiative Transfer of Lyman-series Lines with SKIRT
- **arXiv:** [2608.12527](https://arxiv.org/abs/2608.12527)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (75.8), feedback_bubbles (65.6), molecular_clouds (60.5)
- **Current keyword baseline:** NO
- **BM25 max:** 68.8
- **Semantic max:** 87.6
- **Abstract:** Context. High-resolution X-ray spectroscopy and polarimetry provided by XRISM and IXPE offer new diagnostics of the geometry and kinematics of photo-ionised plasmas around compact objects. Interpreting reprocessed X-ray emission in such systems requires full three-dimensional radiative transfer (3D RT) including photon-ion interactions. Aims. We extend the Monte Carlo (MC) RT code SKIRT by implementing the Lyman-series lines of H-like ions, enabling self-consistent modelling of resonance scattering, radiative recombination, and polarisation of these lines in X-ray photo-ionised plasmas. Methods. We implemented Lyman-series transitions (up to $n=10$) for ions with $Z=$1--30, including fine-structure splitting and linear polarisation in resonance scattering. Two channels for the production of the Lyman-series lines (resonance scattering and radiative recombination) are considered. Results. The implementation reproduces analytical expectations and shows good agreement with Cloudy. The SKIRT simulations naturally capture RT effects such as P Cygni profiles and line-profile distortion in optically thick media, which are inaccessible to the conventional 1D RT codes commonly used in X-rays. In 3D geometries, we find that anisotropic illumination and velocity fields significantly modify the Lyman series line ratios and profiles, all of which are observable with XRISM. Conclusions. The extended version of SKIRT provides a powerful framework for interpreting X-ray line spectra and polarisation from photo-ionised plasmas. It is particularly suited for constraining the geometry and velocity structure in the vicinity of compact objects in the XRISM and IXPE era.

### [A] 75.5 — Diffuse HI emission in the circumgalactic medium of NGC891 and NGC4565 - III: azimuthal profiles
- **arXiv:** [2608.19186](https://arxiv.org/abs/2608.19186)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (75.5), molecular_clouds (63.1), feedback_bubbles (59.0)
- **Current keyword baseline:** NO
- **BM25 max:** 71.2
- **Semantic max:** 94.4
- **Abstract:** Diffuse HI emission in the circumgalactic medium (CGM) of NGC891 and NGC4565 has been previously shown to trace an inflow along minor axes pointings and to co-rotate with the HI disk along major axes pointings out to ~100 kpc (Das2020b,Das2024a). To obtain a 360$^\circ$ view of the inner neutral CGM ($\rm < 25 kpc$ for NGC891, $\rm < 30 kpc$ for NGC4565), we perform deep stare observations with the Green Bank Telescope (GBT) along the off-axes, 45$^\circ$ between principal axes, achieving a 5$σ$ column density sensitivity of $1.1-1.2 x 10^{17} \rm cm^{-2}$ over a 20 kms$^{-1}$ velocity width. While detecting HI emission in the inner CGM with single-dish telescopes is common, separating the true CGM emission from disk contamination is extremely challenging and has so far been largely unsuccessful. To achieve that, we compare our single-dish detections to deep interferometric maps from the Westerbork Synthesis Radio Telescope (WSRT) HALOGAS survey, and improve upon our previous methods by incorporating velocity offset corrections and channel-wise brightness-temperature scaling. We find that $30-38$ % and $18-28$ % of the emission detected by the GBT cannot be explained by WSRT in NGC891 and NGC4565, respectively, implying a true CGM detection. There is $4-6$ ($3-7$) times more HI along the off-axes than major (minor) axes, nullifying the common assumption of azimuthal symmetry of the neutral CGM. The velocity profile of the diffuse inner CGM suggests a lagged co-rotation with the HI disk in both galaxies. This exercise illustrates the power of deep observation and careful cross-instrument comparisons to characterize the diffuse HI in the CGM.

### [A] 75.5 — Polarization of GRB standard X-ray afterglow and its detection prospects by eXTP
- **arXiv:** [2608.15503](https://arxiv.org/abs/2608.15503)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** magnetic_fields (75.5), turbulence (60.5), ism_methods_data (59.8)
- **Current keyword baseline:** NO
- **BM25 max:** 66.4
- **Semantic max:** 82.2
- **Abstract:** The polarization signatures of Gamma-ray Burst (GRB) afterglows serve as a powerful diagnostic tool for studying their environments and jet physics. This work systematically investigates the X-ray (2--8~keV) polarization properties of standard GRB afterglows and assesses their detectability with the Polarimetry Focusing Array aboard the enhanced X-ray Timing and Polarimetry (eXTP) satellite. A Morris global sensitivity analysis is first conducted to identify the dominant parameters, which are then assigned observationally motivated probability distributions. In particular, the isotropic energy, half-opening angle, and initial Lorentz factor are sampled jointly via a Gaussian copula to reproduce the empirical Ghirlanda and Liang correlations. Monte Carlo simulations of $10^{3}$ afterglows are performed and validated against the observed 10~keV flux distributions of a selected Fermi--Swift sample (K--S $p = 0.29$ at $10^{3}~\mathrm{s}$ and $p = 0.18$ at $10^{4}~\mathrm{s}$). The simulations yield an overall polarization event rate of $\lesssim 1.5\%$ for standard GRB X-ray afterglows with eXTP/PFA, reflecting the intrinsically low polarization produced by a random magnetic field confined to the shock plane. The optimal detection window occurs near the jet break at late times, when the PD peaks. For exceptionally luminous events such as GRB~221009A, however, the PD remains above the MDP over the full interval $10^{3}$--$10^{6}~\mathrm{s}$, demonstrating that eXTP/PFA can capture nearly the entire polarization evolution for such rare, bright bursts.

### [A] 75.4 — Diversity of Ionized Gas Structures in Nearby Metal-poor Dwarf Galaxies
- **arXiv:** [2608.19667](https://arxiv.org/abs/2608.19667)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** astrochemistry (75.4), galactic_ism_surveys (69.6), ism_methods_data (65.3)
- **Current keyword baseline:** NO
- **BM25 max:** 53.3
- **Semantic max:** 87.2
- **Abstract:** We investigate whether optical and far-infrared [O III] emission from nearby metal-poor dwarf galaxies can be represented by a homogeneous one-zone ionized-gas model with a single electron temperature and density. Our sample comprises five galaxies from the Herschel Dwarf Galaxy Survey: HS1222+3741, SBS0335-052E, POX186, Haro11, and IZw18. We combine galaxy-integrated or nearly galaxy-integrated [O III] 4363 and 5007 measurements from Seimei/KOOLS-IFU observations and published or archival spectroscopy with Herschel/PACS [O III] 88um measurements. Because [O III] 4363 is not detected in HS1222+3741, the analysis is based on the remaining four galaxies. SBS0335-052E and Haro11 lie near or slightly beyond the low-density boundary of the one-zone diagnostic. Their nominal line ratios favor effective densities of ne<1cm-3, while conservative treatment of the uncertainties allows values up to 40 and 10cm-3, respectively. These remain substantially below densities inferred from independent diagnostics. By contrast, POX186 and IZw18 show no significant discrepancy between the optical--far-infrared [O III] and low-ionization optical diagnostics. Additional optical and ultraviolet diagnostics show that inferred densities can span several orders of magnitude within a galaxy. Representative two-zone models reproduce the [O III] 4363, 5007, and 88um emission in SBS0335-052E and Haro11 by combining relatively dense gas with cooler, low-density gas. The low-density component contributes approximately 61% and 72% of the 88um luminosity, but only 14% and 23% of the 5007 luminosity, respectively. These solutions are not unique and may represent a broader unresolved distribution of gas conditions. Our results show that temperatures and densities inferred from integrated one-zone analyses are effective quantities and that similar diagnostic discrepancies can arise in nearby metal-poor galaxies.

### [A] 75.3 — Nascent Embedded-protostar Survey in Taurus (NEST) I: Protostellar Multiplicity
- **arXiv:** [2608.12186](https://arxiv.org/abs/2608.12186)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** star_formation (75.3), molecular_clouds (70.2), massive_star_formation (67.5)
- **Current keyword baseline:** YES
- **BM25 max:** 69.4
- **Semantic max:** 84.3
- **Abstract:** We present new ALMA 0.9 mm and VLA 9 mm observations in the Taurus Molecular Cloud (TMC) of 25 protostellar systems, containing 40 protostars, observed at 0.3" (~20 au) resolution. Within separations of 18-10,000 au, the ALMA/VLA-observed Taurus sample has a multiplicity fraction (MF), defined as the fraction of systems with at least one companion, of 0.50 +/- 0.07, and a companion fraction (CF), defined as the average number of companions per system, of 0.58 +/- 0.20. To build a more complete census of protostellar multiplicity in this region, we supplement the observed sample with 24 protostars (12 protostellar systems and 5 additional companions associated with systems we observed) previously identified through archival infrared or ALMA observations. Together, these 64 individual protostars (37 systems) define our Taurus+ sample, for which we measure higher values of 0.53 +/- 0.06 and 0.72 +/- 0.19 for the MF and CF, respectively. These multiplicity statistics in the TMC are notably higher than those reported in the more clustered star-forming regions of Orion and Perseus at the ~3-4 sigma level, suggesting that Taurus may preserve a larger fraction of primordial multiples. The separation distributions in our samples show populations of both close and wide multiples, but a deficit at intermediate separations of 200-300 au. This pattern may suggest two distinct formation pathways: close binaries (<200 au) arising primarily from disk fragmentation, and wide multiples (>1000 au) from core fragmentation.

### [A] 75.2 — Identifying Cost-Favorable Locations for Cosmic Explorer
- **arXiv:** [2608.19114](https://arxiv.org/abs/2608.19114)
- **Primary category:** physics.ins-det
- **Categories:** physics.ins-det, astro-ph.IM
- **Top topics:** ism_methods_data (75.2), star_formation (55.2), molecular_clouds (49.6)
- **Current keyword baseline:** NO
- **BM25 max:** 34.3
- **Semantic max:** 86.9
- **Abstract:** Cosmic Explorer (CE) is a proposed next-generation gravitational-wave observatory that aims to extend our gravitational-wave vision to the edge of the observable universe. With a foundation of technology proven by the National Science Foundation's Laser Interferometer Gravitational-Wave Observatory (LIGO), CE will observe black holes and neutron stars across cosmic time, explore the nature of extreme matter with high fidelity, and probe the nature of gravity and fundamental physics. CE's reference design consists of two widely separated L-shaped detectors to be located in the conterminous United States, one with 20 km arms and one with 40 km arms. As of 2026, CE is in its design and site evaluation phase, with plans to begin observing in the early 2040s together with the Einstein Telescope in Europe. The size of CE observatories---up to an order of magnitude larger than the 4 km LIGO observatories---presents a significant challenge for identifying suitable candidate sites where CE will achieve its science goals, be built within cost boundaries, attract and retain a workforce, and align with community values. In this paper, we report on the design and use of a Python package, the Cosmic Explorer Location Search (CELS) package, to identify cost-favorable sites for CE. For a specified detector location and L-shaped geometry in the conterminous United States, CELS estimates site-preparation costs associated with excavation, land clearing, and land acquisition, while accounting for the scientific effects of detector tilt, arm length, and arm opening angle. After describing the package's methods, we present results for a national-level cost and positioning analysis that complements a recent national suitability analysis. We also discuss how future improvements to CELS will allow deeper, more local studies as the Cosmic Explorer team narrows its list of potential locations.

### [A] 75.1 — Investigating the properties of nearby young moving groups using GaiaDR3
- **arXiv:** [2608.18596](https://arxiv.org/abs/2608.18596)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.EP, astro-ph.GA
- **Top topics:** star_formation (75.1), astrochemistry (70.6), massive_star_formation (69.7)
- **Current keyword baseline:** YES
- **BM25 max:** 39.5
- **Semantic max:** 93.9
- **Abstract:** Moving groups, which are gravitationally unbound collections of stars spread over large portions of the sky, pose challenges to their identification. Analyzing the three-dimensional spatial motion of stars is one method to identify their members. Despite several studies in the past, a reliable and conclusive catalog of moving group stars is currently lacking. Our objective is to present a most recent and updated catalog of nearby young moving group (NYMG) candidates in the solar neighborhood and investigate their properties using updated science data from the Gaia Data Release 3 (DR3). We searched for candidates of twelve NYMGs within a distance of 150 pc using Gaia DR3. To determine the membership, we employed the Bayesian algorithm BANYAN-Sigma. We compiled a total list of 3,153 NYMG candidates, of which 1,651 were new candidates. We also assessed the credibility of the literature defined 'Good-box' criterion with the latest comprehensive catalog of NYMGs from our study. We homogeneously estimated the ages of the NYMG candidates using Gaia DR3 photometry data. The analysis revealed that our NYMG candidates display a large scatter on the CMDs resulting in a large range of estimated ages from isochrones. Additionally, we conducted an infrared (IR) excess analysis to identify disk candidates among our final sample. Our spectral energy distribution (SED) analysis found 51 stars with IR excess. We present a largely inclusive list of all the NYMG candidates within 150 pc of Solar neighbourhood using Gaia DR3. The wide range of ages obtained from isochrone fitting underscores the need for more robust age analysis techniques to accurately determine the ages of NYMG members. The presence of IR excess in the 51 stars confirms the existence of disks indicating that they could be potential candidates for exoplanet detections.

### [B] 74.9 — Large eROSITA X-ray sources as 2MRS galaxy groups
- **arXiv:** [2608.17732](https://arxiv.org/abs/2608.17732)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (74.9), massive_star_formation (62.7), astrochemistry (61.6)
- **Current keyword baseline:** NO
- **BM25 max:** 57.6
- **Semantic max:** 93.6
- **Abstract:** We aim to exploit the large area coverage, good sensitivity, and low instrumental background of eROSITA to detect the faint surface brightness emission of galaxy groups from the Two Micron All Sky Survey Redshift Survey (2MRS). Using the data from eROSITA-DE Data Release 1, including images, exposure maps, and local background maps, we performed a wavelet decomposition of image mosaics in the 0.6--2.3 keV band at angular scales of 1/8-16'. We adopted 8-16' scales for source detection and 2-4' scales to improve catalog purity. A novel identification method based on the ranked partial Hausdorff distance fully exploits the X-ray image and group membership information. Random catalogs were used to control match purity, and the identification threshold was chosen to maximize the catalog size at a fixed purity. {We present a catalog of 619 X-ray galaxy groups with 80% purity, and define subsamples with 90% and 97% purity. Bright sources closely match the AXES-2MRS catalog (which is based on ROSAT All Sky Survey data analysis on spatial scales of 12-24'). The X-ray luminosity function of our groups agrees with previous studies down to 5.e41 erg/s. Using dynamical mass estimates, we find that the X-ray counterpart completeness for groups with >=4 members exceeds 60% for masses >2e13 Msun. We modeled the 2MRS group catalog and justify the inclusion of two-member groups in the identification. This study demonstrates that large X-ray sources on spatial scales relevant for cosmological studies of baryonic distributions can be reliably detected and identified using nearby galaxy group catalogs.

### [B] 74.9 — AT 2020afjz (TSS2020a): The First Fast Extragalactic Transient Discovered by TESS
- **arXiv:** [2608.17242](https://arxiv.org/abs/2608.17242)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.CO
- **Top topics:** ism_methods_data (74.9), star_formation (72.2), feedback_bubbles (69.3)
- **Current keyword baseline:** NO
- **BM25 max:** 30.9
- **Semantic max:** 90.3
- **Abstract:** We report the discovery of AT 2020afjz (TSS2020a): the first hour-scale extragalactic transient discovered in optical wavelengths whose complete evolution -- from explosion onset to decay -- is temporally resolved, and the first such transient discovered by TESS. AT 2020afjz was identified as a $>10σ$ detection in the pilot HiLaTS program run within the TESSELLATE Sky Survey, which blindly searches for transient phenomena in TESS data with the TESSELLATE pipeline. Through cross-matching with legacy imaging, we associate it with DES J042144.37$-$383311.3, a member of an interacting galaxy pair at $z_{\rm phot}=0.67^{+0.07}_{-0.10}$. While AT 2020afjz is similar in duration and brightness to GRB afterglows, it exhibits a slow rise time of $\sim1$ hr and lasts for only 2.4 hr above the half-max brightness; modeling the TESS light curve with VegasAfterglow finds that it is best described as either an on-axis "dirty-fireball" or off-axis orphan afterglow. Each of these rare classifications hinge upon a non-detection at gamma-ray energies, but as Fermi-GBM was Earth-occulted at the time of explosion, AT 2020afjz's gamma-quiet nature cannot be definitively confirmed. Regardless, AT 2020afjz demonstrates TESS's power to discover fast extragalactic transients, and heralds a new population awaiting discovery with TESSELLATE.

### [B] 74.9 — Diverse ionized gas conditions in a dynamically hot, interacting galaxy at $z = 9.31$ revealed by JWST/NIRSpec IFU
- **arXiv:** [2608.16996](https://arxiv.org/abs/2608.16996)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (74.9), astrochemistry (70.6), star_formation (63.4)
- **Current keyword baseline:** YES
- **BM25 max:** 65.1
- **Semantic max:** 93.6
- **Abstract:** We present a spatially and spectrally resolved study of an interacting galaxy, Gz9p3 at $z=9.31$, using the James Webb Space Telescope NIRSpec/G395H IFU observation with high-spectral resolution ($R\approx 2700$) mode. Gz9p3 consists of two sub-regions (`core' and `tail'), which show stark contrast in their physical properties. The HII regions in the core are characterized by high electron density ($n_{e}\gtrsim2900$ cm$^{-3}$), low gas-phase metallicity ($0.25$ dex below the mass-metallicity relation), and yet relatively low specific star formation rate (sSFR) among the system. On the other hand, the tail exhibits low electron density ($n_{e}<70$ cm$^{-3}$), relatively high gas-phase metallicity that is consistent with the mass-metallicity relation, and high sSFR. The integrated spectrum thus shows the properties inbetween these two regions. No evidence of ordered rotation in ionized gas is found, suggesting that Gz9p3 is a dynamically hot system. Finally, we find ionized gas outflows characterized by the secondary [OIII]5007 line component throughout most of the system. The outflow velocity is below the escape velocity, making Gz9p3 one of the first galactic systems experiencing a galactic fountain. Overall, our findings indicate that this system is in a phase in which the pristine gas is falling efficiently into the core, diluting the gas metallicity, and enhancing star formation and outflows after the galaxy interaction.

### [B] 74.7 — Impact of Upstream Clumpiness on Supernova Remnant Forward Shock Evolution in Molecular Cloud Environments
- **arXiv:** [2608.17477](https://arxiv.org/abs/2608.17477)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** turbulence (74.7), molecular_clouds (69.7), feedback_bubbles (64.0)
- **Current keyword baseline:** NO
- **BM25 max:** 84.9
- **Semantic max:** 86.2
- **Abstract:** Supernova remnants (SNRs) are widely considered to be the primary accelerators of Galactic cosmic rays. In recent years, detailed observations have significantly progressed for young SNRs interacting with molecular clouds, a prime example being RX J1713.7-3946. When molecular clouds are clumpy, their impact can affect not only radiation properties but also shock wave propagation. Therefore, a quantitative understanding linking observational quantities with the ambient medium structure is highly required. In this study, we perform three-dimensional hydrodynamic simulations to model a molecular cloud with an inhomogeneous density structure driven by supersonic turbulence and subsequent SNR formation. To investigate various pre-supernova environments, we systematically vary the medium clumpiness by replacing gas below a threshold number density with a low-density hot gas, quantifying the relationship between the forward shock velocity and the volume filling factor of the high-density clumps. As a result, we find that at an elapsed time of 1000 yr-a typical age for a young SNR-the forward shock can evolve consistently with the fast shock velocity measured in RX J1713.7-3946, provided that the clump volume filling factor is approximately 10% or less. Considering that hadronic gamma-ray emission originates exclusively from the clumpy, high-density gas, our findings suggest that the total energy of cosmic-ray protons in RX J1713.7-3946 is higher than previously estimated, amounting to at least several percent of the typical supernova explosion energy.

### [B] 74.7 — The deepest color-magnitude diagrams for the benchmark open cluster NGC 2437 from Gaia and VVVX
- **arXiv:** [2608.14514](https://arxiv.org/abs/2608.14514)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (74.7), astrochemistry (61.5), massive_star_formation (60.3)
- **Current keyword baseline:** NO
- **BM25 max:** 55.7
- **Semantic max:** 86.2
- **Abstract:** Deep photometry of Galactic star clusters provides one of the most powerful tools for determining their physical properties. In particular, in low Galactic latitude regions that suffer from heavy extinction and crowding. NGC2437 is the most extended star cluster in the near-IR footprint of the VVV Extended Survey (VVVX), covering more than one degree on the sky. We aim to characterize its physical properties using Gaia DR3 in the optical and the VVVX in the near-IR. We use Gaia DR3 proper motions to select NGC2437 members in order to make optical and near-IR color-magnitude and color-color diagrams. We further exploited the newly constructed VVVX deep stack images to obtain the deepest near-IR color-magnitude diagram currently available for this cluster. We estimate the main physical parameters for NGC2437, including the mean parallax of 0.608 mas and PMs (-3.85, 0.41) mas/yr. The mean reddening E(J-Ks) = 0.059 mag and extinction of A_k = 0.034 mag for the cluster field, with no significant differential reddening spread. A distance modulus of 11.08 mag is estimated, equivalent to a distance of 1644 pc. This places NGC2437 at z=115 pc above the Galactic plane and at a galactocentric distance of 9.24 kpc. We measure the cluster structural parameters, obtaining a core radius of 10.79 arcmin. The estimated total absolute magnitudes are Mk = -4.91 mag and Mv = -3.70 mag. The cluster mean age is 350 Myr, using PARSEC-COLIBRI isochrones for solar metallicity. We measure a binary fraction of 28.6%. We also discuss the implications of the revised cluster parameters for the nearby open cluster NGC2425, the planetary nebula NGC2438, and the evolved OH/IR source OH231.8+04.2. The VVVX deep stacks increase the Ks photometric depth by 1.6 mag, nearly doubling the detected point sources and enabling significantly improved studies of stellar populations throughout the southern Galactic plane.

### [B] 74.6 — Early Planet Formation in Embedded Disks (eDisk). XXIV: Systematic Investigation of Disk Structures based on Visibility Analysis
- **arXiv:** [2608.19364](https://arxiv.org/abs/2608.19364)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.EP, astro-ph.GA
- **Top topics:** ism_methods_data (74.6), feedback_bubbles (69.3), molecular_clouds (69.1)
- **Current keyword baseline:** YES
- **BM25 max:** 68.0
- **Semantic max:** 86.7
- **Abstract:** The dust continuum emission from young protostellar disks encodes key information about their mass distribution and early evolution, yet uniform high-resolution comparative studies remain limited. We present a systematic uv-plane analysis of parametric intensity models applied to ALMA Band-6 (1.3 mm) observations of 23 disks (19 protostellar systems with 4 being in binary) from the eDisk sample, spanning Gaussian profiles to power-law cores with exponential tails (PLCT), including asymmetric extensions. Gaussian models generally fail to reproduce the centrally peaked emission and extended outer structure observed in most disks, whereas the PLCT framework provides a significantly improved description of radial brightness profiles. Incorporating azimuthal asymmetries further reduces residuals in 15 of 17 inclined disks, indicating that departures from axisymmetry are common at early stages. Only two disks, L1489 IRS and Oph IRS63, exhibit clear gap and ring substructures, while most appear smooth at the spatial resolution and sensitivity of our observations. These systems are among the most evolved in the sample, and the absence of flat-spectrum sources limits the evolutionary range probed, {suggesting that the detection of prominent gaps and rings is not common} in the earliest phases of disk evolution. Using a uniform definition of disk radius based on the 95\% enclosed flux, we find a positive correlation with stellar mass, $R_{\rm disk} \propto M_{\star}^{1.5 \pm 0.1}$, with disks in binary systems systematically smaller than those around isolated protostars. While the models capture overall morphology and large-scale asymmetries, distinguishing intrinsic structures from radiative transfer effects in optically thick regions remains challenging.

### [B] 74.4 — Tracing Lyman alpha escape in the CRISTAL-02 galaxy at z~5.3
- **arXiv:** [2608.19439](https://arxiv.org/abs/2608.19439)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (74.4), feedback_bubbles (69.2), astrochemistry (67.3)
- **Current keyword baseline:** NO
- **BM25 max:** 64.3
- **Semantic max:** 85.9
- **Abstract:** Aim. We investigate the mechanisms regulating Lyman-alpha (Ly-a) escape in the star-forming galaxy CRISTAL-02 at z~5.3. The galaxy hosts five distinct clumps, with Clumps A and B suggested as potential active galactic nuclei (AGN) candidates. We study how AGN or star formation activity influences the spatial distribution and escape of Ly-a emission. Methods. Using VLT/MUSE Ly-a and JWST/NIRSpec IFU H-a and H-b observations, complemented by NIRCam UV imaging, we constructed spatially matched emission-line maps. We derived flux, line-ratio, and extinction maps, together with spatially resolved Ly-a escape fractions and ionizing photon production efficiencies. Results. Ly-a emission extends preferentially along the [C ii] outflow direction, while H-a and UV trace the galactic disk. Clumps A and B show contrasting properties: Clump A, with lower dust attenuation, exhibits enhanced Ly-a/H-a ratios and a higher Ly-a escape fraction, whereas Clump B shows stronger H-a and UV emission but suppressed Ly-a. These results suggest that Ly-a escape is influenced by outflows, dust attenuation, and local gas conditions. Conclusions. We present spatially resolved measurements of the Ly-a escape fraction and ionizing photon production efficiency in a galaxy at z~5.3, highlighting the role of feedback-driven gas clearing and anisotropic outflows in shaping Ly-a emission. The evidence favors an outflow, but the available data cannot uniquely distinguish between AGN- and star formation-driven feedback. Future spatially resolved Ly-a, H-a, and [C ii] observations will be crucial for identifying the dominant feedback mechanism.

### [B] 74.4 — Tracking nonlinear solar-wind dynamics over three solar cycles using Wind observations
- **arXiv:** [2608.17037](https://arxiv.org/abs/2608.17037)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, cond-mat.stat-mech, nlin.CD, physics.space-ph
- **Top topics:** turbulence (74.4), star_formation (66.6), ism_methods_data (63.9)
- **Current keyword baseline:** NO
- **BM25 max:** 65.1
- **Semantic max:** 85.9
- **Abstract:** The solar wind is a turbulent, weakly collisional plasma characterized by non-Gaussian fluctuations, long-range correlations, and multifractal dynamics. We investigate the long-term evolution of these properties using hourly proton density measurements obtained directly by the Wind spacecraft over 1995--2025. The use of a single-spacecraft dataset provides an independent test of previous results derived from the multi-spacecraft OMNI database. The three components of the nonextensive $q$-triplet are estimated within one-year sliding windows shifted monthly: $q_{stat}$ from the distribution of density increments, $q_{rel}$ from the decay of the autocorrelation function, and $q_{sens}$ from the multifractal spectrum. Their mean values, $q_{stat}=1.71\pm0.07$, $q_{rel}=4.62\pm0.52$, and $q_{sens}=-0.45\pm0.27$, confirm the persistent presence of heavy-tailed statistics, slow relaxation, and weakly chaotic multifractal dynamics. The parameters nevertheless exhibit distinct temporal variability and relationships with solar activity. The Fourier spectrum of $q_{stat}$ contains a dominant period of approximately $10.1$ years, while its correlation with the sunspot number is positive and moderate ($r=0.611$). Correlation and mutual-information analyses show that $q_{stat}$ is primarily associated with solar proxies, whereas $q_{sens}$ displays stronger relationships with geomagnetic indices and $q_{rel}$ exhibits weaker dependencies. An anomalous enhancement of $q_{stat}$ around 2004 coincides with a sequence of intense interplanetary disturbances, although possible effects related to Wind's orbital transition must also be considered. These findings demonstrate the robustness of the nonextensive description and show that the statistical and dynamical properties of solar wind proton density show evidence of modulation by solar activity.

### [B] 74.2 — The Mass Function of Neutron Stars from Core-Collapse Supernova Simulations
- **arXiv:** [2608.18198](https://arxiv.org/abs/2608.18198)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (74.2), ism_methods_data (53.0), massive_star_formation (53.0)
- **Current keyword baseline:** NO
- **BM25 max:** 51.8
- **Semantic max:** 80.5
- **Abstract:** Using the mapping between progenitor core structure and the gravitational mass of neutron stars derived from sophisticated 3D supernova simulations, we determine the theoretical mass distribution of neutron stars at birth and compare it with neutron star mass function measurements. In the process, we explore the effects of islands of black hole formation and subsequent mass accretion. We show that supernova theory can explain the observed neutron star mass function from its lower-mass peak near $\sim$1.35 $M_{\odot}$ to its higher-mass tail. Moreover, the lower predicted kick speeds expected during the birth of lower-mass neutron stars and the higher expected kick speeds expected on average for higher mass neutron stars both sculpt the observed mass function in desired directions. The upshot of all these influences is to imprint upon the measured neutron star mass function features that reflect the varied physics of both neutron star origins and the neutron-star/black-hole dichotomy. Very approximately, we derive a black hole birth fraction of $\sim$21\%. In summary, we suggest that supernova theory can now be used to explain, however provisionally, various measured attributes of the population of compact objects and that an era of productive engagement between supernova theory and observation is at hand.

### [B] 74.2 — X-ray thread/Nonthermal Radio Filament associations: Evidence for Interstellar Magnetic Reconnection
- **arXiv:** [2608.14830](https://arxiv.org/abs/2608.14830)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, physics.space-ph
- **Top topics:** molecular_clouds (74.2), galactic_ism_surveys (68.7), magnetic_fields (60.9)
- **Current keyword baseline:** NO
- **BM25 max:** 72.2
- **Semantic max:** 85.7
- **Abstract:** Nonthermal radio filaments (NTFs), first discovered at 20-centimeter wavelength more than four decades ago, are among the most enigmatic structures at the Galactic Center. They still defy a clear explanation. These striking narrow features trace intense magnetic fields and often stand in bold contrast to the Galactic plane. Recent discoveries have revealed surprising associations: some NTFs align well with X-ray threads that seem to exhibit Fe He-$α$ emission. Here, I present preliminary results from an ongoing, collaborative, multi-wavelength study aimed at understanding the origins of these filaments, focusing on testing the magnetic reconnection scenario of these associations and shedding new light on the high-energy processes and magnetic phenomena operating under extreme conditions at the heart of our Galaxy.

### [B] 74.2 — Voltage-to-temperature calibration of the High Altitude THz Solar telescope acquisition system
- **arXiv:** [2608.12137](https://arxiv.org/abs/2608.12137)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.SR
- **Top topics:** ism_methods_data (74.2), star_formation (58.5), molecular_clouds (53.8)
- **Current keyword baseline:** YES
- **BM25 max:** 39.0
- **Semantic max:** 85.6
- **Abstract:** The THz range has been under-explored for solar astronomy, mainly due to technological limitations. Only recently, a few new telescopes, such as the High Altitude Terahertz Solar (HATS) photometer, have been monitoring the solar activity in this range of the spectrum. This paper presents the experimental characterization and voltage-to-temperature calibration of the HATS acquisition system. HATS uses a Golay cell for capturing the incoming radiation, modulated by a 20 Hz fork chopper. The amplitude of the signal is then obtained at predetermined time intervals by applying a windowing function and an FFT to the signal. To characterize this acquisition system, a blackbody calibrator, with temperatures varying from 100 to 500 C (373.15 K to 648.15 K), was used as a THz source, and two signal recovery methodologies were compared: sinusoidal curve fitting and FFT combined with six windowing functions (rectangular, Hamming, Hann, Barlett, Blackman, and Flat Top). Our quantitative results demonstrate high linearity in the system's response over the input source's temperature range, with the Hamming window achieving the highest precision, yielding a Root Mean Square Error (RMSE) of 15.48 and a calibration temperature-to-voltage factor of 10.32 +- 0.13 mV/K. In contrast, the Bartlett window presented the highest error (RMSE 16.02). The choice of windowing function had only a minor effect on the calibration factors, which ranged from 10.32 to 10.43 mV/K, all within the experimental uncertainties. Beyond solar photometry, the signal modulation and windowing concepts established here are highly applicable to other fields requiring high-sensitivity thermal detection, such as industrial pyrometry for high-temperature manufacturing, environmental monitoring of atmospheric water vapor, and the development of medical imaging systems based on Terahertz radiation for non-invasive tissue analysis.

### [B] 74.0 — Observations of Disrupted CME Material Falling Back Into the Low Corona
- **arXiv:** [2608.17951](https://arxiv.org/abs/2608.17951)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** molecular_clouds (74.0), star_formation (63.7), feedback_bubbles (60.0)
- **Current keyword baseline:** NO
- **BM25 max:** 45.5
- **Semantic max:** 92.5
- **Abstract:** We present an empirical study of a disrupted CME, parts of which fall back to the Sun, using observations from SOHO, STEREO-A, and SDO. At UT 18:00 on 2024 August 16, a slow CME is overtaken by a faster CME. A leg of the second CME carries part of the slower CME out with it, resulting in an unusually well-defined flux rope leg for this CME. This second CME is observed in radio by the VLA, with Faraday rotation measurements showing a clear magnetic flux rope signature. A strong response is also later seen when the radio-observed line of sight enters the CME leg enriched by material from the disrupted CME. Outside this leg, the rest of the disrupted CME simply disappears and is replaced by a large number of small jet-like downflows. We see clear evidence of this plasma falling back to the low corona in EUV images from SDO, roughly 6-17 hours after the CME is disrupted, with an inferred downward velocity of V=-30 km/s. There is a clear temperature dependence, with the downflows seen first in the 211 bandpass, followed successively by responses at 193, 171, and 304. The downflows are much slower than would be expected for a ballistic descent, so we model the downflows using a kinematic drag model. In the 304 bandpass, coronal rain activity is triggered by the downflowing CME material, suggesting that downflows from the upper corona could be contributing to coronal rain more generally.

### [B] 74.0 — RIOJA. Environmental Effects on Stellar Populations and Ionized Gas in a Protocluster at $z=7.88$
- **arXiv:** [2608.16343](https://arxiv.org/abs/2608.16343)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** atomic_ism (74.0), astrochemistry (73.2), feedback_bubbles (72.3)
- **Current keyword baseline:** NO
- **BM25 max:** 65.9
- **Semantic max:** 90.4
- **Abstract:** Protoclusters in the epoch of reionization provide key laboratories for investigating how environment shapes early galaxy formation and evolution, and may also have contributed to cosmic reionization. We analyze 23 member galaxies of A2744-z7p9OD, a protocluster at $z=7.88$, using JWST/NIRCam and NIRSpec to investigate their stellar population properties, rest-frame UV sizes, and ionized-gas properties. We also quantify the internal structure of A2744-z7p9OD using the projected distance to the most massive galaxy ($D_{\rm YD4}$), and to the nearest neighbor ($D_{\rm nei}$), as global and local environmental indicators, respectively. Stellar mass, SFR on a 100 Myr timescale, dust attenuation, and galaxy size show significant correlations ($p<0.05$) with $D_{\rm YD4}$, but not with $D_{\rm nei}$, suggesting that these properties are primarily linked to the global protocluster structure. The member galaxies also show a large galaxy-to-galaxy variation in R23 ($=\log{(([\mathrm{O}\text{\textsc{iii}}]λ\lambda4960,5008\rmÅ+[\mathrm{O}\text{\textsc{ii}}]λ\lambda3727,3730\rmÅ)/\rm{H}β)}$), implying inhomogeneous chemical enrichment in the protocluster environment. O32 ($=\log{([\mathrm{O}\text{\textsc{iii}}]\lambda5008\rmÅ/[\mathrm{O}\text{\textsc{ii}}]λ\lambda3727,3730\rmÅ)}$) correlates with $D_{\rm YD4}$, indicating that the core region is characterized by low-ionization gas. Together with the non-detection of Ly$α$ emission, the possible neutral-gas reservoir traced by ALMA [C{\sc ii}]~$158μ$m emission, and evidence for high-column-density neutral hydrogen in the core, this suggests a neutral-gas-rich protocluster core where the current escape of ionizing photons may be suppressed, even in a overdense environment during the EoR.

### [B] 73.9 — A High-Resolution Spectroscopic Survey of Directly Imaged Companion Hosts: III. Characterization of the Cold Imaged Planet Hosts AF Lep A and $ε$ Indi A
- **arXiv:** [2608.15912](https://arxiv.org/abs/2608.15912)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** astrochemistry (73.9), ism_methods_data (68.1), massive_star_formation (58.1)
- **Current keyword baseline:** YES
- **BM25 max:** 47.3
- **Semantic max:** 92.4
- **Abstract:** JWST has enabled the measurement of carbon, oxygen, and sulfur abundances in the atmospheres of directly imaged planets. Interpretation of these abundances from a planet formation standpoint requires the corresponding abundances for the host star. In this work, we present detailed characterizations of the cold imaged planet hosts AF Lep A and $ε$ Indi A using high-resolution Gemini/GHOST spectra. We derive the atmospheric parameters $T_{\rm eff}$ and $\log{g}$ using two different approaches, revealing differences in $T_{\rm eff}$ up to $\sim260\,$K. The derived parameters are subsequently incorporated in measurement of 16 elemental abundances (C, O, Na, Mg, Si, S, K, Ca, Sc, Ti, Cr, Mn, Fe, Ni, Zn, Y) and several abundance ratios. Utilizing both the spectral fit and the equivalent width methods, we find solar C/O, C/S and O/S ratios ($<1.5σ$) for AF Lep A and $ε$ Indi A. We compare our measured abundances and their ratios with those of the planets AF Lep b and $ε$ Indi Ab, with the elevated abundances for the planets relative to their host stars strongly indicating formation by core-accretion pathways.

### [B] 73.8 — Millimeter and sub-millimeter characterization of polymers used for infrared filters in high-sensitivity cryogenic microwave telescopes
- **arXiv:** [2608.18793](https://arxiv.org/abs/2608.18793)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (73.8), molecular_clouds (66.3), turbulence (55.4)
- **Current keyword baseline:** NO
- **BM25 max:** 47.0
- **Semantic max:** 92.3
- **Abstract:** Vacuum windows and infrared filters are important transmissive optical components in millimeter receivers, as they hold out the atmosphere and reduce radiative loading on cold stages, thereby improving cryogenic performance. However, the complex optical properties of the materials commonly used for windows and filters are poorly characterized, particularly in-band and in the sub-millimeter regime. The absorption and scattering properties of these materials are becoming increasingly important for designing high-sensitivity millimeter instruments, as their loosely constrained properties are one of the greatest sources of uncertainty remaining in noise modeling. We report the absorption in the millimeter and sub-millimeter regime of nylon 6, nylon 6/6, PTFE and polyethylene (both bulk HDPE and foam HDPE used in radio transparent filter stacks). Additionally, we report the relative power scattered out of the main beam by these materials from 90 to 330 GHz, measured in free space by a robot-enabled scanning vector network analyzer.

### [B] 73.8 — OH Line Detections in Southern Galaxies of the IRAS Revised Bright Galaxy Sample
- **arXiv:** [2608.14473](https://arxiv.org/abs/2608.14473)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (73.8), feedback_bubbles (70.9), astrochemistry (65.3)
- **Current keyword baseline:** NO
- **BM25 max:** 52.0
- **Semantic max:** 92.2
- **Abstract:** We present a systematic study of OH main-line emission and absorption in 186 southern galaxies from the IRAS Revised Bright Galaxy Sample, using archival MeerKAT snapshot data. OH features are detected in 38 galaxies, including eight with OH maser emission (three new) and 30 showing OH absorption, mostly unreported previously. Four absorption systems exhibit weak OH emission superposed on strong absorption. OH-emitting regions are generally more compact than the associated radio continuum. Most absorption profiles are well fit by two Gaussian components (1667 and 1665 MHz), with an average integrated line ratio of $\sim$1.5. LIRGs show an OH emission detection rate of ~13\%, versus significantly lower rates in non-LIRGs. For sources with radio continuum flux densities >20 mJy, OH absorption detection rates reach ~36\% (LIRGs) and ~27\% (non-LIRGs), while no OH absorption features were detected among sources with lower radio continuum flux densities. This suggests that sufficient background continuum is likely an important factor for the detection of OH absorption. Detected OH emitters follow the empirical $L_{\rm OH}$--$L_{\rm FIR}$ relation, consistent with far-infrared pumping, while non-detections show upper limits below the relation. No significant differences are found between OH absorbers and non-detections in infrared luminosity or radio continuum compactness. Stacked spectra of non-detections reveal no significant OH features, suggesting that sensitivity and orientation alone do not fully explain the absence of absorption. In contrast, mid-infrared colors (e.g., W2--W3) and q_TIR differ between the two populations. OH absorption galaxies occupy an intermediate regime in L_HCN/L_CO between OH megamasers and non-detections, implying that OH absorption detectability is linked to dense molecular gas conditions, with extreme star formation potentially suppressing its occurrence.

### [B] 73.8 — High-Energy Neutrinos from Supernova Shock Breakouts in Circumstellar Media: Light Curves, Spectra, and Contribution to the Extragalactic Neutrino Background
- **arXiv:** [2608.13680](https://arxiv.org/abs/2608.13680)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (73.8), ism_methods_data (69.0), turbulence (59.1)
- **Current keyword baseline:** NO
- **BM25 max:** 48.9
- **Semantic max:** 86.3
- **Abstract:** Enhanced mass loss from core-collapse supernova (SN) progenitors shortly before explosion appears to be common, creating a compact, optically thick circumstellar medium (CSM) at $\sim10^{14}-10^{15}$ cm. We derive an analytic description of the light curves and spectra of high-energy neutrinos emitted by nonrelativistic SN shock breakouts through such CSM, as a function of shock velocity and CSM parameters, accounting for the evolution of the hydrodynamic structure and the electromagnetic (EM) spectrum as the shock transitions from being radiation-mediated to collisionless. This evolution determines the time-dependent neutrino production efficiency, the maximum proton/neutrino energy, and the pair-production optical depth. A significant fraction of the neutrino energy is typically emitted within a few days of explosion, during breakout and before the EM light curve peak, with $1-100$ TeV neutrinos carrying $\approx10\%$ of the energy of shock-accelerated protons. The escape of high-energy photons ($>1$~GeV) is suppressed by pair-production for compact CSM configurations. If enhanced mass losses are common, and assuming that shock-accelerated protons carry $\approx10\%$ of the collisionless shock energy, CSM SN breakouts may significantly contribute to the observed high-energy neutrino background, without overproducing a corresponding high-energy gamma-ray background. SNe producing $>1$ neutrino events in a $1\left(10\right){\rm km^2}$ detector are expected at a rate of $\sim0.05\left(1\right){\rm yr^{-1}}$.

### [B] 73.8 — Recycled Gas Dominates the Metal-rich Fuel of Supermassive Black Holes
- **arXiv:** [2608.12462](https://arxiv.org/abs/2608.12462)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (73.8), galactic_ism_surveys (67.5), massive_star_formation (67.1)
- **Current keyword baseline:** NO
- **BM25 max:** 58.0
- **Semantic max:** 85.2
- **Abstract:** Understanding the origin and chemical properties of gas accreted by supermassive black holes (SMBHs) is essential for linking black hole growth to galaxy evolution. Using a suite of 30 high-resolution cosmological zoom-in simulations, we investigate the chemical properties of gas accreted onto SMBHs in massive galaxies with stellar masses of $10^{10.9-11.9}\,\rm M_\odot$ and black hole masses of $10^{8.5-9.7}\,\rm M_\odot$ at $z=0$. By tracing the full cosmological histories of individual gas particles, we identify their origins and enrichment pathways. The accreted gas is classified into four categories: ``early'' gas accreted during the early assembly phase of the main halo, ``external'' gas originating from other galaxies or subhalos, ``recycled'' gas enriched through stellar evolution processes within the primary galaxy, including asymptotic giant branch (AGB) winds and supernova ejecta, and ``smooth'' gas accreted from the intergalactic medium. We find that recycled gas dominates the accretion budget and is already metal rich at early epochs. Gas from other origins typically undergoes gradual chemical enrichment within the galactic environment prior to black hole accretion. The mean abundance ratios show only weak redshift evolution and are broadly compatible with the high metallicities inferred for quasar broad-line regions. Our results suggest that metal-rich gas supply to SMBHs arises naturally from cosmological galaxy evolution and stellar recycling.

### [B] 73.6 — Detection of Aliphatically Deuterated Aromatic Hydrocarbons in the Large Magellanic Cloud 30 Doradus Star-Forming Complex
- **arXiv:** [2608.14984](https://arxiv.org/abs/2608.14984)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** astrochemistry (73.6), massive_star_formation (66.9), molecular_clouds (62.4)
- **Current keyword baseline:** YES
- **BM25 max:** 58.1
- **Semantic max:** 92.0
- **Abstract:** The unidentified infrared (IR) emission (UIE) bands at 3.3, 6.2, 7.7, 8.6, 11.3 and 12.7 micron are ubiquitously seen in a wide variety of astrophysical environments. While the exact assignment of these UIE bands remains controversial, they are generally ascribed to C--H and C--C stretching and bending vibrations of aromatic hydrocarbon molecules. Here, based on observations made with the Near Infrared Spectrograph (NIRSpec) and the Mid Infrared Instrument (MIRI) aboard the James Webb Space Telescope (JWST), we report that the UIE emitters in the 30 Doradus star-forming complex in the Large Magellanic Cloud (LMC) are deuterated and have an appreciable amount of aliphatic content. The spatially resolved NIRSpec and MIRI spectra of 30 Doradus reveal a widespread detection of the 3.4 and 6.85 micron emission features attributed to aliphatic C--H stretch and deformation, respectively, as well as the 4.65 micron feature attributed to aliphatic C--D stretch. Notably, the 6.85 micron feature exhibits three complex substructures at ~6.83, 6.86 and 6.88 micron that have never been reported before.

### [B] 73.5 — The Inbound Gas and Dust Evolution of Interstellar Comet 3I/ATLAS from Optical Spectroscopy and Multi-band Photometry
- **arXiv:** [2608.18371](https://arxiv.org/abs/2608.18371)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.GA
- **Top topics:** astrochemistry (73.5), molecular_clouds (73.4), star_formation (73.1)
- **Current keyword baseline:** YES
- **BM25 max:** 52.5
- **Semantic max:** 91.8
- **Abstract:** Interstellar objects (ISOs) provide direct constraints on the composition and evolution of extrasolar planetary systems. As the third confirmed ISO, comet 3I/ATLAS offers a rare opportunity to study pristine material from another star system. We present a systematic multi-band monitoring campaign conducted from 2025 July to September. To minimize systematic uncertainties, we utilized a homogeneous dataset of SDSS $g', r', i', z_s$ and Johnson-Cousins $BVR$ imaging obtained with MuSCAT3/4 on the 2.0-m Faulkes Telescopes and the 1.5-m Maidanak telescope. We employed a novel multi-aperture technique providing a robust, distance-independent characterization of the coma, alongside optical spectroscopy from SALT and the Nordic Optical Telescope. 3I/ATLAS exhibited a stable reddish color with no significant secular variation during its inbound journey. Spectroscopic analysis reveals carbon-chain depletion, with CN as the only prominent molecular emission. Coma morphology, analyzed via azimuthal averaging and rotational gradient filters, shows a persistent sunward jet at a position angle of $\sim$280$^{\circ}$, indicating sustained and localized outgassing from a high-latitude active region. Light-scattering modeling demonstrates that the observed colors and polarization are consistent with dense aggregates of organic matter and silicate minerals, while water ice sublimation remained insufficient to alter the optical properties. The stability of the coma structures and the homogeneous nature of our dataset indicate that 3I/ATLAS underwent a steady activation phase, preserving a volatile-rich but carbon-chain-poor composition. This characterization points to an object formed in a distinct protoplanetary environment and provides a definitive record of its pre-perihelion evolution.

### [B] 73.5 — Quasar Impostors: Two Extremely UV-Bright ($M_{\rm UV}\approx-23.5$) Reionisation-Epoch Galaxies Powered by Very Massive Stars
- **arXiv:** [2608.18212](https://arxiv.org/abs/2608.18212)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** ism_methods_data (73.5), feedback_bubbles (70.1), astrochemistry (66.0)
- **Current keyword baseline:** NO
- **BM25 max:** 50.6
- **Semantic max:** 91.9
- **Abstract:** The extreme bright end of the galaxy UV luminosity function during reionisation remains poorly constrained, particularly where the galaxy and quasar luminosity functions overlap and source classification becomes ambiguous. We present JWST/NIRSpec and ALMA Band-6 observations of J1450-0144 ($z=6.627$) and J1429-0104 ($z=6.796$), two $M_{\rm UV}\simeq-23.5$ sources originally classified as faint quasars by SHELLQs. NIRSpec reveals blue UV continua, strong P Cygni profiles in N V, Si IV, and C IV, broad He II $\lambda1640$ emission with rest-frame equivalent widths of $8.8\pm1.2$ and $3.7\pm1.1$ Å, respectively, and narrow nebular lines, reclassifying both as extremely UV-luminous galaxies. Standard population-synthesis models cannot simultaneously reproduce the strong He II and wind features, whereas models incorporating very massive stars (VMS; $M\gtrsim100\,M_\odot$) with dedicated wind prescriptions can. These models favor a star-formation duration of 2-4 Myr for J1450-0144, with a broader allowed range for J1429-0104, stellar masses of $\log(M_\star/M_\odot)\approx9.2$-$9.9$, and star-formation rates of $\simeq300$-$540\,M_\odot\,{\rm yr}^{-1}$. Under the same VMS wind models, equivalent-width diagnostics imply $M_{\rm up}\gtrsim225\,M_\odot$ for J1429-0104, while J1450-0144 lies beyond even the $M_{\rm up}=475\,M_\odot$ grid. ALMA detects luminous [C II] 158 $μ$m emission in both systems, with $L_{\rm [CII]}\approx0.8$ and $4.1\times10^{9}\,L_\odot$, respectively. J1429-0104 additionally shows bright dust continuum, with both [C II] and dust offset by $\sim5.4$ kpc from its UV emission. These sources demonstrate that VMS can power some of the most UV-luminous galaxies at cosmic dawn and show that source classifications, and hence the inferred demographics of both galaxies and quasars in the crossover regime, need revisiting.

### [B] 73.4 — Infrared Lines from Sterile-Neutrino Transition Magnetic Moments at JWST
- **arXiv:** [2608.17679](https://arxiv.org/abs/2608.17679)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (73.4), galactic_ism_surveys (61.5), feedback_bubbles (52.1)
- **Current keyword baseline:** NO
- **BM25 max:** 51.0
- **Semantic max:** 91.8
- **Abstract:** We investigate infrared line signatures from radiatively decaying sterile-neutrino dark matter using publicly available JWST/NIRSpec IFU blank-sky observations. The main signal considered is the sterile-to-sterile transition $N_1\to N_2γ$, induced by the transition magnetic dipole coefficient $d_{NNγ}$, with $m_1>m_2$. In contrast to ordinary two-photon decays of axion-like or Majoron-like particles, the observed photon energy is not fixed by the full dark matter mass, but by the small mass splitting $Δm=m_1-m_2$. Thus, a keV-scale sterile-neutrino dark matter state can generate an eV-scale infrared photon line in the JWST band. We construct a $χ^2$-based line-search analysis using the NIRSpec IFU $\rm F170LP$-$\rm G235M$ blank-sky data toward $\rm GN\text{-}z11$, modelling the smooth continuum with a cubic spline and including the Milky Way halo decay flux. In the absence of a significant excess, we derive projected limits on $d_{NNγ}$ and on the decay width $Γ_{N_1\to N_2γ}$ for $0.1~{\rm eV}\lesssimΔm\lesssim1~{\rm eV}$. For a sterile component saturating the dark matter abundance, the strongest sensitivity reaches $d_{NNγ}\lesssim7\times10^{-14}~{\rm GeV}^{-1}$ and $Γ_{N_1\to N_2γ}\lesssim10^{-25}~{\rm s}^{-1}$. We also include a minimal anomalous-Majoron benchmark, $ω\toγγ$, obtaining JWST sensitivity to $λ_{ωγγ}\sim10^{-11}$-$10^{-9}~{\rm GeV}^{-1}$ for $m_ω\sim0.6$-$1~{\rm eV}$.

### [B] 73.4 — Resolving Nearby Supermassive Black Holes with the Black Hole Explorer
- **arXiv:** [2608.16983](https://arxiv.org/abs/2608.16983)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.IM
- **Top topics:** magnetic_fields (73.4), ism_methods_data (70.2), galactic_ism_surveys (65.8)
- **Current keyword baseline:** NO
- **BM25 max:** 59.0
- **Semantic max:** 82.3
- **Abstract:** Recent Event Horizon Telescope results have demonstrated unique and transformative science in gravitational physics and black hole astrophysics enabled by event-horizon-scale imaging of supermassive black holes (SMBHs). Nevertheless, the angular resolution of current ground-based very long baseline interferometry (VLBI) arrays limits such studies to only two sources, precluding systematic investigations of horizon-scale emission across a nearby SMBH population. The proposed Black Hole Explorer (BHEX), a millimeter/submillimeter space VLBI mission, would overcome this limitation by delivering substantially higher angular resolution. Here, we present a series of simulated observations to assess a population of nearby horizon-scale targets accessible with BHEX. Based on a recently developed SMBH number density model, we find that BHEX could infer black hole masses for ~70-90 sources from size measurements, constrain magnetic field structures through linear polarization imaging for ~20-30 sources, and resolve black hole shadows for ~20-25 sources. Targeted observations of ~50 nearby SMBHs are expected to yield measurements for ~30 source sizes and ~10 shadows and linear-polarization patterns. These projections are supported by detailed imaging simulations of general relativistic magnetohydrodynamic (GRMHD) models for eleven nearby SMBHs. Together, our results highlight BHEX as a powerful facility for revealing the demographics of SMBH properties across diverse accretion states, radio loudness, host galaxy environments, and viewing geometries.

### [B] 73.3 — Serendipitous discovery of an almost-dark galaxy in the Virgo Cluster
- **arXiv:** [2608.19326](https://arxiv.org/abs/2608.19326)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (73.3), massive_star_formation (59.9), star_formation (56.4)
- **Current keyword baseline:** NO
- **BM25 max:** 38.9
- **Semantic max:** 79.5
- **Abstract:** Analogues of extreme Local Group galaxies with very low surface brightness and large effective radii must exist elsewhere, still hidden due to current detection limits. We report the serendipitous discovery of a low-mass almost-dark galaxy TTT J1237327+143535 in the Virgo Cluster, observed using the Two-meter Twin Telescope at the Teide Observatory. TTT J1237327+143535 has a central surface brightness of $27.9 \pm 0.2 \, \mathrm{mag arcsec}^{-2}$ in the $g'$-band, an effective radius of $0.9 \pm 0.1 \, \mathrm{kpc}$, and a total stellar mass of $(2.2 \pm 0.4) \times 10^6 \, \mathrm{M_\odot}$. Its effective radius and absolute magnitude are similar to those of galaxies And XXI and And XXIII. The discovery of this extremely low surface brightness, extended, low-mass galaxy suggests the existence of a significant population of almost-dark galaxies in the Virgo Cluster. An in-depth analysis of the Next Generation Virgo Cluster survey, as well as upcoming Rubin Data Releases and the 10-year Rubin Legacy Survey of Space and Time are expected to reveal large samples of this extreme galaxy population, which offers insights on galaxy formation in extreme conditions.

### [B] 73.2 — EON-SII: Design of a transportable picosecond stellar intensity interferometer for compact-star astrophysics
- **arXiv:** [2608.17444](https://arxiv.org/abs/2608.17444)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (73.2), ism_methods_data (72.8), feedback_bubbles (67.6)
- **Current keyword baseline:** NO
- **BM25 max:** 38.3
- **Semantic max:** 91.4
- **Abstract:** Stellar intensity interferometry (SII) measures correlations in photon-arrival fluctuations recorded by telescopes observing bright celestial sources. It can resolve angular scales far smaller than those accessible to a single optical telescope and is largely insensitive to atmospheric turbulence. After the first demonstration of SII on Sirius in 1956, Hanbury Brown and Twiss used the technique to measure the diameters of 32 stars. More recently, VERITAS, MAGIC, H.E.S.S., and CTAO's LST-1 have revived the method, although observations remain restricted to bright targets because of their optical design, optimized for gamma-ray astrophysics, rather than SII. We present EON-SII, the design and performance of a two-telescope intensity interferometer intended to extend the SII technique to compact targets at magnitudes of about V=8.5 up to V=10.7. Each transportable telescope has a 4-m diameter mirror, approximately 9m2 collecting area, an actively aligned 18-panel primary mirror, and Cassegrain optics specified to concentrate at least 90% of the light within 3 arcsec. A fibre-free spectrograph covers 400-550 nm at R~7000-8000 and is designed to provide of order 1000 statistically independent spectral channels.

### [B] 73.2 — H-$α$ Integral Carrington Synoptic Maps Produced by NSO/NISP
- **arXiv:** [2608.13812](https://arxiv.org/abs/2608.13812)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** magnetic_fields (73.2), astrochemistry (58.7), galactic_ism_surveys (57.5)
- **Current keyword baseline:** NO
- **BM25 max:** 58.8
- **Semantic max:** 91.5
- **Abstract:** Monitoring long-term chromospheric activity and large-scale solar structures like filaments and plages is critical for understanding solar magnetic cycles and predicting space-weather events. While photospheric magnetic fields are routinely mapped, a consistent, global reference for chromospheric structures has been absent from H-$α$ observations. This technical report provides a comprehensive description of the methodology used to construct the NSF Global Oscillations Network Group (GONG) H-$α$ Integral Carrington Synoptic Maps from full-disk observations. We outline the processing pipeline developed to transform these observations into 720 x 360 pixel maps binned by Carrington longitude and sine(latitude) and describe characteristics of the final data product.

### [B] 73.2 — Observational Constraints on Horizonless Compact Objects from Thermal Emission in AGNs
- **arXiv:** [2608.13645](https://arxiv.org/abs/2608.13645)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (73.2), star_formation (67.2), feedback_bubbles (59.3)
- **Current keyword baseline:** NO
- **BM25 max:** 56.0
- **Semantic max:** 79.3
- **Abstract:** The Swift Burst Alert Telescope Active Galactic Nuclei Spectroscopic Survey (BASS DR2) provides one of the largest and most complete samples of bright, local (z < 0.1) active galactic nuclei (AGNs) with high-quality spectroscopic measurements. These sources are typically interpreted within the framework of Kerr black holes; however, a wide range of horizonless compact-object scenarios-including naked singularities, black hole mimickers, and other exotic compact objects-have been proposed as alternatives. Largely independent of the physics of the particular horizonless model invoked, an accretion powered, thermally radiating photosphere is expected to develop on astronomically short timescales. In this paper, we investigate whether the presence of such a photosphere is consistent with the observed properties of an appropriate subsample of BASS AGNs. We find that in no instances is such a spectral feature present, and can exclude its existence in significant fraction of objects. For the remaining sources, modest improvements in observational sensitivity and spectral coverage could enable robust exclusion. Our results extend previous horizon-scale tests performed for M87* and Sgr A* to a large AGN population, providing strong, population-level evidence against horizonless alternatives. We conclude by outlining future observational strategies that can further tighten these constraints and significantly increase the number of objects for which horizons are required.

### [B] 73.2 — Interacting Supernovae: a Radio and X-ray Strategy to Constrain the Structure of the Circumstellar Medium
- **arXiv:** [2608.12464](https://arxiv.org/abs/2608.12464)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (73.2), star_formation (59.5), molecular_clouds (58.4)
- **Current keyword baseline:** NO
- **BM25 max:** 49.1
- **Semantic max:** 84.4
- **Abstract:** The interaction of supernova (SN) ejecta with the dense circumstellar medium (CSM) converts shock kinetic energy into radiation across multiple wavebands. We investigate the dependence of the X-ray and radio emission on the CSM geometry, considering spherical, hourglass, and disk shapes for the CSM. We find that the spectral and light-curve properties, both in X-ray and radio, significantly differ for spherical and non-spherical CSM structures. For a non-spherical CSM, the radio light curve flattens out near the peak frequency, due to efficient free-free absorption by the unshocked CSM. Moreover, the early rise of the radio light curve is shallower when the CSM density along the observer line of sight is larger than that in other directions. If the CSM density is lower along the observer line of sight, the radio light curve flattens near its peak, and the reverse-shock component is negligible in X-rays. Building on these features, we provide a method to constrain the CSM structure based on the rising part the radio light curve in the proximity of its peak; we show that the decay part of the radio light curve, after its peak, carries insight on whether the CSM density profile is wind-like or not. We further adopt the X-ray signal to corroborate the information extracted from radio. We test our strategy on SN 1993j and SN 2023ixf. For both SNe, we find that an asymmetric CSM is in excellent agreement with radio and X-ray observations and provides a viable alternative to non-wind scenarios suggested in the literature. Our findings highlight the crucial insight provided by radio and X-ray signals into the mass-loss history of the SN progenitor.

### [B] 73.1 — The VariableTNG project: how baryonic mechanisms shape galaxy properties
- **arXiv:** [2608.17272](https://arxiv.org/abs/2608.17272)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (73.1), star_formation (58.9), galactic_ism_surveys (56.5)
- **Current keyword baseline:** NO
- **BM25 max:** 75.9
- **Semantic max:** 79.2
- **Abstract:** We use 50 Sobol-sampled VariableTNG simulations, varying eight subgrid parameters at fixed cosmology and initial conditions, to determine which baryonic processes regulate galaxies and black holes at $z=6$ and $z=8$. We compare the simulations with recent high-redshift measurements of the stellar mass function, star-forming main sequence, stellar and gas-phase mass-metallicity relations, stellar mass-size relation, and black-hole host and accretion properties. The simulations reproduce several broad trends in these observables, although differences remain in gas-phase metallicity, galaxy size, and the most extreme black-hole populations. Given the substantial uncertainties in both the physical modelling and the observational inference of high-redshift galaxy properties, we regard these differences as diagnostic tensions rather than definitive model failures. Random-forest analyses reveal a clear hierarchy in parameter sensitivity. The abundance of low-mass galaxies is regulated primarily by stellar feedback, particularly the supernova temperature $T_{\mathrm{SN}}$ and thermal wind fraction $τ_{\mathrm{w}}$, whereas the sensitivity of the scatter in the star-forming main sequence is weaker and redshift dependent. The high-accretion tail of black-hole growth depends on black-hole seeding and feedback parameters, but also on $T_{\mathrm{SN}}$, suggesting that stellar feedback indirectly regulates rapid black-hole growth through its impact on the available gas supply. Although cosmic variance can obscure these intrinsic responses in independent small volumes, our controlled experiment identifies stellar feedback as a common physical link between early low-mass galaxy formation and rapid black-hole growth.

### [B] 73.1 — Why is GN-z11 Bright, Compact, and Nitrogen Enhanced? Insights from UV Absorption and Emission Diagnostics
- **arXiv:** [2608.12466](https://arxiv.org/abs/2608.12466)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (73.1), molecular_clouds (68.9), massive_star_formation (68.4)
- **Current keyword baseline:** NO
- **BM25 max:** 69.9
- **Semantic max:** 91.4
- **Abstract:** We investigate the UV spectrum of GN-z11, a luminous, compact galaxy with strong nitrogen lines, at $z=10.60$, using deep JWST/NIRSpec high-resolution IFU and medium-resolution MSA spectra assembled from the JADES, SPURS, and GO programs. After optimized reduction and extraction of the IFU data including an evaluation of statistical and systematic uncertainties, we obtain mutually consistent spectra from the high- and medium-resolution observations. After carefully accounting for the data quality limitations, we identify prominent P-Cygni profiles in NV$λ\lambda1238,1243$, SiIV$λ\lambda1394,1403$, and CIV$λ\lambda1548,1550$, together with broad NIV]$λ\lambda1483,1486$ emission (FWHM $\sim1600$ km s$^{-1}$). The P-Cygni profiles resemble those of massive stars such as O-type stars and luminous blue variables (LBVs), while the broad NIV] emission resembles that of nitrogen-sequence Wolf-Rayet (WN) stars. We fit stellar and active galactic nuclei (AGN) UV spectral models and find that the stellar models are strongly preferred over the AGN models ($Δ$WAIC $=-25$), with the preference driven primarily by the NV P-Cygni profile. These results indicate that the luminous, compact UV continuum of GN-z11 is dominated by massive stars. We derive electron densities from CIII]$λ\lambda1907,1909$, NIII]$λ\lambda1747-1754$, and NIV], with the nitrogen diagnostics extending well beyond the CIII]-based limit and reaching densities of $\gtrsim10^{6.5}$ cm$^{-3}$ for NIV], indicating physically distinct carbon- and nitrogen-emitting nebular components. These findings suggest that the apparent nitrogen enhancement inferred for GN-z11 as a whole may arise when strong narrow nitrogen emission originates from dense gas locally enriched in nitrogen by WN stellar winds and photoionized by nearby massive stars within the same star-forming region.

### [B] 73.0 — The THESAN-ZOOM project: clumpiness of high-redshift galaxies and its connection to bursty star formation
- **arXiv:** [2608.19308](https://arxiv.org/abs/2608.19308)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (73.0), massive_star_formation (70.7), star_formation (64.8)
- **Current keyword baseline:** NO
- **BM25 max:** 97.2
- **Semantic max:** 88.3
- **Abstract:** Recent JWST observations have revealed diverse high-redshift galaxy morphologies, including a population with irregular and clumpy structures. The physical origin of these structures, and the extent to which observational biases shape their appearance, remain uncertain. We present a power-spectrum-based method for quantifying galaxy clumpiness across spatial scales, using the radiation-hydrodynamic simulation suite THESAN-ZOOM, which employs a state-of-the-art galaxy formation model that resolves the multiphase interstellar medium (ISM). Although the total stellar mass distributions in THESAN-ZOOM galaxies are usually smooth, clumpy structures appear in the H$α$, far-ultraviolet (FUV), and optical light distributions. Tracers sensitive to shorter-timescale star formation exhibit more pronounced small-scale structure ($\sim10^{2}$--$10^{3}{\rm pc}$). The corresponding projected light spectra follow $P(k)\propto k^{-1}$ to $k^{-2}$, with progressively shallower slopes for tracers sensitive to more recent star formation, reflecting enhanced small-scale power and greater spatial intermittency in young stellar populations. This behaviour is consistent with a highly compressible, shock-dominated ISM in which stellar feedback and outflows reorganise dense gas into filamentary and clumpy structures. We also find that galaxy clumpiness depends on the treatment of stellar feedback. Weaker early stellar feedback enhances small-scale power in both the mass and light distributions. Clumpiness also varies strongly over the bursty star formation cycle, implying that observed samples may be biased towards galaxies caught in phases of elevated star formation. Galaxy clumpiness, therefore, could provide a complementary probe of the bursty star formation in the early Universe.

### [B] 73.0 — Sr and Ba yields of the First Generation(s) of stars: Constraints from metal-poor stars
- **arXiv:** [2608.17001](https://arxiv.org/abs/2608.17001)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** astrochemistry (73.0), feedback_bubbles (68.9), ism_methods_data (60.0)
- **Current keyword baseline:** NO
- **BM25 max:** 51.3
- **Semantic max:** 91.2
- **Abstract:** We present our chemical abundance analysis of ten new extremely metal-poor stars with $-4.05\leq\mbox{[Fe/H]}\leq-2.33$, based on high-resolution (R $\sim28,000$) Magellan/MIKE spectra. Eight of our stars have low heavy-element abundances of $\mbox{[Sr/H]}<-4.5$ and $\mbox{[Ba/H]}<-4.0$, making them Small Accreted Stellar System (SASS) stars. Four are hyper neutron-capture-element poor with $\mbox{[Sr/H]}<-5.0$, including Gaia DR3 5729400267359655680, which sets a new record for the lowest detected Sr abundance of $\mbox{[Sr/H]} =-6.4$. We identify four distinct [Sr/Ba] groups within the wider SASS star population which span a large range from $\mbox{[Sr/Ba]} =-2.0$ to +1.6, pointing to multiple types of progenitor events and different nucleosynthesis processes/sites. To explore the origins of this large [Sr/Ba] range, we adopt site-agnostic Sr yields of $\mbox{[Sr/H]}=-6$, $-5.75$, $-5.42$, and $-4.93$ for the four groups. Applying those yields suggests that the majority of SASS stars formed from gas enriched by $\sim$1-10 progenitor events, consistent with expectations from their extremely metal-poor nature. We thus attribute the [Sr/H] abundance scatter to intrinsic variations in the Sr yield per nucleosynthesis site/event. Our proposed Sr yields for each [Sr/Ba] group and associated nucleosynthesis origin are a reasonable and representative approximation, good to within a factor of a few, and can constrain future theoretical heavy element nucleosynthesis calculations in early core-collapse supernovae.

### [B] 72.9 — The Atacama Cosmology Telescope: Passband Measurements with an Analysis of Systematic Errors
- **arXiv:** [2608.18348](https://arxiv.org/abs/2608.18348)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (72.9), astrochemistry (50.1), molecular_clouds (44.0)
- **Current keyword baseline:** NO
- **BM25 max:** 44.2
- **Semantic max:** 84.1
- **Abstract:** We present measurements of the spectral response of the four Advanced ACTPol (AdvACT) multichroic detector arrays, which observed in frequency bands centered near 30, 40, 90, 150, and 220 GHz. The passbands were measured with a Fourier transform spectrometer (FTS) combined with coupling optics that direct and match the output of the FTS to the AdvACT receiver. We perform optical simulations of the FTS and coupling optics in order to model frequency-dependent systematic effects in this system. We use these simulations to apply corrections to the measurements and evaluate the remaining systematic uncertainty. We combine these systematic estimates with statistical errors to determine the measured passbands and their uncertainties from our FTS measurement, which are typically 0.75 to 1.5% per detector array. We present the passband characteristics for all measurements made by ACT in a common framework. Additionally, we discuss the performance achieved as well as ways to improve passband measurements in the future.

### [B] 72.7 — The Roman Coronagraph Community Participation Program: corgisim - a simulation suite for the Nancy Grace Roman Space Telescope Coronagraph Instrument
- **arXiv:** [2608.17257](https://arxiv.org/abs/2608.17257)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** ism_methods_data (72.7), astrochemistry (65.7), molecular_clouds (65.4)
- **Current keyword baseline:** NO
- **BM25 max:** 41.0
- **Semantic max:** 83.8
- **Abstract:** NASA's Roman Space Telescope will feature a pathfinder Coronagraph Instrument to demonstrate advanced high-contrast imaging from space, paving the way for future missions like the Habitable Worlds Observatory. The Coronagraph Instrument could obtain imaging, polarimetry and spectroscopy of Jupiter analogs in reflected visible light for the first time. We present the development of an open-source simulation package ``corgisim'' as part of the Roman Coronagraph Community Participate Program. Built on established optical propagation libraries including PROPER and CGISim, corgisim provides a user-friendly, publicly available Python framework for end-to-end simulations of the Coronagraph Instrument observations. The package produces high-fidelity, format-compliant data for pre-launch calibration, pipeline testing, and community applications such as target selection and observation planning. We will give an overview of corgisim's infrastructure, functionalities, and current implementation across planned imaging, polarimetry, and spectroscopy modes, including the ability to simulate host stars, injected companions, and extended disks. We will also highlight suitable applications of corgisim and provide guidance on how users can access and employ the software.

### [B] 72.6 — The galaxies' energy balance problem solved
- **arXiv:** [2608.14023](https://arxiv.org/abs/2608.14023)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (72.6), galactic_ism_surveys (60.7), molecular_clouds (57.5)
- **Current keyword baseline:** NO
- **BM25 max:** 66.8
- **Semantic max:** 83.7
- **Abstract:** We attempt to resolve the long-standing energy balance problem encountered by Radiative Transfer (RT) models, particularly in edge-on galaxies by incorporating a treatment for the clumpy structure of the Interstellar Medium (ISM). A subgrid approach is adopted, treating the quiescent dust clouds as pseudo-dust grains, with equivalent optical and thermal emission properties. Deriving key quantities such as the absorption, scattering and extinction cross-sections enables the virtualisation of the macroscopic clump into a microscopic pseudo-grain that can be included alongside the existing dust model constituents. The addition of the pseudo-grain results in a flatter extinction curve. A library of clump emission spectral energy distributions (SEDs) is constructed for radiation fields of various colours and intensities. The new clumpy model is applied to the edge-on galaxy NGC 891 and, for the first time, is able to achieve a good energy balance, simultaneously fitting both the submm and Near Infrared (NIR) data. The clumpy model is further applied to a small sample of seven galaxies of various inclinations, and the results are compared with those from the purely diffuse models. The clumpy models are characterised by a reduction in dust opacity, and therefore attenuation, compared to their purely diffuse counterparts. Thus, the maximum face-on optical depth in the $B$-band, ${\mathrm max}(τ^{\mathrm f}_{\mathrm B})$, derived from the clumpy models is found to be lower by factors ranging from 1.3 to 2.8. Of the seven galaxies, two are found to be optically thick in their centres, two are found to be moderately optically thick, and three are found to be optically thin.

### [B] 72.4 — A deep learning algorithm for black hole spin estimation using hot-spot secondary images
- **arXiv:** [2608.18208](https://arxiv.org/abs/2608.18208)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.IM
- **Top topics:** ism_methods_data (72.4), feedback_bubbles (57.7), galactic_ism_surveys (53.8)
- **Current keyword baseline:** NO
- **BM25 max:** 47.2
- **Semantic max:** 83.4
- **Abstract:** Sagittarius A* exhibits frequent flaring activity across the electromagnetic spectrum that is often associated with a localized region of strong emission known as a hot spot. We aim to train a deep learning model to provide a link between key parameters of this phenomenon - hot-spot emission radius, and black hole inclination and spin - to the observed angle difference between the primary and secondary image ($ΔPA$) that present and future interferometric arrays could resolve. Using the general relativistic radiative transfer code IPOLE, we generated a library of $\sim100.000$ models with varying system parameters and computed the position angle difference on the image plane between the primary and secondary images of the hot spot. We explore equatorial and non-equatorial circular orbits and evaluate our models against approximate observational constraints, including partial-orbit visibility and observational errors. Our algorithm STIHOS shows remarkable accuracy in calculating spin and inclination from the majority of the observational tests we perform ($σ_{a_*}=0.04,\,σ_i=2^{\circ}$), even in extreme conditions where only half of the orbit is visible. The off-equatorial estimation provides softer constraints in the absence of prior information. Our results demonstrate the importance of hot-spot observations for spacetime estimations. Given the increasing efforts to detect the photon-ring, our framework could prove valuable in interpreting the first observations of lensed emission.

### [B] 72.2 — The Ĝ Infrared Search for Extraterrestrial Civilizations with Large Energy Supplies. V. When Galaxies Glow with Industry
- **arXiv:** [2608.12458](https://arxiv.org/abs/2608.12458)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (72.2), feedback_bubbles (64.3), massive_star_formation (61.0)
- **Current keyword baseline:** NO
- **BM25 max:** 57.9
- **Semantic max:** 83.2
- **Abstract:** We present the most robust stellar population synthesis (SPS)-based search for galaxy-spanning technological waste heat to date, applied to 129 nearby galaxies spanning a wide range of spectral energy distribution (SED) types, including ultraluminous IR galaxies and MIR-luminous active galactic nuclei (AGN). We incorporate the AGENT Dyson sphere formalism into the Flexible Stellar Population Synthesis code at the stellar population level, so nebular and dust emission respond self-consistently to Dyson sphere reprocessing. With \texttt{Prospector}, we perform a suite of 1,419 injection recovery tests across a range of covering fractions, $α$, where we successfully recover the injected covering fractions (best-fit slope $m = 0.92$) and detect them through Bayesian model selection down to $α\sim 4$--$5\%$ in quiescent galaxies. None of our 129 galaxies prefer a Dyson sphere component, and we place the first per-galaxy 95\% upper limits on warm ($T_{\rm BB} \gtrsim 100$K) swarms, reaching a median $α< 0.3\%$ across quiescent hosts without a dominant AGN. Our injection-calibrated detection rates convert these zero detections into a population bound of $<2.6\%$ of galaxies hosting $α= 25\%$ swarms ($95\%$ confidence). Because survey colors cannot separate waste heat from starbursts and AGN, we develop a scaffold for future searches, running from inexpensive archival screens such as the Balmer decrement and the stellar-to-dynamical-mass offset a swarm leaves behind, through resolved fitting with nuclear excision, to PRIMA FIR photometry that makes targeted JWST imaging decisive. We find that the outskirts of quiescent galaxies are the best hunting grounds for future technosignature searches.

### [B] 72.1 — The Effects of M Star Age Dependent Ultraviolet Emission on Detecting and Interpreting Exoplanet Biosignatures
- **arXiv:** [2608.19328](https://arxiv.org/abs/2608.19328)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** astrochemistry (72.1), molecular_clouds (72.1), ism_methods_data (72.1)
- **Current keyword baseline:** NO
- **BM25 max:** 35.4
- **Semantic max:** 90.1
- **Abstract:** Given their abundance and observational advantages, M stars will arguably be the best candidates for characterizing and searching for biosignatures on terrestrial exoplanets in the near future. However, photochemistry that can suppress or enhance key biosignature molecules in planetary atmospheres is primarily driven by UV flux from the host M star, which is influenced by stellar activity that decreases with age. Here, we simulate Pre-Industrial Earth-like and Archean Earth-like atmospheres around M4 and M8 stars from 650 Myr to 5 Gyr old. We find that our Pre-Industrial Earth atmospheres around 5 Gyr M stars have up to ten times more CH$_4$ than those around 650 Myr M stars, producing 68% stronger methane bands in NIR transit spectroscopy. Additionally, photochemical shielding from O$_2$ in our Pre-Industrial Earth atmospheres reduces the impact UV-driven photochemistry on composition, while the Archean Earth exhibits larger compositional changes due to weaker shielding from CO$_2$. Lastly, enhanced CO$_2$ photolysis, driven by the strong net UV flux and high Far/Near-UV ratios of 650 Myr and 1 Gyr M stars, cause our Archean Earth-like planets to produce up to 5.4 dex more O$_3$ than when around 5 Gyr M stars. The excess O$_3$ causes the Archean Earth to become half as reflective in the 0.2-0.3 $\mathrmμ$m Hartley band feature in ultraviolet reflectance spectroscopy, which the Habitable Worlds Observatory may be sensitive to. Without the context of the star's real-time, age-dependent UV radiation, this O$_3$ feature could be misinterpreted as a proxy for low, biogenic O$_2$.

### [B] 72.1 — The X-Ray Continuum Emission Region in the Lensed Quasar SDSS J133907.23+131038.6 is Much Smaller than the Accretion Disk
- **arXiv:** [2608.17041](https://arxiv.org/abs/2608.17041)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** galactic_ism_surveys (72.1), ism_methods_data (66.2), feedback_bubbles (65.8)
- **Current keyword baseline:** NO
- **BM25 max:** 56.6
- **Semantic max:** 90.2
- **Abstract:** We analyze microlensing variability in 15 seasons of optical monitoring data and 4 epochs of new X-ray observations of the doubly-imaged gravitationally lensed quasar SDSS J133907.23+131038.6 to place empirical constraints on the size and structure of that system's X-ray and optical continuum emission regions. Employing a Bayesian Monte Carlo method, we analyzed ground-based optical light curves to constrain the half-light radius of the far-UV source $\log(r_{\rm 1/2, FUV}/{\rm cm})=15.78^{+0.26}_{-0.28}$ at 193 nm, the rest-frame center of the {\it r}-band, assuming a $60^\circ$ inclination angle. This size corresponds to $\sim100\,{\it r}_{\rm g}$ for a $4.0 \times 10^{8} \: {\rm M_{\odot}}$ black hole. We measured the half-light radius of the full band ($0.2-8.0 \: {\rm keV}$) X-ray continuum emission region $\log(r_{\rm 1/2, X_{full}}/{\rm cm})=14.32^{+0.23}_{-0.31}$, a size measurement that is consistent with the radius of the innermost stable circular orbit (ISCO) in the Schwarzschild metric.Two shifted Fe K$α$ lines caused by microlensing are detected in the stacked spectrum of image A at 5.9 and 8.9~keV at $>99\%$ significance.

### [B] 72.1 — Two domains of extended Lyman-alpha emission around galaxies: from local radiation to environmental regulation
- **arXiv:** [2608.16665](https://arxiv.org/abs/2608.16665)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (72.1), atomic_ism (64.4), ism_methods_data (58.5)
- **Current keyword baseline:** NO
- **BM25 max:** 70.5
- **Semantic max:** 90.2
- **Abstract:** We examine the relation between extended Ly$α$ halos around high-redshift galaxies and the main factors responsible for driving the emission in such halos, in particular at distances around and beyond one virial radius $r_\mathrm{vir}$. To reach the required surface brightness sensitivity we take advantage of the MUSE eXtremely Deep Field (MXDF) survey, allowing us to probe levels as faint as $\sim 10^{-20}$ erg cm$^{-2}$ s$^{-1}$ arcsec$^{-2}$ in individual Ly$α$ halos. Our sample consists of the 21 apparently core- and halo-brightest (yet intrinsically low luminosity $\log_{10}$L$_{\mathrm{Ly}α} < 42.3$ erg s$^{-1}$) Ly$α$ emitters (LAEs) in the MXDF at $3<z<4$, with typical virial radii around 20 kpc. We measure their radial surface brightness profiles out to 50 kpc (more than $2r_{\mathrm{vir}}$) and investigate the correlations between surface brightness and internal (star formation rates of the host galaxies, SFR) or external influences (environmental density, $δ+1$). We find a clear break in these correlations at radii around or just below $1r_{\mathrm{vir}}$. Below this break the emission correlates tightly with SFR (as expected) and not at all with $δ+1$. Beyond $\sim 1r_\mathrm{vir}$(20 kpc) we observe the opposite trend with no dependence on SFR, but an emerging correlation with $δ+1$. We compare our measurements with the expected integrated surface brightness from ultrafaint, individually undetected LAEs and find that the latter is insufficient to drive the observed correlation. We conclude that Ly$α$ emission from the outer halos is regulated by the surrounding environment, but originates mostly from diffuse gas rather than discrete sources.

### [B] 72.0 — Towards independent event horizon imaging of the supermassive black holes in M87 and the Milky Way
- **arXiv:** [2608.19675](https://arxiv.org/abs/2608.19675)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.CO
- **Top topics:** ism_methods_data (72.0), star_formation (61.2), galactic_ism_surveys (54.6)
- **Current keyword baseline:** NO
- **BM25 max:** 64.0
- **Semantic max:** 82.9
- **Abstract:** The Event Horizon Telescope (EHT) Collaboration's images of the supermassive black holes in M87 and the Milky Way have provided the first event-horizon-scale views of these objects, opening new avenues for studies of gravitation, accretion physics, and black hole astrophysics. Achieving these results, however, requires imaging under some of the most challenging conditions in radio astronomy, including low signal-to-noise ratios, severe calibration uncertainties, and sparse aperture coverage. With the aim of presenting independent analyses of the public EHT datasets for M87* and Sgr A*, we adopt an approach that is independent in observables, and reconstruction methodology. Our framework is based on closure invariants, a class of interferometric observables that are intrinsically immune to station-based calibration errors and therefore provide robust constraints on source structure. We combine these observables with Generative Deep learning Image Reconstruction with Closure Terms (GenDIReCT), a diffusion-based image reconstruction framework that operates in the latent space of images conditioned on closure invariants. We present independent reconstructions obtained using GenDIReCT on synthetic challenge data sets as well as real EHT data on 3C279 and Centaurus A, and compare them with previously reported results. This work demonstrates the potential of closure-invariant-driven generative imaging as a calibration-resilient framework for Very Long Baseline Interferometry (VLBI) and provides an independent and complementary avenue for interpreting horizon-scale black hole observations.

### [B] 72.0 — Recurrent Multi-year Mg II BAL Variability in SDSS J1333+0012
- **arXiv:** [2608.18211](https://arxiv.org/abs/2608.18211)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (72.0), feedback_bubbles (65.8), molecular_clouds (62.7)
- **Current keyword baseline:** YES
- **BM25 max:** 38.1
- **Semantic max:** 82.9
- **Abstract:** We present a long-term spectroscopic study of Broad Absorption Line (BAL) variability in the quasar J1333+0012 (\zem = 0.9197) using an extensive multi-epoch dataset spanning nearly two decades. The dataset comprises multi-epoch observations from multiple observatories, delivering nearly uniform temporal coverage of the Mg II BAL profile, with close to one spectroscopic observation per year spanning the period from 2008 to 2025. We identify recurrent multi-year variability in the BAL absorption strength, characterized by a rest-frame timescale of $\sim$4 yr. Because the well-sampled baseline covers only a small number of candidate cycles, we present J1333+0012 as a candidate quasi-periodic BAL system. In contrast, contemporaneous optical photometric light curves from CRTS, Pan-STARRS, ZTF, and PTF show no statistically significant correlated variability on comparable timescales. However, ionization-driven variability cannot be ruled out, as the observed optical continuum does not directly trace the unobserved extreme-UV ionizing continuum. The coherence of the variability across distinct velocity components, coupled with the absence of large-scale profile reshaping, is consistent with a geometric origin. We interpret the observed behavior as modulation of the line-of-sight absorption by the rotation of an inhomogeneous shielding-gas structure.

### [B] 72.0 — The Viability of Life in Helium-Dominated Exoplanet Atmospheres
- **arXiv:** [2608.15679](https://arxiv.org/abs/2608.15679)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** ism_methods_data (72.0), astrochemistry (69.7), feedback_bubbles (69.2)
- **Current keyword baseline:** NO
- **BM25 max:** 57.1
- **Semantic max:** 89.9
- **Abstract:** Helium is the second most abundant element in the Universe, yet helium-dominated atmospheres are rarely considered as environments for life. Two assumptions have contributed to this neglect: helium is expected to escape from rocky planets together with hydrogen, and Earth itself lacks a substantial helium envelope. Recent observations and atmospheric evolution models, indicate that rocky exoplanets can retain helium-dominated atmospheres. Here we make the case for life in such environments by synthesizing a largely overlooked body of laboratory research on life in helium-dominated atmospheres. Every organism studied, including bacteria, fungi, protozoa, microalgae, plants, and animals tolerates helium-dominated atmospheres when supplied with essential metabolic requirements. Across a range of pressures, helium has shown no demonstrated toxicity and no fundamental barrier to metabolism, cell division, photosynthesis, nitrogen fixation, or coordinated multicellular activity, including in humans. Helium-dominated atmospheres therefore constitute a viable and underrecognized planetary environment for life. Helium is chemically inert and spectroscopically unobtrusive, so the bulk atmosphere would neither contribute to the chemical destruction of biosignature gases nor strongly obscure their spectral features. Helium-dominated atmospheres also have low mean molecular weights and large scale heights, strengthening spectral features in transmission and improving remote detectability.

### [B] 71.7 — A Systematic Gaia--ZTF Search for Short-Period Blue Compact-Binary Candidates
- **arXiv:** [2608.19493](https://arxiv.org/abs/2608.19493)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** astrochemistry (71.7), star_formation (68.1), ism_methods_data (67.7)
- **Current keyword baseline:** NO
- **BM25 max:** 48.2
- **Semantic max:** 89.7
- **Abstract:** We present a catalog of 147 short-period (10.34--106.46~min) blue compact-binary candidates, identified by combining Gaia DR3 astrometry and photometry with ZTF DR23 light curves via a Gaia selection, period searches, and machine-learning morphology ranking. Of these, 111 lack prior compact-binary classifications. Multiwavelength data (DESI DR1, GALEX, AllWISE) reveal a heterogeneous sample: on the Gaia colour--magnitude diagram, 52 sources lie on the white-dwarf locus, 69 in the hot-subdwarf region, and 26 are intermediate. Among 26 sources with DESI spectra, only about one third follow the white-dwarf cooling sequence; the rest are more luminous blue stars with white-dwarf-like low-resolution spectra. We highlight a prioritized subset of new white-dwarf-locus candidates for follow-up, including ten with periods below 40~min and none with existing radial-velocity data. Under fiducial binary assumptions, 17 of these newly identified white-dwarf-locus candidates would exceed the adopted LISA signal-to-noise threshold (led by a 37~pc white dwarf), with the count depending on chirp mass (9 for $0.15\,M_\odot$, 17 for $0.3\,M_\odot$, 21 for $0.6\,M_\odot$), assuming orbital modulation. However, for most of the white-dwarf-locus sample, observed modulation amplitudes exceed any plausible ellipsoidal signal by three to five orders of magnitude, implying that rotating magnetic or chemically inhomogeneous single white dwarfs offer a viable alternative that ZTF photometry alone cannot rule out---the catalog includes at least one confirmed case. We release the full 147-source catalog, including periods, Gaia/spectroscopic classifications, harmonic/ellipsoidal diagnostics, and supplementary tables of fiducial GW estimates and UV--IR photometry.

### [B] 71.7 — The segmented spiral structure of the Solar neighbourhood traced by young clustered populations
- **arXiv:** [2608.17887](https://arxiv.org/abs/2608.17887)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (71.7), galactic_ism_surveys (65.8), astrochemistry (57.4)
- **Current keyword baseline:** NO
- **BM25 max:** 68.7
- **Semantic max:** 77.4
- **Abstract:** The Milky Way spiral pattern remains poorly constrained, and the youngest tracers in the solar neighbourhood do not always follow a few smooth, continuous logarithmic arms. We analyse young open clusters, both independently and combined with young stellar object (YSO)-based groups, to test whether they define continuous spiral-arm ridges or shorter, partially connected structures. In the (theta_G, ln R_G) plane, we identify local overdensities using a density-supported Bayesian Gaussian Mixture Model (BGMM), introducing published Perseus, Local, Sagittarius, and Scutum arm tracks only afterwards as reference curves. We then apply a Minimum Spanning Tree (MST) analysis in the heliocentric (X,Y) plane to examine spatial connectivity. The open-cluster sample already resolves into several local components, while the addition of YSO-based groups highlights branches and intermediate regions without producing continuous arms. The MST likewise shows distinct local branches at small pruning scales that progressively merge as the linking scale increases. The Local--Sagittarius region provides the clearest agreement between both diagnostics: the BGMM identifies an intermediate component between the reference arms, while the MST connects neighbouring branches through the same region. Overall, young structures near the Sun appear as fragmented, spiral-like segments with partial links rather than smooth continuations of a few grand-design arms. Determining whether this morphology reflects spiral-arm formation mechanisms or subsequent evolution will require additional age, vertical, and kinematic information.

### [B] 71.5 — From the Earth to the Sun
- **arXiv:** [2608.13635](https://arxiv.org/abs/2608.13635)
- **Primary category:** physics.hist-ph
- **Categories:** physics.hist-ph, astro-ph.EP, astro-ph.SR
- **Top topics:** star_formation (71.5), magnetic_fields (60.8), ism_methods_data (60.4)
- **Current keyword baseline:** YES
- **BM25 max:** 26.9
- **Semantic max:** 89.4
- **Abstract:** This year marks 360 years since the founding of the French Academy of Sciences. This is the story of the academy's daring 17th century expedition to measure the Earth-sun distance. A truncated version first appeared in National Geographic Magazine; the following is closer to the original draft, with updated information and references.

### [B] 71.4 — The instantaneous mass accretion rate of novae in quiescence: - an archival ultraviolet optical spectral analysis
- **arXiv:** [2608.18037](https://arxiv.org/abs/2608.18037)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** star_formation (71.4), astrochemistry (67.1), feedback_bubbles (64.0)
- **Current keyword baseline:** YES
- **BM25 max:** 47.2
- **Semantic max:** 83.8
- **Abstract:** Based on archival spectra, we derive the quiescent instantaneous mass transfer rates in novae using synthetic disk spectra generated with tlusty, Gaia parallax-derived distances, and updated color excess values. Our results for nine novae, based on ultraviolet spectra and on a number of optical spectra, yield mass accretion rates that are higher than those derived from simple integration of the UV and optical luminosity. HR Del, 20 years after its eruption, has a mass transfer rate of $4\times 10^{-7}M_\odot$/yr, and is likely burning the accreting H-rich material. V842 Cen, thought to be a low mass transfer system, has a comparable mass accretion rate. For both novae, the enhanced mass transfer must be self-sustained by a feedback loop. RR Pic, with $\dot{M}\approx 3\times 10^{-8}M_\odot$/yr, is better fitted with an accretion disk where the outer region is heated up to 12,000 K, in agreement with H and He emission lines coming from the outer disk and a large emission region on the leading side of the disk. Such a heated disk also gives a good fit to the spectra of CP Lac, and DI Lac with $\dot{M}\sim4.5$ and $9\times 10^{-9}M_\odot$/yr. V1974 Cyg and V533 Her, with an accretion rate of $\sim 3\times 10^{-9}M_\odot$/yr, have a rather flat spectrum. V446 Her and BK Lyn, caught in a state of low accretion, have the lowest mass accretion rates with $\dot{M} \sim 10^{-9}$ and $\sim 10^{-10}M_\odot$/yr respectively. The higher mass transfer rate systems, with $\dot{M}\approx \sim 10^{-7}M_\odot$/yr, agree with the standard disk model; the remaining systems are better fitted when the outer disk is heated to $\sim 12,000$~K. We suggest that irradiation from the heated WD, inner disk, together with tidal interaction, the bright spot, and material overflowing the disk edge, can increase the temperature of the outer disk.

### [B] 71.3 — 3D simulations of magnetospheric accretion in T Tauri stars: I. Disk truncation, stellar torques, and application to observations
- **arXiv:** [2608.17869](https://arxiv.org/abs/2608.17869)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** star_formation (71.3), magnetic_fields (64.4), ism_methods_data (51.7)
- **Current keyword baseline:** NO
- **BM25 max:** 72.4
- **Semantic max:** 82.1
- **Abstract:** Young stars accrete material from their circumstellar disk through their magnetosphere while still contracting, two processes that impact their rotational evolution. We investigate stable and unstable accretion regimes (due to the interchange instability) and examine the associated stellar torques to assess the spin evolution of young stars. We perform 3D MHD simulations of disk accretion onto an inclined stellar dipole. We run 21 simulations with varying stellar stellar rotation rates, dipole field strengths and obliquities, and mass accretion rates. We find that stars with a ratio of truncation to corotation radius $R_t/R_{co} \gtrsim 0.80-0.85$ accrete via a stable regime, while accretion becomes unstable otherwise. Besides, our $R_t/R_{\ast}$ parametrization weakly depends on the mass accretion rate and the dipolar intensity, while strongly on the stellar rotation rate. We derive torque formulae for each flow component affecting the stellar rotation, i.e. accretion, magnetospheric ejections and stellar winds. Finally, we apply our results to a sample of young stars with measured magnetic fields, mass accretion rates, and rotational periods and find that most of them should currently accrete in an unstable regime and undergo spin-up torques. Our study comforts and expands upon previous results. Unstable accretion should lead to a net spin-up torque on the central star, while stable accretion can lead to stellar spin-down. When applying our truncation radius and torque prescriptions to observational data, we find that most young stars in our sample should be in a spin-up state. Thus, the angular momentum problem for young stars remains.

### [B] 71.3 — X-ray Flaring and Variability in NGC 1275, the Heart of the Perseus Cluster
- **arXiv:** [2608.13281](https://arxiv.org/abs/2608.13281)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** star_formation (71.3), galactic_ism_surveys (69.4), molecular_clouds (66.1)
- **Current keyword baseline:** NO
- **BM25 max:** 51.2
- **Semantic max:** 86.7
- **Abstract:** NGC 1275 is the central galaxy in the Perseus Cluster. The active galactic nucleus (AGN) within NGC 1275 is notable for its strong and variable radio activity, tied to the production of radio jets that inflate large bubbles in the hot intracluster medium (ICM). High spatial resolution X-ray imaging can separate the AGN from the bright ICM, but monitoring the mass accretion rate onto the black hole and establishing disk-jet connections in NGC 1275 requires a high cadence. Here, we report on X-ray monitoring of NGC 1275 using data taken over 20 years with the Neil Gehrels Swift Observatory. Modeling the temporally constant ICM in each observation allows X-ray emission from accretion onto the black hole to be traced reliably, with typical flux errors of $\sim 3\%$. X-ray flaring by a factor of $\sim2$ over mere days is detected starting on MJD 59956 (2023 Feb. 21). The flares imply an emission region consistent with $r \leq 870~(10^{8}~M_{\odot}/M_{BH})~ GM/c^{2}$. The profile of the flaring is inconsistent with simple predictions for tidal disruption events. A flare appears roughly 300 days later in radio monitoring data at 43 GHz. Overall, our results indicate that coordinated, moderate-resolution X-ray imaging and radio monitoring could potentially trace disk-jet connections in the AGN that most vividly impact large-scale structure, and be extended to other sources that impact their hosts.

### [B] 71.2 — Identifying AGNs from X-ray detections$-$II: Metallicity calibrations for the $\rm N_2O_2$ and $\rm N_2S_2$ diagnostics
- **arXiv:** [2608.16825](https://arxiv.org/abs/2608.16825)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (71.2), molecular_clouds (63.3), ism_methods_data (60.2)
- **Current keyword baseline:** NO
- **BM25 max:** 51.1
- **Semantic max:** 81.9
- **Abstract:** Emission-line ratios from ions with nearly identical ionization potentials offer a robust solution to the degeneracies inherent to traditional active galactic nuclei (AGNs) metallicity diagnostics. We introduce new semi-empirical metallicity calibrations for the $\rm N_2O_2$ and $\rm N_2S_2$ diagnostics, explicitly designed to isolate the chemical abundance from the incident radiation field. By coupling an extensive grid of CLOUDY photoionization simulations directly to the intrinsic 2$-$10 keV X-ray luminosity ($L_{\rm X}$) and benchmarking against Seyfert~2 nuclei from the Burst Alert Telescope AGN Spectroscopic Survey (BASS), we establish robust relations valid across the metallicity regime of $8.0 \lesssim 12+\log({\rm O/H}) \lesssim 9.1$ ($0.2 \lesssim Z/Z_{\odot} \lesssim 2.6$). The $\rm N_2O_2$ and $\rm N_2S_2$ indices trace co-spatial emitting volumes within the narrow-line regions (NLRs), enabling this framework to resolve the significant $L_{\rm X}$-driven systematic biases we previously identified in the standard $\rm N_2$ and $\rm N_2O_3$ indices. While the $\rm N_2O_2$ ratio proves to be virtually independent of nebular structural variations, the $\rm N_2S_2$ index exhibits a subtle, yet discernible, electron density ($N_{\rm e}$) susceptibility due to the low critical density ($N_{\rm c}$) of the [S II]$λ\lambda6716,6731$ doublet. Nevertheless, both diagnostics yield highly precise metallicity constraints with tight root-mean-square residual dispersions of $\sim 0.081$ dex for $\rm N_2O_2$ and $\sim 0.121$ dex for $\rm N_2S_2$. We propose the $\rm N_2O_2$ and $\rm N_2S_2$ calibrations as highly optimized, unbiased metallicity tracers for AGNs.

### [B] 71.1 — Planetary systems in the light of asteroseismology: metallicity threshold for the planetary systems and age-metallicity relation
- **arXiv:** [2608.15849](https://arxiv.org/abs/2608.15849)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.EP
- **Top topics:** astrochemistry (71.1), massive_star_formation (61.0), star_formation (59.4)
- **Current keyword baseline:** YES
- **BM25 max:** 35.8
- **Semantic max:** 81.8
- **Abstract:** We compiled data for 127 hosts (plus six candidates) and used them as constraints to construct interior models of the hosts using the {\small MESA} code. Two significant conclusions emerge from these models. First, except for a few stars, the hosts' metallicity ($Z_0$) is greater than 0.007. This suggests a possible suppression of the occurrence of planets below $Z_0\approx0.007$. Second, it concerns how chemical evolution unfolds in the galactic disc. For a given $Z_0$ value, considering the oldest stars, there is a linear relationship between $Z_0$ and age ($t_9$). This line is around $t_9=13.4$ Gyr at $Z_0=0$, a value consistent with the age of the Galaxy. The linear relationship continues until around $t_9=6$ Gyr, and the maximum value of $Z_0$ remains constant between $t_9=2-6$ Gyr. We further modelled 12 hosts classified as red clump (RC) stars in the literature, explicitly accounting for mass loss along the red giant branch. These models highlight the critical role of mass-loss assumptions in determining the initial masses and ages of RC hosts, and their implications for the survival and evolution of close-in planets. Another key outcome of this study is the discovery of the relationship between $Z_0$ and the observed metallicity ($Z_{\rm s}$) for the hosts. We obtain a useful expression for $Z_0$, the input parameter for the models, as a function of stellar mass, radius, and $Z_{\rm s}$. This expression can be used to estimate $Z_0$ based on the reduced surface metallicity due to microscopic diffusion. We also derive an expression for planetary mass relative to the orbital semimajor axis and host mass. This expression may indicate a mass distribution near the inner disc where these planets formed, except for hot-Jupiters. Planet radii appear to depend on the planet's mass and irradiation energy, as well as the orbital period.

### [B] 71.0 — Inferring the Dark from the Observable: Estimating Halo Masses Using Galaxy Properties
- **arXiv:** [2608.19154](https://arxiv.org/abs/2608.19154)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** star_formation (71.0), galactic_ism_surveys (70.4), feedback_bubbles (65.2)
- **Current keyword baseline:** NO
- **BM25 max:** 43.4
- **Semantic max:** 88.0
- **Abstract:** The formation and evolution of galaxies are interconnected with that of their host halos. Given this closely related evolutionary history, it should follow that galaxy properties are correlated with their host halo mass. Previous works have shown that star formation rates of galaxies in cluster halos differ systematically from those in field halos, suggesting that host halo mass plays a significant role in the history of galaxy evolution. Here, we examine the correlations between observable galaxy properties - such as stellar mass, star formation rate, half-stellar radius, $r-$band magnitude, and color - and the underlying host halo mass of galaxies. Central galaxy observables are used to probe host halo mass, while satellite galaxy properties are used to estimate subhalo mass. We perform this analysis using random forest, ordinary least squares (OLS), and symbolic regression. Random forest regression can assess the relative significance of different observable galaxy properties, while OLS and symbolic regression can quantify their relationship with the host halo mass. Our results show that gas mass is generally the most significant property in central galaxies of all halo mass ranges, followed by stellar mass and observed $r-$band magnitude. Adding parameters such as the colour and magnitude of galaxies improves host halo mass estimations compared to standard stellar-to-halo mass relations. These results show that halo mass likely has a multi-dimensional dependence on galaxy properties and open the avenue of finding a simple way to constrain halo mass based on what is directly observable in galaxy surveys. Finding the observables that have the strongest correlation with halo mass can also motivate future surveys on which areas to concentrate in detail.

### [B] 71.0 — Gaia DR3 Limits on Stellar Engine Technosignatures in Nearby Stars
- **arXiv:** [2608.16060](https://arxiv.org/abs/2608.16060)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** ism_methods_data (71.0), star_formation (70.9), astrochemistry (61.7)
- **Current keyword baseline:** YES
- **BM25 max:** 44.7
- **Semantic max:** 88.8
- **Abstract:** An operating stellar engine that transfers momentum to its host star could produce an approximately persistent transverse acceleration during the Gaia Data Release 3 (DR3) observing epoch. We search for such accelerations among 406,984 quality-selected Gaia DR3 stars with nominal distances below 200 pc (about 650 light-years), using 8,890 published Acceleration7 solutions. Because long-period binaries and astrometric systematics can produce similar sky-plane curvature, we model these conventional explanations together with a broad component that can absorb any remaining persistent acceleration or model mismatch. At $a_0 = 2.60 \times 10^{-4}$ m s$^{-2}$, where essentially the entire parent sample is searchable, mapping the residual weights evaluated at the one-sided 95% profile-limit point gives a parent-population fraction limit of $1.21 \times 10^{-5}$. Multiplying this fraction by the parent-sample size gives a summed upper-limit weight of about five star-equivalents above the threshold. Toward the lowest acceleration thresholds, the searchable fraction declines rapidly, so the corresponding bounds primarily describe the reach of the search. No individual source is interpreted as a technological signal.

### [B] 70.8 — Concerns regarding recurrent fluorescence's impact on smaller diffuse ISM aromatics
- **arXiv:** [2608.17886](https://arxiv.org/abs/2608.17886)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (70.8), astrochemistry (62.0), feedback_bubbles (57.3)
- **Current keyword baseline:** YES
- **BM25 max:** 63.1
- **Semantic max:** 88.6
- **Abstract:** Recent research implied that recurrent fluorescence (RF) could bolster smaller aromatics against fragmentation in the diffuse ISM, yet that hypothesis is contested by timescales for unrelenting dissociative recombination (electrons), and unceasing dissociating photons. Specifically, neutral cyanonaphthalene can sustain $13.6$ eV photoionization, and the ensuing cation's excess energy is channeled through intramolecular vibrational redistribution (IVR), with RF providing the radiative stabilization pathway ($\simeq7$ eV negligible survival limit). However, that cation endures dissociative recombination every $τ\approx0.5^{+5.6}_{-0.4}$ years, which deposits $\simeq 8.6$ eV and exceeds the limit. Moreover, that is paired with $7-13.6$ eV photodestruction each $τ\approx16^{+223}_{-14}$ years (total visual dust extinction $A_V=0-1$, and $τ\approx4^{+7}_{-2}$ years for $A_V\approx0$). Recent laboratory characterizations of RF were seminal, but the mechanism may not overturn models indicating a gap in smaller $N_C\approx7-11$ diffuse ISM aromatics, nor support those molecules as viable diffuse interstellar band carriers.

### [B] 70.8 — A JWST/MIRI Study of Dust in a Sample of Normal Type IIP Core Collapse Supernovae
- **arXiv:** [2608.16979](https://arxiv.org/abs/2608.16979)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (70.8), galactic_ism_surveys (70.0), star_formation (69.1)
- **Current keyword baseline:** NO
- **BM25 max:** 49.1
- **Semantic max:** 88.5
- **Abstract:** Core collapse supernovae (CCSNe) are invoked as major dust producers in the early Universe, yet the amount of dust they form, the timescale over which it grows, and the physical conditions that regulate the yield remain uncertain. We present a detailed JWST/MIRI mid-infrared (MIR) imaging census of 11 nearby Type IIP CCSNe spanning $\sim$1-7 yr after explosion, investigating dust emission across the different phases of their evolution. The spectral energy distributions show a coherent evolution from hot ($\sim$1500 K), 5-8 $μ$m emission at $\sim$400 d to prominent 10 and 18 $μ$m emission features at later epochs ($\sim$600-2500 d). The cool dust temperatures range from $\sim120$ to $250$ K and dust masses from $\sim10^{-4}$ to $10^{-2} M_{\odot}$. The current sample shows no statistically significant correlation between measured dust mass and peak luminosity, plateau duration, or explosion energy. SNe with early high ionization features, indicative of confined CSM, are often among the dust-rich objects in the sample. The measured 1-7 yr dust yields are insufficient to account for dust in typical $z > 6$ galaxies, but support a role for CCSNe as producers of seed dust for subsequent grain growth.

### [B] 70.8 — Local Interstellar Flow Parameters from the First Intersection of IMAP-Lo's Parameter Tubes
- **arXiv:** [2608.14939](https://arxiv.org/abs/2608.14939)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** astrochemistry (70.8), feedback_bubbles (64.4), galactic_ism_surveys (64.2)
- **Current keyword baseline:** YES
- **BM25 max:** 51.3
- **Semantic max:** 81.4
- **Abstract:** The Sun's motion through the interstellar medium creates a flow of interstellar neutral (ISN) atoms through the heliosphere. ISN He, due to its high universal abundance and relatively low ionization rate, is the most abundant of the interstellar species near 1 au and ideal for flow parameter determination. The Interstellar Boundary Explorer (IBEX) measurements of ISN He flow parameters (speed, temperature, and direction) yielded a tube in 4D parameter space -- narrow in cross-section but highly extended along one parameter axis (e.g., ecliptic longitude direction). This ``4D parameter tube'' results in large systematic uncertainties, a direct consequence of IBEX-Lo's fixed viewing orientation on the spacecraft. On the Interstellar Mapping and Acceleration Probe (IMAP), the articulation of the IMAP-Lo boresight using its pivot platform enables multiple viewing orientations of the ISN flow for significant systematic uncertainty reduction. We provide first results that definitively intersect ISN parameter tubes for elongation angles $79^\circ$, 94$^\circ$, and 109$^\circ$, resulting in precise interstellar parameters: speed $26.37 \pm 0.82$ km s$^{-1}$, ecliptic longitude direction $74.85^\circ \pm 0.96^\circ$, ecliptic latitude direction $-5.212^\circ \pm 0.035^\circ$, and temperature $7740^{+770}_{-730}$ K. The inferred flow of the Very Local Interstellar Medium is not consistent with either the Local Interstellar Cloud or the G-Cloud, but rather an intermediate state. IMAP is now positioned to study the detailed physics of this complex, nearby interstellar region. By resolving and understanding its physics, we determine how the heliosphere responds to the local interstellar flow, and how it may evolve in time

### [B] 70.8 — ATLAS. IV. A JWST+MUSE Demographic Study of Ly$α$ Profiles in Little Red Dots
- **arXiv:** [2608.14534](https://arxiv.org/abs/2608.14534)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (70.8), ism_methods_data (69.1), astrochemistry (68.0)
- **Current keyword baseline:** NO
- **BM25 max:** 41.2
- **Semantic max:** 88.5
- **Abstract:** We present an initial demographic study of Ly$α$ profiles in little red dots (LRDs) at $z=3$--9 using $R\sim1000$--4000 spectroscopy. Our sample consists of 8 LRDs observed in the VLT/MUSE Deep and Wide surveys and 23 LRDs observed with JWST/NIRSpec grating spectroscopy from JADES, CANUCS, and GO programs including SPURS. We identify Ly$α$ emission in 5 MUSE LRDs and 9 JWST LRDs. Only two of them exhibit broad Ly$α$ emission (FWHM $>1000\ \mathrm{km\ s^{-1}}$), both reported previously. The other Ly$α$-emitting LRDs show narrow Ly$α$ emission (FWHM $<1000\ \mathrm{km\ s^{-1}}$), with FWHMs mostly in the range 300--600 $\mathrm{km\ s^{-1}}$, comparable to or slightly larger than those of high-redshift star-forming galaxies (100--500 $\mathrm{km\ s^{-1}}$). We measure the fraction of broad Ly$α$ emitters above a broad Ly$α$ luminosity threshold of $L_{\mathrm{Ly}α,\mathrm{broad}}=10^{42}\ \mathrm{erg\ s^{-1}}$, obtaining $0.10^{+0.12}_{-0.07}$ for LRDs, about five times higher than the $2σ$ upper limit of $<0.02$ for high-redshift star-forming galaxies. Although we reproduce the broad Ly$α$ component reported in a previous stacking analysis of eight LRDs, albeit with a large uncertainty, we find no evidence for broad Ly$α$ emission in either the larger JWST stack, after excluding the two individually detected broad Ly$α$ emitters, or the higher-resolution MUSE stack. These results suggest that broad Ly$α$ emission is not ubiquitous among LRDs. Instead, LRDs with broad Ly$α$ emission appear to represent a rare population that may correspond to a particular evolutionary stage, potentially associated with unusually strong outflows or other distinctive physical conditions.

### [B] 70.8 — Stellar tidal systematics in apsidal-motion searches for circumbinary planets: CH Ind and SW CMa
- **arXiv:** [2608.13269](https://arxiv.org/abs/2608.13269)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** star_formation (70.8), astrochemistry (65.5), ism_methods_data (65.2)
- **Current keyword baseline:** YES
- **BM25 max:** 30.4
- **Semantic max:** 88.5
- **Abstract:** Thornton et al. (2026) reported 27 non-transiting circumbinary-planet candidates from excess apsidal motion in TESS eclipsing-binary timings. The classical stellar contribution is sensitive to target-specific radii, apsidal constants $k_2$, and rotation. We re-evaluate two evolved, double-lined eclipsing binaries in that sample: the pulsating system CH Ind and the Am system SW CMa. Their component masses and radii have been measured in dedicated binary studies, allowing the stellar contribution to be calculated directly. For CH Ind, six independent TESS sector nodes give $\dotω_{\rm obs}=1.82^{+0.99}_{-0.94}\times10^{-3}\ {\rm deg\,cycle^{-1}}$, while a coeval fit to the measured binary components predicts $\dotω_{\rm stars}=2.05^{+0.43}_{-0.34}\times10^{-3}\ {\rm deg\,cycle^{-1}}$. For SW CMa, its measured dimensions raise the classical term by a factor of about 16; the published target-specific prediction, $0.670\pm0.020\times10^{-3}\ {\rm deg\,cycle^{-1}}$, agrees with the observed $0.690\pm0.050\times10^{-3}\ {\rm deg\,cycle^{-1}}$. Neither system shows a significant excess prograde component. The comparison shows that candidates from a bulk search require target-specific binary models before a third-body interpretation is assigned.

### [B] 70.7 — The Total and Polarized Radio Emission from the Innermost Jets of a High-Redshift Quasar and a Candidate at Parsec-Scale Resolution
- **arXiv:** [2608.18691](https://arxiv.org/abs/2608.18691)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (70.7), turbulence (68.2), magnetic_fields (64.3)
- **Current keyword baseline:** NO
- **BM25 max:** 44.2
- **Semantic max:** 88.4
- **Abstract:** High-frequency very long baseline interferometry (VLBI) polarimetry probes synchrotron-emitting plasma closer to the central engines of radio-loud active galactic nuclei (AGNs), but observations above 43 GHz are technically demanding. We present 22-GHz European VLBI Network observations of the $z=4.31$ quasar J1510+5702 and J1606+3124, whose published spectroscopic redshift, $z=4.56$, is uncertain; a photometric estimate gives $z_{\rm phot}=0.9\pm0.1$. For the published $z>4$ redshifts, 22 GHz corresponds to rest-frame frequencies above 118 GHz. Polarized emission is detected in J1510+5702, and a low-level polarized signal is recovered from the brightest feature of J1606+3124. Adopting $z=4.56$, that feature has a brightness temperature of $T_{\mathrm{b,VLBI}}=(7.4\pm0.8)\cdot10^{10}$ K, allowing a mildly Doppler-boosted interpretation, while the young compact-source scenario also remains viable. The core of J1510+5702 has $T_{\mathrm{b,VLBI}}=(1.08\pm0.15) \cdot10^{12}$ K, implying a Doppler factor of ${\sim}22$ under the equipartition assumption. This component has a ${\sim}3.5$ % fractional polarization. These observations show that cm-wavelength VLBI can access rest-frame millimeter-band polarization in bright $z>4$ jets.

### [B] 70.6 — Beyond Idealized PAHs: Infrared Signatures of Carbon-Chain Defects from Shock Synthesis
- **arXiv:** [2608.18505](https://arxiv.org/abs/2608.18505)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.IM, astro-ph.SR
- **Top topics:** ism_methods_data (70.6), molecular_clouds (69.1), turbulence (66.2)
- **Current keyword baseline:** YES
- **BM25 max:** 51.6
- **Semantic max:** 86.3
- **Abstract:** Polycyclic aromatic hydrocarbons (PAHs) are widely recognized as carriers of the aromatic infrared bands (AIBs). However, most spectral models rely on idealized structures that fail to capture the energetic environments of interstellar PAH formation. This work investigates the infrared (IR) signatures of PAHs formed under shock conditions and explores whether produced defective structures can explain observational features unpredicted by standard, idealized models. We combine two-stage reactive molecular dynamics simulations of PAH formation via condensation and shock processing with density functional theory spectral calculations, and compare our theoretical results with James Webb Space Telescope (JWST) observations of NGC 7023 and MRK 1066. Shock processing produces PAHs featuring fullerene-like carbon skeletons and linear carbon-chain attachments. These structural defects yield distinct IR signatures, including prominent carbon-chain stretching features at 4.6-5.5 micron that is absent in ideal PAHs, and significantly enhanced out-of-plane skeletal modes in the 14.5-20 micron regime. Our findings attribute the observed 5.2 micron band in NGC 7023 and MRK 1066 to carbon-chain vibrations and the 15-18 micron emission to curved skeletal modes, providing observational support for the prevalence of defective, shock-formed PAHs in the interstellar medium.

### [B] 70.6 — A chemo-dynamical search for planet-candidate hosts of possible extragalactic origin
- **arXiv:** [2608.13895](https://arxiv.org/abs/2608.13895)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.EP, astro-ph.GA
- **Top topics:** astrochemistry (70.6), galactic_ism_surveys (70.5), star_formation (63.3)
- **Current keyword baseline:** NO
- **BM25 max:** 68.3
- **Semantic max:** 88.3
- **Abstract:** To date, all known exoplanetary systems have been identified around stars currently residing in the Milky Way, whereas planets formed in external galaxies remain largely unexplored. Such systems would offer a unique probe of planet formation in galactic environments distinct from the Milky Way. We combine a literature-compiled sample of Kepler, K2, and TESS planet-candidate host stars with Gaia DR3 astrometry and radial velocities, and incorporate metallicities and [Mg/Fe] abundances from the LAMOST DR9 DD-Payne catalogue, to search for candidate accreted-halo planet hosts. We identify 11 planet-candidate hosts with halo-like kinematics, five of which have reliable chemical abundance measurements. Among these, four systems exhibit low metallicities ([Fe/H]<-0.7) and low [Mg/Fe] ratios that are inconsistent with the canonical Milky Way thick-disc sequence, indicative of enrichment histories characteristic of accreted dwarf galaxies. We further carry out a uniform false-positive assessment using Gaia RUWE, Gaia DR3 neighbourhood checks, odd--even transit-depth comparisons, secondary-eclipse searches, independent BLS period recovery, and comparison with ExoFOP and available follow-up information. This vetting identifies EPIC~211407755 and TIC~239541449 as the most plausible, although still unvalidated, planet-candidate systems. TIC~293432942 is more likely associated with a blended or otherwise binary-related false positive, whereas TIC~184739529 remains a high-risk giant-companion candidate whose planetary nature is uncertain. If confirmed, EPIC~211407755 and TIC~239541449 would suggest that planetary systems can form in dwarf-galaxy environments and subsequently survive accretion into the Milky Way.

### [B] 70.6 — JWST Detects a Dusty AGB-like Source Before the Type Ia-CSM Supernova 2026sqf
- **arXiv:** [2608.13321](https://arxiv.org/abs/2608.13321)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.HE
- **Top topics:** feedback_bubbles (70.6), star_formation (64.1), astrochemistry (58.9)
- **Current keyword baseline:** NO
- **BM25 max:** 42.6
- **Semantic max:** 81.2
- **Abstract:** Supernova (SN) 2026sqf recently appeared in the nearby face-on spiral galaxy NGC 3310 and has shown signs of strong interaction with a circumstellar medium (CSM). Such intense interaction, rare among nearby SNe, offers a valuable opportunity to reveal details on the origin and nature of its progenitor system. We analyzed the early-phase spectra and light curves (LCs) of SN 2026sqf. The general shapes of the observed spectra, the strengths of the emission lines, and the LC evolution all suggest that SN 2026sqf belongs to the rare SN Ia-CSM subclass. If confirmed, this would be the closest known member of this class, at D~19 Mpc. We also report the first candidate progenitor system for a thermonuclear supernova identified in JWST pre-explosion imaging, and the first evidence for a (probable) carbon-rich AGB donor to the exploding white dwarf (WD). Our results are consistent with the expectation that SNe Ia-CSM emerge from a system consisting of a WD and an AGB star undergoing a common-envelope phase. The CSM mass and dust content are consistent with expectations for an AGB environment, but the narrow-line width exceeds superwind expansion velocities, favoring an episodic ejection. Binary interaction shortly before the explosion is a natural explanation, though the channel and timescale remain uncertain. Late-time follow-up, especially with JWST, will test the identification and the conclusions of our early-phase analysis.

### [B] 70.5 — No Evidence for Nearby Circumstellar Material in the Type Ia Supernova 2025rbs
- **arXiv:** [2608.13655](https://arxiv.org/abs/2608.13655)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA, astro-ph.SR
- **Top topics:** astrochemistry (70.5), feedback_bubbles (69.4), star_formation (68.7)
- **Current keyword baseline:** NO
- **BM25 max:** 100.0
- **Semantic max:** 88.2
- **Abstract:** We present a high-resolution spectral time series of the Type Ia supernova (SN) 2025rbs discovered in the nearby galaxy NGC 7331. The Automated Planet Finder (APF) at Lick Observatory and the MAROON-X/IGRINS-2 at Gemini North were used to obtain echelle spectra between -5 and 15 days with respect to the epoch of maximum light. Several unsaturated NaID absorption components along the line of sight are identified, but there is no evidence of time variance in any of them. We measure the equivalent width of the observed diffuse interstellar band around 5780 A and constrain the extinction along the line of sight to SN 2025rbs as $A_V = 0.64\,\pm\,0.32$ mag, corresponding to a moderate reddening of $E(B-V) = 0.21\,\pm\,0.10$ mag (assuming $R_\mathrm{V}$ = 3.1). The observed Ca II H & K interstellar absorption roughly traces NaID in velocity space, suggesting a common origin. Quantitative comparisons between the column densities of Na and Ca gas in these host clouds ($N_{NaID}$ / $N_{Ca II}$ of order unity) argue against their origin in the Galactic halo gas and instead support absorption due to the interstellar gas of NGC 7331. Time invariance of all the observed absorption features suggests a lack of nearby circumstellar material ($\lesssim$ 10$^{16}$ cm) around the progenitor system of SN 2025rbs. This supports a progenitor scenario for SN 2025rbs with minimal ambient circumstellar gas, consistent with a double-degenerate CO white dwarf binary system.

### [B] 70.5 — Evidence for the First Globular Cluster Stellar Stream beyond the Milky Way
- **arXiv:** [2608.12254](https://arxiv.org/abs/2608.12254)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** star_formation (70.5), massive_star_formation (63.4), galactic_ism_surveys (61.5)
- **Current keyword baseline:** NO
- **BM25 max:** 51.4
- **Semantic max:** 88.1
- **Abstract:** The dark matter content of ultra-diffuse galaxies is the subject of considerable debate. Stellar streams, which form when a host galaxy tidally strips stars from an orbiting stellar system, provide a powerful technique to constrain the dark matter content of external galaxies. The stripped stars form long, thin leading and trailing tidal arms that persist for billions of years. Stellar streams from globular clusters are particularly sensitive probes of dark matter halos and substructure. Globular cluster streams are expected to exist in a variety of host galaxy types, but so far, they have only been observed in the Milky Way. We present evidence for the first extragalactic globular cluster stellar stream, identified in deep Hubble Space Telescope imaging of the ultra-diffuse galaxy, UGC9050-Dw1. The stream's morphology, colour, and apparent association with a compact source support the globular cluster progenitor interpretation observationally, and we reproduce the observed surface brightness with simulated globular cluster stellar populations. We use generative stream modelling, which fits dynamical models directly to the stream morphology, to constrain the mass of the progenitor and present the first stream-based halo constraint for an ultra-diffuse galaxy. The stream models point to a globular cluster origin and suggest a massive dark matter host halo. By extending the reach of globular cluster stream analysis to external galaxies, this work opens a new chapter in dark matter science.

### [B] 70.4 — Low Ly$α$ Visibility in Galaxy Overdensities: Reionization Topology and Neutral-Fraction Ceilings from DIVER over $4.8<z<11$
- **arXiv:** [2608.19311](https://arxiv.org/abs/2608.19311)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** astrochemistry (70.4), galactic_ism_surveys (62.9), massive_star_formation (54.4)
- **Current keyword baseline:** NO
- **BM25 max:** 51.5
- **Semantic max:** 80.9
- **Abstract:** Ly-alpha emission is widely used to trace cosmic reionization, but its interpretation depends on how Ly-alpha visibility varies with galaxy environment. We use deep JWST/NIRSpec observations from Deep Insights into UV Spectroscopy at the Epoch of Reionization (DIVER) in GOODS-N to measure Ly-alpha visibility for 250 galaxies at 4.8<z<11. The sample contains 84 Ly-alpha detections, including 44 strong emitters with rest-frame Ly-alpha equivalent width W_Lyalpha>25 A. We combine these measurements with H-alpha and [O III] emitters from JWST/NIRCam wide-field slitless spectroscopy to map the density field around each DIVER galaxy. Galaxies with high Ly-alpha equivalent widths (W_Lyalpha>25 A) or high effective Ly-alpha escape fractions (f_esc,Lyalpha^eff>0.05) tend to lie farther from nearby H-alpha and [O III] emitters than galaxies with lower Ly-alpha visibility. The clearest signal occurs near the prominent GOODS-N overdensity at z~5.2, where fewer than 15% of galaxies show strong Ly-alpha emission. This trend is opposite to the simplest inside-out reionization expectation that overdensities produce larger ionized regions and enhance Ly-alpha visibility. Possible explanations include circumgalactic and local intergalactic opacity, dense absorbers, and gas kinematics. We also derive an empirical upper envelope for f_esc,Lyalpha^eff and calibrate it with reionization simulations. Interpreting this envelope as a limiting IGM-attenuation signal gives neutral-fraction ceilings of <x_HI>_max=0.36, 0.76, 0.74, 0.84, and 1.0 at z~5.2, 5.8, 6.7, 7.7, and 9.8, respectively. The z~8 ceiling disfavors an almost completely neutral IGM at this epoch. These results support patchy reionization already underway by z~8 and show that galaxy Ly-alpha visibility encodes both large-scale ionization topology and near-source gas structure.

### [B] 70.4 — Candidates for the most [$O_{III}$] $\lambda5007$-luminous planetary nebula in the Milky Way. I. Integrated light properties of NGC 6572, NGC 6884, and M 1-71
- **arXiv:** [2608.17380](https://arxiv.org/abs/2608.17380)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** galactic_ism_surveys (70.4), atomic_ism (63.9), ism_methods_data (60.5)
- **Current keyword baseline:** NO
- **BM25 max:** 73.2
- **Semantic max:** 80.9
- **Abstract:** The bright-end cutoff of the planetary nebula luminosity function (PNLF) serves as an extragalactic standard candle. However, the physical properties of planetary nebulae (PNe) at the PNLF cutoff have been studied only in nearby galaxies, where the PNe appear mostly as point sources. Galactic PNLF is further poorly constrained, primarily due to uncertainties in Galactic PN distances. Following a recent Galactic PNLF survey based on Gaia distances, we aim to characterise PN candidates at the Galactic PNLF cutoff. We observed three PN candidates at the Galactic PNLF cutoff using the Potsdam Multi-Aperture Spectrophotometer (PMAS). We determined their chemical abundances and constructed photoionisation models to derive the central star luminosity (L) and effective temperature (Teff). We constrained the central star masses and most likely distances consistent with the prediction of stellar evolution models. Using these distances, we determined the absolute magnitude M5007. PNe of our sample are located within the top 1 mag of the Galactic PNLF (-4.20 < M5007 <-3.60), with similar nebular properties and a narrow progenitor mass range (1.30-1.75 Msolar). The measured extinction is mostly dominated by the foreground Galactic extinction. The trend between the circum-nebular extinction and central star mass of our PNe is in agreement with those derived in the Large Magellanic Cloud (LMC) and M31. All PNe in our sample exhibit weak-emission line star (wels) features in their spectra, but we confirmed that some of these lines originate from the nebula. The PNe are similar in terms of their nebular properties and evolutionary stage. Their characteristics are also consistent with the most [OIII]5007-luminous PNe in the LMC and M31. We demonstrate the importance of circum-nebular extinction and the initial-final mass relation (IFMR) to understand the universality of PNLF as a standard candle.

### [B] 70.3 — The Ultrafast Line-Driven Wind from the Double-Degenerate Merger Remnant WD J005311
- **arXiv:** [2608.19037](https://arxiv.org/abs/2608.19037)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.HE
- **Top topics:** star_formation (70.3), feedback_bubbles (70.0), ism_methods_data (60.1)
- **Current keyword baseline:** NO
- **BM25 max:** 58.4
- **Semantic max:** 80.7
- **Abstract:** We systematically construct steady-state wind solutions for double-degenerate merger remnants consisting of a degenerate oxygen-neon core and an optically thick expanding envelope powered by carbon-shell burning, with winds accelerated by radiation pressure including line driving. For a given envelope composition, each solution is characterized by two eigenvalues: the degenerate core mass, $M_{\rm WD}$, and the total envelope and wind mass, $ΔM$. We find that wind solutions exist for $M_{\rm WD} \gtrsim 1.0\,M_\odot$. For a given $M_{\rm WD}$, the solutions transition with decreasing $ΔM$ from slow, continuum-driven winds to ultrafast, line-driven winds, forming a sequence that can be interpreted as the temporal evolution of a merger remnant. We apply these solutions to WD J005311, a Galactic double-degenerate merger-remnant candidate with an ultrafast wind of $v_{\rm w} \sim 0.05\,c$. Its luminosity, effective temperature, and mass-loss rate are consistently reproduced with $M_{\rm WD} \sim 1.15-1.25\,M_\odot$ and $ΔM \sim (1.8-5.7)\times 10^{-3}\,M_\odot$. Combining our evolutionary analysis with observations of the surrounding nebula Pa 30 and historical records of SN 1181, we argue that WD J005311 began launching a continuum-driven wind $400-650$ yr after the putative merger and transitioned to the ultrafast-wind phase approximately $100$ yr ago. This phase is expected to continue for another $\sim 1000$ yr, during which the WD will remain below the Chandrasekhar mass and avoid collapse into a neutron star. Before the continuum-driven wind phase, the remnant may have passed through a more bloated, hydrostatic giant phase with a slower but more massive wind. Future observations of the wind nebula could test this scenario by revealing signatures of interactions between the slow, massive wind and the ultrafast wind.

### [B] 70.3 — Safe Domain Adaptation for Physics: Overcoming Nuisances, Label Shifts, and Simulation Priors
- **arXiv:** [2608.18190](https://arxiv.org/abs/2608.18190)
- **Primary category:** cs.LG
- **Categories:** cs.LG, astro-ph.IM, physics.data-an
- **Top topics:** ism_methods_data (70.3), star_formation (55.6), astrochemistry (54.0)
- **Current keyword baseline:** NO
- **BM25 max:** 33.3
- **Semantic max:** 87.9
- **Abstract:** Domain adaptation is widely used to make neural networks trained on simulations applicable to experimental data. Its premise is that the two domains differ only in nuisances, and that the quantity of interest is distributed identically in both. In physics neither assumption holds: simulations can be wrong about the physics, and the distribution of the target quantity - an energy spectrum, a redshift distribution - is often the measurement itself. We study the consequences of such mismatches on a toy air-shower benchmark in which a detector-response nuisance, a physical simulation shift, and an energy-spectrum shift can be switched on separately or together. Standard adversarial adaptation handles the conditional shifts, but once the two spectra differ it aligns them, replacing an uncontrolled bias by one anchored on the simulation prior. We present adaptive domain adaptation, which reweights the simulated events so as to focus domain adaptation on the genuine physical mismatch alone. Since the predicted spectrum depends on model training configuration, we provide a label-free model selection rule for selecting the near-the-best operation point.

### [B] 70.2 — A dual-polarization whitened-template trigger for real-time radio detection of extensive air showers
- **arXiv:** [2608.19898](https://arxiv.org/abs/2608.19898)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (70.2), turbulence (60.4), feedback_bubbles (58.6)
- **Current keyword baseline:** NO
- **BM25 max:** 32.1
- **Semantic max:** 87.8
- **Abstract:** Autonomous radio stations require a first-stage trigger that rejects measured background while preserving weak extensive-air-shower pulses under tight hardware constraints. We present a dual-polarization trigger based on a 16-sample whitened pulse template evaluated continuously on the orthogonal north-south and east-west channels of an Auger Engineering Radio Array station. The template is derived from detector-folded air-shower pulses and whitened using the covariance of measured background. Responses from both polarizations are combined within a fixed timing radius and compared with a calibrated threshold. On an independent test set, the trigger reaches an efficiency of 0.97, with a 95 percent confidence interval of 0.96 to 0.98, at a frame-equivalent candidate rate of 3.39 kHz. At the same operating point, an unwhitened dual-polarization template reaches 0.41 efficiency and an amplitude trigger reaches 0.16. Efficiency remains at least 0.94 in every populated signal-to-noise bin. Replay of 159.29 ms of continuous measured background yields a score-cluster rate of 6.64 kHz, below the 71.4 kHz capacity of the downstream module. The FPGA implementation accepts one dual-polarization sample per clock, closes timing at 200 MHz, and uses 2377 lookup tables, 5330 registers, and 32 digital signal-processing blocks. Register-transfer-level simulation agrees bit for bit with the reference implementation for 400 traces. These results show that background covariance, pulse morphology, and dual-polarization consistency can be combined in a compact real-time radio trigger.

### [B] 70.2 — Optical Spectroscopy of TeV-emitting BL Lac Candidates
- **arXiv:** [2608.14412](https://arxiv.org/abs/2608.14412)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (70.2), astrochemistry (59.1), magnetic_fields (57.7)
- **Current keyword baseline:** NO
- **BM25 max:** 64.9
- **Semantic max:** 80.7
- **Abstract:** TeV-emitting BL Lacertae (BL Lac) blazars have important implications for the study of jet phenomenology, particle acceleration, and ultra high-energy cosmic ray production. They also allow for indirect studies of the extragalactic background light, cosmic magnetic fields, and axion-like particles. The upcoming Cherenkov Telescope Array (CTA), a ground-based gamma-ray observatory, will expand the observed TeV-emitting BL Lac population and enhance the aforementioned fields of study. However, reliable redshifts are crucial for planning and interpreting observations with CTA and only about 50% of gamma-ray BL Lacs have spectroscopic redshifts. We performed medium resolution optical spectroscopy of 16 TeV-emitting BL Lac candidates with the SALT and MDM telescopes. We measured spectroscopic redshifts for the full sample, ranging from 0.059 to 0.4, including 5 new spectroscopic redshift measurements.

### [B] 70.1 — Panchromatic JWST Observations and Models of the Dim Type Iax Supernova 2024vjm at 200 days
- **arXiv:** [2608.15040](https://arxiv.org/abs/2608.15040)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.HE
- **Top topics:** astrochemistry (70.1), ism_methods_data (65.6), feedback_bubbles (64.1)
- **Current keyword baseline:** YES
- **BM25 max:** 59.8
- **Semantic max:** 82.0
- **Abstract:** We report JWST spectra and photometry of the underluminous SN Iax 2024vjm obtained 202.8 restframe days post-explosion. The spectrum exhibits a rich set of forbidden lines from low-ionization, intermediate-mass, and iron-group elements, notably the [Ni II] 6.64 micron resonance line, which is a direct indicator of stable nickel. Strong CO and SiO emission is detected alongside a warm dust continuum; the spectral properties are consistent with pre-existing rather than newly formed dust. Synthetic spectra were computed with the generalized stellar atmospheres code PHOENIX/1D using simplified ejecta models. The models reproduce the overall spectral energy distribution and the molecular emission features reasonably well, but substantially underestimate the strength of the mid-infrared atomic forbidden lines, leaving the synthetic spectrum dominated by molecular emission. Experiments in which the molecular opacity is suppressed do not recover the forbidden lines; instead, the emission peak migrates to Co and Fe transitions near 2 microns. We attribute this discrepancy to poorly constrained collisional rates and possibly to an excess of iron-group material in the current ejecta models. A prominent feature at 12.8 microns is not well accounted for by the [Ne II] 12.81 micron line, indicating that the 12.8 micron feature may be largely due to [Fe III]. The presence of CO, SiO, and stable nickel together with the non-detection of neon places tight constraints on the total ejecta mass and the nucleosynthetic yields of SNe Iax progenitor systems.

### [B] 70.0 — Wet Removal and Cloud Enhancement: The Microphysics of Cloud-Haze Interactions on Sub-Neptunes
- **arXiv:** [2608.19100](https://arxiv.org/abs/2608.19100)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** star_formation (70.0), molecular_clouds (63.1), feedback_bubbles (61.8)
- **Current keyword baseline:** NO
- **BM25 max:** 58.1
- **Semantic max:** 87.5
- **Abstract:** Aerosols are a near-ubiquitous feature of sub-Neptune atmospheres, yet their microphysical nature remains poorly understood. Both condensate clouds and photochemical hazes have been proposed to explain observations, but have largely been studied in isolation. Here we present a new bin-scheme microphysical model, adapted from CARMA, that couples cloud and haze formation through heterogeneous nucleation - the dominant mode of cloud formation in the Solar System - in which haze particles act as cloud condensation nuclei (CCN). Applying this model to KCl clouds on GJ 1214 b-like warm sub-Neptunes, we find that the microphysical contact angle $θ$ between cloud and haze particles governs distinct regimes of aerosol behavior: at moderate contact angles ($25^\circ \lesssim θ\lesssim 70^\circ$), hazes are efficiently removed from the upper atmosphere through "wet removal" as they seed gravitationally-settling clouds; at small contact angles ($θ\lesssim 25^\circ$), heterogeneous nucleation instead produces an enhanced population of mixed cloud-haze particles at high altitudes, dramatically increasing aerosol optical depth ("cloud enhancement"). These structural changes produce differences of up to four scale heights in transmission spectra, with strong effects at optical and near-infrared wavelengths relevant to JWST NIRISS/SOSS, while wavelengths beyond about 3 microns remain comparatively unaffected. We map these effects across orders of magnitude in metallicity, haze production rate, and vertical mixing strength, establishing their generality across sub-Neptune parameter space. Because heterogeneous nucleation is a universal phase-change process, this framework extends naturally to other exoplanet atmospheres and potentially any astrophysical environments where condensation onto foreign substrates may occur, including protoplanetary disks and stellar outflows.

### [B] 70.0 — Revised $^{45}$V($p,γ$)$^{46}$Cr reaction rate and its impact on the production of $^{44}$Ti in core-collapse supernovae
- **arXiv:** [2608.17757](https://arxiv.org/abs/2608.17757)
- **Primary category:** nucl-ex
- **Categories:** nucl-ex, astro-ph.HE, astro-ph.SR, nucl-th
- **Top topics:** feedback_bubbles (70.0), star_formation (65.5), ism_methods_data (63.5)
- **Current keyword baseline:** YES
- **BM25 max:** 28.4
- **Semantic max:** 80.5
- **Abstract:** The thermonuclear $^{45}$V($p,γ$)$^{46}$Cr reaction is the primary leakage pathway from the $^{44}$Ti--$^{45}$V quasi-equilibrium cluster during $α$-rich freeze-out in core-collapse supernovae (CCSN), governing the final abundance of the $γ$-ray-emitting isotope $^{44}$Ti. A recent high-resolution $γ$-ray study [C. Cousins \textit{et al.}, Phys. Rev. Lett. 136, 252701 (2026)] identified ten previously unknown low-spin proton-unbound states in $^{46}$Cr, enabling the first experimentally constrained $^{45}$V($p,γ$)$^{46}$Cr reaction rate using the AME2020 mass excess, $\text{ME}(^{46}\text{Cr}) = -29472(11)$~keV. Here, we adopt the four-fold more precise CSRe mass excess $\text{ME}(^{46}\text{Cr}) = -29477.2(2.6)$~keV [M.~Wang \textit{et al.}, Phys. Rev. C \textbf{106}, L051301 (2022)] to recalculate the reaction rate. Including proton capture on the ground and first two excited states of $^{45}$V alongside new shell-model proton spectroscopic factors, we reduce mass-related rate uncertainties to a subdominant level. The revised rate is up to 69% higher than that of Cousins \textit{et al.} at $α$-rich freeze-out temperatures ($T \simeq 1.5$--$2$~GK). CCSN nucleosynthesis calculations show this revised rate increases the ejected $^{44}$Ti yield by $\sim$26% in a $20\,M_\odot$ model compared to The \textit{et al.} [ApJ \textbf{504}, 500 (1998)], while causing negligible changes for the SN~1987A trajectory. We demonstrate that $^{44}$Ti production sensitivity is dictated by the ejecta electron fraction ($Y_e$): the reaction significantly affects proton-rich ejecta ($Y_e \approx 0.50$) but has little impact on neutron-rich ejecta ($Y_e \approx 0.496$), where lower free-proton abundances suppress reaction flow. This reconciles conflicting results from past sensitivity studies.

### [B] 70.0 — Eclipse Timing of the Eccentric Planet HD 80606b with JWST: Constraints on a Second Planet and other Dynamical Effects
- **arXiv:** [2608.16816](https://arxiv.org/abs/2608.16816)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** star_formation (70.0), astrochemistry (55.6), magnetic_fields (55.4)
- **Current keyword baseline:** NO
- **BM25 max:** 41.1
- **Semantic max:** 87.5
- **Abstract:** A variety of effects can perturb the orbital properties of single planets in close orbits around their host stars. HD80606 b is a highly eccentric ($ε$=0.93) exoplanet orbiting its host G5V star, HD80606. HD80606 b became a compelling target for exoplanet research after (Laughlin et al 2009) discovered that the 4.16 MJup planet transits and is eclipsed by HD80606, thereby enabling photometric and spectroscopic observations to yield a wealth of information about the object. The exquisite precision of recent JWST eclipse timing offers an opportunity to investigate whether the orbit of HD80606 b is modified due to a variety of mechanisms, including General Relativity, tidal torques, or the presence of a second perturbing planet. We have used over 25 years of radial velocity data plus eclipse and transit observations to place limits on the precession of HD80606 b's orbit and to assess which of these effects, if any, are observable. The new models are consistent with constant values of period, eccentricity and the argument of periastron, $ω$, with a limit on $\dotω$ at the level of the predicted GR drift. The PRV and timing data limit the mass and location of a second planet external to HD80606b. Timing offsets between JWST eclipses relative to the Pearson et al (2022) predictions are attributed to the poor constraints on $\sqrtε (\cos\ ω, \sin\ ω)$ with only the single eclipse measurement available (Spitzer 2009) in that analysis and to an over-weighting of the eclipse timing in that earlier analysis.

### [B] 69.8 — NMMA-Astro-COLIBRI: An Automated Light-Curve Supernovae Classification Service in the Multi-Survey Era
- **arXiv:** [2608.17568](https://arxiv.org/abs/2608.17568)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.IM
- **Top topics:** ism_methods_data (69.8), feedback_bubbles (63.5), star_formation (60.0)
- **Current keyword baseline:** NO
- **BM25 max:** 33.6
- **Semantic max:** 80.2
- **Abstract:** The surge in publicly available photometric alerts from wide-field surveys requires automated tools for real-time transient classification. We present NMMA--Astro-COLIBRI, an on-demand Bayesian classification service that couples the Nuclear-physics and Multi-Messenger Astrophysics (NMMA) inference framework to the Astro-COLIBRI real-time multi-messenger platform. After the detection of an optical transient, if photometry is available, it is quality-filtered. The filtered photometry is fitted by nested sampling against a user-selected model from a library of eleven supernova templates; results are delivered to every user within minutes. Applying two or more models on the same optical transient, the service reports the corresponding log Bayes factors as a quantitative ranking of competing subtypes. We demonstrate the workflow on SN 2021ugl (ZTF21abotose), a Type IIb supernova initially mistaken for a kilonova candidate by automated real-time pipelines, comparing competing supernova and kilonova models. In an early-time configuration using only the first ~ 6 days of photometry in two bands (ZTF g and r), so ten days before spectroscopic confirmation, the empirical Type IIb template recovers the correct classification, favored over both the kilonova template and the kilonova-mimicking shock-cooling model. In the full 47-day, three-band baseline, it again achieves the highest evidence over every competing supernova and kilonova template. These results highlight the importance of a comprehensive supernova template library for kilonova discrimination in the multi-survey era.

### [B] 69.7 — Gal3D: Superellipsoid Modeling of Radial 3D Galaxy Structure in IllustrisTNG and EAGLE Simulations
- **arXiv:** [2608.12933](https://arxiv.org/abs/2608.12933)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (69.7), feedback_bubbles (56.6), astrochemistry (56.1)
- **Current keyword baseline:** NO
- **BM25 max:** 49.8
- **Semantic max:** 87.2
- **Abstract:** Galaxy morphology and structure are key tracers of galaxy formation and evolution, making accurate measurements of intrinsic three-dimensional (3D) shape essential for linking morphology to galaxy assembly and for comparing numerical simulations. We present Gal3D, a framework that reconstructs smoothed density fields from particle data and quantifies the radial 3D structure of simulated galaxies by fitting superellipsoids to iso-density surfaces. The method recovers axis ratios, orientations, center offsets, and superellipsoid indices ($S_a$, $S_b$, $S_c$), enabling a flexible characterization of diverse galactic structures such as disks, classical bulges, box/peanut bulges, and triaxial components. Applying Gal3D to galaxies in the IllustrisTNG and EAGLE simulations, we find that the radial extent of flattened disk regions increases with stellar mass up to $M_{*,30}\sim10^{11}\,M_\odot$ and then declines sharply, with EAGLE galaxies showing a saturation at $M_{*,30}\sim10^{10.5}\,M_\odot$. The bar-related $ \varepsilon_{ab}\equiv 1-b/a$ strengthens above $M_{*,30}\sim10^{10.5}\,M_\odot$ in both simulations, but remains systematically weaker in EAGLE. In TNG, outer bar regions are commonly associated with elevated $S_a$ and $S_c$, indicating enhanced boxiness and more prominent box/peanut-shaped bulges, whereas such higher-order signatures are weak or absent in EAGLE. At the highest stellar masses, flattened disks become less prominent, while inner prolate or triaxial structures remain common and massive EAGLE galaxies have more prolate or triaxial outer stellar bodies than their TNG counterparts. These results demonstrate that Gal3D provides a practical framework for quantifying intrinsic radial 3D structure and comparing morphology across cosmological simulations.

### [B] 69.6 — Accretion of AGN Stars under Influence of Disk Geometry II: The Adiabatic Regime and Runaway Collapse Induced by Self-gravity
- **arXiv:** [2608.18249](https://arxiv.org/abs/2608.18249)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.EP, astro-ph.HE, astro-ph.SR
- **Top topics:** star_formation (69.6), feedback_bubbles (62.0), galactic_ism_surveys (54.9)
- **Current keyword baseline:** NO
- **BM25 max:** 56.8
- **Semantic max:** 77.4
- **Abstract:** Accretion onto massive stars embedded in Active Galactic Nuclei (AGN) disks around supermassive black holes (SMBHs) is regulated to the stellar Eddington rate in the fast-diffusion or radiatively-efficient limit, $c/τ> c_s$, where $τ$ is the optical depth of the accretion flow and $c_s$ the sound speed. However, when the ambient density is sufficiently high, the opposite slow-diffusion limit applies. In this regime, accretion proceeds quasi-adiabatically and forms a hydrostatic circumstellar envelope (CSE) that stalls further mass inflow in the absence of self-gravity. We perform 3D hydrodynamic simulations in the adiabatic limit to investigate the structure and evolution of such envelopes. For low thermal mass ratios, $q_{\rm th} \equiv M_\star/M_{\rm th}$ where $M_{\rm th}=c_s^3/(GΩ)$ is the thermal mass, the CSE boundary smoothly matches the ambient disk entropy and density without forming a shock. In contrast, when $q_{\rm th} \gg 1$, a strong shock develops at the envelope boundary, substantially increasing the entropy of the envelope and thereby regulating its structure and mass, $M_{\rm env}$. In marginally self-gravitating disks with Toomre parameter $Q \sim 1$, we find that at sufficiently large $q_{\rm th}$ the envelope mass satisfies $M_{\rm env}/M_\star \gtrsim 1$. This condition is equivalent to stating that the post-shock material entering the envelope possesses lower radiation entropy than the characteristic stellar value, which triggers dynamical runaway growth on a dynamical timescale once envelope self-gravity is included in our simulations. In realistic AGN disk environments with SMBH mass $\sim 10^8M_\odot$, runaway may occur close to the minimum self-gravitating radii and produce supermassive stars of $\sim 10^5M_\odot$.

### [B] 69.6 — Stability of circumbinary orbits in misaligned triple star systems
- **arXiv:** [2608.15316](https://arxiv.org/abs/2608.15316)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** star_formation (69.6), feedback_bubbles (56.0), magnetic_fields (54.1)
- **Current keyword baseline:** YES
- **BM25 max:** 36.9
- **Semantic max:** 87.0
- **Abstract:** We investigate the stability of circumbinary orbits in hierarchical triple star systems, focusing on the effects of a misaligned outer companion star. Test particles are subject to competing gravitational torques from the inner binary and the outer binary companion. With secular theory we estimate the outer radius of particle stability, where the torques balance. We find good agreement with $n$-body simulations across a wide range of triple star configurations. Stable circumbinary orbits can exist even in strongly misaligned triples. Polar and highly inclined orbits with respect to the inner binary can remain stable over a substantial radial range, which is insensitive to the triple star misalignment. Orbits that are close to coplanar or retrograde coplanar to the inner binary are more susceptible to instability when the mutual inclination between the binaries is large. These findings indicate that misaligned and polar circumbinary disks and planets can survive in triple star systems under a broad set of conditions. The analytic criterion identifies where stable material may exist, with implications for the formation and detection of circumbinary planets in multiple-star systems.

### [B] 69.5 — A self-consistent solar coronal heating model by Alfvenic waves
- **arXiv:** [2608.15221](https://arxiv.org/abs/2608.15221)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, physics.plasm-ph
- **Top topics:** magnetic_fields (69.5), feedback_bubbles (56.1), turbulence (56.0)
- **Current keyword baseline:** NO
- **BM25 max:** 99.7
- **Semantic max:** 71.0
- **Abstract:** Alfvenic waves are prevalent throughout the solar atmosphere and are believed to play an essential role in coronal heating, classified as alternating current (AC) heating in contrast to direct current (DC) heating associated with quasi-static magnetic field line braiding. The relative importance of AC versus DC heating depends on the details of the photospheric driver and on the configuration of the magnetic field. Moreover, even if AC heating prevails, several wave dissipation mechanisms have been proposed, and which of them dominates remains unclear, as its efficiency depends on plasma compressibility and density inhomogeneity. We address these issues by performing three-dimensional radiative magnetohydrodynamic (MHD) simulations of a coronal loop spanning from the upper convection zone to the corona, which self-consistently capture many relevant physical processes. We find that the corona is predominantly heated by AC heating, with Alfven wave turbulence providing the primary contribution, accounting for at least 80% of the entire coronal heating in the present simulation. Our results strongly support the use of Alfven wave turbulence-based models employed in space weather and stellar activity research, such as the Alfven Wave Solar Model (AWSoM) and the Magnetohydrodynamic Algorithm outside a Sphere (MAS).

### [B] 69.5 — Magnetoacoustic Portals in Quiet-Sun Fluxtubes Revealed by Chromospheric Spectropolarimetry with SUNRISE III/SCIP
- **arXiv:** [2608.14192](https://arxiv.org/abs/2608.14192)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** magnetic_fields (69.5), feedback_bubbles (62.3), ism_methods_data (56.6)
- **Current keyword baseline:** NO
- **BM25 max:** 76.4
- **Semantic max:** 79.8
- **Abstract:** Acoustic waves propagate into the chromosphere, contributing to energy transport and their dynamics. Their upward propagation is restricted to frequencies above the acoustic cutoff frequency. The magnetic field configuration plays a key role in determining whether acoustic waves can propagate upward because the cutoff frequency is reduced in regions where the field is inclined with respect to gravity, forming so-called magnetoacoustic portals. Previous studies linked magnetic fields and oscillations in quiet regions, but these analyses were based on photospheric magnetic field information, leaving chromospheric structure unconstrained. This study investigates the coupling between acoustic waves and magnetic topology using photospheric and, for the first time, chromospheric spectropolarimetry in a quiet region, obtained with the Sunrise Chromospheric Infrared SpectroPolarimeter (SCIP) aboard the Sunrise iii balloon-borne solar observatory launched in 2024. The SCIP sit-and-stare observations sampled magnetic features in which the line-of-sight field strength exhibits multiple sharp spatial peaks in the photosphere while becoming broader and weaker at two heights in the chromosphere, indicating expanding fluxtubes. The chromospheric velocity field in these fluxtubes exhibits strong 5-minute oscillations, while the surrounding regions show weak 3-minute oscillations. In these fluxtubes, sawtooth temporal velocity variations are associated with intensity enhancements, suggesting steepened shocks. Fluxtubes with low-frequency oscillations are identified not only in network regions but also in weak internetwork regions. These results provide observational evidence that fluxtubes expanding into the chromosphere act as magnetoacoustic portals, in both network and internetwork regions, allowing low-frequency waves to propagate upward and driving chromospheric dynamics via shocks.

### [B] 69.4 — The CMZ Asymmetries: Feeding or Feedback?
- **arXiv:** [2608.13734](https://arxiv.org/abs/2608.13734)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (69.4), feedback_bubbles (53.3), galactic_ism_surveys (52.5)
- **Current keyword baseline:** YES
- **BM25 max:** 71.3
- **Semantic max:** 74.5
- **Abstract:** Three-fourths of the dense gas and dust in the CMZ is located at positive longitudes and positive radial velocities. The majority of compact 24 micrometer wavelength sources are at negative longitudes. These two asymmetries indicate either a recent asymmetric injection of gas along the bar dust lanes, or that most of the molecular gas is contained in a small number of massive, gravitationally bound clouds, or a major feedback episode which dissociated an entire sector of the CMZ's dense gas.

### [B] 69.4 — Astronomical Cardiology II: A Search For Heartbeat Stars Using APOGEE and TESS
- **arXiv:** [2608.12474](https://arxiv.org/abs/2608.12474)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** star_formation (69.4), astrochemistry (60.0), feedback_bubbles (59.1)
- **Current keyword baseline:** YES
- **BM25 max:** 37.0
- **Semantic max:** 86.7
- **Abstract:** Stellar binaries in short-period, highly eccentric systems with significant tidal deformations near pericenter, also known as heartbeat stars, are a laboratory for studying dynamical tides and oscillations in stars. We identify 50 heartbeat stars using TESS light curves of stars identified as binaries using SDSS APOGEE. We fit their phase-folded TESS light curves with an analytic model to measure their orbital periods, eccentricities, inclinations, and arguments of periastron. We measure the mass function of targets with enough APOGEE radial velocity observations to obtain a constraint on the secondary mass. We confirm our previous results that the non-giant heartbeat stars have started to evolve off the main sequence and that the fraction of (near) main sequence binaries that are heartbeat stars rises rapidly with effective temperature.

### [B] 69.3 — Heating Up the Black Hole X-ray Binary Accretion Disk by Superradiance
- **arXiv:** [2608.18200](https://arxiv.org/abs/2608.18200)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, hep-ph
- **Top topics:** ism_methods_data (69.3), atomic_ism (59.8), star_formation (59.1)
- **Current keyword baseline:** NO
- **BM25 max:** 37.4
- **Semantic max:** 86.6
- **Abstract:** A superradiant cloud of ultralight axions around a black hole, that is part of an X-ray binary system, can heat up its accretion disk and be detected by the thermal X-ray spectrum emitted by the disk. We consider a derivative coupling of the axions to the plasma fermions and calculate the emissivity of the inverse bremsstrahlung process that results in a temperature fluctuation of the disk. Based on the thin-disk model and the multicolor disk model, we derive the thermal spectrum with axion heating, which shows an enhanced thermal photon flux and a red-/blue- shifted peak spectral frequency. A single bump hunting search of the axion heating signature in the thermal spectrum of a $10M_\odot$ black hole X-ray binary with a spectral measurement sensitivity of 10\% (1\%) can derive the constraint on axion-electron coupling $|g_{ae}|\gtrsim7.5\times 10^{-12} ~(2.4 \times 10^{-12})$ for axion mass $m_a=5.2\times 10^{-12}\,$eV in a saturated $|211\rangle$ state, and $|g_{ae}|\gtrsim4.5\times 10^{-12} ~(1.4 \times 10^{-12})$ for axion mass $m_a=1.0\times10^{-11}\,$eV in a saturated $|322\rangle$ state. The projected sensitivities are competitive with those from XENONnT. A detailed continuum fitting can further improve the detectability and provide a complementary bound to the black hole spin-down measurement.

### [B] 69.3 — Improved constraints on the Milky Way potential using the M68 stream and DESI spectroscopic data
- **arXiv:** [2608.15334](https://arxiv.org/abs/2608.15334)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (69.3), star_formation (66.9), astrochemistry (66.4)
- **Current keyword baseline:** NO
- **BM25 max:** 81.4
- **Semantic max:** 83.7
- **Abstract:** We present a selection of stars belonging to the stellar stream of the M68 (NGC 4590) globular cluster, also known as Fjörm. This star selection is an improvement on previous ones that used only Gaia data, as it incorporates spectroscopic measurements from the DESI survey and photometric data from the DESI Legacy Surveys. The selection contains 96 stars, each with five phase-space parameters from Gaia-DR3 and radial velocity from DESI, covering the entire observed section of the stream. This constitutes the largest selection of M68 stream stars with measured radial velocities to date. The observed stream is wider than expected from N-body simulations, and the stars farthest from the centre of the stream appear to be correlated in radial velocity space. This suggests that these stars cannot have been stripped from the cluster in a static axisymmetric potential. By modelling a mock sample of stream stars created using an N-body simulation, we found that we could reliably constrain the disc mass $M_{\rm d}$ and the dark matter halo axis ratio $q_{\rm h}$ of the Milky Way. This is because the stream flows close to and almost parallel to the disc. Using the 44 stars that are consistent with having been stripped from the cluster, combined with measurements of the Milky Way's rotation curve, we constrain the Galactic potential, obtaining $M_{\rm d} = 5.34 \pm 0.57 \times 10^{10}$ M$_{\rm sun}$ and an oblate halo of $q_{\rm h} = 0.83^{+0.06}_{-0.05}$. Additionally, by fitting the stream track, we estimate the Heliocentric distance of M68 to be $r=10.55\pm0.09$ kpc.

### [B] 69.3 — AT 2024qfm: a luminous fast blue optical transient at a redshift of z = 0.2267 identified by Lasair-ZTF
- **arXiv:** [2608.13003](https://arxiv.org/abs/2608.13003)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (69.3), molecular_clouds (61.6), star_formation (61.2)
- **Current keyword baseline:** NO
- **BM25 max:** 31.4
- **Semantic max:** 79.6
- **Abstract:** Luminous fast blue optical transients (LFBOTs) emit from x-ray to radio wavelengths, epitomised by the discovery of AT 2018cow in a host galaxy at 65 Mpc. In the following eight years eleven more have been found, at redshifts $0.075 \lesssim z \lesssim0.34$, plus one identified retrospectively from 2016. Here we present the discovery of AT 2024qfm, classified as an LFBOT in a host galaxy at $z = 0.2267 \pm 0.0002$. Its ultraviolet-to-optical luminosity and rapid 13 day fade closely match AT 2018cow. We describe how the transient was identified in the Zwicky Transient Facility alert stream using a custom filter in the Lasair broker that flags flux gradients over time. Another LFBOT candidate was identified with the same methodology (AT 2024kth). The physical origin of LFBOTs remains debated with no firm consensus, and further progress requires more discoveries, host-galaxy characterisation, and multi-wavelength analysis to constrain theory. We discuss this discovery in the context of Rubin Observatory's Legacy Survey of Space and Time (LSST), whose sensitivity will increase the effective LFBOT survey volume tenfold relative to ZTF, out to $z \lesssim 0.6$, and show that our FastFinder filter could recover such events. We highlight the challenge of detecting their fast evolution with sufficiently low latency to trigger multi-wavelength follow-up that can constrain theoretical models.

### [B] 69.2 — A Catalog of Homogeneously Derived Stellar Parameters for Spectroscopic Survey Stars
- **arXiv:** [2608.17734](https://arxiv.org/abs/2608.17734)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.EP
- **Top topics:** ism_methods_data (69.2), astrochemistry (64.5), star_formation (54.8)
- **Current keyword baseline:** YES
- **BM25 max:** 48.1
- **Semantic max:** 80.6
- **Abstract:** Uniformly derived stellar parameters are vital for exoplanet demographic studies because they directly influence the inferred planetary masses, radii, and bulk densities. This study presents a new homogeneous catalog of physical stellar parameters for 5533 single stars observed by the HARPS, HIRES, and CARMENES radial-velocity (RV) surveys. Stellar parameters are determined using a Bayesian framework with two independent sets of stellar evolutionary models: MIST and PARSEC, using published spectroscopic parameter estimates and catalog values as priors. The resulting stellar effective temperatures, masses, radii, and surface gravities are compared and evaluated for consistency with stellar parameters listed in major exoplanet catalogs. While our estimates show consistency with those listed in external catalogs, we identify method-dependent differences in stellar masses for low-mass and pre-main-sequence stars, as well as G and K giants, where isochrone-based solutions may be affected by age-mass degeneracies. For low-mass stars such as M-dwarfs, the catalog provides masses derived from established mass-luminosity empirical relations, which tend to be more reliable. This catalog provides the largest uniformly derived stellar reference sample for Doppler survey targets and also illustrates the applicability and limitations of stellar-parameter homogenisation methods for future RV exoplanet demographics studies.

### [B] 69.1 — Strict Limits on Helium Absorption from LHS 1140 b from Four JWST NIRISS Transits
- **arXiv:** [2608.13470](https://arxiv.org/abs/2608.13470)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** ism_methods_data (69.1), star_formation (67.0), molecular_clouds (60.8)
- **Current keyword baseline:** NO
- **BM25 max:** 37.7
- **Semantic max:** 86.3
- **Abstract:** Orbiting in the habitable zone of its host star, the 1.7 $R_\oplus$, 5.6 $M_\oplus$ planet LHS 1140 b is a target of great interest. Recently Cherubim et al. (2026) published a detection of metastable He escaping from the atmosphere of LHS 1140 b, simultaneously providing the first concrete inference of an atmosphere on this planet and indicating that the atmosphere is He-rich and H-poor as would be expected due to Gyrs of fractionated mass loss. In this work, we analyze four archival transits of LHS 1140 b, spanning Dec 2023 to Jul 2026, taken with the NIRISS instrument on JWST, for evidence of He absorption. Each of the four visits disfavours the presence of He absorption compared to a flat continuum with odds ratios ranging from 3.9--11.6:1. He absorption with an amplitude and width equivalent to that observed by Cherubim et al. (2026) is strongly ruled out by the data with odds ratios from 300--8.6$\times$10$^4$:1 compared to a flat continuum --- though it should be noted that none of the JWST transits are contemporaneous with the Cherubim et al. (2026) detection. We also fit the absolute out-of-transit stellar spectra from these four visits, as well as an additional JWST NIRISS transit of planet c, to search for evidence of stellar variability, but find consistent photosphere and herterogeneity parameters in all five datasets. In all, our work provides a set of strict limits on He escape from LHS 1140 b that will be valuable to future studies into the nature and evolution of this intriguing world.

### [B] 69.0 — The Roman Coronagraph Community Participation Program: trials and triumphs of designing an observing program for a technology demonstration instrument
- **arXiv:** [2608.17077](https://arxiv.org/abs/2608.17077)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (69.0), molecular_clouds (65.7), astrochemistry (63.7)
- **Current keyword baseline:** NO
- **BM25 max:** 31.5
- **Semantic max:** 82.1
- **Abstract:** The Coronagraph Instrument onboard the Nancy Grace Roman Space Telescope serves as a crucial technology pathfinder for the Habitable Worlds Observatory, with on-sky verification of high-contrast imaging techniques and the potential to image a Jupiter analog in reflected light for the first time. Together with the Roman Project Team, the Community Participation Program (CPP) is responsible for target selection, preparatory observations, developing an exposure time calculator, target database, data reduction pipeline, simulation tools, and engagement with the broader community. Here we present an overview of the CPP activities over the past two years with an emphasis on observation planning activities for the initial in-orbit checkout and the first six months of the observation phase. Finally, we present future opportunities for the astronomical community to interact with the data as it becomes public early in the mission.

### [B] 69.0 — SN 2023gfo: A Peculiar Type IIP Supernova with High Luminosity and Normal Plateau Duration
- **arXiv:** [2608.16006](https://arxiv.org/abs/2608.16006)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA, astro-ph.SR
- **Top topics:** feedback_bubbles (69.0), star_formation (67.6), molecular_clouds (55.1)
- **Current keyword baseline:** YES
- **BM25 max:** 43.1
- **Semantic max:** 84.5
- **Abstract:** We present near-infrared (NIR) and optical observations of the highly reddened Type IIP supernova (SN) 2023gfo in the nearby galaxy NGC 4995 ($d = 26.4 \pm 3.2$ Mpc), which reached a high peak luminosity of $M_V = -18.6$ mag. The SN was initially detected as a faint red event, with $B-V = 0.8$ mag at the beginning of the plateau phase. By comparison with template, we estimate a total extinction of $A_V = 2.1$ mag. After correcting for this extinction, we derive a peak quasi-bolometric luminosity of $(5.9 \pm 1.5)\times10^{42}$ erg s$^{-1}$, placing this event among the most luminous SNe IIP, while its plateau duration remains within the normal range. The early-phase optical spectrum exhibits a P-Cygni profile of H$α$, with a broad absorption of $V$ = $13{,}800$ km s$^{-1}$, which is among the highest observed for SNe IIP at comparable epochs. The high luminosity and the normal plateau duration suggest that this event represents an outlier. Applying an analytical model, we infer an unusually large progenitor radius. This may indicate that the progenitor experienced an extreme energy injection from the core to the envelope shortly before explosion, resulting in a substantially inflated radius. While ejecta-circumstellar matter (CSM) interaction could in principle account for the high luminosity, we find no observational evidence supporting strong interaction.

### [B] 68.9 — Quadrupole White-light Sources in an X1.2 Flare Observed by ASO-S/LST/WST and SDO/HMI
- **arXiv:** [2608.18980](https://arxiv.org/abs/2608.18980)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** feedback_bubbles (68.9), molecular_clouds (61.5), astrochemistry (57.0)
- **Current keyword baseline:** NO
- **BM25 max:** 55.8
- **Semantic max:** 86.1
- **Abstract:** We present observations of an X1.2 white-light flare on 2023 January 6, which exhibits a rare quadrupolar white-light source configuration. This event was observed by the White-light Solar Telescope (WST; 3600 Å) aboard the Advanced Space-based Solar Observatory and the Helioseismic and Magnetic Imager (HMI; 6173 Å) aboard the Solar Dynamics Observatory. Four flare-related footpoints (labeled as FP1--FP4) were nearly simultaneously identified in both WST 3600 Å and HMI 6173 Å continua, associated with a quadrupolar magnetic configuration and a failed filament eruption. The inner sources of FP1 and FP2 showed a similar enhancement of $\sim$65%/10% in the WST/HMI continuum, while the outer sources of FP3 and FP4 exhibited weaker responses. The inner footpoints had earlier responses in UV and EUV bands and were spatially coincident with the hard X-ray (HXR) footpoint sources. The two southern footpoints (FP2 and FP4) showed stronger HXR and white-light emissions than their northern counterparts (FP1 and FP3), with FP4 uniquely exhibiting a distinct HXR emission above 60 keV, in contrast to the absence of such an emission at FP3. Notably, faint WST 3600 Å enhancements at FP4 were observed during the gradual phase, temporally consistent with the fallback of filament material. This X1.2 flare presents a novel quadrupolar white-light structure, enriching our understanding of the generation and evolution of white-light flares.

### [B] 68.9 — Coronal gas excitation as a tracer of supermassive black hole mass: on the mid-IR coronal [Ne v] lines
- **arXiv:** [2608.16304](https://arxiv.org/abs/2608.16304)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (68.9), turbulence (64.7), molecular_clouds (63.8)
- **Current keyword baseline:** NO
- **BM25 max:** 56.3
- **Semantic max:** 86.1
- **Abstract:** Coronal lines (CL) may be a reliable proxy of supermassive black hole (SMBH) masses in active galactic nuclei (AGN) because the production of these high ionisation potential (IP) lines is sensitive to the shape of the ionising continuum which, for a thin accretion disc, relies on the black hole mass. In this work we study the connection between the [Ne\,v] coronal lines and the SMBH mass. We analyse the \textit{Spitzer spectra} of a sample of 27 AGN spanning three orders of magnitude in SMBH mass. Fluxes and the electron density in the coronal gas medium were measured after fitting Gaussians to both the $\rm [Ne\,v]14μm$ and $\rm [Ne\,v]24μm$ lines where detected at high signal to noise. Line fluxes were normalised to the Br$γ_{\rm broad}$ emission from the broad line region. We found strong correlations between the $\rm [Ne\,v]14μm/Brγ_{\rm broad}$ and $\rm [Ne\,v]24μm/Brγ_{\rm broad}$ line ratios and the SMBH mass. For this sample of 27 AGN we find scatters of 0.54 and 0.53 dex, respectively. These correlations support the theory that the coronal gas excitation is sensitive to a range of SMBH masses because of the dependence on the shape of the ionising continuum. The electron densities of the coronal medium are of the order 1000$\rm cm^{-3}$ supporting their nuclear origin. A comparison with density values derived from JWST for a subsample of objects confirm this conclusion. These results further demonstrate the ability to use CL as a SMBH mass proxy, allowing for accurate SMBH mass measurements in AGN.

### [B] 68.9 — Year-timescale changes in AGN radio luminosity as seen by the ASKAP Variables and Slow Transients Survey
- **arXiv:** [2608.15711](https://arxiv.org/abs/2608.15711)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (68.9), star_formation (66.5), ism_methods_data (62.5)
- **Current keyword baseline:** NO
- **BM25 max:** 53.0
- **Semantic max:** 79.1
- **Abstract:** A few dozen previously radio-quiet active galactic nuclei (AGN) have been observed to transition to radio-loud at 1-3 GHz frequencies over timescales of more than a decade, and this has has been interpreted to be due to newly launched jets. We identified 101 compact radio sources out of a sample of 64,972 non-blazar AGN which increased in flux density by 80-1800% over 1-6 years in the 887.5 MHz Australian SKA Pathfinder Variables and Slow Transients survey. We obtained optical spectra and radio SEDs using new observations and archival survey data. We determined 60 sources were consistent with extrinsic variability due to refractive interstellar scintillation and 41 were variable due to intrinsic causes, with 26 continuously brightening and two transitioning from radio-quiet to radio-loud. We concluded that young radio jets launched by either tidal disruption events or changes in the accretion properties were responsible for the continuously brightening AGN. These sources were non-variable at higher frequencies over the same time period, as expected for an expanding emission region. Fourteen sources had inverted or peaked SEDs initially which either flattened below the turnover or evolved into steep SEDs, consistent with young, expanding jets. Twelve sources had non-variable steep or gigahertz-peaked SEDs, which suggested these hosted more slowly evolving jets. We investigated the previously discovered AGN with newly launched jets, and found several have faded at multiple frequencies, which suggested the observed radio-loudness was temporary, rather than the onset of a sustained period of radio activity.

### [B] 68.9 — Large-Scale Dynamos Driven by Shear-Flow-Induced Jets
- **arXiv:** [2608.12530](https://arxiv.org/abs/2608.12530)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.HE, physics.flu-dyn, physics.plasm-ph, physics.space-ph
- **Top topics:** turbulence (68.9), star_formation (53.5), molecular_clouds (53.5)
- **Current keyword baseline:** NO
- **BM25 max:** 75.7
- **Semantic max:** 74.0
- **Abstract:** At every scale they occupy, magnetic fields affect various phenomena, including star formation, cosmic ray transport, charged particle acceleration, space weather, transport in planetary atmospheres, and laboratory plasmas. These fields are often generated and sustained by turbulent flows in a process called the dynamo. In 1955, E. N. Parker parameterized the effects of small-scale turbulence to propose a mean-field dynamo theory. The widely used theory reproduces observed large-scale fields but suffers from difficulty in tuning parameters as they are not justified from first principles: Studies of turbulent flows show tangled magnetic fields, which are folded and fragmented into small-scale structures due to shear-flow straining. Here, considering a shear flow that is unstable and driven, we develop analytic theory and perform three-dimensional (3D), advanced computer simulations of turbulence with up to 4096 x 4096 x 8192 grid points, showing ab initio generation of quasi-periodic, large-scale magnetic fields. The generation occurs via the mean-vorticity effect---an additional mean-field dynamo process postulated in 1990. Crucial to this dynamo is the prior generation of large-scale 3D jets, robustly produced as topologically protected and exact nonlinear solutions of the magnetohydrodynamic equations. The jet-driven dynamo applies to shear-driven laboratory and astrophysical systems. These include binary neutron star mergers, where the reported dynamo likely operates on microsecond timescales to produce in milliseconds some of the strongest magnetic fields in the Universe, providing signals for multimessenger astronomy.

### [B] 68.8 — From Variability to SED Modeling: A Multiwavelength Study of the Neutrino Blazar TXS 0506+056
- **arXiv:** [2608.17526](https://arxiv.org/abs/2608.17526)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** ism_methods_data (68.8), star_formation (59.0), molecular_clouds (55.9)
- **Current keyword baseline:** YES
- **BM25 max:** 36.6
- **Semantic max:** 85.9
- **Abstract:** The blazar TXS 0506+056 is the first source that was reported to be associated with high-energy extragalactic neutrino events and is one of the major targets for multi-messenger studies. We carried out multi-wavelength optical monitoring of this object on 24 nights in the period from 2018 to 2023. The overall light curves exhibit a dimming trend superposed by some small-amplitude fluctuations, and intraday variability was detected on four nights. Bluer-when-brighter behaviors were observed on both intraday and long timescales and were more pronounced on long timescales, while a weak redder-when-brighter trend was detected on one night. No significant time lags were found between variations at different optical wavelengths. We also retrieved the multi-broadband data from some monitoring programs. The data reveal complex, asynchronous flaring in different wavebands. A cross-correlation analysis shows that the high-energy emission (optical to gamma-ray) is co-spatial and leads the radio emission by a substantial time of about 800 to 900 days, suggesting that the radio emission originates from a downstream region of the jet. We performed time-dependent lepto-hadronic modeling of the spectral energy distributions for three representative epochs, the 2017 neutrino-associated flare, a post-flare phase, and a deep quiescent state, revealing an evolution in the radiative properties of the emission regions. The modeling results provide a phenomenological framework for interpreting the long-term multiwavelength behavior of TXS 0506+056 in a multi-messenger context.

### [B] 68.7 — Detectable subhalo impacts in Milky Way streams
- **arXiv:** [2608.19321](https://arxiv.org/abs/2608.19321)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO, hep-ph
- **Top topics:** ism_methods_data (68.7), galactic_ism_surveys (68.5), star_formation (67.3)
- **Current keyword baseline:** NO
- **BM25 max:** 57.2
- **Semantic max:** 85.9
- **Abstract:** Dark matter subhalos leave gravitational imprints in the stellar streams of the Milky Way. Observing individual strong impacts of subhalos offers a compelling way to constrain and discover potentially dark subhalos down to $10^6 M_\odot$, allowing for new tests of the particle physics properties of dark matter. We develop a pipeline and statistical framework to forecast the expected number of detectable subhalo impacts on stellar streams, based on morphological and kinematic data from surveys such as LSST and Via. Starting from a catalog of confirmed stellar streams, we focus our efforts on 14 promising streams that are relatively well-modeled with a particle spray algorithm. Our criteria for a detectable impact is a deviation at 95% CL from the best-fit polynomial proxy model for the stream, which accounts for stream modeling uncertainties and regulates the effect of distant impacts that are degenerate with these uncertainties. Among the 14 streams studied, we find that 5 streams have an expected number of detectable impacts greater than 0.2. With LSST and Via data, the stream Jet has $5.15^{+1.10}_{-0.95}$ expected detectable impacts, followed by Orphan-Chenab ($1.40^{+0.62}_{-0.47}$), ATLAS-Aliqa Uma ($1.25^{+0.60}_{-0.44}$), GD-1 ($0.55^{+0.43}_{-0.28}$), and Palomar 5 ($0.40^{+0.39}_{-0.23}$), where error bars are the 95% containment on the Poisson mean. These values rely on the assumed subhalo population, which can give a factor of few systematic uncertainty in the predictions. We also consider effects of different particle dark matter models on the number of impacts, finding a suppression by a factor of $\sim 4$ for warm dark matter and fuzzy dark matter models at their current mass bounds and an $O(1)$ enhancement for a toy model of self-interacting dark matter.

### [B] 68.7 — The Spin Angular Momentum and Black Hole Mass Components of Sagittarius A*
- **arXiv:** [2608.17978](https://arxiv.org/abs/2608.17978)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.HE, gr-qc
- **Top topics:** ism_methods_data (68.7), star_formation (65.2), molecular_clouds (54.9)
- **Current keyword baseline:** NO
- **BM25 max:** 39.3
- **Semantic max:** 85.8
- **Abstract:** The dimensionless spin angular momentum, dimensionless spin function, and blackhole mass components of Sagittarius A* (Sgr A*) were obtained by Daly et al. (2024) by applying the outflow method to six independent sets of simultaneously or contemporaneously obtained X-ray and radio data. Here, results obtained for Sgr A* with the outflow method are reviewed. Consistent results were obtained with each data set. Set I (the preferred data set) indicates that Sgr A* has a dimensionless spin angular momentum $a_* = (0.90 ~\pm~ 0.06)$ and a dimensionless spin function $F = (0.62 ~\pm~ 0.10)$. The results are consistent with the value of $a_* = (0.93~\pm~ 0.15)$ obtained with the outflow method applied to an independent data set (Daly 2019). The application of the outflow method to a weak compact radio source such as Sgr A* in its current state is most accurately determined with simultaneous or contemporaneous radio and X-ray measurements.

### [B] 68.7 — The reddening of NGC 7469 and evidence for variable extinction
- **arXiv:** [2608.15663](https://arxiv.org/abs/2608.15663)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (68.7), galactic_ism_surveys (64.2), astrochemistry (63.7)
- **Current keyword baseline:** NO
- **BM25 max:** 44.0
- **Semantic max:** 85.9
- **Abstract:** We estimate the reddening of the broad-line region and continuum of the active galactic nucleus NGC 7469 during the 1996 International AGN Watch multi-wavelength monitoring campaign using seven different reddening indicators. As was found for NGC 5548, these indicators support velocity-integrated broad hydrogen line ratios being close to Case B values. All the indicators point to substantial reddening of E(B-V) = 0.44 +/-0.03 for NGC 7469 during mid-1996. We find evidence for a gradual increase of about 10% in the reddening during the seven weeks of the 1996 campaign. Decades-long optical monitoring before and after the campaign is also consistent with modest changes in the extinction from year to year.

### [B] 68.6 — Infrared Spectroscopy of Cyanonaphthalenes under Interstellar Relevant Conditions and Their Potential Connection with Astronomical Aromatic Infrared Bands
- **arXiv:** [2608.14964](https://arxiv.org/abs/2608.14964)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, physics.chem-ph
- **Top topics:** astrochemistry (68.6), molecular_clouds (64.5), atomic_ism (64.4)
- **Current keyword baseline:** YES
- **BM25 max:** 68.1
- **Semantic max:** 85.8
- **Abstract:** Context. Aromatic infrared bands (AIBs) are widely observed in diverse astrophysical environments and are generally attributed to vibrational emission from polycyclic aromatic hydrocarbons (PAHs). The recent interstellar detection of 1-cyanonaphthalene (1-CNN) and 2-cyanonaphthalene (2-CNN) has motivated detailed infrared spectroscopic studies of cyano-substituted PAHs. Aims. We aim to characterize the infrared spectra and vibrational modes of neutral 1-CNN and 2-CNN under cold and gas-phase conditions and to assess their possible spectroscopic relevance to the astronomical AIBs. Methods. The gas-phase infrared spectra of neutral 1-CNN and 2-CNN were measured in a cold molecular beam using ion-dip spectroscopy. The observed bands were assigned with the aid of harmonic and anharmonic calculations at the B3LYP/N07D level. Infrared emission spectra were subsequently simulated from the experimental spectra within a single-photon approximation framework. Results. We report the infrared spectra of neutral 1-CNN and 2-CNN measured under cold and gas-phase conditions relevant to the interstellar medium. Their vibrational features were assigned in detail, including fundamental vibrations as well as overtone and combination bands. The simulated emission spectra exhibit features in several wavelength regions associated with prominent AIBs, including the aromatic CH stretching region near 3.3 micron, the CC stretching region near 6.2 micron, the mixed CH in-plane bending and CC stretching region at 8.6-8.9 microns, and the CH out-of-plane bending region between 10 and 15 microns. Conclusions. The present spectra provide laboratory reference data for small cyano-substituted PAHs and offer useful clues for interpreting selected AIB regions. These results suggest that cyanonaphthalene molecules are promising contributors to the aromatic infrared bands.

### [B] 68.6 — A Reproducible Two-Boundary Kinematic Correction for Baryonic Rotation-Curve Reconstruction in an 84-Galaxy SPARC Benchmark
- **arXiv:** [2608.14101](https://arxiv.org/abs/2608.14101)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (68.6), molecular_clouds (61.0), ism_methods_data (60.3)
- **Current keyword baseline:** NO
- **BM25 max:** 66.1
- **Semantic max:** 85.8
- **Abstract:** We present a reproducible computational validation and failure analysis of the empirical omega kinematic correction introduced by Flynn and Cannaliato (2025). The algorithm is deliberately minimal: one coefficient per galaxy is calculated from the innermost and outermost measured rotation-curve points and applied to the full observed radial profile before comparison with a baryonic reconstruction assembled from SPARC gas, disk, and bulge components. We preserve the predecessor's frozen 84-galaxy benchmark and publish its exact membership so that the transformation, not sample re-selection, is the object of validation. Without fitting the transformation to the baryonic residual, the primary maximum-disk reconstruction reduces the mean observed-baryonic discrepancy from 51.82 to 30.15 km/s across the frozen 84-galaxy benchmark. Bounded mass-to-light-ratio optimization further reduces the descriptive sensitivity-fit value to 25.45 km/s, while the simple Keplerian reference has a mean RMSE of 74.20 km/s in our earlier analysis [15]. Recalculation from the 84 per-galaxy records shows a resolved mass-to-light optimization benefit (delta RMSE > 0.05 km/s) in 53 galaxies and no resolved change in 31. Six galaxies do not beat the Keplerian reference; all six occur at Upsilon_max <= 0.111, whereas their omega values are not concentrated at the high end of the sample. We specify the complete deterministic workflow, native units, endpoint invariants, uncertainty propagation, and formula-level regression checks required to prevent grouping and sign errors. The complete 84-galaxy panel set, population-level error distributions, and failure diagnostics are retained as inspectable outputs. The result is a reproducible astronomical data-transformation benchmark rather than a proposed force law or replacement for dark matter or modified gravity.

### [B] 68.5 — Updates to WFC3/UVIS Encircled Energy Values in Select Filters
- **arXiv:** [2608.12110](https://arxiv.org/abs/2608.12110)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (68.5), ism_methods_data (67.7), molecular_clouds (60.8)
- **Current keyword baseline:** NO
- **BM25 max:** 31.6
- **Semantic max:** 85.6
- **Abstract:** We present updated encircled energy (EE) curves for a subset of UVIS filters. These are derived from a reanalysis of the drizzled Point Spread Function (PSF) data underlying the current EE calibration together with new measurements from deep observations of the PSF wings. Improved centroiding and analysis techniques applied to the drizzled PSFs produce more accurate EE values at small radii ($r \le 10$ pixels), bringing the results into closer agreement with a large archival PSF study (Huynh et al. 2025). At large radii, we leverage deep observations of the PSF wings in six filters and compare the fraction of light between 2" and 6" with predictions from an optical model of the PSF (Hartig 2009). For filters with pivot wavelengths $ \gtrsim{4000} \mathrm{\mathring{A}}$, the model agrees with the empirical data, but over-estimates the EE for UV filters by $\sim0.5$% at 2". The revised EE solutions affect the UVIS zeropoints, which are derived from aperture photometry in a 0.4" (10 pixel) radius and corrected to 6" using EE tables (Calamida et al. 2022). Overall, the impact is small; the EE at 0.4" is larger by $ \gtrsim{0.5}$ % (0.005 mag) for several filters (F218W, F225W, F275W, F775W, F814W, F845M), especially for UVIS2. In contrast, the EE value is generally smaller at 0.4" for long-pass filters (F200LP, F350LP, F850LP), with F850LP differing by $\sim2 $ % (0.02 mag). Updated EE tables will be delivered together with a revised set of UVIS inverse sensitivity tables and zeropoints later in 2026. In the interim, we provide EE tables for commonly used filters in Appendix A.

### [B] 68.2 — Laser Metrology for Precision Alignment of Transmission Gratings in the REDSoX Soft X-ray Polarimeter
- **arXiv:** [2608.13640](https://arxiv.org/abs/2608.13640)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.HE
- **Top topics:** molecular_clouds (68.2), ism_methods_data (57.4), feedback_bubbles (48.6)
- **Current keyword baseline:** NO
- **BM25 max:** 41.3
- **Semantic max:** 78.1
- **Abstract:** The Rocket Experiment Demonstration of a Soft X-ray Polarimeter (REDSoX) is a NASA sounding-rocket mission designed to perform the first astrophysical spectropolarimetry in the 0.2-0.4 keV energy band. The instrument uses critical-angle transmission (CAT) gratings to disperse incident X-rays onto laterally graded multilayer (LGML) mirrors, requiring 48 individual gratings to be co-aligned to within 6 arcminutes in yaw, pitch, and roll. To support the systematic assembly of the grating array, we adapted a scanning laser-reflection metrology technique in which normal-reflected, angled-reflected, and diffracted ultraviolet laser beams are measured using three position-sensitive detectors (PSDs). Changes in the measured beam positions are used to reconstruct the local yaw, pitch, and roll of each grating and provide real-time feedback during mechanical adjustment. We demonstrate the system using a prototype miniature grating structure containing two gratings. Following co-alignment, the assembly underwent a flight-level random-vibration test followed by a qualification-level sine sweep. Measurements obtained before and after testing showed that the relative grating orientations were retained to within 1 arcminute, less than 17% of the REDSoX co-alignment tolerance. This work establishes a reproducible and scalable approach to the assembly and verification of large transmission-grating arrays for REDSoX and future X-ray spectroscopic instruments.

### [B] 68.1 — Plasma Turbulence in the Lunar Environment Across Solar Wind and Magnetotail Conditions: Observations from Chandrayaan-2 Radio Science experiment
- **arXiv:** [2608.15512](https://arxiv.org/abs/2608.15512)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, physics.space-ph
- **Top topics:** turbulence (68.1), ism_methods_data (62.2), molecular_clouds (61.6)
- **Current keyword baseline:** NO
- **BM25 max:** 54.6
- **Semantic max:** 78.1
- **Abstract:** The Moon's transit between the solar wind and Earth's magnetotail exposes the near-lunar environment to large and rapid variations in plasma density and flow structure. Two-way coherent S-band radio occultation measurements from Chandrayaan-2 were used to quantify electron-density fluctuations integrated along the Earth-Moon line of sight. Observed frequencies were processed to remove geometric Doppler contributions derived from relativistic light-time modeling. The remaining frequency residuals represent the cumulative effect of plasma irregularities along the ray path. Power spectral densities were computed for 54 intervals from 2022, yielding temporal spectral indices in the range $1.05 \le α\le 2.66$, corresponding to spatial indices $4.05 \le p \le 5.66$ indicating ion-kinetic and dissipation-range scales. Of the 54 intervals, 9 were classified as inside the modeled magnetopause, 17 in the bow shock/magnetosheath, and 28 in the solar wind. Spectral indices measured inside the magnetopause are marginally higher than those in the bow shock and solar wind, though the difference is not statistically significant given the limited magnetotail sample. No measurable correlation is found between spectral slope and geomagnetic activity, indicating that the observed variability is dominated by local plasma structure rather than inner-magnetospheric conditions.

### [B] 68.1 — The B-Index as a Diagnostic of Cool Stars: Assessing Metallicity Dependence of TiO Absorption in the Visible Spectrum
- **arXiv:** [2608.14084](https://arxiv.org/abs/2608.14084)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** astrochemistry (68.1), magnetic_fields (67.2), feedback_bubbles (61.0)
- **Current keyword baseline:** NO
- **BM25 max:** 46.7
- **Semantic max:** 85.1
- **Abstract:** Molecular absorption features constitute essential diagnostics of late-type stellar atmospheres, with titanium oxide (TiO) bands serving as sensitive tracers of effective temperature and magnetic activity. While near-infrared TiO indices are well established, visible-band diagnostics provide complementary constraints for stellar classification and parameter estimation. This study investigates the metallicity dependence of the B-index, a TiO absorption measure centered at 567 nm, through synthetic spectra generated with ATLAS9 and high-resolution observations from the HARPS spectrograph. The synthetic grid spans effective temperatures between 3500-4000 K and metallicities from [Fe/H] =-4 to +0.2, while the observational sample comprises 23 MK spectral types stars with effective temperatures between 3500-4000 K. Both theoretical and empirical analyses demonstrate that the B-index exhibits negligible sensitivity to stellar metallicity, with only marginal correlations detected. Therefore, there is no requirement to include this feature in the calculation of the B-index. The B-index's low sensitivity to metallicity reinforces its utility as an effective tool for spectral classification, stellar atmosphere modeling, and the study of magnetically active stars.

### [B] 67.7 — Dianoga simulations of galaxy clusters and groups: Properties of the baryonic components
- **arXiv:** [2608.17570](https://arxiv.org/abs/2608.17570)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, astro-ph.GA
- **Top topics:** feedback_bubbles (67.7), star_formation (63.0), astrochemistry (60.2)
- **Current keyword baseline:** NO
- **BM25 max:** 85.1
- **Semantic max:** 77.5
- **Abstract:** We introduce the Dianoga set of cosmological simulations of galaxy clusters and groups, specifically aimed at studying the impact of the implementation of AGN feedback and star formation. Using the OpenGadget3 code, we carry out simulations of 28 regions centred on massive galaxy clusters, and of a cosmological box. This generates a sample of 293 halos with M_{200}> 1.5 x 10^{13} M_{\odot}. Parameters of AGN feedback in the reference implementation were minimally calibrated exclusively to match the local relation between SMBH masses and stellar masses of host galaxies. Simulations are compared to observed galaxy stellar mass function (GSMF), stellar mass fraction in clusters and groups, BCG masses, scaling relations between ICM/IGM properties and profiles of their thermodynamical properties. In the appendix, we show how results vary as we modify the reference feedback model in six alternative configurations. Our reference model predicts a GSMF in general agreement with observations, albeit overestimated in the high end. BCG stellar masses and mass fractions are higher than observed in massive clusters, while being closer to observations for groups. Predicted properties of the ICM/IGM are in general agreement with observations, with the core regions of simulated clusters having entropy and temperature profiles that are slightly less "cool-cored" than observed. A comparison with other implementations of AGN feedback highlights that models including thermal evaporation of the sub-resolution interstellar medium succeed to bring BCG masses and stellar mass fractions closer to observation, and to increase the cool-coreness of simulated clusters. Our results demonstrate that the details of the interface between AGN energy injection and the sub-resolution interstellar medium model are at least as critical as the total feedback efficiency itself.

### [B] 67.7 — Measuring Simulated Circumgalactic Medium Turbulence with Emission-Weighted Projected Velocity Structure Functions in FOGGIE
- **arXiv:** [2608.17013](https://arxiv.org/abs/2608.17013)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** turbulence (67.7), galactic_ism_surveys (65.5), molecular_clouds (52.8)
- **Current keyword baseline:** YES
- **BM25 max:** 100.0
- **Semantic max:** 81.9
- **Abstract:** The spatially-resolved kinematics of line emission from the circumgalactic medium (CGM) of a galaxy can contain information about the CGM turbulence, which may play an important role in galaxy evolution. Due to the region's diffuse nature, there have been limited observations of low-redshift CGM emission until recent efforts that use spatially-resolved emission line kinematics to probe CGM turbulence. We use velocity structure functions (VSFs) as a measure for the properties of turbulence using the high-resolution cosmological zoom-in FOGGIE simulations. We focus on the location of the "turnover" in the VSF slope, often used as a measurement of the turbulence driving scale, and study how resolution, measurement area size, projection effects, and gas temperature influence the inferred CGM turbulence driving scale. We find that projection significantly lowers the VSF normalization but we do not find significant differences in the slope between 3D VSFs and emission-weighted projected 2D VSFs. We find that the size of the area used to measure the VSF, which can be thought of as the size of the emission nebula for a given instrument sensitivity, correlates directly with the turnover location in the VSF. These dependencies should be considered when using VSFs to interpret CGM turbulence from emission data, as projection, resolution and sensitivity constraints, and the temperature of the gas probed will all have a measurable effect on the VSF structure and the corresponding inferred turbulent properties.

### [B] 67.7 — Chondrule formation in the outer disk from the primary three-dimensional chemical composition of CM chondrules
- **arXiv:** [2608.12931](https://arxiv.org/abs/2608.12931)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** molecular_clouds (67.7), massive_star_formation (58.8), star_formation (58.7)
- **Current keyword baseline:** NO
- **BM25 max:** 63.7
- **Semantic max:** 84.6
- **Abstract:** Chondrules and their associated fine-grained rims record key processes in the early protoplanetary disk, yet the links between chondrule chemistry, morphology, and matrix complementarity remain poorly constrained. We investigate the major, minor, and trace element compositions of 66 chondrules and FGRs from the relatively unaltered CM carbonaceous chondrites Asuka 12236, Paris, and Maribo, together with their 3D morphology, using LA-ICP-MS and X-ray tomography. CM chondrules record systematic metal loss and evaporation of Si-rich mesostasis, driving initially CI-like precursor compositions toward more Mg- and Si-rich bulk compositions along the CI ratio line and toward increasingly Si-poor forsteritic assemblages. GEMS-like materials in pristine CM matrices closely mirror chondrule compositions and likely represent complementary condensates derived from evaporated mesostasis. Dust accreted onto chondrules is predominantly CI-like but contains about 14 wt.% complementary condensate material represented by chondritic amorphous silicates, reconciling Mg/Si complementarity between chondrules and matrix with the preservation of primordial organics and presolar grains. Morphological observations show no significant sectioning bias, consistent with CM chondrules being dominated by agglomerates of ~100 um microspherules. Many display grape-bunch textures produced by welding of smaller chondrules with metal-rich or CI-like rims. This structure may explain the chondrule moderately volatile-element plateau at about 0.3xCI. We propose a "micro-chondrule-first" scenario in which localized heating events produced small molten droplets that subsequently accreted CI-like dust and ice, aggregated, and experienced limited aqueous alteration. These observations place new constraints on chondrule formation in the outer disk and highlight the importance of localized melting and aggregation processes.

### [B] 67.6 — Hector Galaxy Survey: Falling in Between - Infalling Galaxies in the Midst of the Abell 3667 Merger
- **arXiv:** [2608.18621](https://arxiv.org/abs/2608.18621)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (67.6), star_formation (64.2), atomic_ism (63.0)
- **Current keyword baseline:** NO
- **BM25 max:** 42.7
- **Semantic max:** 84.4
- **Abstract:** Whether cluster mergers enhance ram pressure stripping (RPS) and accelerate member galaxy evolution remains an open question. Here, we investigate galaxy populations in the nearby merging cluster Abell 3667 ($z\simeq0.0553$) using spatially resolved data from the Hector Galaxy Survey. We define an RPS sample combining Hector-selected galaxies with ionised gas disturbances (e.g., asymmetric tails or truncated disks) and supplementary, optically identified jellyfish galaxies lacking Hector data. Most of the RPS sample ($\sim 71^{+10}_{-7}\%$; 20/28) lies within $R_{200}$, where the merger impact is greater. Most asymmetric galaxies ($\sim 73^{+14}_{-8}\%$; 11/15), especially those with extreme RPS signatures, are concentrated in the inner cluster ($R \lesssim 0.6\, R_{200}$), along the merger axis between two shock-tracing radio relics. These central asymmetric galaxies show two spatial and kinematic groups: one at the North-West (NW) subcluster, downstream of its radio relic in a region of high-velocity intracluster medium (ICM) bulk motion, with blueshifted line-of-sight velocities; and a mostly redshifted population near the main cluster (MC), which also shows a turbulent ICM. Despite their projected association with the MC core and NW substructure, both samples' velocities indicate they are not bound to them. Tail orientations give insight into orbital histories: NW tails point away from the cluster centre and often align with the merger axis, suggesting merger-driven stripping, while MC tails show neither pattern clearly. Tails are broadly westward, with MC tails tracing due west and NW tails shifted northwest, pointing to two distinct filamentary accretion events for the NW and MC populations. Together, our results indicate enhanced RPS in the heart of A3667, driven mainly by infalling galaxies accreted along nearby filaments interacting with the merger-driven turbulent environment.

### [B] 67.6 — Supernova remnant 0509-67.5 is consistent with an explosion inside an old planetary nebula (SNIP)
- **arXiv:** [2608.18196](https://arxiv.org/abs/2608.18196)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (67.6), feedback_bubbles (65.2), astrochemistry (55.3)
- **Current keyword baseline:** NO
- **BM25 max:** 50.7
- **Semantic max:** 84.4
- **Abstract:** I critically examine claims in the paper arXiv:2608.11978 that the double-detonation (DDet) scenario explains the type Ia supernova (SN Ia) remnant (SNR Ia) SNR 0509-67.5, and find the arguments supporting the DDet scenario weak; hence, I reiterate my claim that the core-degenerate (CD) scenario, where a lonely white dwarf (WD), which is the merger product of a lower-mass WD and the core of an asymptotic giant branch star, exploded inside an old planetary nebula, i.e., an SNIP, best explains SNR 0509-67.5. I find that the flat edge of the SNR in the north-northeast, which in the DDet scenario is due to a shadow by the companion to the WD that exploded, is not unique in this SNR, and that the circumstellar matter, i.e., an old planetary nebula, shaped this edge, as well as other structures on the edge of this SNR. I emphasize that analyses of SNRs Ia and SNe Ia at late stages must consider the claim that most normal SNe Ia are SNIPs, implying that old planetary nebulae can heavily shape their morphologies. The bulk velocity inferred from an iron emission line in SNR 0509-67.5, which the DDet explosion attributes to the orbital motion of the exploding WD around its companion, can be an outcome of the explosion of a near-Chandrasekhar lonely WD; an off-center delayed-detonation transition explosion can form asymmetrical nucleosynthesis, while leading to a bulk motion of nickel that decays to iron. I repeat my claim that the CD scenario of a SNIP is the most likely scenario for SNR 0509-67.5.

### [B] 67.6 — High-spectral-resolution Observations of the [S II] Emission-line Doublet in the Filamentary Nebula Surrounding NGC 1275
- **arXiv:** [2608.14888](https://arxiv.org/abs/2608.14888)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (67.6), turbulence (65.0), galactic_ism_surveys (59.3)
- **Current keyword baseline:** NO
- **BM25 max:** 58.3
- **Semantic max:** 81.3
- **Abstract:** We analyze new high-spectral resolution SITELLE observations (R = $λ/Δλ$ = 7000) of the filamentary nebula surrounding NGC 1275, central galaxy of the Perseus cluster. We present here analysis of the \sii$\lambda6716$ and \sii$\lambda6731$ emission line doublet, using its ratio to determine the electron density of the optically emitting filaments. We compare these measurements with electron densities derived from deep Chandra X-ray observations of the intra-cluster medium (ICM) to determine if any correlations in density can be found. We report the detection of a clear dichotomy between the outer filaments, displaying on average lower \sii\text{ }emission line ratio of $\sim 1.1$ and the inner filaments displaying higher ratios of $\sim 1.3$. These results indicate that most of the gaseous filaments lie close to the low-density threshold for the density measurement of $\sim 10^2\text{ cm}^{-3}$. Using radial profiles, we find that the inner filaments have a roughly constant density, whereas the ICM density decreases with radius. In the outer filaments, we observe hints of local connections between the densities of the ICM and optical filaments, but no clear correlation seems to be observed overall. We also combined these density measurements with cold molecular CO gas observations to derive a relationship between temperature, density and pressure for the multiphase environment surrounding NGC 1275. Finally, we investigated potential models to explain the observed density measurements and explored similar studies of filamentary nebula around other central galaxies of cool-core galaxy clusters.

### [B] 67.6 — Widefield Arecibo Virgo Extragalactic Survey: II. Characterizing the HI properties and environment of the WAVES South region
- **arXiv:** [2608.13411](https://arxiv.org/abs/2608.13411)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (67.6), feedback_bubbles (64.6), atomic_ism (60.5)
- **Current keyword baseline:** NO
- **BM25 max:** 78.6
- **Semantic max:** 84.5
- **Abstract:** Context. Galaxy clusters are extreme environments where interactions with the hot intracluster medium drive rapid galaxy evolution. These processes can result in the formation of optically dark gas clouds, as previously observed in Virgo and other clusters. Aims. We investigate the distribution and properties of neutral hydrogen (HI) in two large adjoining regions of the Virgo cluster to understand how the cluster environment influences galaxy transformation. Specifically, we examine the gas content of both star-forming and quiescent populations and search for evidence of gas-loss driven evolution. Methods. We cataloged the 21cm HI Widefield Arecibo Virgo Extragalactic Survey (WAVES) South data using visual and automatic source extraction methods. By combining these results with an optically selected sample, we compared the HI properties of WAVES South with the previously studied VC1 region. To probe gas reservoirs below the nominal detection limit, we performed a stacking analysis of radio spectra across the WAVES South, VC1 and VC2 footprints. Results. We detected 56 HI sources with a median root mean square (rms) noise of 0.8 mJy, including 50 galaxies, two gas clouds (one being optically dark), and the ALFALFA Virgo 7 complex. Our results reveal a significantly lower detection fraction in WAVES South compared to the VC1 region. Stacking showed no new HI detection at a 0.080 mJy rms with a maximum of 157 stacked objects from WAVES South, VC1, and VC2. Conclusions. The lower HI detection fraction suggests that WAVES South is a more dynamically relaxed and evolved environment than the VC1 region. The presence of residual HI in a small subset of early-type galaxies supports a model of dwarf irregular to dwarf elliptical transformation via environmental stripping. Finally, we note a possible evolutionary link between optically dark clouds and recently discovered "blue blobs."

### [B] 67.5 — An Empirical Effective-Temperature Calibrations for Galactic B/A Supergiants
- **arXiv:** [2608.18619](https://arxiv.org/abs/2608.18619)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.IM
- **Top topics:** ism_methods_data (67.5), astrochemistry (65.8), feedback_bubbles (53.9)
- **Current keyword baseline:** NO
- **BM25 max:** 58.4
- **Semantic max:** 84.4
- **Abstract:** We present empirical effective temperature Teff calibrations for Galactic supergiants of spectral types B5-A5 based on optical spectra. The relationships were derived from a reference sample with adopted literature temperatures and use equivalent widths, central line depths, and ratios of selected spectral features as temperature indicators. Quadratic relationships are established for individual diagnostics and their ratios. Collectively, the calibrations span a Teff interval from 8 400 K to 14 700K, while the validity range of each relationships is individually specified. Detailed quantitative atmospheric analyzes remain indispensable for deriving physically consistent stellar parameters. However, their application to extensive spectroscopic samples is observationally and computationally demanding. The empirical relationships presented here provide a homogeneous and readily applicable temperature scale for the characterization of Galactic BA supergiants. The complete calibration tables, including fitted coefficients and uncertainty information, together with an interactive Python tool to apply the relationships, are publicly available through Zenodo. The reduced continuum-normalized spectra and associated metadata are published through a VO--compliant service of the Kazakhstan National Virtual Observatory.

### [B] 67.5 — The VariableTNG project: Unveiling the physical drivers of galaxy quenching
- **arXiv:** [2608.17011](https://arxiv.org/abs/2608.17011)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (67.5), ism_methods_data (48.3), star_formation (45.3)
- **Current keyword baseline:** NO
- **BM25 max:** 73.3
- **Semantic max:** 72.2
- **Abstract:** Understanding the physical processes that regulate galaxy quenching is a key challenge in galaxy formation and evolution. The VariableTNG (VTNG) project provides a laboratory to investigate these processes, as it systematically varies eight parameters of galaxy formation while keeping the initial conditions fixed, allowing the effects of individual feedback prescriptions to be isolated. We use interpretable machine-learning techniques as a tool to identify the parameters that most strongly regulate the quenched galaxy fraction. Our goal is to quantify the relative importance of the galaxy formation and feedback parameters that regulate the quenched galaxy fraction at z=0, determine how their influence changes across stellar mass and environment. We compute the quenched galaxy fraction for 26 VTNG boxes as a function of stellar mass, black hole mass, and gas mass, considering both the total galaxy population and separate samples of central and satellite galaxies. We train Random Forest regressors to predict the variation of the quenched fraction relative to the TNG100-1 model and use SHAP values to quantify both the magnitude and direction of the influence of each parameter. Our analysis reveals that only a small subset of the VTNG parameters dominates the variance of the quenched fraction. The stellar feedback wind parameter is the primary driver at low stellar masses, while its importance gradually shifts toward AGN-related parameters at higher masses. The supernova temperature also plays an important role at both extremes of the stellar-mass range. This transition persists when the galaxy population is divided into central and satellite systems. Comparisons with observational measurements further suggest that variations in these feedback parameters may contribute to the discrepancies between the fiducial TNG100-1 model and the observed passive galaxy population.

### [B] 67.4 — Toward Operational Solar Flare Peak Flux Nowcasting: A Strategy Combining Real-Time Data, Machine Learning, and NOAA Flare Detection Criteria
- **arXiv:** [2608.20062](https://arxiv.org/abs/2608.20062)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** star_formation (67.4), ism_methods_data (60.9), molecular_clouds (57.1)
- **Current keyword baseline:** YES
- **BM25 max:** 30.0
- **Semantic max:** 84.3
- **Abstract:** We present the RMN strategy (Real-time data, machine learning, and NOAA flare detection criteria) for nowcasting the peak soft X-ray flux of ongoing solar flares under operationally realistic conditions. The strategy combines real-time GOES 0.1-0.8 nm X-ray observations with an attention-based sequence-to-sequence Long Short-Term Memory model. Under the NOAA flare detection criteria, predictions are evaluated at one-minute intervals from three minutes after the cataloged onset to the observed peak using the preceding 60 minutes of X-ray observations. We apply the RMN strategy to C-, M-, and X-class flares observed by GOES-8-18 from 1997 to 2024 using four-fold cross-validation. The major results of this study are as follows. First, the model nowcasts peak soft X-ray flux with RMSE and PE values of 0.26 and 3.11\% for the $\geq$C-class group, 0.45 and 5.59\% for the $\geq$M-class group, and 0.87 and 12.76\% for the X-class group. The higher discrepancy toward stronger flare groups indicates that peak-flux prediction is more challenging for higher-intensity flares. Second, the model performance depends on flare rise time and prediction time, with larger errors for longer rise time events and improved performance as the prediction time approaches the flare peak. Shorter rise time events approach their final peak more rapidly, providing a clearer indication of the eventual peak, whereas the larger difference for longer rise time events may partly reflect more complex temporal evolution. Third, empirical coverage based on total uncertainty remains high but decreases for stronger flares, with noise uncertainty contributing more than model uncertainty.

### [B] 67.4 — Nonlinear velocity power spectrum: modeling the cosmological dependence on the Hubble constant and cold dark matter density
- **arXiv:** [2608.16489](https://arxiv.org/abs/2608.16489)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** turbulence (67.4), molecular_clouds (50.5), star_formation (47.2)
- **Current keyword baseline:** NO
- **BM25 max:** 66.3
- **Semantic max:** 77.2
- **Abstract:** In this paper we present a semi-analytical model for the velocity power spectrum in $\La$CDM cosmology for wave numbers $k<1/$Mpc. We mainly concentrate on the dominant divergence part but also present some results on the vorticity contribution. We divide cosmological parameters into evolution and shape parameters and model the dependence of the evolution parameter $h$ and of the shape parameter $\om_{\rm cdm}$ with an accuracy better than 2.5\%. A surprising finding of our study is that the velocity power spectrum becomes independent of $\om_{\rm cdm}$ on nonlinear scales. A python implementation of the model is publicly available.

### [B] 67.4 — Radio Properties of RS Canum Venaticorum Variables in VLASS and RACS
- **arXiv:** [2608.13653](https://arxiv.org/abs/2608.13653)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.HE
- **Top topics:** astrochemistry (67.4), ism_methods_data (65.3), feedback_bubbles (63.3)
- **Current keyword baseline:** NO
- **BM25 max:** 46.2
- **Semantic max:** 84.3
- **Abstract:** We performed a systematic search for radio emission from RS Canum Venaticorum (RS CVn) binaries, selected from the International Variable Star Index (VSX) catalog, in the Very Large Array Sky Survey (VLASS; three epochs) and Rapid ASKAP Continuum Survey (RACS; two epochs) data. We detected 108 candidate radio-emitting RS CVn in at least one epoch. Several of these systems rank among the most radio-luminous RS CVn binaries reported to date. The radio and X-ray luminosities, obtained from cross-matching with the eROSITA and ROSAT X-ray catalogs, are consistent with the Guedel-Benz relation for magnetically active stars, but are also comparable to radio-luminous quiescent black hole X-ray binaries, indicating a potential for misidentification between these two classes. Analysis of optical, radio, and stellar properties indicates that optically bright RS CVn (i.e., those with at least one giant component) are radio-quieter and have periods that are consistent with lower coronal activity. However, two of these optically bright RS CVn systems show persistent and unusually high radio specific luminosities (>2e17 erg/s/Hz) across all observed epochs, showing that stellar activity can produce relatively persistent radio signals as bright as quiescent black hole binaries.

### [B] 67.3 — The VLA and High-Frequency SETI: Expanding the Search for Life
- **arXiv:** [2608.18275](https://arxiv.org/abs/2608.18275)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** feedback_bubbles (67.3), astrochemistry (65.0), star_formation (63.2)
- **Current keyword baseline:** NO
- **BM25 max:** 34.7
- **Semantic max:** 81.2
- **Abstract:** The Commensal Open-Source Multimode Interferometer Cluster (COSMIC) runs software that searches for technologies elsewhere in the Universe ("technosignatures") using the Karl G. Jansky Very Large Array (VLA). Specifically, it searches for narrowband signals that drift in frequency over time as a result of Doppler motions. Although this is the first study of high-frequency technosignatures that has been published from the COSMIC system on the VLA, it follows closely on previous work completed by an undergraduate research intern. Within the field of view of the VLA, the software on COSMIC creates coherent beams directed toward stars that may contain exoplanets from the Gaia catalogue. The recorded results follow a real-time software pipeline and are examined for technosignatures. Using a Taylor-Tree De-Dispersion algorithm to find narrow-band drifting signals, each recorded beam (coherent and incoherent) is searched for signals with a drift-rate with magnitudes up to $\pm$50Hz/s. All detections are stored as "hits" with the relevant snippet of data stored for posterity. The purpose of this work is to extend the high-frequency search by reviewing data from February 2024 to the present. Our study examines the impact of previously implemented and novel filters to find a selection of candidate signals. At the final stage of the pipeline, our objective is to study these resultant candidate signals spatially through imaging. The observations therefore probe regions of frequency and signal parameter space that have received comparatively limited coverage in previous SETI surveys.

### [B] 67.3 — GEMS JWST: Hold on to your HATS(-6 b), a sub-solar metallicity giant planet with water, methane and ammonia in its atmosphere
- **arXiv:** [2608.16990](https://arxiv.org/abs/2608.16990)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** astrochemistry (67.3), ism_methods_data (66.2), massive_star_formation (63.4)
- **Current keyword baseline:** NO
- **BM25 max:** 45.8
- **Semantic max:** 84.1
- **Abstract:** HATS-6 b is one of several recently discovered Giant Exoplanets orbiting M-dwarf Stars (GEMS) and is part of a JWST survey that aims to compare bulk and atmospheric properties of these rare planets against their FGK star counterparts. HATS-6 b is a warm ($\mathrm{T_{eq}}\sim700$ K), Saturn-mass ($M_p\sim0.3~\mathrm{M_J}$), Jupiter-radius ($R_p\sim1~\mathrm{R_J}$) planet that transits its star every $\sim$ 3 days. In this study, we present the transmission spectrum of HATS-6 b obtained with two transits using the PRISM mode of JWST Near Infrared Spectrograph (NIRSpec), spanning a wavelength range of $0.6-5.3$ um. Analyzing these JWST observations using an iterative approach between forward modeling and free chemistry retrievals, we derive a low metallicity ($\log\mathrm{[M/H]}=-1.99^{+0.2}_{-0.2}$) sub-solar C/O ($\log\mathrm{[C/O]=-0.46^{+0.2}_{-0.2}}$) atmosphere, and find strong evidence for H$_2$O, CH$_4$, and NH$_3$ at volume mixing ratios (in $\log[X]$) of $-4.88_{-0.24}^{+0.25}$, $-5.38_{-0.19}^{+0.18}$, and $-6.03_{-0.19}^{+0.18}$, respectively. We consistently retrieve a significantly lower $\mathrm{T_{eq}}$ than predicted from the orbital configuration of HATS-6 b, which was impervious to any data reduction and retrieval choices, suggesting a non-zero bond albedo. Our planetary interior models retrieve bulk metallicities three orders of magnitude larger than our retrieved atmospheric metallicity, also suggesting that the atmosphere is not well-mixed. We find an excess feature around 3 um, and expand on possible explanations for this, such as the presence of HCN or hydrocarbons like C$_2$H$_4$. Yet, due to the degeneracies present for hydrocarbon features in this wavelength region, we do not draw any conclusions about the excess feature and instead encourage further observations and follow-up of this intriguing target.

### [B] 67.1 — Responses of the X-ray spectrometer/imager STIX onboard Solar Orbiter
- **arXiv:** [2608.19420](https://arxiv.org/abs/2608.19420)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.IM
- **Top topics:** ism_methods_data (67.1), astrochemistry (59.1), molecular_clouds (57.1)
- **Current keyword baseline:** YES
- **BM25 max:** 34.9
- **Semantic max:** 83.9
- **Abstract:** Solar flares are explosive events that release X-rays from hot plasma and accelerated electrons. The STIX instrument on the Solar Orbiter provides imaging spectroscopy of solar X-ray emissions from 4 to 150 keV. To interpret the STIX data accurately, understanding the instrument's response is crucial. Given the complexity of interactions of X-rays with the instrument, we developed a detailed Monte Carlo model for STIX based on Geant4. The model accurately depicts the instrument's components, such as grids, detectors, X-ray windows, and collimators, with their responses. We studied various effects, including grid shadowing, fluorescent X-rays emitted by materials in STIX, and grid transmission, to assess their impacts on STIX's scientific goals. Model validation was performed using Crab Nebula observations, a standard calibration source that provides reliable ground truth for X-ray instruments. Our simulations align with the Crab Nebula observations within the uncertainties, thereby validating the accuracy of the Geant4 model and showcasing its potential for interpreting STIX data. With the help of the generated response matrices, which are indispensable for solar spectroscopy, we discuss the applications and limitations of the model for future STIX data analysis.

### [B] 67.1 — ADORA: a differentiable optical modeling and astrometric retrieval framework for SHERA
- **arXiv:** [2608.19409](https://arxiv.org/abs/2608.19409)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (67.1), astrochemistry (53.5), star_formation (53.0)
- **Current keyword baseline:** NO
- **BM25 max:** 37.4
- **Semantic max:** 83.9
- **Abstract:** Searching for Habitable Exoplanets with Relative Astrometry (SHERA) is a proposed Small Explorer mission concept designed to measure the separation of nearby binary stars at microarcsecond-class precision. Recovering this signal requires separating astrophysical motion from coupled changes in pointing, plate scale, wavefront error, spectral response, and detector calibration. We present the Astrometric Differentiable Optics and Retrieval Algorithm (ADORA), an image-domain framework that combines a three-plane differentiable physical-optics model with a layered astrometric inference algorithm. The forward model includes a diffractive pupil, mirror-specific wavefront error and beamwalk, polychromatic source and throughput models, and configurable detector effects. Per-frame registration states are treated locally and eliminated through Schur reduction before the slower astrometric and instrument state is updated in a prior-whitened Fisher eigenbasis. Five-minute matched-model simulations show no detected separation bias at the current Monte Carlo depth and approximately 11 uas realization-to-realization scatter. A SHERA target sweep reveals a more-than-fivefold variation in astrometric information between Alpha Centauri and 61 Cygni, motivating future target-dependent accumulation and update cadence. High-order-wavefront knowledge error can drive the retrieval toward a strongly biased astrometric solution while leaving the local posterior sigma nearly unchanged, demonstrating that statistical curvature alone does not capture unmodeled bias. Pixel-position errors across the tested range remain near the matched-model recovery scale indicating robustness to certain detector calibration errors. ADORA provides a flexible framework for studying astrometric extraction, calibration-bias diagnosis, and future SHERA requirements.

### [B] 67.1 — Brightest group and cluster galaxies as indicators of relaxation
- **arXiv:** [2608.16481](https://arxiv.org/abs/2608.16481)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (67.1), astrochemistry (64.5), feedback_bubbles (62.0)
- **Current keyword baseline:** NO
- **BM25 max:** 35.8
- **Semantic max:** 83.9
- **Abstract:** Context. Galaxy groups and clusters are widely used to probe the evolution of the cosmic web and cosmology, while assuming that they are relaxed. Aims. We identify the properties of the brightest halo galaxies (BHGs) that can be used to predict the most likely sample of dynamically relaxed host halos. Our work combines thoroughly studied galaxy clusters with less frequently analysed groups. Methods. Our analysis was based on data from the IllustrisTNG simulations. We considered several observationally motivated parameters, including the offset of the BHG from the potential well of the host system ($d_\text{off}$) and from the r-band luminosity centre ($d_\text{lum}$), the distance between the brightest and second-brightest galaxies ($d_{12}$), and the r-band magnitude gap between them ($Δm_{12}$). The primary analysis was performed at redshift $z=0$, with an additional investigation of the redshift evolution of halo relaxation up to $z=1$. The observable proxies were applied to construct a halo mass function (HMF), which was then compared to the HMF of the relaxed sample defined from 3D information commonly used in theoretical approaches. Results. We find that $d_\text{off}$ and $Δm_{12}$ are effective indicators of group and cluster relaxation, particularly when used in combination. The selection criteria of $d_\text{off}<0.05~R_{200}$ and $Δm_{12}>1.6$ mag allowed us to reproduce an HMF that closely matches that of the relaxed halo population. These criteria can be applied to observations up to $z\sim0.2$ within a mass range $\text M_{200}\geq10^{12.5}\text M_\odot$ ($\text M_\text{*, BHG}\gtrsim10^{10.9}\text M_\odot$), including groups and clusters in the selection. In this mass range, $15-23\%$ of the systems are considered fully relaxed at $z=0$. The fraction of relaxed haloes decreases with redshift up to $z\sim0.4$, after which the decrease is far slower.

### [B] 67.1 — MeerKAT Reveals Evidence of a Radio Megahalo at GHz Frequency
- **arXiv:** [2608.12042](https://arxiv.org/abs/2608.12042)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (67.1), ism_methods_data (64.4), molecular_clouds (57.5)
- **Current keyword baseline:** NO
- **BM25 max:** 29.1
- **Semantic max:** 83.9
- **Abstract:** Radio megahalos are recently discovered large-scale diffuse synchrotron sources identified through LOFAR observations. We present MeerKAT L-band observations of the massive galaxy cluster RXC~J0528.9$-$3927, that reveals faint emission surrounding its central radio halo. At 1.28 GHz, the known $\sim1.14$ Mpc halo is embedded within previously unreported low-surface-brightness emission extending to $\sim2$ Mpc. The surface-brightness profile of the emission shows a distinct flattening beyond $\sim0.55R_{500}$, suggesting that the outer emission forms an additional component. These properties make the cluster a candidate megahalo system and potentially the first detected at GHz frequencies, although deeper multi-frequency observations are required for confirmation.

### [B] 67.0 — ALMA high resolution observations of Betelgeuse: Persistent structure spanning the inner atmosphere
- **arXiv:** [2608.19339](https://arxiv.org/abs/2608.19339)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** molecular_clouds (67.0), ism_methods_data (64.5), astrochemistry (63.6)
- **Current keyword baseline:** YES
- **BM25 max:** 52.7
- **Semantic max:** 80.7
- **Abstract:** The extended atmosphere of red supergiants (RSGs) forms an important link in the process of mass loss and the subsequent enrichment of the interstellar medium. Large-scale convection is thought to play a significant role, which is likely to result in irregularities in the surface. High resolution, high contrast sub-mm images of Betelgeuse - one of the closest RSGs - are used to probe the structure and temporal stability of the inner 1-2$R_\star$ of its atmosphere. Using ALMA in the longest baseline configuration, continuum emission and lines of SiO and CO and their isotopomers were observed at $λ$0.6-1.4mm, giving beamwidths down to 7mas at the shortest wavelengths. These were compared with a similar observation taken at 0.9mm approximately 7 years earlier. The observed continuum emission arises mostly from an optically-thick mm/sub-mm photosphere of radius 1.1-1.3$R_\star$ with a relatively constant temperature of $\sim$2300K, but with two hotter patches to the NE and SW. The brightest of these has a temperature enhancement of $\sim$800K, and its location and intensity appears relatively unchanged since the 2015 observation. The sub-mm photosphere shows deviations of up to $\pm$ 6% in radius, with weaker continuum extending out to $\sim$2.5$R_\star$ - similar to the extent of clumpy emission in SiO and CO. The hot regions of gas and deviations from radial symmetry are thought to be associated with active shocks driven by underlying convective cells, although their lifetimes appear longer than model predictions. They lie near the proposed poles of the star, which might suggest enhanced and relatively stable polar convection. The present data show no clear evidence for stellar rotation in the extended line emission or absorption against the photosphere, although the structure of the gas emission has changed significantly since 2015.

### [B] 67.0 — A systematic comparison of green valley selection criteria across multiparameter spaces using a homogeneous ultraviolet-optical dataset
- **arXiv:** [2608.12260](https://arxiv.org/abs/2608.12260)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (67.0), astrochemistry (61.4), star_formation (58.9)
- **Current keyword baseline:** NO
- **BM25 max:** 47.7
- **Semantic max:** 76.8
- **Abstract:** We present a systematic comparison of commonly adopted green valley (GV) selection criteria by examining their distributions across multiple observational and physical parameter spaces. Using a homogeneous ultraviolet-optical dataset constructed from the Galaxy Evolution Explorer (GALEX) and the Sloan Digital Sky Survey (SDSS), we construct GV samples based on rest-frame $u-r$ and NUV$-r$ colours, specific star formation rate, and the $D_n(4000)$ spectral index. These samples are analysed in colour--stellar mass, colour--magnitude, and star formation rate--stellar mass diagrams. We find that the different selection criteria identify statistically distinct subsets of GV galaxies occupying different regions of parameter space. Ultraviolet-based selections are compact in NUV$-r$ colour space but shift toward optically red galaxies and lower star formation activity in the star formation rate--stellar mass plane. The $u-r$-selected sample is more tightly confined in optical colour space but is biased toward higher star formation rates, whereas the $D_n(4000)$-based selection yields the most heterogeneous population. In contrast, the sSFR-selected GV sample exhibits the most consistent behaviour across all parameter spaces. Despite these differences, all selection methods span a similar stellar mass range, indicating that the observed variations arise primarily from differences in star formation activity rather than stellar mass. The relatively small overlap between the different selection criteria demonstrates that GV identification is strongly diagnostic-dependent and that the commonly adopted one-dimensional definitions are not interchangeable. These results highlight the importance of combining complementary diagnostics to obtain a more complete and physically meaningful picture of transitional galaxy populations.

### [B] 66.9 — Modeling Relativistic Tidal Disruptions of MESA Stars
- **arXiv:** [2608.19402](https://arxiv.org/abs/2608.19402)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA, astro-ph.SR, gr-qc
- **Top topics:** star_formation (66.9), feedback_bubbles (51.6), ism_methods_data (49.4)
- **Current keyword baseline:** NO
- **BM25 max:** 38.2
- **Semantic max:** 76.6
- **Abstract:** Tidal disruption events (TDEs) occur when a star passes so close to a black hole that its self-gravity is overcome by the external tidal field. As the star passes, it initially deforms, then is ripped apart, and some of its material eventually falls back on bound orbits, forming an accretion disk around the black hole. A Newtonian model of TDEs, based on stellar perturbation theory of MESA stars, was recently introduced as an alternative to computationally intensive hydrodynamical simulations. In this work, we add relativistic corrections to the model, incorporating equatorial Kerr geodesics, relativistic tidal fields, and relativistic fallback times. Compared to the Newtonian case, we find that stars are disrupted earlier in their orbit, which gives them less time to accumulate physical deformations. Additionally, we find that the increased distance from the black hole at the time of disruption makes the fallback time longer. However, the black hole spin has a negligible impact on fallback time, except for orbits with exceptionally close pericenter. Our results allow for a more accurate calculation of fallback rates than the Newtonian model, while also remaining computationally cheap. The code is available on GitHub.

### [B] 66.9 — The Koi Pond: A Strongly Lensed Protocluster Core hosting a Diverse Population of DSFGs
- **arXiv:** [2608.15997](https://arxiv.org/abs/2608.15997)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (66.9), molecular_clouds (66.6), feedback_bubbles (66.3)
- **Current keyword baseline:** NO
- **BM25 max:** 60.5
- **Semantic max:** 83.6
- **Abstract:** We present James Webb Space Telescope (JWST) and Atacama Large Millimeter Array (ALMA) observations of PJ0846+15, \textit{The Koi Pond}, a strongly lensed protocluster core at Cosmic Noon. This field offers a magnified view of 11 dusty star-forming galaxies (DSFGs) all at $z=2.67$ (within $ΔV=800$ km s$^{-1}$) spanning a projected extent of $>300$ kpc lensed by a $z=0.77$ foreground cluster. NIRCam and ALMA Band 6 continuum measurements map the stellar distribution and thermal dust emission respectively at a spatial resolution of $\sim$0.15$^{\prime\prime}$. This analysis reveals a diverse population of DSFGs, with evidence of both interacting and non-interacting systems exhibiting a wide range of morphological features including spiral arms, bars, bulges, clumps/stellar clusters, tidal tails/debris and displaced molecular gas reservoirs. Comparing the rest-frame J- band continuum (F444W) vs (i-J) color (F277W$-$F444W), we find a wide range of values, suggesting a $>$1-dex spread in stellar mass and a dust attenuation reddening of $ΔA_{\mathrm{V}} > 1$ mag. The DSFG members exhibit varying dust sizes relative to the stellar emission, ranging from compact dusty cores to galaxy-wide emission. Resolved color maps of individual sources showing a spread as high as F277W$-$F444W$=2$ mag suggesting complex stellar-to-dust geometry. Although gas-rich mergers are identified in the core, the most red and dust emitting members are disks exhibiting clumpy structure indicating secular growth can drive these starburst events. Such a remarkable range in properties within this sample suggest DSFGs in protocluster core environments follow diverse evolutionary pathways towards their transition into quiescent, elliptical cluster galaxies.

### [B] 66.8 — CIBER $\times$ galaxy cross-correlations reveal a bright, low-redshift NIR background
- **arXiv:** [2608.12116](https://arxiv.org/abs/2608.12116)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, astro-ph.GA
- **Top topics:** galactic_ism_surveys (66.8), massive_star_formation (59.7), ism_methods_data (56.9)
- **Current keyword baseline:** NO
- **BM25 max:** 54.6
- **Semantic max:** 83.5
- **Abstract:** We perform the first tomographic analysis of near-IR extragalactic background light (EBL) anisotropies, cross-correlating CIBER 1.1 and 1.8 $μ$m imager data with photometric galaxy catalogs from DESI Legacy Survey DR8 and Hyper-Suprime-Cam Ultra-Deep Survey. We measure significantly higher cross-power than expectations from an integrated galaxy light (IGL) model on scales $\ell < 2000$, concentrated at low redshift ($z\lesssim 0.6$). Cluster member galaxies and associated structure account for 15-20\% of the large-angle cross-power, indicating that group- and galaxy-scale halos contribute the bulk of the signal. Through a parametric halo model decomposition, we detect two-halo and one-halo clustering in cross-power at high significance, with amplitudes that decline smoothly across $z=0{-}1$. The inferred one-halo cross-power is of similar amplitude between DESI-LS and the deeper HSC catalog, implying a scenario in which low-redshift EBL fluctuations are amplified by contributions from lower-mass halos with satellites and/or diffuse intra-halo light (IHL). Converting our two-halo fits into estimates of $b_I \times dI/dz$, we find that standard IGL predictions underestimate our measurements, even when assuming an intensity bias as high as 3, similar to that of large SZ clusters, suggesting that a higher $dI/dz$ is required to reconcile observed discrepancies. Lastly, we find that correlated large-scale structure (LSS) at $z<1$ accounts for a substantial fraction of the CIBER auto-power reported in earlier work. These results identify low-redshift LSS as a significant and previously unappreciated contributor to near-IR EBL fluctuation measurements, setting the stage for cross-correlation science with CIBER-2, SPHEREx and a variety of LSS tracers.

### [B] 66.7 — Orbital Migration of Interacting Stellar Mass Black Holes in Disks around Supermassive Black Holes. III. Mass Distribution of Hierarchical Mergers
- **arXiv:** [2608.13641](https://arxiv.org/abs/2608.13641)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.HE
- **Top topics:** feedback_bubbles (66.7), massive_star_formation (63.4), star_formation (62.8)
- **Current keyword baseline:** NO
- **BM25 max:** 38.1
- **Semantic max:** 83.3
- **Abstract:** Active galactic nucleus (AGN) disks are a promising location for the formation of binary black holes (BBHs) that will merge on relatively short timescales and be detected by LIGO-Virgo-KAGRA (LVK). To compare the mass function (MF) of black holes (BHs) undergoing hierarchical mergers in AGN disks to the inferred MFs from LVK observations, we perform 360 simulations with an N-body code augmented to include an analytic model for migration torques and other gas forces. We focus on the region surrounding migration traps in AGN disks where migration torques cancel out and BHs converge. We find that regardless of changes in the initial MF and BBH merger criteria, frequent mergers deplete the number of BHs with masses $\lesssim 10$~$M_\odot$ and fill the upper mass gap with a roughly uniform distribution from 40--100~$M_\odot$, with a slight overabundance around ${\approx}70~M_\odot$ from resonant orbiters. We also find an average merger rate of $\sim 6$~Gpc$^{-3}$~yr$^{-1}$ for migration-trap-aided BBH mergers in our AGN disk model. $\sim 40\%$ of these mergers have uneven mass ratios and 16\% have a primary mass $\in[50-100]~M_\odot$. Therefore, AGN disks could easily be the source of BBH mergers observed by LVK that are difficult to produce through traditional stellar evolution channels. Our simulations also form a separate higher-mass intermediate mass black hole (IMBH) population $>200~M_\odot$ after $\sim 2$~Myr. Future gravitational wave detectors can use observations of this IMBH population to constrain models of AGN accretion disks.

### [B] 66.6 — Design, assembly, and initial test results of a cryostat for holographic characterization of microwave telescopes
- **arXiv:** [2608.19337](https://arxiv.org/abs/2608.19337)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (66.6), molecular_clouds (64.5), turbulence (52.4)
- **Current keyword baseline:** NO
- **BM25 max:** 45.3
- **Semantic max:** 80.6
- **Abstract:** We describe the design, fabrication, assembly, and room-temperature vacuum qualification of a 1.4-m long cylindrical cryostat developed for holographic testing of cryogenic microwave telescope optics. The system consists of a welded 6061-aluminum vacuum vessel containing nested 45- and 4-K aluminum radiation shields, cooled by a two-stage pulse-tube cryocooler through commercial OFHC copper flexible thermal straps. The intermediate 45-K stage intercepts radiative, conductive, and wiring heat loads from room temperature, while the 4-K stage defines the volume used for optical testing. The cryostat includes a 38-cm aperture for a microwave-transparent vacuum window and is sized to accommodate full-scale optical assemblies relevant to cosmic microwave background instrumentation. We summarize the cryostat architecture, lightweighted radiation shields, G-10 support flexures, welded vacuum-vessel fabrication, and room-temperature leak-checking campaign. Iterative helium leak checking and weld repair reduced the observed leak rate in the cryostat by over three orders of magnitude.

### [B] 66.6 — The effect of galaxy interactions on star formation rates in the COLIBRE simulations
- **arXiv:** [2608.12132](https://arxiv.org/abs/2608.12132)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (66.6), star_formation (60.7), astrochemistry (59.8)
- **Current keyword baseline:** NO
- **BM25 max:** 61.7
- **Semantic max:** 83.2
- **Abstract:** Observations and theory indicate that galaxy interactions enhance star formation rates (SFRs). However, the degree of enhancement and its dependence on the properties of the interacting galaxies vary across different studies. In this work, we use the COLIBRE simulations of galaxy formation to investigate the effect of interactions on the SFRs of star-forming galaxies at redshift $z\approx0$. The COLIBRE simulations capture the multiphase nature of the interstellar medium and have volumes up to $200^3$ and $400^3$ cMpc$^3$ at m6 (gas and dark-matter particle mass $\sim10^6~\mathrm{M_\odot}$) and m7 ($\sim10^7~\mathrm{M_\odot}$) resolutions, respectively. After constructing samples of interacting galaxies (with mass ratios $>0.1$) and isolated controls, matched in stellar mass, large- and small-scale environment, and redshift, we show that the average specific SFR (sSFR) of interacting galaxies is enhanced by up to a factor of $\approx2$ for separations of $\approx10$ kpc. The enhancement decreases with pair separation but remains significant out to $\approx200$ kpc. The enhancement increases with increasing numerical resolution, is more pronounced in the central regions of galaxies, and decreases with increasing stellar mass at fixed separation. Mergers with higher mass ratios induce stronger sSFR enhancement. We compare our results with observational data from the SDSS, finding good agreement in the dependence of the mean sSFR enhancement on separation, but underpredicting its normalisation by a factor of $\approx2$. Finally, we show that the pre-merger sSFR enhancement of resolved interactions accounts for $\approx2$ per cent of the $z\approx0$ cosmic SFR density.

### [B] 66.5 — Evolution of lunar wake potentials: structure, energy conversion, and their imprints on velocity distributions
- **arXiv:** [2608.18383](https://arxiv.org/abs/2608.18383)
- **Primary category:** physics.space-ph
- **Categories:** physics.space-ph, astro-ph.EP, physics.plasm-ph
- **Top topics:** turbulence (66.5), molecular_clouds (59.8), star_formation (56.8)
- **Current keyword baseline:** NO
- **BM25 max:** 44.5
- **Semantic max:** 83.2
- **Abstract:** We study the evolution of electric potentials in the lunar wake. The wake potential exhibits two distinct spatial scales. The macroscopic scale arises from solar wind expansion into the vacuum, with a potential length-scale growing with distance from the Moon; the microscopic scales arises from ion acoustic shocks near the wake center, with transition layers spanning tens of local Debye lengths. This two-scale potential mediates energy conversion between ions and electrons during wake refilling. The macroscale potential retards electrons and accelerates ions to supersonic velocities, converting electron thermal energy to ion kinetic energy. The microscale potential then decelerates ions to subsonic velocities and heats both species, converting ion kinetic energy back to thermal energy. Together, the two-scale potential imprints distinct signatures on velocity distributions, including ion beams and electron flat-top distributions, consistent with ARTEMIS observations.

### [B] 66.4 — Variable Star Polarimetry with PICSARR-2
- **arXiv:** [2608.18051](https://arxiv.org/abs/2608.18051)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.SR
- **Top topics:** astrochemistry (66.4), magnetic_fields (60.5), molecular_clouds (59.7)
- **Current keyword baseline:** YES
- **BM25 max:** 40.6
- **Semantic max:** 83.0
- **Abstract:** We describe the upgraded Polarimeter using Imaging CMOS Sensor and Rotating Retarder 2 (PICSARR-2), describe its applications, and characterize its performance for stellar polarimetry on a 36-inch and 14-inch telescope. On the larger telescope in the SDSS $g^\prime$, $r^\prime$ and $i^\prime$ filters a precision of $σ_p=$ 5.7 ppm on bright stars is recorded using a fast modulation rate corresponding to frame exposures of 12 ms; accounting for the internal errors in the individual observations gives a limiting precision of $e_p=$ 1.3 ppm. Longer frame rates are required for stars with $m > 5$, but the recorded errors only underperform a photon shot noise derived extrapolation for $m > 8$, when even longer frame exposures are required. Stars as faint as $m = 11$ were observed. The position angle precision is measured as 0.0845 degrees, and there is very good agreement between observations made by both the PICSARR-2 and HIPPI-2 polarimeters. On the smaller telescope the instrument's performance approaches similar levels, and there is good cross-platform stability in the observation of standard stars. PICSARR-2 is therefore an excellent instrument to explore stellar variability due to a range of phenomena; examples from our ongoing pulsating star campaign and other variable star programs are presented.

### [B] 66.4 — X-ray Activity of the RS CVn-type Star σ Gem with the First-Year Observations of Einstein Probe
- **arXiv:** [2608.14009](https://arxiv.org/abs/2608.14009)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.SR
- **Top topics:** ism_methods_data (66.4), astrochemistry (64.0), star_formation (63.4)
- **Current keyword baseline:** NO
- **BM25 max:** 51.6
- **Semantic max:** 80.0
- **Abstract:** Context. Stellar flares are energetic events driven by the sudden release of magnetic energy in the stellar atmosphere. Studying these flares is crucial for understanding their impact on exoplanets, the circumstellar environment, and stellar evolution itself. The launch of the Einstein Probe (EP) offers a unique opportunity to systematically detect such events. Aims. We present a systematic analysis of the flaring activity of the active RS CVn-type binary σ Gem, utilizing the first-year monitoring data from the Wide-field X-ray Telescope (WXT) aboard EP. Our goals are to demonstrate the unique capability of EP in monitoring stellar X-ray activity and detecting flares, by identifying and characterizing extreme X-ray flares on σ Gem and estimating their occurrence rate. Methods. We developed a data-processing pipeline to select and extract EP-WXT observations, producing a background-subtracted, vignetting-corrected light curve. We employed the Bayesian Blocks method to detect significant flares in the long-term X-ray light curve. For each identified flare, we performed light curve and spectral fitting to derive the flare parameters. Results. Between October 2024 and April 2025, WXT detected 6 distinct flares from σ Gem. Their durations ranged from 21 hours to 3 days, with peak X-ray luminosities (0.5-4 keV) of 3.7 * 10^31 to 7.0 * 10^32 erg/s and total energies of 1.1 * 10^36 to 4.4 * 10^37 erg, placing them among the "superflare" class. Conclusions. Using σ Gem as a case study, we demonstrate an analysis process for flare detection and analysis with EP-WXT data, which provides new statistical constraints on its flaring behavior. Applying this methodology to the growing EP stellar archive promises to yield a vast sample of X-ray flares, which will significantly advance our understanding of stellar magnetic activity.

### [B] 66.4 — How Neutron Star Radii Encode the Dense-Matter Equation of State and Hadron-Quark Transition
- **arXiv:** [2608.12632](https://arxiv.org/abs/2608.12632)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, hep-ph, nucl-ex, nucl-th
- **Top topics:** ism_methods_data (66.4), star_formation (54.9), turbulence (51.7)
- **Current keyword baseline:** NO
- **BM25 max:** 40.2
- **Semantic max:** 83.0
- **Abstract:** We investigate how future high-precision neutron star (NS) radius measurements encode microscopic information about the dense-matter equation of state (EOS), focusing on a possible first-order hadron--quark phase transition and the resulting mass--radius topology. Within a Bayesian framework using meta-model EOSs with nine microscopic parameters, we analyze mock radius measurements $R_{1.4}=11.9\pmσ_R$ km with $σ_R=0.9$ and $0.1$ km for canonical NSs. We introduce inverse EOS--radius mappings that give the posterior mean of each EOS parameter as a function of $R_{1.4}$. Their slope measures radius sensitivity, while their curvature determines the leading precision dependence of the posterior mean through the Jensen expansion. Resolving the mappings into four mass--radius topologies, Connected, Disconnected, Both, and No-Quark-Matter, reveals a clear hierarchy of information. The symmetry-energy parameters $L$ (slope) and $K_{\rm sym}$ (curvature) are strongly encoded in $R_{1.4}$ and their posterior means shift appreciably with improved radius precision, whereas the higher-order hadronic parameters show stronger topology dependence. Among the transition parameters, the transition density $ρ_t$ is the most strongly encoded in $R_{1.4}$, while the energy-density jump and quark-matter sound speed are more strongly associated with the topology of the full mass--radius sequence. Since the different topologies have strongly overlapping $R_{1.4}$ distributions, even precise radius measurements cannot by themselves identify the topology or uniquely determine the high-density transition properties. These results provide a parameter-dependent hierarchy for assessing the scientific return of future high-precision radius measurements and complementary probes of high-density

### [B] 66.3 — Imprints of Mass Accretion History on Galaxy Cluster Morphology
- **arXiv:** [2608.18031](https://arxiv.org/abs/2608.18031)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** massive_star_formation (66.3), star_formation (60.4), galactic_ism_surveys (53.4)
- **Current keyword baseline:** NO
- **BM25 max:** 45.6
- **Semantic max:** 82.8
- **Abstract:** Variations in dynamical states of galaxy clusters can introduce biases and scatter in observable-mass relations. The dynamical state of a cluster is an emergent feature of its mass accretion history (MAH), it is therefore useful to constrain the MAH of the cluster. In this work, we characterize 305 massive clusters from The300 project by connecting features from their projected stellar distributions to their mass accretion histories (MAH). As a baseline, we first correlate host dark matter halo dynamical state indicators at $z=0$ with their MAH via the Spearman rank correlation coefficient $ρ_{\mathrm{sp}}$. Both substructure mass fraction and center-of-mass offset measurements correlate strongly with the MAH measured between $0.1\lesssim z\lesssim 1$. We repeat this exercise with morphological measurements of projected stellar density maps, many of which exhibit moderate correlation strength with different times in the MAH. Broadly, core morphological measurements ($r \leq 30\,\mathrm{kpc}$) correlate better with early-time MAH. Core-excised ($50\,\mathrm{kpc} \leq r \leq 1\,\mathrm{Mpc}$) morphological measurements correlate better with late-time MAH. We further quantify the MAH prediction power of both traditional dynamical state indicators and morphological parameters using Multivariable Conditional Abundance Matching (MultiCAM). MultiCAM employs simple rank-ordering operations, making it straightforward to translate to observed datasets. We find reasonable ($ρ_{\mathrm{sp}} \geq 0.6$) performance for predictions of the mass fraction between $1\lesssim z\lesssim 0.1$, though with notable information loss when using projected quantities. In one example application of our methodology, we use the coefficients of the MultiCAM models to select subsamples of galaxy clusters that have accreted more (or less) of their $z = 0$ mass budget over a given time frame.

### [B] 66.3 — Diffuse Dwarf Galaxies in Galaxy Clusters: I. Stellar Populations and Radial Gradients
- **arXiv:** [2608.17375](https://arxiv.org/abs/2608.17375)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (66.3), massive_star_formation (63.4), star_formation (54.3)
- **Current keyword baseline:** NO
- **BM25 max:** 63.7
- **Semantic max:** 82.9
- **Abstract:** We use Keck/KCWI spectroscopy to study one ultra-diffuse galaxy (UDG) and five Nearly-UDGs (NUDGEs) in the Perseus cluster, together with an additional UDG in the Coma cluster. As the first paper in a series, we focus on the global and radial stellar population properties of our sample. We find that these galaxies host intermediate-to old stellar populations, with typical ages of ~7 Gyr, low metallicities ([M/H]$\simeq$ -0.9 dex), and enhanced [Mg/Fe] abundances (~0.3 dex), consistent with previous studies. Six galaxies lie within the scatter of the present-day mass-metallicity relation (MZR), whereas the Coma UDG (DF11) is more consistent with the MZR of high-z galaxies (z ~ 2). We find no strong correlation between global stellar population properties and cluster infall parameters, suggesting that any environmental impact is not easily traceable through integrated stellar populations. We go one step further and measure radial gradients for three galaxies. Two show flat age and mildly negative metallicity gradients, similar to classical dwarfs, while one shows a rising metallicity profile as recently found in other UDGs. Comparing with classical dwarfs, we find a continuous correlation between metallicity gradient and globular cluster (GC) richness, where more GC-rich systems tend to show rising profiles. We propose that preferential tidal disruption of GCs in the inner regions of galaxies naturally produces rising metallicity profiles, unlike GC-poor classical dwarfs. This mechanism, potentially coupled with strong stellar feedback from early concentrated star formation, may explain the unusual rising metallicity profiles observed in GC-rich UDGs/NUDGEs.

### [B] 66.2 — Generative artificial intelligence for reconstructing neutron-star matter
- **arXiv:** [2608.17457](https://arxiv.org/abs/2608.17457)
- **Primary category:** nucl-th
- **Categories:** nucl-th, astro-ph.HE, astro-ph.IM, hep-ph, nucl-ex
- **Top topics:** ism_methods_data (66.2), turbulence (58.0), astrochemistry (58.0)
- **Current keyword baseline:** NO
- **BM25 max:** 42.6
- **Semantic max:** 82.7
- **Abstract:** Neutron-star cores hold the only known matter in the universe that is simultaneously cold and strongly interacting, compressed beyond nuclear density into a state of unknown composition. The equation of state links stellar masses, radii and tidal deformabilities to this regime, but recovering this key quantity from sparse observations is an ill-posed inverse problem. Existing analyses bury a prior in a fixed functional form, unevenly weighting admissible solutions and biasing the result. We reconstruct the equation of state with a denoising diffusion model that keeps prior, physics and data separate: it learns an inspectable, physically motivated prior anchored to first-principles nuclear theory, while perturbative-QCD and astrophysical constraints are imposed exactly. Future measurements therefore will update the posterior by reweighting alone, without retraining or resampling. The inferred radius of 12.6 km and tidal deformability of 469 at 1.4 solar masses reproduce Gaussian-process and heavy-ion-informed inferences despite a far broader prior. We find near-conformal but still stiff matter in the heaviest stars, consistent with a gradual hadron-quark crossover and disfavouring a strong first-order phase transition. More broadly, coupling a learned prior to exactly enforced physics establishes a template for ill-posed inverse problems where theory and data constrain different regions.

### [B] 66.2 — The Roman Coronagraph Community Participation Program: data reduction pipeline design and implementation
- **arXiv:** [2608.17048](https://arxiv.org/abs/2608.17048)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (66.2), molecular_clouds (60.8), star_formation (57.5)
- **Current keyword baseline:** NO
- **BM25 max:** 33.4
- **Semantic max:** 76.0
- **Abstract:** The Roman Space Telescope Coronagraph Instrument will demonstrate a series of technologies and techniques to enable the direct detection of reflected-light planets with space-based observatories. To characterize and validate the performance of the Coronagraph Instrument, the Community Participation Program is developing corgidrp, an open-source Python-based data reduction pipeline. The pipeline can process data from the required and best-effort observing modes and their associated calibration sequences into calibrated science-ready data products. We present the software design and implementation of corgidrp and the motivation behind specific design decisions. We describe the software architecture, data flow, processing steps, automation tools, testing framework, and development philosophy. We also outline future development plans in preparation for on-sky data.

### [B] 66.1 — eROSITA cosmology with galaxy groups: hot gas budget out to the virial radius
- **arXiv:** [2608.17735](https://arxiv.org/abs/2608.17735)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** feedback_bubbles (66.1), galactic_ism_surveys (64.2), ism_methods_data (52.6)
- **Current keyword baseline:** NO
- **BM25 max:** 55.1
- **Semantic max:** 80.2
- **Abstract:** Non-gravitational processes that expel hot gas beyond the virial regions of groups and clusters of galaxies, known collectively as baryonic feedback, play a key role in reshaping the matter distribution of the Universe on Mpc scales. We use eROSITA observations of a complete sample of 25 galaxy groups selected from the first public release of the eROSITA-DE data (eRASS1) and identified with the Two Micron Redshift Survey optical group catalogue (2MRS). We extract and fit surface brightness (SBx) profiles and present hot gas mass and hot gas fraction profiles out to $R_{200}$. We perform a Bayesian analysis of $M_{\mathrm{gas}}-M_{\mathrm{tot}}$, $L_{\mathrm{X}}-M_{\mathrm{tot}}$, and $L_{\mathrm{X}}-M_{\mathrm{gas}}$ relations, taking into account the aperture covariance effects. At $R_{500}$, we report uniformly flat SBx profiles with a mean $β$ parameter of $0.38 \pm0.04$, steepening to $β= 0.76\pm0.19$ beyond $R_{500}$. We measure a sub-cosmic hot gas fraction at the median mass of our sample $M_{500} = 2.54\times10^{13}M_{\odot}$ of $ f_{\mathrm{gas,500}} = 4.32\pm0.42\%$. Similarly, at $R_{200}$ and the median mass $M_{\mathrm{ 200}} = 3.69\times10^{13}M_{\odot}$, we obtain $f_{\mathrm{gas,200}}=5.78\pm0.69\%$. Our $f_{\mathrm{gas}}-M_{\mathrm{tot}}$ and $L_{\mathrm{X}}-M_{\mathrm{tot}}$ relations show significant deviations from the predictions of the strong feedback variants of the FLAMINGO simulation ($2.5σ$ to $8.0σ$ tension), while fiducial FLAMINGO and BAHAMAS provide the closest match to our measurements. Using our measured baryon fractions and the \texttt{SP(k)} model, we infer a $10\%-15\%$ reduction in the matter power spectrum at $k = 5\ h\ \mathrm{Mpc}^{-1}$ relative to a dark matter-only universe, in agreement with fiducial FLAMINGO and BAHAMAS, while revealing a growing tension on smaller scales with the strong feedback variants.

### [B] 66.1 — The Roman Coronagraph Community Participation Program: early calibration plan and pilot observation of a companion
- **arXiv:** [2608.17348](https://arxiv.org/abs/2608.17348)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** molecular_clouds (66.1), ism_methods_data (60.3), astrochemistry (55.1)
- **Current keyword baseline:** NO
- **BM25 max:** 30.6
- **Semantic max:** 82.6
- **Abstract:** Roman is set to launch in weeks! The Coronagraph Instrument - technology pathfinder for future direct imaging missions - is ready to fly too. According to predictions, laboratory tests and high fidelity simulations, it will open a new contrast regime enabling the imaging of mature, giant planets in visible reflected light. The Community Participation Program is responsible for preparing a comprehensive observing program with associated data processing software and calibrations. We give a brief update about the on-going "baseline" calibration plan for the first months. Additionally, we describe a pilot program aiming for the stellar companion HD 29992 B at moderate ~1e-5 to ~1e-6 Band 1 (575 nm) contrast, to be carried out as soon as the instrument is operational. The idea is to generate a canonical data set with a self luminous companion that is easily recoverable. This functional checkout will be precious to best prepare our community, exercise our calibration plan and suite of tools.

### [B] 66.1 — 4U 1538-52 in a Heartbeat: Broadband X-ray Spectral Properties from XMM-Newton and NuSTAR
- **arXiv:** [2608.14938](https://arxiv.org/abs/2608.14938)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** molecular_clouds (66.1), star_formation (56.5), feedback_bubbles (55.5)
- **Current keyword baseline:** NO
- **BM25 max:** 58.4
- **Semantic max:** 75.5
- **Abstract:** Galactic high-mass X-ray binaries (HMXBs) are important systems for studying accretion mechanisms onto compact objects and for investigating the complex stellar winds of massive stars. In particular, HMXBs hosting a neutron star allow us to reveal the structure of the accreted material in X-ray pulsars and consequently to investigate how matter behaves under extreme conditions of pressure and density. These are major scientific goals for XRISM and NewAthena. Here we report on the first out-of-eclipse XMM-Newton observation of the HMXB 4U 1538-52, complemented by NuSTAR coverage. Our campaign aimed to investigate stellar-wind variability and continuum changes with high-resolution spectroscopy at a critical orbital phase: when the neutron star is in inferior conjunction. Thanks to simultaneous observations covering both soft and hard X-rays, we obtain the most detailed X-ray view of the accreted material in 4U 1538-52 to date. In particular, we perform time-resolved spectroscopy down to the pulse period of the neutron star to highlight wind clumping properties and accretion structures. In this dataset, we observe a bright flare reaching $\sim$10$^{37}\,\rm{erg\,s^{-1}}$ probably induced by the accretion of a $10^{20}\,\rm{g}$ clump, followed by a luminosity dip forming a heartbeat-like episode. This event is followed by three local absorption peaks with local variability of the order of the pulse period, and a gradual hardening of the underlying spectrum throughout the observation. This could indicate the presence of both small-scale and large-scale overdense structures in the vicinity of the neutron star, which can be attributed to clumps and filamentary structures embedded in the accretion wake. These observational evidences are further supported and reproduced by 3D hydrodynamic simulations.

### [B] 65.9 — The MAGPI Survey: Emission Line Products Data Release and the Role of Spectroscopic Aperture Covering Fraction on the Balmer Decrement-Stellar Mass Relation
- **arXiv:** [2608.18464](https://arxiv.org/abs/2608.18464)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO
- **Top topics:** galactic_ism_surveys (65.9), astrochemistry (61.2), ism_methods_data (57.1)
- **Current keyword baseline:** NO
- **BM25 max:** 80.7
- **Semantic max:** 82.3
- **Abstract:** The Middle Ages Galaxy Properties with Integral field spectroscopy (MAGPI) survey is a Large Program on the European Southern Observatory Very Large Telescope using the MUSE instrument. This paper presents the data release for the MAGPI emission line products and includes emission line maps for 836 galaxies at $0.05\leq z_\mathrm{spec}\leq 0.424$ ($\mathrm{H}α$-window) and aperture-based emission line measurements for 2,607 galaxies at $0.05\leq z_\mathrm{spec}\leq 1.50$ (upper bound is [OII] cut-off), both based on the GIST software, for all 56 MAGPI fields. We use these data to examine dust attenuation, which represents a major source of uncertainty in the derived properties of galaxies that are critical to constrain models of galaxy evolution. We examine the role that the spectroscopic aperture covering fraction ($f_c$) has on the relationship between the Balmer decrement ($\mathrm{BD}=F(\mathrm{H}α)/F(\mathrm{H}β)$; a common proxy for dust attenuation) and the total stellar mass ($M_\star$). Several studies have suggested that the BD-$M_\star$ relation may be redshift invariant; however, the compared surveys often have different $f_c$ due to their differing fibre or slit sizes that can cause systematic offsets. Our results indicate that $f_c$ has a significant impact on this relationship, due to galaxies having negative BD radial gradients, which are more negative for more massive galaxies at $z\lesssim0.4$. Comparing spectroscopic surveys with $\left<f_c\right> \gtrsim 0.5$, we find that the BD-$M_\star$ relation shows a preference for redshift evolution and is roughly consistent with the behaviour of UV stellar continuum attenuation redshift evolution ($A_\mathrm{FUV}$-$z$), with the average dust attenuation in galaxies peaking at $z\sim1.2$ and decreasing at lower and higher redshifts.

### [B] 65.8 — Asteroseismic analysis of red giants in eclipsing binaries using two methods: implications for scaling relations and chemical composition
- **arXiv:** [2608.18250](https://arxiv.org/abs/2608.18250)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** astrochemistry (65.8), feedback_bubbles (52.5), star_formation (49.7)
- **Current keyword baseline:** YES
- **BM25 max:** 50.6
- **Semantic max:** 75.1
- **Abstract:** The study of solar-like oscillating red giants in eclipsing binaries (EBs) provides a unique opportunity to advance stellar astrophysics by combining dynamical mass and radius measurements with asteroseismic constraints. EBs provide precise fundamental parameters (e.g. mass, radius, and luminosity) independent of distance, while solar-like oscillations probe stellar interiors and enable tests of asteroseismic scaling relations used to determine stellar masses and radii. {We apply two different methods to estimate the initial chemical composition of the systems. In Method I, the initial helium abundance ($Y_0$) is treated as the free parameter, whereas in Method II the free parameter is the initial metallicity ($Z_0$), assuming a relation between $Y_0$ and $Z_0$. We construct interior models individually for the components of 11 EBs and obtain coeval solutions for eight systems.} The ages and chemical compositions derived from the two methods are generally consistent with each other. Our results provide important clues about the chemical evolution of a part of the Galactic disk. Moreover, using the parameters obtained for two oscillating stars, Tek Ayak (KIC 8410637) and KIC 9970396, instead of solar reference values in the scaling relations yields masses and radii that are in much better agreement with the dynamical solutions without requiring additional corrections.

### [B] 65.8 — The fraction of periodic SN Ib/c light curves
- **arXiv:** [2608.18207](https://arxiv.org/abs/2608.18207)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (65.8), ism_methods_data (62.3), star_formation (58.1)
- **Current keyword baseline:** NO
- **BM25 max:** 39.1
- **Semantic max:** 82.3
- **Abstract:** Periodic luminosity modulations have been recently identified for the stripped-envelope supernovae SN 2022jli and SN 2022esa, motivating a systematic search for a similar behavior in a larger sample. Such modulations may indicate the explosions arise in binary progenitor systems. We perform the first systematic search for periodic modulation in a sample of 34 Type Ib/c supernovae with high quality photometry from the Zwicky Transient Facility. We develop and apply a statistically rigorous pipeline for detecting periodic modulation in light curves. The pipeline successfully recovers the previously reported periodic undulations of SN 2022jli and SN 2022esa, and identifies SN 2020sgf as an additional promising periodic candidate. Injection-recovery simulations are used to quantify the survey sensitivity as a function of period and modulation amplitude. Comparing the observed detections with recent population synthesis models shows that, under the adopted assumptions, models predicting intrinsic periodic fractions of order ~20% are consistent with the observations. Our results suggest that periodically modulated SN 2022jli-like events may represent a significant sub-population of stripped-envelope supernovae rather than being exceptionally rare events, while demonstrating a methodology suitable for future wide-field transient surveys.

### [B] 65.8 — pynucastro 3: A community library for nuclear astrophysics
- **arXiv:** [2608.17049](https://arxiv.org/abs/2608.17049)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (65.8), feedback_bubbles (57.8), star_formation (57.7)
- **Current keyword baseline:** NO
- **BM25 max:** 39.2
- **Semantic max:** 82.3
- **Abstract:** We describe the latest release of pynucastro: a community python library for nuclear astrophysics. The goal of the pynucastro project is to build the tools needed to interactively explore nuclear properties, reaction rates, and networks, and to export these networks to a variety of simulation codes. Major changes in pynucastro since the last major release include new rate approximations, a stellar equation of state, support for the StarLib library and rate uncertainties, and new tools for exploring networks.

### [B] 65.6 — $R_{\rm e}$, or not $R_{\rm e}$: Developing $R_5\equiv R_{-2}$ as a scale radius for galaxy sizes, masses, and mass-to-light ratios
- **arXiv:** [2608.17680](https://arxiv.org/abs/2608.17680)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** ism_methods_data (65.6), galactic_ism_surveys (58.2), feedback_bubbles (47.6)
- **Current keyword baseline:** NO
- **BM25 max:** 36.4
- **Semantic max:** 82.0
- **Abstract:** The effective half-light radius $R_{\rm e}$ marks an arbitrary 50-per-cent light boundary, and scaling relations involving such effective radii and their associated surface brightnesses, $μ_{\rm e}$, depend systematically on the adopted percentage. Here, a gradient-defined scale, $R_5\equiv R_{-2}$, is developed as an alternative. It is the projected radius where the logarithmic slope of the intensity profile is equal to $-2$, corresponding to a slope of the surface-brightness profile of $5.00\,\text{mag dex}^{-1}$, and the radius at which the luminosity contributed per logarithmic radial interval is maximal. It can be measured non-parametrically or with a parametrized fit. For the Sérsic $R^{1/n}$ family, the exact relation $R_5=(2n/b_n)^n\,R_{\rm e}$ is derived, with $R_5/R_{\rm e}\rightarrow{\rm e}^{1/6}\approx1.181$ as $n\rightarrow\infty$. Reparameterizing the (now $b_n$-free) $R^{1/n}$ model in terms of the observable pair $(R_5,μ_5)$ removes the non-linear (radial scale)-(concentration, $n$) coupling and because the local slope is $5\,\text{mag dex}^{-1}$ at $R_5$, correlated measurement errors in $R_5$ and $μ_5$ largely cancel when deriving the inferred total magnitude. Additionally, an exact single-integral identity is provided to relate any projected light fraction to the fraction within a sphere of the same radius. The directly observable $R_5$ is connected, through a weakly $n$-dependent factor, to the anisotropy-insensitive intrinsic radius $r_{-3}$, yielding a refined $n$-dependent Wolf-type mass estimator $M_{-3}$ and spatial mass-to-light ratio $(M_{\rm dyn}/L)_{-3}$. Past half-light substitutions in dynamical mass estimators have introduced systematic concentration-dependent offsets of 12-18 per~cent in enclosed mass and a range $>20$ per~cent in the mass-to-light ratio. Dynamical mass estimators for (dark matter)-free stellar systems are also provided.

### [B] 65.5 — Size-Mass Relation Shows Its Colours: Contrasting Physical Imprints of Galaxy Evolution in Rest-Frame UV and Optical
- **arXiv:** [2608.18776](https://arxiv.org/abs/2608.18776)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (65.5), ism_methods_data (62.1), feedback_bubbles (59.7)
- **Current keyword baseline:** NO
- **BM25 max:** 42.3
- **Semantic max:** 81.9
- **Abstract:** The galaxy size-mass relation (SMR) is a key scaling relation used to constrain the physical processes that build galaxy structure, yet it is almost always measured in a single rest-frame optical band, where the light traces the bulk of the old stellar mass. Tracing younger populations with flux-weighted ages of ~100-500 Myr and low-metallicity stars, the rest-frame near-ultraviolet opens a new stellar window on this scaling relation. Because each process redistributes the light of young and old stars differently, the same mechanism shifts the slope and zero point of the SMR by different amounts in the two wavelength regimes. Here we review and synthesize the effects of main physical processes on the form of the SMR for star-forming and quiescent galaxies in the rest-UV and optical. For each process, we start from its underlying physics, the galaxy stellar masses it affects, and the light it adds/removes/rearranges, anchoring the predictions to observations and simulations. We validate the predicted imprints with forward Monte Carlo modelling. The two-wavelength view breaks several degeneracies that single-band analyses cannot, most notably between minor mergers, dry major mergers, and adiabatic expansion. These results motivate joint rest-UV and optical SMR measurements with current and upcoming wide-field imaging surveys.

### [B] 65.5 — Radiation damage to the Hubble Space Telescope has been several years out of phase with the Solar cycle
- **arXiv:** [2608.18214](https://arxiv.org/abs/2608.18214)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP, astro-ph.SR, physics.ins-det, physics.space-ph
- **Top topics:** astrochemistry (65.5), ism_methods_data (64.8), feedback_bubbles (54.7)
- **Current keyword baseline:** YES
- **BM25 max:** 32.0
- **Semantic max:** 81.9
- **Abstract:** As well as obtaining beautiful images of the Universe, the Hubble Space Telescope's CCD detectors are sensitive radiation dosimeters that have been monitored in Low Earth Orbit for more than 24 years. The rate of radiation damage they received has varied over each Solar cycle, but several years out of phase with the appearance of sunspots or coronal mass ejections. We investigate functional forms that successfully fit the time series of damage to telescopes elsewhere in the Solar system. We obtain remarkably accurate fits to Hubble data but with physically absurd parameter values. During image post-processing, such fits can be used empirically, to correct more than 99.5% of the radiation damage's effect on image quality. However, fits to the time series with physically reasonable parameters produce worse performance. Our results highlight the diversity of radiation environments in different parts of our Solar system, and the complexity of Low Earth Orbit in particular. Our results also motivate continued monitoring of radiation damage to currently operational spacecraft, to more reliably predict the rate of degradation in (and useful lifespan of) future missions.

### [B] 65.5 — SCExAO/CHARIS High-Contrast Pre-Launch Vetting of Roman Coronagraph Technology Demonstration PSF Reference Stars
- **arXiv:** [2608.17008](https://arxiv.org/abs/2608.17008)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.IM, astro-ph.SR
- **Top topics:** astrochemistry (65.5), molecular_clouds (61.5), star_formation (61.2)
- **Current keyword baseline:** YES
- **BM25 max:** 30.3
- **Semantic max:** 81.9
- **Abstract:** We present deep, SCExAO/CHARIS high-contrast integral field spectroscopy and archival imaging of four candidate Roman Coronagraph PSF reference stars within/near the Roman Continuous Viewing Zone and potentially suitable for the Coronagraph's key technology demonstration targets HIP 71618 and HIP 54515. For CHARIS data, we achieve 5-$σ$ contrasts down to $\sim$1.4$\times$10$^{-5}$, $\sim$6$\times$10$^{-6}$, and 10$^{-6}$ to 4$\times$10$^{-7}$ at 0\farcs{}16, 0\farcs{}25, and 0\farcs{}5 to 1\arcsec{}. Companion mass limits rule out brown dwarfs at $ρ$ $\sim$ 0\farcs{}15--0\farcs{}25 and massive planets at wider separations around all targets. More critically, for three of the four references our analysis disfavors companions with $V$ band contrasts brighter than 10$^{-8}$, 10$^{-9}$, and $10^{-10}$ at 0\farcs{}15, 0\farcs{}3, and 1$\arcsec{}$. Unless these targets have faint substellar companions within $ρ$ $\sim$ 0\farcs{}15, they likely lack background stars or companions that could corrupt the Roman Coronagraph's dark hole digging to preclude detecting reflected-light planets. For $α$ Cep, our limits are a factor of $\sim$10 worse but still meet the TTR5 limit of 10$^{-7}$ beyond $ρ$ $\sim$ 0\farcs{}25: beyond 0\farcs{}4, they exclude a Jupiter-twin reflected-light companion (10$^{-9}$). Archival Keck/NIRC2 data likewise find no substellar companions with $Δ$V $>$ 10$^{-8}$ at wider separations. Finally, we assess the observability of HIP 71618 and HIP 54515 -- updated for Roman's launch date of August 30, 2026. Adding $γ$ Boo -- not currently in the Roman CPP team reference-star list -- would improve schedulability for the tech demo's key targets.

### [B] 65.4 — Causes of Hot Jupiter Inflation from Causal Discovery
- **arXiv:** [2608.16988](https://arxiv.org/abs/2608.16988)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** ism_methods_data (65.4), feedback_bubbles (62.7), star_formation (59.6)
- **Current keyword baseline:** NO
- **BM25 max:** 34.1
- **Semantic max:** 81.7
- **Abstract:** Hot Jupiters often have radii larger than predicted by standard cooling--contraction models, but it remains unclear which process supplies or preserves the extra internal heat. We analyze 328 short-period giant planets with measured $M_p$, $R_p$, $P_{\rm orb}$, and host-star $T_{\rm eff}$ using causal discovery, a statistical framework that asks which observed properties remain directly connected to planet radius after the others are accounted for. As a check, the same pipeline recovers the expected mass--radius connection for a super-Earth control sample. For hot Jupiters, the preferred graph links $R_p$ directly to $P_{\rm orb}$ and $T_{\rm eff}$, but not to $M_p$. Since incident flux increases with $T_{\rm eff}$ and decreases with $P_{\rm orb}$ at fixed stellar properties, this paired dependence is naturally interpreted as a population-level signature of irradiation-regulated inflation. Comparing the graph with analytic radius-excess scalings suggests a comparatively important role for Gold--Soter thermal tides, with kinetic/mechanical heating and ohmic dissipation potentially contributing alongside them. Purely period-controlled gravitational tides are disfavored as the sole explanation because they lack a leading dependence on stellar temperature. Distinguishing thermal tides, kinetic/mechanical heating, ohmic dissipation, and mixed scenarios will require radius-excess measurements that control for incident flux, age, composition, stellar properties, and selection effects. More broadly, this work shows how causal discovery can turn population-level exoplanet data into physically interpretable tests of hot-Jupiter inflation. Causal discovery complements parametric Bayesian population models by testing which observables retain direct conditional dependence on $R_p$ without imposing a specific radius relation, although the modest sample size limits the scope of the inferred graph.

### [B] 65.4 — Evidence for Dynamical Filtering: High Binary Fraction, Hard-binary Excess, and Unresolved Triples in the Surviving Core of NGC 6791
- **arXiv:** [2608.13955](https://arxiv.org/abs/2608.13955)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** star_formation (65.4), astrochemistry (61.4), feedback_bubbles (60.3)
- **Current keyword baseline:** YES
- **BM25 max:** 37.9
- **Semantic max:** 81.7
- **Abstract:** We present a deep photometric analysis of the main-sequence (MS) population in the old, metal-rich open cluster (OC) NGC 6791 using Gaia Data Release 3 data. After correcting for differential reddening, we use the Bayesian model comparison to test whether stellar rotation can account for the observed MS broadening and find that a rotation-dominated interpretation is strongly disfavored. We therefore infer that unresolved multiplicity is the primary contributor to the photometric offsets. We derive a high-q companion fraction of $54.3\% \pm 2.8\%$ for systems with $q \gtrsim 0.5$, significantly higher than typical values reported for most OCs and the field. The inferred offset distribution is not consistent with a flat mass-ratio distribution but instead shows an excess toward high mass ratios ($q \sim 0.8$--$1.0$), suggestive of preferential survival of hard binaries in a dynamically evolved environment. We also identify a population of stars lying above the equal-mass binary limit ($ΔG > 0.75$ mag), which is difficult to explain with ordinary MS binaries alone and is plausibly interpreted as candidate unresolved triple or higher-order multiple systems. A Kolmogorov--Smirnov test, together with Monte Carlo label-shuffling experiments, shows no statistically significant difference between the projected radial distributions of the single-star and binary/multiple populations within the observed field. Taken together, these results are consistent with the picture that NGC 6791 is the dynamically processed inner remnant of a once more massive cluster.

### [B] 65.3 — The FLARE Facility
- **arXiv:** [2608.17332](https://arxiv.org/abs/2608.17332)
- **Primary category:** physics.plasm-ph
- **Categories:** physics.plasm-ph, astro-ph.HE, astro-ph.IM, astro-ph.SR, physics.space-ph
- **Top topics:** molecular_clouds (65.3), magnetic_fields (64.2), astrochemistry (57.9)
- **Current keyword baseline:** NO
- **BM25 max:** 68.7
- **Semantic max:** 81.6
- **Abstract:** The Facility for Laboratory Reconnection Experiments (FLARE) has been constructed to study magnetic reconnection in multiple X-line regimes relevant to space, astrophysical, and fusion plasmas. Building upon the successful design of the Magnetic Reconnection Experiment (MRX), FLARE features a larger physical volume, stronger magnetic fields, and an independent ohmic heating drive to significantly extend the accessible parameter space, targeting Lundquist numbers up to S ~ 10^5 and normalized system sizes up to λ~ 10^3. This paper details the facility's core engineering components, including the primary vacuum vessel, internal flux cores, highly segmented external coil systems, modular capacitor banks, and the safety interlock and control architecture. An initial diagnostic suite is presented, comprising high-resolution 2D magnetic probe arrays, triple Langmuir probes, a fully fiber-coupled interferometer, ion Doppler spectroscopy, and fast camera imaging. Initial operations demonstrate the device's experimental flexibility and reliability, successfully executing symmetric push-pull reconnection, spheromak merging, and asymmetric downstream configurations. Currently operating within "Stage 2.5" with S ~ 2,500 and λ~ 60 for anti-parallel reconnection, FLARE provides immediate access to the multiple X-line regimes. Planned hardware upgrades, advanced diagnostic additions, and integration with fully kinetic simulations will further expand its capabilities as it transitions into a collaborative user facility for the broader plasma science community.

### [B] 65.2 — Modelling mountains on accreting magnetized neutron stars
- **arXiv:** [2608.17508](https://arxiv.org/abs/2608.17508)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, gr-qc
- **Top topics:** magnetic_fields (65.2), star_formation (49.7), ism_methods_data (46.7)
- **Current keyword baseline:** NO
- **BM25 max:** 71.3
- **Semantic max:** 69.4
- **Abstract:** Continuous gravitational waves from accreting neutron stars in Low Mass X-ray Binaries are one of the main targets for current and next generation ground based detectors. In order to select the most promising astrophysical sources, however, reliable predictions for the signals are required, and it is therefore necessary to develop models that consistently account for the combined effects of magnetic stresses, accretion-induced heating, and the elastic response of the crust.}{We present a model for computing the quadrupolar deformation, incorporating for the first time the coupled effects of a poloidal magnetic field, deep crustal heating, and crustal elasticity. Perturbations to the star's structure driven by the Lorentz force density and by thermally-induced density variations are computed by solving a system of linearised deformation equations in the crust, for which we consider the full elastic response, while the ocean and core treated as barotropic fluids. We identify a threshold accretion rate whose value depends on crustal microphysics and the superfluid gaps in the core, above which magnetic stresses and asymmetric accretion drive deformations of opposite sign, while below this threshold their roles are reversed. The predicted eccentricities reach magnitudes up to $\varepsilon\sim 10^{-11}$, corresponding to characteristic gravitational-wave strains accessible to next-generation detectors such as the Einstein Telescope or Cosmic Explorer, but generally below the sensitivity of current LIGO, Virgo and KAGRA interferometers. These results are consistent with the non-detection of continuous gravitational waves from accreting neutron stars in Low Mass X-ray Binaries in recent observational campaigns, but highlight the need of reliable models to understand the impact of gravitational wave emission in these systems and select relevant targets for future searches.

### [B] 65.1 — A Social Network Analysis of JWST General Observer Programs: The Emergence of a Decentralized Heterarchy
- **arXiv:** [2608.15883](https://arxiv.org/abs/2608.15883)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (65.1), massive_star_formation (63.0), feedback_bubbles (57.4)
- **Current keyword baseline:** NO
- **BM25 max:** 38.0
- **Semantic max:** 81.3
- **Abstract:** Developing proposals to execute programs on space telescopes involves networks of astronomers coalescing around ideas and plans for observations. When aggregated, these program level networks allow a collective structure of the overall social network of astronomers using a telescope to be created and analysed. We do this using program level investigator data over the first five cycles of accepted General Observer (GO) programs on the James Webb Space Telescope (JWST). The aggregate network contains 5252 unique astronomers with 144740 connections between them based on their program level participation. We apply a modularity class coefficient to visualize the sub communities that evolved within the aggregate network. Ten dominant sub communities emerge that are shown to correlate at various levels with the JWST scientific categories as defined by the Space Telescope Science Institute (STScI). These sub communities vary in size as well as diversity of countries and institutions represented. Analysis of the research interests of investigators within sub communities reveals that separation along the long axis of the graph is associated with the scale of science performed at community level (AU scale vs kpc Gpc scale). While the social network structures based on institutional affiliation and country of institution are highly centralized, the aggregate network at the investigator level is highly heterarchical and decentralized. It appears to be supportive of cross disciplinary interaction, and institutionalized integration between planetary system and cosmic structure science that is wide and redundant, rather than mediated by a small set of critical brokers. Results have implications for access policy (time allocation processes on telescopes leaving behind a legacy of heterarchical social networks) and access strategy (astronomer need to access networks before accessing telescopes).

### [B] 65.1 — An ALMA view of the Jet-Arc CO clouds toward the TeV $γ$-ray source HESS J1023-575 and Westerlund 2; Evidence for the footprints of microquasar jets, the very powerful cosmic-ray accelerator in the Galactic disk
- **arXiv:** [2608.14988](https://arxiv.org/abs/2608.14988)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** molecular_clouds (65.1), galactic_ism_surveys (50.1), astrochemistry (45.2)
- **Current keyword baseline:** NO
- **BM25 max:** 56.6
- **Semantic max:** 74.3
- **Abstract:** The TeV $γ$-ray source HESS J1023-575 (HESSJ 1023 hereafter) is one of the brightest H.E.S.S. sources near the young massive cluster Westerlund 2. HESS J1023 shows a remarkable positional alignment with the Jet and Arc CO clouds on its eastern and western sides over 170 pc length. We have carried out sub-pc scale observations of the CO clouds with ALMA and have discovered that the clouds consist of numerous thin filamentary features of $\sim$0.5 pc width and 10--20 pc length at distance of 7.5 kpc, which are well aligned with the Jet-Arc axis. Based on the magneto-hydrodynamical model of microquasar jets launched from {the center of the $γ$-ray source} HESS J1023-575, we present an interpretation that the thin filamentary clouds are the footprints of the microquasar jets on the HI gas. The model also explains the dissimilar Jet vs. Arc clouds in terms of HI density difference on each side. By using the density of the CO and HI gas and the $γ$-ray luminosity, we have calculated the cosmic ray proton energy $W_{\rm p}$ to be 7$\times$10$^{48}$ erg under the hadronic scheme, which is ten times larger than those derived in the TeV $γ$-ray SNRs RX J1713.7-3946 and RX J0852.0-4622. It is likely that HESS~J1023 has been active over 1-10 Myr, which is significantly longer than the duration of cosmic ray acceleration of the SNRs. HESS~J1023 is therefore an outstanding source of cosmic rays equivalent to at least 1000 SNRs, and is possibly the most powerful CR accelerator in the Galactic disk. A high energy compact source in HESS~J1023, which is likely a Myr-old black hole or neutron star, remains veiled due to heavy extinction.

### [B] 65.0 — Astrobiology and the Transformation of Scientific Epistemology
- **arXiv:** [2608.17728](https://arxiv.org/abs/2608.17728)
- **Primary category:** physics.hist-ph
- **Categories:** physics.hist-ph, astro-ph.EP
- **Top topics:** ism_methods_data (65.0), star_formation (62.1), astrochemistry (57.2)
- **Current keyword baseline:** NO
- **BM25 max:** 35.9
- **Semantic max:** 81.3
- **Abstract:** Astrobiology occupies an unusual position within the philosophy of science. Confronted with the n = 1 problem - having only a single example of life to study - it attempts to investigate life beyond Earth while relying entirely on Earth's biosphere as its reference point, a constraint that creates unique epistemic challenges. Unlike traditional sciences with clear predictive frameworks, astrobiology operates as what we might call a transient science: a discipline functioning without foundational certainties, relying predominantly on abductive reasoning, and confronting hypotheses that may remain untestable for decades. It is, in essence, a science of absence - of evidence, certainty, and analogy - where progress lies in refining conceptual and experimental tools to recognize unfamiliar forms of life. This positions astrobiology alongside emerging fields like artificial intelligence and cognitive science within a broader transformation of how scientific knowledge is constructed when dealing with phenomena that transcend direct empirical access.

### [B] 64.9 — Modelling s-process chemical clocks: insights from high-precision Kepler data
- **arXiv:** [2608.17480](https://arxiv.org/abs/2608.17480)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** astrochemistry (64.9), feedback_bubbles (47.3), star_formation (44.0)
- **Current keyword baseline:** NO
- **BM25 max:** 58.9
- **Semantic max:** 74.1
- **Abstract:** We present Galactic chemical evolution (GCE) models for the chemical clocks [Zr/Ti] and [Ce/Ti], tracing first- and second-peak s-process nucleosynthesis, and compare them with a high-precision sample of 68 Kepler red giant stars with asteroseismic ages from individual-mode frequencies and high-resolution spectroscopy. Using a multi-zone GCE framework, we explore variations in metallicity-dependent asymptotic giant branch (AGB) nucleosynthetic yields, including proposed enhancements to high-metallicity Ce production. Our baseline model reproduces [Zr/Ti] and the high-$α$ sequence in both age and metallicity space, but systematically underestimates [Ce/Ti] at young ages and intermediate metallicities, indicating a persistent deficit in second-peak s-process enrichment over the last $\sim6$ Gyr of Galactic disc evolution. Increasing second-peak yields from high-metallicity AGB stars only partially reduces this discrepancy, suggesting that simple yield rescaling is insufficient and more fundamental revisions to s-process nucleosynthesis at high metallicity, alongside a self-consistent treatment of stellar dynamics, may be required. In fact, models reproduce abundance trends more tightly in metallicity than in age space, with additional age scatter partly attributed to radial migration. This Letter highlights the diagnostic power of precise asteroseismic ages for GCE studies and the limitations of current models in capturing the complex interplay between s-process nucleosynthesis and stellar dynamics.

### [B] 64.9 — The Roman Coronagraph Community Participation Program: Observation planning and data reduction for polarimetric mode
- **arXiv:** [2608.17133](https://arxiv.org/abs/2608.17133)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** molecular_clouds (64.9), ism_methods_data (60.6), astrochemistry (57.4)
- **Current keyword baseline:** NO
- **BM25 max:** 33.7
- **Semantic max:** 81.2
- **Abstract:** Reflected-light polarimetry of exoplanets constrains and resolves degeneracies in atmospheric properties, while polarized light observations of debris disks enable the characterization of dust-grain properties. The best-effort polarimetric mode of the Roman Coronagraph Instrument will be able to perform multi-wavelength observations of planetary systems using both the Hybrid Lyot Coronagraph (HLC) and the Shaped Pupil Coronagraph (SPC). This paper presents an overview of observation planning, simulations, and data reduction procedures for the polarimetric mode of the Roman Coronagraph. As an initial test of simulation and data reduction, a dataset of polarimetric observing sequences for the debris disk HD 172555 in HLC mode was generated using corgisim with estimated observation parameters, and data reduction was performed using corgidrp, incorporating all relevant noise factors and calibration products. Currently, mock calibration products are used in corgidrp; these will be replaced with simulated calibration products in future updates

### [B] 64.8 — The Kick Velocities of Neutron Stars in Binary Systems
- **arXiv:** [2608.19690](https://arxiv.org/abs/2608.19690)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA, astro-ph.HE
- **Top topics:** star_formation (64.8), astrochemistry (55.6), massive_star_formation (51.3)
- **Current keyword baseline:** NO
- **BM25 max:** 69.8
- **Semantic max:** 81.0
- **Abstract:** Neutron stars (NSs) receive natal kicks on their formation in supernovae (SNe). We consider constraints placed on the natal kick magnitudes by NSs in different kinds of binary systems. We compare observed systems to predictions from the COMPAS rapid population synthesis code, where we apply kick models with varied natal kick prescriptions. Specifically, we compare binary orbits (i.e., periods and eccentricities) and systemic kick estimates of (1) Gaia observations of NS-harboring binaries (Gaia NSs), (2) NS low-mass X-ray binaries (LMXBs), (3) NS-white dwarf binaries (NSWDs), (4) NS high-mass X-ray binaries (HMXBs) and in particular Be X-ray binaries (BeXBs), and (5) double NSs (DNSs). In this comparison, we find that we can reproduce most of the observed properties of the Gaia NSs, LMXBs, and NSWDs with natal kicks calibrated to the velocities of young isolated pulsars, although we need "rocket" kicks to explain the Gaia NS eccentricities. The HMXBs and DNSs, in contrast, show evidence of significantly reduced NS natal kicks. In particular, we find that an apparent correlation between eccentricity and systemic kick for DNSs can be explained by Blaauw kicks, if the natal kicks are ${\lesssim}\,10\,$km$\,$s$^{-1}$. Although our model does not align well with low-metallicity Gaia NSs, high-eccentricity BeXBs, and DNS mass estimates, we provide alternative hypothetical explanations for these systems. We conclude that a model in which NSs that are formed in binaries with high-mass companions receive significantly reduced natal kicks can provide a relatively consistent explanation for the observed NSs in binary systems.

### [B] 64.8 — Shaping SHAPE - A spectro-polarimeter onboard Chandrayaan-3 to observe Earth as an Exoplanet
- **arXiv:** [2608.19371](https://arxiv.org/abs/2608.19371)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** ism_methods_data (64.8), magnetic_fields (62.3), star_formation (61.2)
- **Current keyword baseline:** NO
- **BM25 max:** 41.5
- **Semantic max:** 81.1
- **Abstract:** Spectro-polarimetry of HAbitable Planet Earth (SHAPE) is an experimental instrument onboard the Propulsion Module (Orbiter) of the Chandrayaan-3 mission, designed to perform disc-integrated spectro-polarimetric observations of Earth from lunar and highly elliptical Earth orbits. SHAPE is a compact, lightweight spectro-polarimeter comprising three subsystems: the Electro-Optical Detector System (EODS)-Optics, EODS-Electronics, and Radio Frequency Source (RFS). An Acousto-Optic Tunable Filter (AOTF), driven by an in-house-developed 80$-$135 MHz RF source, provides spectral filtering in the near-infrared (NIR) wavelength range of 1.0$-$1.7 $μ$m and produces two narrow-band beams with mutually perpendicular linear polarization states. The instrument optics, with a field of view of approximately 2.6°, focus the two beams onto InGaAs detectors. A spectral resolution of 2$-$4 nm is achieved using in-house-designed low-noise front-end electronics. The instrument also incorporates processing and power electronics for signal processing, detector biasing, and subsystem control. We present the overall instrument design, results from pre-launch ground-based testing, and in-orbit operational performance. The current configuration enables SHAPE to measure disc-integrated signatures of Earth over a range of phase angles, providing a test bed for characterizing Earth-like exoplanets and benchmarking future exoplanet observations.

### [B] 64.8 — FLAGS II: Constraining Galaxy Formation Models with Dimensionality Reduction of Direct Observables
- **arXiv:** [2608.12471](https://arxiv.org/abs/2608.12471)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (64.8), ism_methods_data (63.6), astrochemistry (59.1)
- **Current keyword baseline:** NO
- **BM25 max:** 33.1
- **Semantic max:** 81.0
- **Abstract:** Comparisons between observations of galaxies and theoretical predictions are regularly performed using physical properties, which are inferred by the often slow and biased process of SED fitting. Forward modelling facilitates a reliable alternative, whereby models are evaluated using direct observables alone. However, these datasets become high-dimensional when collating observations from multiple telescopes, leading to sparse sampling, memory intensity and visualisation difficulties. We show that 2D embeddings of JWST and HST photometric fluxes, constructed using the non-linear dimensionality reduction algorithm UMAP, preserve sufficient information to differentiate between five models. Using a simple $χ^{2}$-like metric, we show that JAGUAR reproduces the population of bright galaxies $(m_{\mathrm{AB}}<26)$ in GOODS-S six times as well as SC-SAM and twelve times as well as SAGE. By adjusting the hyperparameters, we quantify how well each model replicates the distribution of SED shapes. The template SED approach of SPRITZ and the lack of photoionisation in SAGE cause significant discrepancies, highlighting the importance of comprehensive forward modelling. The embedded position of each galaxy can be identified $>100$ times faster than inferring its properties with Bayesian SED fitting, making this approach an ideal alternative for deriving statistical model constraints from large surveys such as LSST and Euclid, and performing simulation-based inference with CAMELS.

### [B] 64.4 — Cluster finding with outskirt stellar masses and percolation
- **arXiv:** [2608.19768](https://arxiv.org/abs/2608.19768)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, astro-ph.GA
- **Top topics:** massive_star_formation (64.4), star_formation (62.9), galactic_ism_surveys (57.5)
- **Current keyword baseline:** NO
- **BM25 max:** 41.5
- **Semantic max:** 80.5
- **Abstract:** The abundance of galaxy clusters is a powerful cosmological probe, but optical cluster cosmology is limited by selection systematics, in particular the projection effects that affect cluster finders based on galaxy populations such as the red sequence. The outer stellar mass ($M_\mathrm{out}$) of cluster central galaxies -- e.g., the stellar mass in a 50-100 kpc annulus -- offers an alternative selection that relies only on the central galaxy and is therefore largely free from projection effects. Its primary systematic is instead satellite contamination, since massive clusters can host more than one galaxy with high outer stellar mass. Using the IllustrisTNG300 simulation at $z=0.4$, we quantify this contamination and investigate a simple, proximity-based percolation method to mitigate it, in which galaxies with lower outer stellar mass lying within a given radius of a more massive galaxy are removed from the sample. We find that the satellite fraction defined by the friends-of-friends (FoF) algorithm is modest even without percolation ($\leq 15\%$ for $M_\mathrm{out} > 10^{10}\,\mathrm{M}_\odot$ and $<10\%$ for $M_\mathrm{out} > 10^{11}\,\mathrm{M}_\odot$), and that percolation reduces it further, with the improvement increasing for percolation radii up to $3.0\,R_{200c}$. For a moderately high outer stellar mass cut ($\sim 4\times10^{10}\,\mathrm{M}_\odot$) and percolation radius ($\sim 2.0\,R_{200c}$), we recover a cluster sample that is both highly complete and pure for halo masses $\gtrsim 10^{14}\,\mathrm{M}_\odot$. These results indicate that outer stellar mass, combined with simple percolation, has the potential to provide a clean and readily calibratable selection of massive galaxy clusters.

### [B] 64.4 — Time-dependent Evolution of Proton Spectra in Supernova Remnants and Their Contribution to Galactic Cosmic Rays
- **arXiv:** [2608.18481](https://arxiv.org/abs/2608.18481)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (64.4), astrochemistry (52.1), turbulence (50.7)
- **Current keyword baseline:** NO
- **BM25 max:** 44.1
- **Semantic max:** 73.4
- **Abstract:** Recent $γ$-ray observations indicate that the proton spectra of supernova remnants (SNRs) are well described by broken power laws, with both the spectral break energy, $E_{\mathrm{br}}$, and the low-energy spectral index, $α$, exhibiting systematic evolution with SNR age. The physical origin of these evolutionary trends and their implications for the Galactic cosmic-ray (CR) population remain poorly understood. In this work, we develop the temporal evolution model for protons in SNRs by extending the semi-analytical framework of Zhang \& Fang, in which both the maximum acceleration energy and the injection spectral index evolve with the dynamical evolution of the remnant. The calculated proton spectra reproduce the age-dependent trends of both $E_{\mathrm{br}}$ and $α$ inferred from observations. We adopt the proton spectrum at the onset of the radiative phase as the source spectrum for Galactic CR propagation and incorporate the intrinsic dispersion of source spectral indices among SNRs. The resulting cumulative Galactic proton spectrum is then calculated within a diffusion model. The propagated spectrum agrees well with the observed CR proton flux over a broad energy range, particularly above several tens of GeV. Our results provide a self-consistent framework linking the time-dependent evolution of proton acceleration in individual SNRs to the Galactic CR proton spectrum observed at Earth, and further support the long-standing hypothesis that SNRs are the dominant sources of Galactic CR protons below the knee.

### [B] 64.4 — Investigating The Effects of Early Dark Energy on Large-scale Structure Within the EDENS Suite
- **arXiv:** [2608.17212](https://arxiv.org/abs/2608.17212)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (64.4), astrochemistry (63.1), turbulence (62.4)
- **Current keyword baseline:** NO
- **BM25 max:** 41.3
- **Semantic max:** 80.5
- **Abstract:** Early Dark Energy (EDE) models have been suggested as a possible solution to the so-called Hubble Tension, a discrepancy of the measurement of the Hubble constant at early and late times. In this paper, we investigate the effects of EDE on large-scale structure probes of cosmology via the EDENS (Early Dark Energy N-body Simulations) suite. The EDENS suite extends the reach of available EDE simulations considerably by adding volume and resolution. We derive several key metrics, such as the halo mass function, the nonlinear power spectrum, and the concentration-mass relation. Furthermore, we implement a halo occupation distribution model to populate the simulations with synthetic galaxies. This allows us to measure the galaxy-galaxy correlation function and galaxy bias. We choose an EDE model that is consistent with observations across several probes and allows for the increase of the present day value of the Hubble constant to resolve the Hubble tension. This model adds three more parameters to the standard $Λ$CDM model. Additionally, it requires small shifts in the best-fit $Λ$CDM cosmological parameters to accommodate existing observational constraints. We find significant differences between the standard $Λ$CDM model and the EDE model, suggesting that some of our chosen metrics may allow us to distinguish EDE from $Λ$CDM, and future observations should help further constrain possible cosmological models. We release outputs from our simulations via the OpenCosmo data portal.

### [B] 64.3 — Re-evaluating the resolved mass-metallicity relation with a self-consistent metallicity calibration
- **arXiv:** [2608.20239](https://arxiv.org/abs/2608.20239)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (64.3), galactic_ism_surveys (55.9), feedback_bubbles (53.7)
- **Current keyword baseline:** NO
- **BM25 max:** 40.2
- **Semantic max:** 73.2
- **Abstract:** Aims. The mass-metallicity relation (MZR) is essential for understanding the chemical evolution of galaxies. Whether the star formation rate (SFR) plays a role in setting the metallicity has long been debated. Using various metallicity calibrations can result in different conclusions for this fundamental yet unresolved issue. Methods. We apply a self-consistent metallicity calibration based on photoionization models to re-evaluate the resolved and integrated MZR. We utilize the integral field unit data from SDSS-IV/MaNGA, with $\sim 3.5\times10^6$ spaxels and $\sim$ 4550 galaxies. We compare our preferred metallicity calibration with several strong-line calibrations in the literature and direct method metallicity. We analyze the metallicity residual of MZR to evaluate the effects of SFR and apply the partial correlation coefficient to quantify the effects. Results. The metallicity calibration we used shows the best consistency with the direct method. We provide 3 equations for resolved MZR, and verify that local SFR does not show significant correlation with metallicity. Considering the integrated properties, (s)SFR do not present correlation with the metallicity residuals. The results suggest that an equilibrium of inflow and outflow is favored, and the mass-metallicity relation does not have a secondary dependence on SFR.

### [B] 64.3 — The progenitors of $z\gtrsim10$ JWST galaxies in the COLIBRE simulations
- **arXiv:** [2608.19007](https://arxiv.org/abs/2608.19007)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** massive_star_formation (64.3), star_formation (63.4), atomic_ism (59.4)
- **Current keyword baseline:** NO
- **BM25 max:** 57.1
- **Semantic max:** 80.3
- **Abstract:** JWST has revealed a large population of luminous galaxies ($M_{\rm UV}\lesssim -20$) at redshifts $z \gtrsim 10$, widely interpreted as posing a challenge to models of galaxy formation within the $Λ$CDM cosmology. Here, we search for counterparts of the JWST galaxies in the COLIBRE simulations of galaxy formation. Although these simulations have not been tuned to reproduce any $z > 0$ observations, we find a population of COLIBRE galaxies with properties similar to those of the JWST galaxies, and trace them to their earliest evolutionary phases, $z\simeq25$, to investigate the onset of galaxy formation. We study the evolution of galaxy stellar masses, sizes, star formation rates, UV magnitudes, metallicities, central black hole masses, and molecular gas and dust content, finding good agreement with observationally inferred properties at $z > 10$, except for UV magnitudes and dust masses, which COLIBRE underpredicts and overpredicts, respectively. Our results indicate that the standard galaxy formation physics and $Λ$CDM cosmology adopted in COLIBRE are sufficient to reproduce a broad range of properties of the most extreme $z > 10$ JWST galaxies - including their compact sizes, stellar masses, gas content, and metallicities. We show that the discrepancies with the UV magnitudes and dust masses can both be attributed to the uncertain rate of grain growth at high redshift, possibly alongside a top-heavy stellar initial mass function. These findings provide strong evidence that the standard cosmological model can naturally explain even the most extreme galaxies in the early Universe.

### [B] 64.1 — Non-ideal MHD and protostellar feedback effects on disc formation and evolution in numerical simulations of star cluster formation
- **arXiv:** [2608.19518](https://arxiv.org/abs/2608.19518)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA
- **Top topics:** molecular_clouds (64.1), star_formation (60.3), astrochemistry (59.5)
- **Current keyword baseline:** NO
- **BM25 max:** 100.0
- **Semantic max:** 73.0
- **Abstract:** While recent surveys have resolved hundreds of nearby protostellar discs, numerical simulations assuming ideal magnetohydrodynamics (MHD) have historically struggled to achieve disc formation due to efficient angular momentum removal by magnetic torques. Non-ideal MHD effects, relevant at the low ionization fractions typical of molecular clouds, have been shown to reduce the effectiveness of magnetic braking and promote disc formation. In this work, we present the results from a suite of calculations following the gravitational collapse of 50 $M_{\odot}$ turbulent molecular cloud cores down to the formation and evolution of stellar systems and protostellar discs. We use the radiation-MHD code GIZMO including non-ideal MHD (Ohmic resistivity, ambipolar diffusion, and the Hall effect) and the STARFORGE numerical framework for modeling star formation and stellar feedback. We compare the effects of assuming ideal vs. non-ideal MHD and including sub-grid protostellar jet feedback on disc formation and evolution. Discs form in all of our models but are least massive in the model with ideal MHD and sub-grid jet feedback. Apart from the ideal MHD$+$jets model, we do not observe any significant differences in disc properties between the ideal and non-ideal MHD models; however, ideal MHD discs are embedded in smaller rotating envelopes. Disc sizes are in general agreement with those of observed discs. Jet feedback increases core fragmentation and reduces final stellar masses. Our results suggest that magnetic braking does not efficiently suppress disc formation, regardless of whether ideal or non-ideal MHD is assumed, under the dynamical conditions in which multiple stellar systems form.

### [B] 64.0 — Catalytic formation of H_2 on carbonaceous dust grains - implications for interstellar observations
- **arXiv:** [2608.16149](https://arxiv.org/abs/2608.16149)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** molecular_clouds (64.0), galactic_ism_surveys (62.0), astrochemistry (61.6)
- **Current keyword baseline:** YES
- **BM25 max:** 91.1
- **Semantic max:** 80.0
- **Abstract:** We use kinetic Monte Carlo (KMC) simulations to study molecular hydrogen formation on carbonaceous dust grain surfaces, validated against recent laboratory measurements of H$_2$ formation on coronene films at temperatures from 10 to 250 K. The model uses a three-dimensional amorphous carbon lattice with heterogeneous physisorption ($45 \pm 5$ meV) and chemisorption ($1.75 \pm 0.25$ eV) sites, and tracks both Langmuir--Hinshelwood (LH) and Eley--Rideal (ER) formation channels within a stochastic Gillespie event-driven framework. The model reproduces the measured efficiency curve within the experimental uncertainties, including the isothermal (constant surface temperature) measurements at 100 - 250 K. The simulations correctly describe the phase boundary between the LH and ER driven processes as functions of grain temperature and the observed crossover. Under interstellar medium conditions, 10 - 250 K and n = 10 - 10$^4$ cm$^3$, the model predicts three distinct regimes for the formation efficiency $ε$, the fraction of impinging H atoms released as H$_2$. At 10 K diffusion is slow and $ε\approx 0.06$. Between 20 K and 80 K, LH dominates and $ε\approx 0.28$. Above 150 K, an ER plateau at $ε= 0.19$ is sustained by chemisorption-trapped H atoms. The LH-to-ER crossover occurs between 100 and 120 K. At 100 K we observe a 16\% density-dependent stochastic enhancement, which rate-equation models cannot capture. At T$_{dust}$ = 60 K, n = 10$^3$ cm$^3$ we find the ratio of H$_2$ formation to free-fall time $t_{{\rm H}_2}/t_{\rm ff} \approx 0.93$, so dust-catalysed H$_2$ chemistry can keep pace with gravitational collapse in high-redshift star-forming environments.

### [B] 63.9 — Microlensify: a Transformer Based Machine Learning Classifier for Microlensing Events Trained on TESS Light Curves
- **arXiv:** [2608.19419](https://arxiv.org/abs/2608.19419)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP, astro-ph.GA, astro-ph.SR, cs.LG
- **Top topics:** ism_methods_data (63.9), star_formation (46.2), feedback_bubbles (45.8)
- **Current keyword baseline:** NO
- **BM25 max:** 49.8
- **Semantic max:** 72.8
- **Abstract:** Microlensing can reveal populations of faint compact objects that are otherwise difficult to detect. Depending on their design, all-sky surveys have the potential to search for these objects across the sky. The Transiting Exoplanet Survey Satellite (TESS), primarily designed to detect transiting exoplanets, also provides near all-sky coverage with high cadence. In this work, we use TESS data to search for microlensing candidates using both traditional and machine-learning methods and to identify associated false positives in high-cadence surveys. Microlensify is a physics-informed, transformer-based variational autoencoder trained on simulated single-lens microlensing light curves and real TESS Sector 12 data. The model classifies events, reconstructs light curves, and estimates microlensing event durations. Applied to $\sim 5.6$ million TESS light curves, it identified between $0.036\%$ and $1.89\%$ as microlensing candidates across different TESS pipelines. After applying microlensing detection metrics and cross-matching with SIMBAD, we obtained a final list of candidates and identified false positives including long-period variables, Mira variables, cataclysmic variables, red giants, and transients. We also found Gaussian-like peaks caused by asteroid crossings, a potential source of false positives in high-cadence microlensing surveys. The model also predicts event duration with an accuracy of $R^2 = 0.97$. The model was further tested on published events from different ground-based microlensing surveys, confirming 92.7% as microlensing, demonstrating its applicability across surveys with different cadences.

### [B] 63.8 — Enabling Quantitative Polarimetry for Keck/NIRC2: Preliminary Mueller Matrix Model Calibration
- **arXiv:** [2608.14873](https://arxiv.org/abs/2608.14873)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** magnetic_fields (63.8), ism_methods_data (61.5), molecular_clouds (56.3)
- **Current keyword baseline:** NO
- **BM25 max:** 45.8
- **Semantic max:** 76.9
- **Abstract:** The Keck/NIRC2 infrared imager was upgraded in 2025 with dual-beam polarimetric observing modes spanning approximately 1.1--4.1 microns (JHKL' bands). We present a preliminary JHK calibration of NIRC2 Polarimetry using a wavelength-dependent Mueller matrix model of the Keck tertiary mirror (M3), half-wave plate (HWP), image rotator (IMR), downstream optics, and Wollaston prism. We constrain the model downstream of M3 using dome flat sequences spanning ten HWP and nine IMR angles in each band. Although the model reproduces the dominant modulation, the residuals show structure dependent on HWP and IMR angle. Measurement matrix inversion of unpolarized standard star observations gives M3 diattenuations of 0.0119+/-0.0009, 0.0098+/-0.0004, and 0.0068+/-0.0005 in J, H, and Kp, substantially closer to Fresnel predictions for aluminum than the values derived from dome flats. The larger dome flat modulation may indicate polarization in the incident dome illumination or Mueller matrix model inaccuracies. These results establish an initial calibration framework while motivating improved input polarization constraints, fixed HWP parameters from previous laboratory measurements, model validation with polarized standard stars, and extension to L'.

### [B] 63.7 — Testing Statistical Isotropy in the FRB Sky Distribution: A Selection-Function-Aware Framework
- **arXiv:** [2608.20135](https://arxiv.org/abs/2608.20135)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (63.7), galactic_ism_surveys (54.1), astrochemistry (43.7)
- **Current keyword baseline:** NO
- **BM25 max:** 57.2
- **Semantic max:** 72.6
- **Abstract:** We perform a test of statistical isotropy in the Universe using the sky distribution of fast radio bursts (FRBs), based on a compilation of $4066$ events detected by multiple surveys. Our method is based on the two-point angular correlation function $w(θ)$ as in the Landy--Szalay estimator, together with a tomographic absolute-anisotropy statistic, and estimates their observational uncertainties from complementary jackknife and bootstrap resampling. Both estimators are confronted with hierarchical ensembles of isotropic mock catalogs that propagate the uncertainties of empirically reconstructed survey selection functions, as well as the Poisson fluctuations of the isotropic realizations. The significances are obtained from a covariance-aware, SVD-regularized $χ^2$ statistic calibrated empirically against the mock ensemble, and we evaluate four nested scenarios that progressively incorporate a Galactic-plane mask and the survey selection functions. As for our results, we find that the raw FRB sky is strongly inconsistent with isotropy; Galactic masking alone reduces the tension by only a factor of $\sim 3$, whereas the selection functions reduce it by nearly four orders of magnitude, showing that the apparent anisotropy is driven by the highly non-uniform sky coverage of the contributing surveys, overwhelmingly dominated by CHIME. Only when both effects are combined we obtain that the observed distribution is fully consistent with statistical isotropy. This result is independently corroborated by the absolute-anisotropy estimator, and is stable under variations of the analysis parameters. Therefore, we find that the FRB sky distribution is consistent with statistical isotropy, helping confirm one of the main predictions of the standard model scenario.

### [B] 63.5 — A binary black hole merger rate comparison within the same metallicity - star formation rate framework
- **arXiv:** [2608.13648](https://arxiv.org/abs/2608.13648)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.CO, astro-ph.GA
- **Top topics:** star_formation (63.5), astrochemistry (63.2), massive_star_formation (60.5)
- **Current keyword baseline:** NO
- **BM25 max:** 43.2
- **Semantic max:** 79.0
- **Abstract:** Recent studies have suggested that binary population synthesis models, when coupled with observationally based, metallicity-dependent star formation rate density, overpredict the observed local binary black hole (BBH) merger rate density. The significance of this tension might vary depending on the specific code and parameters adopted. Thus, a more extensive exploration of the parameter space is required. In this work, we perform such an extended analysis by considering BBH merger efficiencies coming from multiple population synthesis codes across a wide range of physical assumptions and parameter's choices. We adopt an observationally motivated metallicity distribution, exploring several variations to encompass observational uncertainties. We find that the tension persists: in almost all our metallicity variations, 14 out of 18, none of the models considered predicts a local BBH merger rate within or below the observed $90\%$ credible interval. Even in the four most favorable metallicity variations, only $\lesssim 10\%$ of the models are consistent with the observational constraints. We show that such a discrepancy originates from the low-metallicity tail contributed by low-mass galaxies and starbursts, as well as from the use of iron abundance rather than oxygen abundance in deriving the metallicity distribution. Even literature models that predict moderate BBH merger rates shift toward higher merger rates when combined with observationally motivated metallicity distributions. Although not comprehensive of all the literature models, our analysis suggests that models featuring stronger natal kicks and/or non-standard treatments of mass-transfer and common-envelope physics provide the most promising avenue for alleviating the tension with the observed local BBH merger rate.

### [B] 63.5 — Titanium Oxide Absorption as a Proxy to Detect Long term Variation and Activity Cycle in Proxima Centauri
- **arXiv:** [2608.12686](https://arxiv.org/abs/2608.12686)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** astrochemistry (63.5), magnetic_fields (62.5), star_formation (55.2)
- **Current keyword baseline:** NO
- **BM25 max:** 41.4
- **Semantic max:** 79.4
- **Abstract:** Stellar activity cycles on magnetically active stars can be estimated by molecular absorption bands. We have previously introduced a molecular index which compares absorptional line strength of the TiO567nm with its nearby continuum has previously been introduced. In this work we use this indicator to evaluation long-term activity variations for Proxima Centauri star, using spectroscopic data from HARPS. The results indicate periodicity with an activity period of 2873(+47.4-53.9) days, which is similar to the previous measurements from other indicators.

### [B] 63.4 — Mapping the Information Geometry of an Unresolved Dark Matter Population using a Differentiable Strong Lensing Simulator
- **arXiv:** [2608.18224](https://arxiv.org/abs/2608.18224)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, astro-ph.IM
- **Top topics:** turbulence (63.4), ism_methods_data (50.4), star_formation (40.6)
- **Current keyword baseline:** NO
- **BM25 max:** 31.6
- **Semantic max:** 72.2
- **Abstract:** Strong gravitational lensing is a unique probe of the matter power spectrum on small scales, where the abundance of dark matter subhalos in galaxies could be used to distinguish the predictions of the concordance cold dark matter model from alternatives such as warm dark matter. Extracting this signal poses major computational challenges, since perturbations of the lensing potential induced by substructure can be degenerate with both the macro-model of the lens and highly flexible models of the background source. Here, we introduce a framework to quantify these degeneracies using a differentiable strong-lensing simulator. Substructure is represented in a spectral basis confined to an annular domain surrounding the lensed image, allowing signals from a population of NFW subhalos to be encoded in a finite vector space. We then use the Fisher matrix to determine how much information about substructure is absorbed by nuisance components of the model. We find that macro-model degeneracies are largely confined to low-order perturbations of the lensing potential, while degeneracies with the source model can strongly suppress sensitivity across a broad range of scales as the expressivity of the source model is increased. Finally, we introduce the Fisher Graph Laplacian prior as a diagnostic tool to study how the internal degeneracies of the source model can be used to regulate the sensitivity of the data to an unresolved population of dark matter subhalos.

### [B] 63.4 — A Critical Eddington Ratio for X-Shaped Radio Galaxies
- **arXiv:** [2608.16976](https://arxiv.org/abs/2608.16976)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (63.4), galactic_ism_surveys (57.5), star_formation (54.6)
- **Current keyword baseline:** NO
- **BM25 max:** 59.2
- **Semantic max:** 72.2
- **Abstract:** We derive a quantitative condition for the formation of X-shaped radio galaxies by evaluating the competition between black hole spin evolution and the radiative fading of relic plasma within our previously proposed framework. The simultaneous visibility of two jet axes requires that the timescale for spin evolution across zero, t_trans, be shorter than the fading timescale of relic radio emission, t_fade. We estimate the transition timescale as t_trans about 5 million /lambda yr, where lambda is the Eddington ratio, and derive a visibility timescale t_fade about equal to 5-20 Myr based on the evolution of the synchrotron break frequency for typical lobe magnetic fields and redshifts. This leads to a critical Eddington ratio lambda_crit in the range 0.3-1, above which systems can exhibit X-shaped morphologies. We show that this threshold naturally produces an environmental dependence, as radiatively efficient accretion is more readily sustained in low-density environments, while feedback in rich clusters tends to drive systems toward radiatively inefficient states with a larger fraction of systems having lambda much less than lambda_crit, suppressing XRG formation. We further demonstrate that the observed low fraction of X-shaped radio galaxies (about 1-5%) arises from the limited overlap window combined with geometric and detectability effects. These results provide a quantitative and testable extension of our previous model, linking X-shaped morphology to accretion rate and environmental conditions through a simple timescale criterion.

### [B] 63.4 — Mixing stochasticity relinquishes evidence for magnetorotational hypernovae
- **arXiv:** [2608.14788](https://arxiv.org/abs/2608.14788)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.HE, astro-ph.SR
- **Top topics:** feedback_bubbles (63.4), star_formation (61.7), turbulence (57.2)
- **Current keyword baseline:** NO
- **BM25 max:** 50.9
- **Semantic max:** 72.1
- **Abstract:** A recent work claimed by fitting the observed elemental abundance pattern of a halo star with the total yields from single super-/hypernova events that only a magnetorotational hypernova event (a very energetic supernova event that also produces r-process elements) could be the source of the observed abundances. Here, we show that the star's peculiar abundance pattern is better fitted within the framework of mixing stochasticity with yields from a normal core collapse supernova (ccSN; Energy$_{\rm exp}$ $\sim 10^{51}$ erg.) and a neutron star merger (NSM). The stochastic mixing model outperforms the hypernova fitting significantly, (r.m.s 0.24 vs 0.44) i.e., favours the composition from common events (ccSN + NSM) over the magnetorotational hypernova scenario. We also discuss the origin of the star and the possibility of enrichment of its birth cloud by both a ccSN and a NSM.

### [B] 63.4 — Performance Analysis of the Asgard/NOTT Nulling Interferometer: Optimizing Observing Modes for High-contrast Detection
- **arXiv:** [2608.13737](https://arxiv.org/abs/2608.13737)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (63.4), astrochemistry (60.5), star_formation (56.1)
- **Current keyword baseline:** NO
- **BM25 max:** 42.5
- **Semantic max:** 75.7
- **Abstract:** We evaluate the performance of three beam-combination schemes, single-Bracewell, asymmetric dual-Bracewell, and symmetric dual-Bracewell, for the forthcoming Asgard/NOTT nulling interferometer at the Very Large Telescope Interferometer. Utilizing the SCIFYsim end-to-end simulator, we assess the instrument's performance by deriving the precision of calibrated null measurements as a function of stellar magnitude and simulating observations of varying hot exozodiacal dust (HEZD) distributions and a hot Jupiter. The study reveals distinct trade-offs for each observing mode. The single-Bracewell mode provides high throughput and preserves spatial information but suffers from poor error suppression. The asymmetric dual-Bracewell mode offers the strongest error suppression for detecting point-like sources, but it inherently suppresses symmetric astrophysical signals such as expected from HEZD. The symmetric dual-Bracewell mode provides a middle ground with modest error suppression while being sensitive to symmetric emission. We conclude that utilizing a combination of all three observing modes provides a robust strategy for detecting HEZD, constraining the structure of its distribution, and identifying false positives from stellar companions.

### [B] 63.4 — The Delay Time Distribution of Quasi-Periodic Eruptions
- **arXiv:** [2608.12261](https://arxiv.org/abs/2608.12261)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (63.4), feedback_bubbles (56.6), star_formation (55.4)
- **Current keyword baseline:** NO
- **BM25 max:** 38.8
- **Semantic max:** 79.3
- **Abstract:** Quasi-periodic eruptions (QPEs) are quasi-periodic X-ray bursts observed in the nucleus of a galaxy. Multiple pieces of observational evidence link QPEs to tidal disruption events (TDEs), which occur when stars are disrupted after approaching a supermassive black hole too closely. Post-starburst galaxies are overrepresented among the host galaxies of both TDEs and QPEs, though the mechanism causing this overrepresentation is unknown. While their physical origin is unclear, the delay time distribution (DTD) of QPEs, or rate of QPEs as a function of time since a burst of star formation, can constrain what mechanisms influence the QPE rate and possible QPE formation channels. We compile a catalog of 10 QPE host galaxies with optical spectra, model the stellar populations with Bagpipes, and retrieve the age of the most recent burst of star formation to construct the DTD of QPEs. We find that the QPE rate increases with post-burst age to reach a peak at ~1 Gyr relative to a control sample, similar to the observational TDE DTD, though we cannot rule out a flat distribution of burst ages relative to a control sample. However, the fraction of QPE host galaxies with high (>1%) burst mass fractions is larger than the fraction of galaxies with high burst mass fractions in either a sample of TDE host galaxies or a sample of control galaxies. If the preferred QPE formation channel requires extreme mass ratio inspirals (EMRIs), then such EMRIs may be more readily produced by large, ~1-Gyr-old bursts of star formation.

### [B] 63.3 — Physics of Circular Polarized Ion-Scale Waves in Hybrid Simulations of Alfvénic Fluctuations
- **arXiv:** [2608.14151](https://arxiv.org/abs/2608.14151)
- **Primary category:** physics.plasm-ph
- **Categories:** physics.plasm-ph, astro-ph.SR
- **Top topics:** turbulence (63.3), magnetic_fields (52.7), molecular_clouds (51.1)
- **Current keyword baseline:** NO
- **BM25 max:** 54.9
- **Semantic max:** 79.1
- **Abstract:** Ion cyclotron waves (ICW) and fast magnetosonic/whistler waves (FMW) are fundamental electromagnetic modes at ion kinetic scales, yet their generation mechanisms and roles in plasma evolution remain poorly understood. We analyze a 2.5D hybrid simulation of broadband Alfvénic fluctuations, where the proton velocity distribution is modeled as a sum of two bi-Maxwellian components: a thermal core and a drifting beam. Using wavelet-based wave identification, bi-Maxwellian VDF fitting, and the PLUME linear dispersion solver, we find that ICW behave as linear modes. Growth is intermittent, occurring when core temperature anisotropy builds up, and is driven mainly by the core (the beam contributes negligibly). Poynting flux analysis shows that ICW are predominantly forward-propagating, with a net energy flux ratio of $+1$ across all frequencies, consistent with the initial condition. FMW present a stark contrast: PLUME solutions often yield very small (near-zero) linear growth/damping rates. The species decomposition breaks down when $|γ/ω_r| \gtrsim 0.368$, indicating that linear theory predicts these waves to be strongly damped and not describable by linear eigenmodes. Nevertheless, FMW are clearly observed in the wavelet helicity spectrogram, indicating that they are generated by nonlinear processes (e.g., parametric decay or phase steepening) and persist despite linear damping. The net energy flux ratio for FMW is close to $+1$ at low frequencies but decreases at higher frequencies, yet never reaches zero (net energy flow remains forward). These results demonstrate that ICW are linear, core-driven waves that transfer energy to the plasma, while FMW are heavily damped, nonlinearly generated waves.

### [B] 63.2 — J0011+3443: a GPS compact symmetric object, gravitational lens, or dual AGN?
- **arXiv:** [2608.19928](https://arxiv.org/abs/2608.19928)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** molecular_clouds (63.2), ism_methods_data (57.6), star_formation (54.3)
- **Current keyword baseline:** NO
- **BM25 max:** 42.3
- **Semantic max:** 79.0
- **Abstract:** We present new multi-frequency VLBA observations of \object{J0011+3443} (TXS\,0008+344, $z=0.89$) at 2.3, 4.9, 8.5, and, for the first time, 23.6\,GHz. The source consists of two compact components A and B at a projected separation of $314\pm2$\,pc, plus a third feature C detected at 23.6\,GHz at $0.6$\,mas from A. Archival low-resolution radio measurements confirm an integrated gigahertz-peaked spectrum, with an observed-frame peak frequency of $ν_\mathrm{peak}=0.73\pm0.08$\,GHz and a peak flux density of $S_\mathrm{peak}=879\pm125$\,mJy. Comparison with nearly frequency-matched low-resolution measurements shows that the VLBA recovers $0.85\pm0.11$ of the 4.85\,GHz flux density and $0.50\pm0.06$ of the 8.46\,GHz flux density. The lower recovered fraction at 8.5\,GHz suggests that low-surface-brightness emission is resolved out or falls below the VLBA surface-brightness sensitivity. We therefore interpret the VLBA component spectra as spectra of the compact recovered emission only. The 23.6\,GHz morphology, the absence of a detected flat-spectrum core, the similar compact spectra of A and B, and the steep integrated GHz spectrum favor an interpretation of \object{J0011+3443} as a GPS-class compact symmetric object, possibly in a short-lived or relic phase, although a dual-AGN origin cannot be excluded without multi-epoch astrometry.

### [B] 63.2 — Redshift dependence and dipolar velocity corrections in cosmographic reconstructions through Type Ia supernova samples
- **arXiv:** [2608.15858](https://arxiv.org/abs/2608.15858)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc
- **Top topics:** galactic_ism_surveys (63.2), astrochemistry (61.8), feedback_bubbles (59.6)
- **Current keyword baseline:** NO
- **BM25 max:** 39.1
- **Semantic max:** 79.0
- **Abstract:** We perform a cosmographic analysis of Type Ia supernovae using the Pantheon+\&SH0ES, DES-SNY5 and Union3 compilations. We consider different redshift intervals, analyzed through a third-order Taylor expansion and a Padé $(1,2)$ approximation of the luminosity distance. First, we first infer the cosmographic parameters directly from the observed supernova redshifts. Afterwards, we extend the analysis by including a dipole correction associated with the local peculiar velocity field, constraining both its amplitude and direction. For Pantheon+\&SH0ES, the Cepheid calibration allows a direct determination of the Hubble constant, whereas for DES-SNY5 and Union3 we fix $H_0$ to set the absolute distance scale. By progressively increasing the maximum redshift of the sample, we study how the inferred cosmographic parameters depend on the adopted redshift interval. We find that the Hubble constant obtained from Pantheon+\&SH0ES remains consistent with previous determinations for both cosmographic parameterizations. Instead, the agreement of the deceleration $q_0$ and jerk $j_0$ parameters with the $Λ$CDM values depends on the adopted compilation and improves mainly for Pantheon+\&SH0ES as the redshift interval is enlarged. Moreover, the reconstructed dipole parameters remain stable across the redshift intervals considered, with velocity amplitudes of order $300\,\mathrm{km\,s^{-1}}$, for all three supernova samples. Finally, fixing the dipole parameters with the cosmic microwave background values leads to a slight shift from the fiducial $Λ$CDM values of the deceleration $q_0$ and jerk $j_0$ parameters.

### [B] 63.1 — Multi-lane type II radio bursts: Insights into shock propagation in the corona
- **arXiv:** [2608.19295](https://arxiv.org/abs/2608.19295)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** molecular_clouds (63.1), feedback_bubbles (61.8), turbulence (56.3)
- **Current keyword baseline:** NO
- **BM25 max:** 48.7
- **Semantic max:** 78.9
- **Abstract:** Type II solar radio bursts are considered as the signatures of the coronal shocks. These bursts are generated from plasma waves excited by magnetohydrodynamic (MHD) shocks, and then converted into radio waves at the local plasma frequency and/or its harmonics. Hence, these bursts often have fundamental-harmonic (FH) and band-splitting (SB) structures, which provide insights into shock generation and propagation in the corona, hence, in turn, the corresponding coronal conditions. In the present study, we analysed an unusual multi-lane type II burst observed with ground-based solar radio spectrographs on May 29, 2024, between 14:24 and 14:43 UT. The start and end frequencies of the type II burst were 450 MHz and 25 MHz, respectively. By combining spectral information with radio imaging data, we found that radio waves were escaping from the corona via emissions from distinct shock regions. In addition, along with the traditional FH and SB, there were multi-lane structures in the type II bursts. Our analysis suggests complex, inhomogeneous shock dynamics near the leading edge (LE) of the coronal mass ejection (CME). This indicates that the plasma material compresses more strongly in these forefront regions. This was confirmed by radio imaging observations, which showed that the higher-frequency emission occurred at a higher altitude than the lower-frequency emission. Our results suggest that the shock geometry and plasma inhomogeneity play an important role in the generation of type II bursts, leading to traditional fundamental-harmonic split-band (FH-SB) pairs with additional splitting in the type II bands.

### [B] 62.9 — The Roman Coronagraph Community Participation Program: pre-launch reference star list and impact of reference star properties on post-processing performance
- **arXiv:** [2608.17057](https://arxiv.org/abs/2608.17057)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP, astro-ph.SR
- **Top topics:** molecular_clouds (62.9), astrochemistry (54.3), star_formation (53.7)
- **Current keyword baseline:** YES
- **BM25 max:** 43.7
- **Semantic max:** 78.6
- **Abstract:** The upcoming Roman Coronagraph will be the first high-contrast instrument in space capable of high-order wavefront sensing and control technologies, a critical technology demonstration for the proposed Habitable Worlds Observatory (HWO) that aims to directly image and characterize habitable exoEarths. The nominal Roman Coronagraph observing plan involves alternating observations of a science target and a bright, nearby reference star for both wavefront calibration and reference differential imaging post-processing. Reference star criteria for the most demanding coronagraph mode are restrictive, limiting the sample to only 40 candidates for which thorough observational vetting is needed to assess their suitability. Reference star properties such as resolved diameters, presence of circumstellar dust, and close point sources may also have more subtle impacts on post-processing efficacy that may inhibit final contrast performance. In this work, we describe the current progress of the CoronaGraph Instrument Reference stars for Exoplanets (CorGI-REx) observing campaign, a 300+-hour observing campaign that utilizes instruments from around the world to vet reference stars for high-order wavefront control suitability. We will present the pre-launch list of reference star candidates being utilized for the Roman Coronagraph Observation Phase constructed from a thorough analysis of high contrast and interferometric observations. We will also present the results of simulations investigating the impact of reference star resolved diameters and companions on post-processing performance. We conclude by discussing the importance of reference star selection for scheduling observations and optimizing contrast performance for the Roman Coronagraph along with implications for HWO coronagraph operations.

### [B] 62.8 — Interpretations of the $10\%$ polarization observed in the early forward-shock afterglow of GRB 091208
- **arXiv:** [2608.15494](https://arxiv.org/abs/2608.15494)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** magnetic_fields (62.8), molecular_clouds (43.4), feedback_bubbles (43.1)
- **Current keyword baseline:** NO
- **BM25 max:** 90.4
- **Semantic max:** 66.4
- **Abstract:** The $\sim10\%$ optical polarization observed at the early stage of GRB 091208B comes from the forward shock emission, which is higher than the conventionally predicted value. Polarizations of the forward shock radiation would depend on the observational geometry and the post-shock magnetic field structure. This magnetic field could arise either from the compression of a pre-existing magnetic field (i.e., the magnetic field in the outer medium) or from the shock-generated instabilities. In this paper, we use a synchrotron radiation model to fit the light curve and polarization observations of GRB 091208B. Two scenarios are considered: one is the case of a slightly off-axis observer, and the other is with a large-scale ordered magnetic field component in the burst environment. We found both scenarios could interpret the observations of GRB 091208B. For the slightly off-axis observation scenario, the observational angle is restricted to be within the range of (1.02, 1.05) times the jet half-opening angle. For the large-scale ordered magnetic field component scenario, the ratio between the ordered component to the random component is constrained to be around 1.

### [B] 62.8 — High-order Paschen emission from the quiet-Sun off-limb chromosphere
- **arXiv:** [2608.14034](https://arxiv.org/abs/2608.14034)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** feedback_bubbles (62.8), ism_methods_data (58.7), astrochemistry (58.7)
- **Current keyword baseline:** NO
- **BM25 max:** 48.6
- **Semantic max:** 78.5
- **Abstract:** We report the detection of high-order hydrogen Paschen emission lines (Pa~15, Pa~16, and Pa~17) in the quiet-Sun chromosphere off the solar limb using the Chromospheric Infrared SpectroPolarimeter (SCIP) on board the {\sc Sunrise~iii} balloon telescope. These lines reveal thread-like structures resembling spicules and exhibit systematically smaller Doppler velocities than Ca~II~854.2~nm, suggesting that they are optically thinner and more affected by line-of-sight averaging, especially near the limb. Non-LTE radiative transfer synthesis using the spherically symmetric one-dimensional code \texttt{rhsphere} reproduces the overall spectral properties. The observed ratios among three Paschen lines show systematic deviations from synthetic and theoretical results, suggesting that additional physical effects may influence the formation of high-order Paschen lines. The study demonstrates the potential of high-order Paschen lines as a new diagnostic of optically thin plasma in the off-limb chromosphere.

### [B] 62.8 — The atmospheric vertical structure of Uranus and Neptune from thermochemical models: the impact of model assumptions
- **arXiv:** [2608.13157](https://arxiv.org/abs/2608.13157)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** astrochemistry (62.8), molecular_clouds (52.8), star_formation (51.9)
- **Current keyword baseline:** NO
- **BM25 max:** 48.7
- **Semantic max:** 78.5
- **Abstract:** The composition and temperature-pressure profile of the atmospheres of Uranus and Neptune are not well-determined. As observational data are limited, we often rely on chemical equilibrium computations to infer atmospheric abundances and cloud formation. The inferred atmospheric structures, however, strongly depend on several fundamental assumptions such as the elemental abundances and ratios, the condensation properties of the assumed species, or a reference temperature for the adiabatic structure. In this study we investigate the effects of different metallicities (1 to 80 solar), element ratios (C/O and S/N, from 0.1 to 2 and 0.19 to 1.6) and 1 bar temperatures (66 to 86 K) on the vertical structure of ice giant atmospheres. In particular, we use the chemical equilibrium code \texttt{FastChem} to derive mixing ratios and cloud structures for CH$_4$, NH$_3$, H$_2$S, H$_2$O and NH$_4$SH. We find that the models are very sensitive to the assumed parameters, yielding drastically different possible atmospheric structures. For the cases considered here, we find that mixing ratios and cloud deck altitudes can vary by more than an order of magnitude. Additionally, thermal profiles can differ by several tens of kelvins due to composition and 1-bar temperature. We advise that future ground-based observations and a dedicated mission to Uranus and/or Neptune are required to better characterize the atmospheric structure and composition of ice giants.

### [B] 62.8 — The Wave-Regulated Precursor of a Near-Parallel Interplanetary Shock Observed by Parker Solar Probe
- **arXiv:** [2608.12606](https://arxiv.org/abs/2608.12606)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, physics.plasm-ph, physics.space-ph
- **Top topics:** magnetic_fields (62.8), feedback_bubbles (61.6), molecular_clouds (59.6)
- **Current keyword baseline:** NO
- **BM25 max:** 36.0
- **Semantic max:** 78.5
- **Abstract:** Diffusive shock acceleration, at shocks from coronal mass ejections to supernova-remnant blast waves, presupposes a scattering wave field that the accelerated particles themselves maintain. This self-regulation has not been resolved in situ. We report Parker Solar Probe observations of a fast (~2800 km/s), near-parallel interplanetary shock at 0.24 AU on 2023 March 13 and separate its upstream wave field into four families, a classification not made before at a fast shock near the Sun. Right-hand and left-hand circularly polarized families over a common wavenumber band, with a field-aligned linearly polarized family, are cyclotron-resonant with the suprathermal-to-MeV protons streaming from the shock: the beam drives the field that scatters it, and the measured mean free path, half the precursor scale, leaves the beam anisotropic enough to sustain the drive. Outside this loop lies a weak, oblique, linearly polarized component, a few per cent of the wave power, resolved here for the first time at an in situ foreshock. Its in-phase density and field-magnitude fluctuations identify the compressive part as fast magnetosonic and shift the cyclotron-resonance energies of the resonant families by up to 13 % along the precursor. Acceleration at shocks inside 0.3 AU is governed upstream, in a foreshock the shock builds for itself.

### [B] 62.7 — A model for the enhanced production rate of early-type hypervelocity stars in the Galactic halo
- **arXiv:** [2608.18475](https://arxiv.org/abs/2608.18475)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.HE
- **Top topics:** star_formation (62.7), feedback_bubbles (55.3), turbulence (49.0)
- **Current keyword baseline:** NO
- **BM25 max:** 60.8
- **Semantic max:** 71.3
- **Abstract:** About twenty late B-type hypervelocity stars (HVSs) traveling faster than the Galactic escape velocity have been discovered in the Galactic halo, many of which were ejected from the Galactic center (GC). Recently, we have advocated that these HVSs most likely formed in the nuclear star cluster (NSC) $150$--$500\, \rm{Myr}$ ago and were predominantly ejected via the gravitational slingshot of a past intermediate-mass black hole (IMBH) orbiting the supermassive black hole (SMBH) Sgr~A$^{*}$. Here we explore the constraints of the production rate of young HVSs on the star formation region of the NSC. We propose that the young HVS progenitors are born in a lopsided eccentric disk that is comparable in radius to the NSC. By numerically tracking the orbital evolution of disk stars, we find that they undergo rapid angular momentum relaxation at formation due to eccentric disk instability, and that their slingshot interactions with the SMBH-IMBH binary at distances $\simeq 100\, \rm{au}$ produce HVSs at a rate of $10^{-5}$--$10^{-4}\, \rm{yr}^{-1}$. The rate is expected to trace the disk formation history, increasing with the accumulation of disk stars and dropping rapidly after the star formation stopped at $150\, \rm{Myr}$ ago. The rate is consistent with the observation and orders of magnitude higher than that expected for an old relaxed population in the literature, enhanced due to the gravitational torque from the non-spherical GC potential and radial velocity anisotropies of the disk stars. Our results imply that young HVSs should have a distinct radial and angular distribution from old ones.

### [B] 62.6 — Automatically distinguishing Rubin transients from AGN using variability metrics
- **arXiv:** [2608.18823](https://arxiv.org/abs/2608.18823)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.CO
- **Top topics:** ism_methods_data (62.6), astrochemistry (58.2), star_formation (57.0)
- **Current keyword baseline:** NO
- **BM25 max:** 60.3
- **Semantic max:** 72.8
- **Abstract:** Stochastic variability of active galactic nuclei (AGN) can produce contaminants in the search for explosive extragalactic transients (such as supernovae and tidal disruption events). In the new era of the Rubin Observatory's Legacy Survey of Space and Time (LSST), previously uncatalogued AGN, especially those with luminosity near the survey detection limits, are expected to produce a flood of detections that have the potential to contaminate surveys targeting other transients, leading to inefficient use of spectroscopic follow-up time. For surveys aiming to statistically characterise transient demographics, it is advantageous to use easily modelled and reproducible selection criteria to distinguish AGN from other transients, rather than machine learning. We test enacting cuts based on simple data-driven photometric variability parameters to distinguish non-AGN extragalactic transients from standard AGN variability on both Zwicky Transient Facility photometry and simulated LSST photometry from the MALLORN data set. We also investigate the impact of light curve history availability, redshift range and filter selection on selection efficiency. We find that a two-dimensional cut incorporating the ratio of detection flux and pre-detection standard deviation and the ratio of detection flux to pre-detection mean flux is the most effective cut. This approach is easily scalable as these values are included in the LSST alert packets. We provide estimates of the completeness and purity of the sample produced by enacting this cut, and gauge the AGN contamination avoided. The parameters utilised in this approach could also be implemented as features for identifying AGN in a photometric classifier.

### [B] 62.6 — In-situ measurements of space plasma: recent progress and future challenges
- **arXiv:** [2608.16734](https://arxiv.org/abs/2608.16734)
- **Primary category:** physics.space-ph
- **Categories:** physics.space-ph, astro-ph.IM, physics.ins-det, physics.plasm-ph
- **Top topics:** magnetic_fields (62.6), molecular_clouds (52.9), turbulence (51.7)
- **Current keyword baseline:** NO
- **BM25 max:** 47.9
- **Semantic max:** 78.3
- **Abstract:** Space plasmas like the solar wind or the Earth's space environment offer unique opportunities to observe fundamental plasma processes and their impact in situ. With modern space instrumentation, we measure the velocity distribution function of the plasma particles as well as the electromagnetic fields at high resolution and with minimal perturbation of the observed plasma systems. Plasma measurements like this are often not possible in laboratory settings on Earth. This review article focuses on modern diagnostic methods for the in-situ detection of plasma particles in space. It presents the detection principle of top-hat electrostatic analysers and highlights recent examples of scientific discoveries based on data from the heliospheric space missions Parker Solar Probe and Solar Orbiter. These examples demonstrate the capabilities of modern space plasma instrumentation. The article then discusses future directions in space plasma physics as well as the involved challenges in terms of the required plasma diagnostics. These new developments include, for example, upcoming and proposed space missions such as the operational space-weather mission Vigil, the multi-spacecraft mission HelioSwarm, the Mars mission M-MATISSE, and the electron-astrophysics mission Debye.

### [B] 62.5 — The SPT-3G+ receiver design
- **arXiv:** [2608.20235](https://arxiv.org/abs/2608.20235)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.CO
- **Top topics:** star_formation (62.5), ism_methods_data (61.5), molecular_clouds (56.6)
- **Current keyword baseline:** NO
- **BM25 max:** 36.4
- **Semantic max:** 78.1
- **Abstract:** We present the thermo-mechanical design of the cryostat and camera optics for SPT-3G+, a new receiver being developed for the South Pole Telescope (SPT). The receiver consists of 14 detector arrays of 90/150 GHz dichroic polarization-sensitive pixels, totaling 24,080 transition-edge sensor detectors. Each detector array lies at the end of an optics tube, each approximately 240 mm in diameter and 772 mm in length, which are arranged in a hexagonal close-packed configuration to achieve a 4 degree diameter field of view. Each optics tube contains four anti-reflection coated lenses fabricated from different materials (alumina, silicon, and nylon) that are designed to also provide infrared filtering that reduces the radiative loading on the cryogenic stages. The optics and detectors are cooled by a combination of a pulse tube cooler for the 40 K and 4 K stages, and a dilution refrigerator for the 1 K and 100 mK stages. Thermal modeling predicts the heat load to be less than 26 W and 1 W for the 40 K and 4 K stages, respectively. The 1,550 kg cryostat has a 1.1 meter diameter at the vacuum window, which is located near the telescope Gregorian focus, and 1.75 meters in height and length. Fabrication of the cryostat will begin in 2026, with installation on the SPT scheduled for the 2028-29 austral summer, ahead of the 2029 winter observing season.

### [B] 62.4 — Transient Early Dark Energy-Like Dynamics as a Mechanism for Enhanced Early Structure Formation in the JWST Era
- **arXiv:** [2608.20288](https://arxiv.org/abs/2608.20288)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (62.4), feedback_bubbles (57.5), star_formation (54.2)
- **Current keyword baseline:** NO
- **BM25 max:** 45.6
- **Semantic max:** 70.9
- **Abstract:** The discovery of massive galaxies at redshifts $z\gtrsim10$ by the James Webb Space Telescope (JWST) has renewed interest in cosmological mechanisms capable of enhancing early structure formation while preserving the successful large-scale predictions of the standard $Λ$CDM model. We investigate a phenomenological scenario in which an exotic dark matter species can undergo a transient early dark energy-like phase during the radiation-dominated era ($10^{-7}\lesssim a\lesssim10^{-5}$) before reverting to pressureless cold dark matter. We utilize the generalized dark matter framework to model this species, which is restricted to a sub-percent fraction of the total dark matter component by CMB, BAO and Type Ia supernova data. Its background and perturbation dynamics are characterized by a time-dependent equation of state, $w(a)$, and a time- as well as scale-dependent sound speed, $c_s^2(a,k)$. The temporary negative equation of state, combined with our phenomenological pressure-response prescription, induces a finite interval of negative effective sound speed squared. This triggers an instability-driven growth of density perturbations over a limited range of comoving scales, thereby enhancing the formation of early dark matter halos. We find that the enhanced halo abundance can substantially reduce the star-formation efficiencies required to reproduce the observed abundance of JWST galaxies relative to the standard $Λ$CDM scenario, especially at higher redshifts. Our results demonstrate that transient early dark energy-like dynamics in a subdominant dark matter component provide a viable mechanism for enhancing early structure formation and offer a new framework for interpreting the abundance of high-redshift galaxies observed by JWST and future surveys.

### [B] 62.3 — Towards end-to-end Bayesian forward models in global 21-cm cosmology: surrogate modelling and marginalisation of beam uncertainty
- **arXiv:** [2608.18962](https://arxiv.org/abs/2608.18962)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, astro-ph.IM
- **Top topics:** ism_methods_data (62.3), magnetic_fields (50.4), astrochemistry (47.9)
- **Current keyword baseline:** NO
- **BM25 max:** 81.4
- **Semantic max:** 77.8
- **Abstract:** Robust statistical inference in global 21-cm cosmology requires end-to-end uncertainty quantification that jointly handles the highly degenerate cosmological signal, foreground emission, and instrumental response. Although electromagnetic simulations capture physical antenna properties in a parametrised way, multi-hour runtimes make their integration within likelihood-based sampling frameworks infeasible. Most existing approaches therefore assume a single precomputed beam, a fragile assumption given our demonstration that realistic mismatches can severely bias the recovered cosmological and foreground parameters. To address this, we present an accelerated and differentiable Bayesian framework that incorporates an informed surrogate representation of chromatic beam uncertainty directly into a forward-modelling pipeline. Treating the physical antenna properties as nuisance quantities, we apply a two-stage decomposition directly to simulated directivity patterns, reducing the instrumental parameterisation by two orders of magnitude while retaining the angular and spectral structure required for accurate beam reconstruction. Exploiting the linearity of the resulting surrogate, we use analytical marginalisation to allow the continuous instrumental uncertainty to be propagated into the final posteriors and Bayesian evidence without directly sampling the beam space. Testing the framework against a suite of unseen beams and cosmological signals, we recover the true inputs at approximately the instrumental-noise level. We further show that, for the uncertainty considered here, as few as 100 electromagnetic simulations are sufficient to construct an effective surrogate, substantially reducing the simulation burden for future analyses. This framework provides a scalable, statistically rigorous route towards hardware-accelerated uncertainty quantification in global 21-cm cosmology.

### [B] 62.3 — No Helium Detected in LHS 1140 b from Four JWST NIRISS/SOSS Transits
- **arXiv:** [2608.13473](https://arxiv.org/abs/2608.13473)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** star_formation (62.3), ism_methods_data (61.3), molecular_clouds (58.9)
- **Current keyword baseline:** NO
- **BM25 max:** 41.5
- **Semantic max:** 77.9
- **Abstract:** In the effort to determine which low-mass exoplanets have atmospheres, LHS 1140 b remains one of the most favorable targets. Its large size (5.6 $\rm M_{\oplus}$ and 1.7 $\rm R_{\oplus}$) and relatively long orbital period (24.7 days) imply an atmosphere may be likely, and notably, recent interior models favor either a hydrogen-dominated "mini-Neptune" or a "water world" over a true terrestrial planet. Another possibility is that it has a helium-rich atmosphere. This hypothesis is supported by recent ground-based observations that detected the metastable helium triplet during transit. These observations indicated there may be current helium escape from the planet's upper atmosphere, yet the signal was not detected during a subsequent observation, suggesting time-variable escape. Here we present four observations of LHS 1140 b with JWST NIRISS/SOSS, which covers the metastable helium triplet, obtained between 2023 and 2026. These observations span the epoch of the ground-based measurements, and although none were contemporaneous with the ground-based transits, all four are sensitive to helium absorption at the previously reported level. However, we detect no helium absorption in any visit. We reject the best-fit ground-based model at $>3σ$ in each visit, and find no clear trend in mass-loss with time. Our results suggest the reported ground-based detection may be spurious, although variability cannot be excluded if detectable helium absorption occurs in $\lesssim50\%$ of transits. The nature of LHS 1140 b thus remains a mystery until future transmission and emission analyses are complete.

### [B] 62.2 — An Optical Illusion: High Electron Densities Create Extremely Metal-Poor Galaxy Impostors
- **arXiv:** [2608.20339](https://arxiv.org/abs/2608.20339)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** massive_star_formation (62.2), astrochemistry (59.8), galactic_ism_surveys (59.0)
- **Current keyword baseline:** NO
- **BM25 max:** 66.2
- **Semantic max:** 77.7
- **Abstract:** JWST has enabled the discovery of dozens of extremely metal-poor galaxies (EMPGs) with metallicities below $5\%\,Z_{\odot}$, representing a significant leap toward detecting the first galaxies without metals. However, accurate metallicity measurements require careful determination of physical conditions in the ionized gas. In this paper, we study four galaxies that appear to be EMPGs when analyzed using the direct $T_e$ method with the common low-density assumption ($n_e=10^3\,{\rm cm}^{-3}$). To test whether their metal-poor status holds when accurately measuring the density, we apply the direct method with a self-consistent determination of electron temperature ($T_e$) and density ($n_e$) in the high-ionization zone using the [OIII]$λ$5008, [OIII]$λ$4364, and [OIII]$λ$1666 lines, using JWST/NIRSpec data from the SPURS program in the Abell 2744 lensed field. We find that three out of four galaxies in our sample have extremely high electron densities ($n_e \sim 10^{5}-10^{6}\,{\rm cm^{-3}}$), which suppress the [OIII]$λ$5008 line and lead to underestimates of metallicity by up to $\sim1.1\,$dex when this density is not accounted for, and have true metallicities of 12+log(O/H) $\sim7.3-8.2$. Failure to account for high densities can therefore lead to systematic misclassification of metal-poor galaxies and biased conclusions about early chemical enrichment.

### [B] 62.2 — Substructure evolution from protoplanetary to debris disks driven by mutually gravitating planetesimals and implications on Kepler resonances and free-floating planets
- **arXiv:** [2608.19329](https://arxiv.org/abs/2608.19329)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** feedback_bubbles (62.2), star_formation (58.6), astrochemistry (55.9)
- **Current keyword baseline:** YES
- **BM25 max:** 44.4
- **Semantic max:** 77.7
- **Abstract:** Motivated by recent observations suggesting rings found in debris disks are wider than those in protoplanetary disks, we consider a picture in which planetesimals formed in radially narrow dust traps radially diffuse into debris rings via mutual scattering. Under this picture, evolving the fractional widths ($Δr/r$) of resolved debris rings back to a few Myr according to the theoretical $t^{1/5}$ evolutionary trajectory reproduces the protoplanetary ring distribution. We inferred the product of the ring mass and individual planetesimal mass required to reach the observed debris ring widths at their ages, finding that $M_\mathrm{disk}\times m$ ranges from $10^{-3}$ to $10^{3} \, M_\oplus^2$. The distribution of $M_\mathrm{disk} \times m$ appears to correlate with the stellar mass, peaking at 1.5 to 2 $M_\odot$, which resembles the stellar mass dependence of the giant exoplanet occurrence rate. The population of resolved debris rings lie close to the $Δr / r = 10 \, h$ equipartition relation expected of a planetesimal ring that formed narrow, with typical resolved debris disks still expected to be broadening radially and vertically at present. If sufficiently massive ($\sim$10 $M_\oplus$), this radial broadening can send a few Mercurys to the terrestrial region within 10 Myr, making debris disks a plausible source of planetesimals disrupting resonant chains among Kepler planets. Within Gyr timescales, outer planetesimal belts can also eject $\sim$1% of their mass into interstellar space if they consist of Moon-sized bodies or above, suggesting that the slow and steady intrinsic evolution of massive debris disks could contribute to the interstellar free-floating population of terrestrial-planet-sized bodies.

### [B] 62.2 — $\texttt{Aether.jl}$ : A High-Performance 3D MHD and Multifluid Dust Code Written in a Dynamic Language with an Interactive Human-AI Development Framework
- **arXiv:** [2608.14048](https://arxiv.org/abs/2608.14048)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (62.2), turbulence (62.0), molecular_clouds (59.3)
- **Current keyword baseline:** NO
- **BM25 max:** 62.2
- **Semantic max:** 77.7
- **Abstract:** We present $\texttt{Aether}$, a new finite-volume code for compressible hydrodynamics and magnetohydrodynamics, written in Julia and primarily designed for GPU systems. The code solves the MHD equations with constrained transport in Cartesian, cylindrical, and spherical-polar coordinates, using standard high-order Godunov methods. An arbitrary number of dust fluids can be coupled to the gas through stiff mutual drag. It was developed from scratch with interactive Human-coding agent workflow; the paper documents the framework of this workflow alongside the numerical methods. Performance-critical kernel is written through $\texttt{KernelAbstractions}$, and supports runs on CPUs and GPUs from multiple vendors. $\texttt{Aether}$ can be ran either from an interactive notebook or batch scripts, keeping prototyping, production runs, and analysis in a single language. We verify the implementation through a series of hydrodynamic, MHD, and dust tests. Although written in a dynamic language, $\texttt{Aether}$ achieves comparable or even higher single-GPU throughput than C++ code on the same hardware. In weak scaling on Frontier, parallel efficiency stays above $93\%$S on 4096 GCDs. These results show that a dynamic language now supports production astrophysical MHD simulations on exascale systems. $\texttt{Aether}$ and its Jupyter notebook example suite are publicly available.

### [B] 62.2 — Time-dependent multi-energy neutrino emission from symbiotic recurrent novae: the role of accretion disks
- **arXiv:** [2608.13814](https://arxiv.org/abs/2608.13814)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (62.2), star_formation (56.7), ism_methods_data (51.3)
- **Current keyword baseline:** NO
- **BM25 max:** 44.5
- **Semantic max:** 77.8
- **Abstract:** Symbiotic recurrent novae provide a unique laboratory for studying thermonuclear explosions, shock evolution, and nonthermal particle acceleration in dense circumstellar environments. In this work, we develop a time-dependent, multi-energy framework to describe neutrino emission from such systems, consistently incorporating both MeV neutrinos produced during thermonuclear runaway and GeV neutrinos generated through hadronic interactions in nova-driven shocks. Using RS Oph as a benchmark source, we model the evolution of the shock interacting with both the red giant wind and a dense accretion disk surrounding the white dwarf. We show that the resulting neutrino signal exhibits a characteristic two-component temporal structure: an early, rapidly rising MeV component tracing nuclear burning, followed by a delayed GeV component governed by shock propagation and particle acceleration. The presence of an accretion disk can significantly enhance the early-time GeV neutrino emission by providing a dense target for proton-proton interactions. This leads to a pronounced neutrino flux within the first few hours after eruption, a feature absent in wind-dominated scenarios. We further evaluate the detectability of these signals and find that while the MeV component remains below current detection thresholds, the GeV neutrino emission from nearby systems may become accessible to next-generation detectors. Our results highlight the critical role of the circumstellar structure in shaping nova neutrino emission and demonstrate that symbiotic recurrent novae are promising targets for future multi-messenger observations.

### [B] 62.1 — Dipolar power asymmetry in wide-angle correlations of galaxy density, velocity and ellipticity
- **arXiv:** [2608.19039](https://arxiv.org/abs/2608.19039)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, hep-ph
- **Top topics:** turbulence (62.1), galactic_ism_surveys (59.9), ism_methods_data (52.2)
- **Current keyword baseline:** NO
- **BM25 max:** 81.9
- **Semantic max:** 74.9
- **Abstract:** The large-scale structure of the universe has the potential to probe anomalies suggested by observations of the cosmic microwave background. In this work, we focus on a position-dependent dipolar modulation of the primordial power spectrum and develop a full-sky formalism for computing correlation functions of galaxy density, velocity and ellipticity. By comparing the correlation functions obtained with and without the plane-parallel approximation, we show that wide-angle corrections become non-negligible for opening angles $Θ\gtrsim 30^\circ$. Our results demonstrate that wide-angle corrections must be taken into account when testing the dipolar modulation with future large-scale structure surveys.

### [B] 62.1 — A Search for helium in the atmospheres of three sub-Neptunes and a super-Earth around M-dwarfs
- **arXiv:** [2608.19030](https://arxiv.org/abs/2608.19030)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** ism_methods_data (62.1), astrochemistry (60.4), star_formation (58.3)
- **Current keyword baseline:** NO
- **BM25 max:** 54.6
- **Semantic max:** 75.5
- **Abstract:** Thousands of sub-Neptunes have been discovered mainly through space-based surveys such as Kepler and TESS. Their bulk compositions and internal structures are thought to reflect their formation and evolutionary pathways, and atmospheric observations provide constraints on these processes. The near-infrared helium triplet is a potential tracer of extended, escaping H/He atmospheres. Recent models that include geometric effects suggest that planets orbiting nearby late M dwarfs may offer favorable conditions for detecting this signal. Nevertheless, helium has been reported for only three planets around M dwarfs to date. We conducted high-resolution transmission spectroscopy of three sub-Neptunes (TOI-2136b, TOI-654b, and LP 791-18c) and a super-Earth (TOI-1634b) orbiting M dwarfs with the InfraRed Doppler (IRD) spectrograph on the Subaru Telescope. We find no statistically significant helium absorption in any target; accordingly, we derive 95% confidence upper limits on the helium line depth of 1.36%, 0.60%, 2.07%, and 3.00%, and on the equivalent width of 7.3, 2.1, 7.4, and 9.1 mÅ, for TOI-2136b, TOI-1634b, TOI-654b, and LP 791-18c, respectively. We further explored constraints on the upper-atmospheric temperature and mass-loss rate by comparing these results with isothermal Parker-wind models. While we have compared with self-consistent ATES models of primordial H/He atmospheres spanning a range of assumed X-ray luminosities, changes in the assumed XUV flux do not appear to account for the non-detections. The results suggest that these planets have metal-enriched H/He primary atmospheres or non-primordial atmospheres, such as water-rich envelopes. Future observations of other absorption lines, such as Lyman-$α$, H-$α$, and H$_2$O, may provide further constraints on these atmospheres.

### [B] 62.1 — Launching Jets in Tidal Disruption Events: Magnetic Flux Advection and Plasma Loading
- **arXiv:** [2608.14258](https://arxiv.org/abs/2608.14258)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (62.1), molecular_clouds (52.6), magnetic_fields (49.9)
- **Current keyword baseline:** NO
- **BM25 max:** 59.8
- **Semantic max:** 70.6
- **Abstract:** A tidal disruption event (TDE) occurs when a star approaches a black hole (BH) and is disrupted by its tidal forces. Although several hundred TDEs have been identified to date, only a small fraction are accompanied by relativistic jets. These jets are thought to be Poynting-flux-dominated outflows powered by the Blandford--Znajek (BZ) mechanism. However, the origin of the magnetic flux and plasma needed to power BZ jets remain unclear. In this Letter, we propose a scenario in which magnetic flux is initially stored in a pre-existing low-Eddington accretion disk around BH, and is subsequently advected toward the BH by the super-Eddington accretion flow formed after the stellar disruption. We show that stars with low densities, such as red giants, can supply sufficient magnetic flux to power a BZ jet. Once sufficient magnetic flux accumulates near the BH, an equatorial current sheet forms where magnetic reconnection produces high-energy gamma rays. We find that photon--photon pair production by these gamma rays supplies the BH magnetosphere with sufficient plasma to launch and sustain a BZ jet. We further show that this mechanism simultaneously provides enough radiating particles to account for the observed prompt emission.

### [B] 61.8 — Continuum Variability in AGN: Evidence for Systematically Suppressed Fluctuations in the BAL Population
- **arXiv:** [2608.18287](https://arxiv.org/abs/2608.18287)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (61.8), feedback_bubbles (58.5), astrochemistry (55.7)
- **Current keyword baseline:** NO
- **BM25 max:** 42.3
- **Semantic max:** 77.3
- **Abstract:** We aim to compare the flux variability of Broad Absorption Line quasars (BAL) to non-BAL quasars, controlling for black hole parameters to inform models concerning the generation of the BAL phenomenon. Using SDSS DR16 and ZTF $g$- and $r$-band light curves, we select quasars with $1.57 \leq z \leq 2.00$ and $18.5 \leq rmag \leq 19.8$. This redshift range ensures that the $g$-band covers the C IV emission line (and trough in BALs) while the $r$-band probes continuum variability, and allows black hole mass (MBH) estimates via Mg II. We quantify variability using excess variance and damped random walk (DRW) parameters ($σ_{\mathrm{DRW}}$, $τ_{\mathrm{DRW}}$). We also compared the DRW metrics in bins of MBH and Eddington ratio (REdd) to isolate the influence of the BAL phenomenon in objects with the same physical properties. Excess variance and $σ_{\mathrm{DRW}}$ are consistently smaller for BALs, confirming lower long-term variability, while the $g$-band exhibits higher variability than the $r$-band across both populations. These differences persist in fixed bins of MBH and REdd, indicating that the suppressed variability in BALs is not simply driven by differences in these properties between BAL and non-BAL samples. These results show that BAL quasars are systematically less variable than non-BAL quasars in both bands, confirming that this suppression is an intrinsic feature of the continuum rather than an effect of emission or absorption line contamination. The samples could be made to agree if BAL MBH values were systematically overestimated by a factor $\gtrsim 4$, implying a significantly higher REdd. Alternatively, the lower variability in BALs can be related to their lower X-ray luminosities, or to significant nuclear obscuration, if the inner part of the accretion disc were more obscured in BALs and more variable than the rest of the disc.

### [B] 61.8 — The dust-rich, gas-depleted protosolar disk as the birthplace of chondrules
- **arXiv:** [2608.16204](https://arxiv.org/abs/2608.16204)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** molecular_clouds (61.8), star_formation (59.3), feedback_bubbles (51.8)
- **Current keyword baseline:** NO
- **BM25 max:** 60.2
- **Semantic max:** 77.2
- **Abstract:** Chondrules are the primary components of primitive meteorites known as chondrites, and understanding their formation and accumulation is essential for elucidating the history of planet formation in the Solar System. Although a variety of chondrule formation mechanisms have been proposed, it remains challenging to satisfy the key constraints on chondrule abundance, formation timing, and mineralogical and chemical characteristics within a single model. In particular, the planetesimal bow-shock model, once considered one of the leading candidates, now faces a fundamental difficulty: Jupiter's formation likely depleted gas in the protosolar disk, potentially lowering the gas density below that required for efficient chondrule formation by planetesimal bow shocks. Here we propose an alternative mechanism that can occur in a gas-depleted environment: heavy bombardment of eccentric planetesimals by debris dust. After Jupiter formed in the protosolar disk, the region interior to its orbit became gas-depleted, leading to the formation of a geometrically thin debris-dust layer. When planetesimals enter the dust layer at high speed, large quantities of molten silicate droplets are produced. These droplets cool and solidify into chondrules and are reincorporated into the dust layer. Using analytical calculations, we find that our model can potentially explain the abundance, formation timing, and mineralogical and chemical characteristics of chondrules. This study links the formation of Jupiter and the accompanying evolution of the protosolar disk to the origin of terrestrial planets, asteroids, and meteorites, thereby offering a new framework for the formation of the Solar System.

### [B] 61.7 — Evidence of self-organized criticality in the prompt emission of a bright gamma-ray burst
- **arXiv:** [2608.17964](https://arxiv.org/abs/2608.17964)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (61.7), feedback_bubbles (58.5), turbulence (52.7)
- **Current keyword baseline:** NO
- **BM25 max:** 50.3
- **Semantic max:** 77.1
- **Abstract:** Gamma-ray bursts (GRBs) are the most energetic explosive events in the Universe, yet the physical mechanism of their prompt emission remains a mystery. Especially, it is unclear whether the energy dissipation mechanism in the GRB jet is dominated by kinetic energy or magnetic energy. Here, we studied the pulses in the prompt emission of the second brightest GRB to date, GRB 230307A, which was accurately measured by the Gravitational wave high-energy electromagnetic counterpart all-sky monitor (GECAM), with focus on the cumulative distributions of peak counts and duration of pulses as well as the waiting time between pulses. We find that these cumulative distributions show scale-invariant behavior, well consistent with the prediction of the self-organized criticality (SOC) theory. This is the first robust evidence of an SOC feature in the prompt emission of a single GRB. Moreover, the statistical properties of pulses in the prompt emission of GRB 230307A are very similar to those of solar flares. Our findings suggest that the prompt emission of GRB is powered by the dissipation of magnetic energy in the ultra-relativistic jet, supporting the Poynting-flux-dominated prompt models.

### [B] 61.7 — The PANSY Meteor Head-echo Orbit Catalogue: Continuous Antarctic Radar Observations of Southern Meteoroid Streams
- **arXiv:** [2608.17589](https://arxiv.org/abs/2608.17589)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, physics.space-ph
- **Top topics:** star_formation (61.7), ism_methods_data (59.8), magnetic_fields (56.9)
- **Current keyword baseline:** NO
- **BM25 max:** 39.4
- **Semantic max:** 77.2
- **Abstract:** Meteor head echoes from high-power, large-aperture radars provide pulse-resolved positions and velocities for individual micrometeoroids in a submillimeter-radius range that contribute significantly to the mass influx to Earth. We present the first meteor head-echo orbit catalogue from the Antarctic Syowa Mesosphere--Stratosphere--Troposphere/Incoherent Scatter radar (PANSY). The catalogue contains two million meteors and 50 million pulse-resolved measurements. The observed radiant distribution contains the helion, antihelion, south toroidal and apex sources, and provides unprecedented head-echo coverage of southern ecliptic latitudes. The initial detection-height distribution is found to be double-banded, with both bands increasing in height with meteor speed and exhibiting distinct radiant distributions, consistent with a mixture of meteoroid-size differences and differential ablation. Estimation of dynamic mass indicates that the survey is sensitive to initial radii of approximately 100 micrometers. As part of an initial exploration of the catalogue, we investigate the nighttime alpha Capricornids (CAP) and the extended Daytime Capricornids-Sagittariids (DCS) radiant. Their similar activity durations at opposite nodes are consistent with membership in the CAP--169P/NEAT complex. The radiant distribution suggests a new meteor shower candidate, with peak flux near solar longitude 110 degrees, mean Sun-centered ecliptic radiant longitude 291.0 degrees, latitude -48.2 degrees, and geocentric speed 48.7 km s^{-1}. During catalogue production, event-level raw voltage cuts are retained temporarily to support improvements in data analysis. This first catalogue release, covering 2025 January 26 to 2026 July 26, will be useful for further studies of the southern-hemisphere Earth-crossing meteoroid population.

### [B] 61.6 — Probabilistic kilonova prediction from gravitational wave inferred binary neutron star parameters
- **arXiv:** [2608.20262](https://arxiv.org/abs/2608.20262)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, gr-qc
- **Top topics:** ism_methods_data (61.6), star_formation (55.1), turbulence (48.6)
- **Current keyword baseline:** NO
- **BM25 max:** 35.5
- **Semantic max:** 68.9
- **Abstract:** Kilonovae provide a key electromagnetic window into binary neutron star mergers, revealing the properties of the merging system while probing r-process nucleosynthesis of the Universe. However, only a few kilonova candidates have been detected to date, with AT2017gfo being the only one associated with a gravitational wave event, GW170817. In this work, we present \textsc{Genova}, a probabilistic framework for predicting kilonova spectra and light curves directly from gravitational wave posterior samples of binary neutron star mergers. This method uses a conditional normalising flow to learn the distribution of rest-frame spectra conditioned on the source-frame component masses, tidal deformabilities, viewing angle and time since merger. Other kilonova model parameters, such as ejecta opacities, are marginalised over during training, so that their effects are propagated into the predicted spectra as predictive uncertainty. In the self-consistency test, the flow model reproduces the median light curves with residuals typically below $\sim 0.1$ mag, and the ratio of the predicted central 68\% interval widths remains predominantly between $0.8$ and $1.4$ over $\sim 0.4$--$8.0$ days. Comparisons with a physically distinct kilonova model show that the probabilistic prediction can remain informative beyond the model used for training. We apply \textsc{Genova} to GW170817/AT2017gfo using multi-band observations, including newly re-reduced $Y$-, $J$-, $K_s$-band photometry from the Visible and Infrared Survey Telescope for Astronomy, which we present in this work. The resulting predictive intervals broadly encompass the observations while capturing both gravitational wave posterior uncertainty and the variation induced by marginalised kilonova model parameters.

### [B] 61.6 — Kinematics and Dynamics of the Open Cluster NGC 2302
- **arXiv:** [2608.18550](https://arxiv.org/abs/2608.18550)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.SR
- **Top topics:** star_formation (61.6), astrochemistry (58.7), feedback_bubbles (57.5)
- **Current keyword baseline:** NO
- **BM25 max:** 44.9
- **Semantic max:** 77.1
- **Abstract:** Open clusters are ideal observational testbeds to understand the dynamics of stellar systems. We present a dynamical study of the young open cluster NGC 2302. The latest Gaia data and $UBVIJHK_s$ photometric data are used in this study. A total of 117 stars are selected as the genuine members using the Gaia data. This cluster is, on average, reddened by $<E(B-V)> = 0.24 \pm 0.06$ (s.d.). The ratio of total-to-selective extinction ($R_V$) in the direction of NGC 2302 is $2.8 \pm 0.1$. The cluster distance is determined to be $1.16 \pm 0.08$ kpc using Gaia parallaxes. Theoretical isochrone fitting for $Z = 0.008$ on color-magnitude diagrams yields an age of $80 \pm 20$ Myr. The relative proper motions of individual members show no significant radial expansion or contraction. NGC 2302 contains a total stellar mass of $333 \pm 48 M_{\odot}$. The one-dimensional velocity dispersion is approximately 0.26 km s$^{-1}$, which is comparable to the viral velocity dispersion of 0.27 km s$^{-1}$ derived from its total mass. Its relaxation time is estimated to be approximately 90 Myr, which is similar to the age of the cluster within the uncertainty in age estimation. Finally, we report a pattern of mass segregation in the radial distribution of stellar masses. Our results suggest that NGC 2302 is virialized and currently approaching a state of dynamical relaxation. However, because no definitive evidence of kinetic energy equipartition is found, the possibility of the in-situ formation of high-mass stars within the central region should be carefully considered.

### [B] 61.5 — Ripples in the OCEANS: Broad Line Variability of Little Red Dots
- **arXiv:** [2608.12487](https://arxiv.org/abs/2608.12487)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (61.5), feedback_bubbles (61.3), molecular_clouds (58.1)
- **Current keyword baseline:** NO
- **BM25 max:** 55.0
- **Semantic max:** 76.9
- **Abstract:** Little Red Dots (LRDs) are a unique class of compact, red sources discovered in the JWST extragalactic deep fields. Determining if they are indeed powered by accreting supermassive black holes (SMBHs) is one of the main drivers of the intense study of these objects. Evidence for variability in these objects provides a direct test for the active galactic nucleus (AGN) nature of their central engine. In this study, we present a variability analysis of 6 LRDs observed by the $R \sim 2700$ OCEANS survey and leverage archival $R \sim 1000$ spectroscopic data from the CEERS and RUBIES surveys. We report marginal detections of $\rm Hα$ broad-line (BL) variability in the LRDs OCEANS-100424/RUBIES-42232 (27\% variability at 2.1$σ$ significance) and OCEANS-35829/RUBIES-49140 (GlimmIr/Irony; 50\% variability at 1.5$σ$ significance). The other 4 LRDs in our sample do not show evidence for BL variability, with a 1$σ$ upper limit of $4.8 \% - 30\%$ variability between their epochs of observations. We also find no evidence ($<1σ$) for continuum variability in our LRD sample. We compare our results to a sample of SDSS-RM quasars to determine the probability of our broad $\rm Hα$ variability detections. We find that the probability of reproducing 2 variable and 4 nonvariable quasars is $4.71\%$, corresponding to $\sim 2 σ$ departure from typical quasar variability. The detection of BL $\rm Hα$ variability in 2 LRDs provides some evidence for the AGN nature of these objects as opposed to pure scattering models.

### [B] 61.4 — Could John Ellard Gore have pre-empted the Hertzsprung-Russell diagram?
- **arXiv:** [2608.18799](https://arxiv.org/abs/2608.18799)
- **Primary category:** physics.hist-ph
- **Categories:** physics.hist-ph, astro-ph.SR
- **Top topics:** star_formation (61.4), astrochemistry (58.0), galactic_ism_surveys (55.4)
- **Current keyword baseline:** YES
- **BM25 max:** 33.3
- **Semantic max:** 76.7
- **Abstract:** John Ellard Gore (1845-1910) was an Irish amateur astronomer, prolific science writer and civil engineer. He was an inaugural member of the British Astronomical Association when it was founded in 1890 and was invited to become the first Director of its Variable Star Section. Through careful reasoning, Gore reached remarkably modern conclusions about the nature of stars, including their sizes, distances and luminosities. This paper explores whether he might have been able to produce an early form of what is now known as the Hertzsprung-Russell (H-R) diagram.

### [B] 61.4 — On-sky demonstration of dual-field interferometry at the CHARA Array
- **arXiv:** [2608.17204](https://arxiv.org/abs/2608.17204)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (61.4), star_formation (60.0), magnetic_fields (58.6)
- **Current keyword baseline:** NO
- **BM25 max:** 42.7
- **Semantic max:** 75.0
- **Abstract:** Dual-field interferometry uses a bright reference star for real-time fringe tracking, allowing a second beam combiner to record long coherent integrations on a fainter off-axis science target. At the Center for High Angular Resolution Astronomy (CHARA) Array, we implement this mode using the six-telescope MIRC-X and MYSTIC beam combiners in the H and K bands, respectively. We first demonstrated this capability in summer 2025 on the hierarchical triple $α$~Piscium. MIRC-X tracked component A in the $H$ band, while MYSTIC observed component B in the K band, resolving the 7~mas Ba--Bb subsystem and measuring the relative astrometry of the 1.85~arcsec A--B pair with an uncertainty of 234~$μ$as. Here, we describe subsequent phase-tracking testing, preliminary sensitivity simulations, and planned instrumental upgrades aimed at extending this mode to faint off-axis science targets.

### [B] 61.4 — JWST MIRI Medium Resolution Spectrometer Point Fixed Pattern Corrections: Cleaner and Higher Signal-to-Noise Spectra of Point Sources
- **arXiv:** [2608.13464](https://arxiv.org/abs/2608.13464)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (61.4), star_formation (59.9), molecular_clouds (59.5)
- **Current keyword baseline:** NO
- **BM25 max:** 33.0
- **Semantic max:** 76.8
- **Abstract:** The JWST Mid-Infrared Instrument Medium Resolution Spectrometer provides the capability to obtain spectra from 5-28 micron. The JWST data reduction pipeline removes the majority but not all of the instrument artifacts and the signal-to-noise (S/N) of the resulting spectra are limited by fixed pattern noise. Building on previous work, Point Fixed Pattern Corrections (PFPCs) are constructed using observations of O, A, and G dwarf flux calibration stars and asteroids taken using the default four point dither pattern. The PFPCs can be applied to spectra of point sources taken with target acquisition and the same dither pattern. They can be used alone or with the pipeline residual fringe correction depending on the sources spectral properties. Both narrow and broad artifacts are removed by the PFPCs improving the spectra regardless of their S/N. For higher S/N observations, the PFPCs significantly improve the S/N by up to factors of a few and S/N values of 1000 or more. The MRS-PFPC python package is provided to allow anyone to utilize the PFPCs for their own data.

### [B] 61.3 — PowerFull: fast and accurate computation of the relativistic angular galaxy power spectrum including local primordial non-Gaussianity
- **arXiv:** [2608.18334](https://arxiv.org/abs/2608.18334)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc
- **Top topics:** ism_methods_data (61.3), galactic_ism_surveys (59.1), turbulence (54.3)
- **Current keyword baseline:** NO
- **BM25 max:** 55.8
- **Semantic max:** 73.8
- **Abstract:** Current and forthcoming wide-field galaxy surveys, such as SPHEREx and Euclid, provide a unique opportunity to probe the ultra-large scales of structure formation, where primordial non-Gaussianity, often parameterized by $f_\text{NL}$, is expected to leave its most detectable imprint. At the same time, these surveys inevitably enter regimes where relativistic and wide-angle effects become significant, requiring careful modeling to extract unbiased cosmological information. We address these challenges by applying the total-angular-momentum (TAM) formalism to describe redshift-space clustering beyond the flat-sky approximation. The standard Fourier-mode description, which characterizes distortions by the angle between a mode and a line of sight, becomes ill-defined over wide fields, whereas the TAM basis naturally separates radial and angular contributions and incorporates the relevant relativistic effects. Within this framework, we provide a new parameterization of wide-angle predictions that can be compared directly with survey data. We then introduce PowerFull, a modification of the Julia-based 2-FAST package, which enables efficient computation of the full relativistic angular power spectrum. Finally, using Fisher information matrix-based analyses, we show that a survey like SPHEREx reaches $σ(f_\text{NL}) \sim 1$, but that neglecting the relativistic and wide-angle contributions shifts the recovered $f_\text{NL}$ by an amount of order its own uncertainty: at this precision the inferred value is biased unless the clustering is modeled consistently.

### [B] 61.3 — On the Acceleration of Pulsar Timing computations using Normalising Flows and Parallelisation
- **arXiv:** [2608.13991](https://arxiv.org/abs/2608.13991)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.HE
- **Top topics:** turbulence (61.3), ism_methods_data (59.5), star_formation (57.6)
- **Current keyword baseline:** NO
- **BM25 max:** 39.6
- **Semantic max:** 76.7
- **Abstract:** Single-Pulsar Noise Analysis (SPNA) and Gravitational Wave (GW) searches done on Pulsar Timing Array (PTA) datasets have everlastingly suffered from the computational bottleneck arising due to high dimensionality and multi-modality of the PTA likelihood landscape, along with strong correlations amongst various single-pulsar noises and ensemble-level common noise processes. We addressed this outstanding issue by employing a Normalising Flow-based Preconditioned Monte-Carlo sampling technique implemented in the POCOMC package, for the first time on PTA-specific computations, and comparing the achieved acceleration with the widely used PTMCMCSAMPLER and DYNESTY packages. We further investigated the acceleration achieved via parallelisation over an increasing array of communicating nodes on a high-performance computing (HPC) resource, by employing the PARALLEL_BILBY architecture with DYNESTY. We tested the acceleration on realistic long baseline simulated datasets with SPNA and Common Red Noise (CRN) analysis. We found PARALLEL_BILBY to be the most efficient in parallelisation, achieving a runtime of ~10min and ~100min with 16 nodes for spatially uncorrelated and Hellings and Downs-correlated CRN searches, respectively. POCOMC outperforms in single node performance requiring only ~10h for correlated search. PTMCMCSAMPLER was found to be the least efficient. We envisage POCOMC to be of great importance for PTA analyses, without requiring any GPU or HPC support, while also performing ensemble-level GW searches within a manageable time span. These results have everlasting implications with increasing data volumes and need to incorporate more complicated models, which were otherwise beyond reach due to the associated computational costs.

### [B] 61.2 — Vera C. Rubin LSST Synthetic Magnitudes derived from Gaia XP Spectra
- **arXiv:** [2608.17922](https://arxiv.org/abs/2608.17922)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.GA, astro-ph.SR
- **Top topics:** galactic_ism_surveys (61.2), ism_methods_data (60.8), star_formation (55.7)
- **Current keyword baseline:** NO
- **BM25 max:** 81.8
- **Semantic max:** 69.6
- **Abstract:** Context. In the context of Milky Way studies, the Vera C. Rubin Observatory's Legacy Survey of Space and Time is often described as a deep extension of the Gaia survey. In the future, joint analysis of the Gaia and LSST data promises to bring new insights into our understanding of the Galaxy's structure and formation history. However, the relatively small overlap in the magnitude ranges of the two surveys raises the question of how to perform a joint calibration of these datasets. Aims. In this paper, we produce high-quality synthetic LSST photometry from Gaia XP low-resolution spectra, using SDSS and DES observed photometry to calibrate the spectra. Methods. We develop a method of empirical correction of Gaia XP spectra using SDSS Stripe 82 photometry. We project sources for which Gaia XP data are available onto a magnitude-magnitude grid and calculate residuals between uncorrected synthetic and observed SDSS magnitudes, which are then used to derive correction coefficients across spectral regions corresponding to each photometric band. Results. The correction significantly reduces systematic trends and scatter in the synthetic magnitudes: the median residuals decrease by an order of magnitude (e.g., for the u band the improvement is from 0.038 to 0.002 mag), and the standard deviation of residuals typically becomes up to factor of two smaller (e.g., for the u band from 0.2 to 0.07 mag). Conclusions. Our correction approach improves the reliability of synthetic photometry derived from Gaia XP spectra and enables joint analysis of Gaia and LSST data for studies of Galactic structure and stellar populations.

### [B] 61.2 — Simulation tools for realistic high-order wavefront correction with the Roman Coronagraph
- **arXiv:** [2608.17831](https://arxiv.org/abs/2608.17831)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (61.2), molecular_clouds (60.6), turbulence (47.0)
- **Current keyword baseline:** NO
- **BM25 max:** 32.4
- **Semantic max:** 75.8
- **Abstract:** The Roman Space Telescope Coronagraph Instrument (Roman CGI) will demonstrate high-contrast imaging from space using coronagraphic masks, deformable mirrors, and high-order wavefront sensing and control (HOWFSC). After the baseline technology demonstration, the Roman Coronagraph Community Participation Program (CPP) will pursue science and engineering studies that require realistic predictions of instrument behaviour, observing efficiency, and wavefront control performance. This paper describes \texttt{corgihowfsc}, a configurable simulation framework for repeatable Roman CGI HOWFSC studies. The framework preserves the Roman ground-in-the-loop (GITL) workflow represented by the NASA \texttt{cgi-howfsc} package, while allowing the images to be generated by the higher-fidelity \texttt{corgisim} model. In this configuration, \texttt{cgi-howfsc} remains the reference implementation for estimation, control, and compact-model Jacobian generation; \texttt{corgisim} can supply more flight-like images for studies of instrument performance and robustness. \texttt{corgihowfsc} also coordinates exposure planning, camera settings, expected iteration timing, and contrast normalisation of the HOWFSC loop through \texttt{cgi-eetc}, calibration-related workflows through \texttt{cgi-coralign}, structured diagnostics, and local or distributed execution. By exposing observing modes, image models, probe choices, estimators, controllers, deformable-mirror settings, and runtime options through reusable configuration files, \texttt{corgihowfsc} enables controlled comparisons between reference compact-model simulations and higher-fidelity HOWFSC studies.

### [B] 61.2 — Energy Partitioning in Dust-catalyzed $\mathrm{H_2}$ and HD Formation Revealed by Molecular Simulations Considering Nuclear Quantum Effects
- **arXiv:** [2608.13843](https://arxiv.org/abs/2608.13843)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** molecular_clouds (61.2), astrochemistry (59.7), turbulence (59.0)
- **Current keyword baseline:** YES
- **BM25 max:** 66.1
- **Semantic max:** 76.4
- **Abstract:** Molecular hydrogen formation on interstellar dust grains is a key surface process in the interstellar medium, but the redistribution of the recombination energy between the substrate and the nascent molecule remains poorly understood. Here, we use ring-polymer molecular dynamics (RPMD) with a machine-learning force field to investigate energy partitioning during $\mathrm{H_2}$ and $\mathrm{HD}$ formation on graphene at $T=25, 50$ and $100 \mathrm{K}$. We focus on the chemisorbed-H recombination pathway previously identified as the dominant low-temperature channel on bare graphitic surfaces when nuclear quantum effects are included. The desorbing molecule retains the major fraction of the effective surface-mediated released energy, while graphene absorbs a smaller but non-negligible part. This molecular retention fraction is nearly temperature-independent over the investigated range. In contrast, the post-formation molecular kinetic-energy distribution changes more strongly with temperature: rovibrational motion dominates at low temperature, whereas center-of-mass translation becomes increasingly important at $100 \mathrm{K}$. $\mathrm{H_2}$ and $\mathrm{HD}$ exhibit broadly similar total energy retention, with only modest isotope-dependent differences in their internal kinetic-energy partitioning. These results provide an energy-resolved microscopic picture of surface-mediated energy redistribution in $\mathrm{H_2}$/$\mathrm{HD}$ formation, with implications for formation-pumping signatures in high-excitation $\mathrm{H_2}$ lines, vibrationally excited $\mathrm{H_2}$ chemistry, and collisional excitation of coexisting molecules by translationally hot nascent $\mathrm{H_2}$ in cold interstellar gas.

### [B] 61.2 — SNIFFLES I: Intended Emission, Unwanted Emission, and Unintended Radiation from Low-Earth Orbiting Satellites Impacting Radio Astronomy from 1-26 GHz
- **arXiv:** [2608.12999](https://arxiv.org/abs/2608.12999)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (61.2), star_formation (53.6), molecular_clouds (49.7)
- **Current keyword baseline:** NO
- **BM25 max:** 48.8
- **Semantic max:** 69.4
- **Abstract:** We present the first results of SNIFFLES, an ongoing observational programme to characterise intended emission, unwanted emission, and unintended radiation from NGSO systems across common radio astronomy receiver bands from 1-26 GHz (L, S, C, X, and K bands). Using the Australian 22 metre Mopra radio telescope near Coonabarabran, New South Wales, with followup observations from a single dish of the ATCA interferometer and its new BIGCAT backend, we conducted 4629 tracked observations of satellites from four NGSO constellations (Starlink, OneWeb, Amazon Leo, and Guowang), amounting to 375.9 hours of telescope time. Satellite identification was confirmed by correlating detected Doppler shifts with predicted ephemerides. We detected 2345 instances of intended emission, unwanted emission, and unintended radiation at 300+ unique frequencies from three of the four systems. The detections span all three interference classes affecting radio astronomy: (1) intended emission (including DTD), (2) unwanted emission (OOBE, including up to the fourth harmonic of the Starlink DTD signal at approximately 2.6 GHz, with the fourth harmonic detected near 10.5 GHz), and (3) unintended radiation from satellite platform electronics. Several detections fall within primary radio astronomy allocations, including 1613.19 MHz within the protected OH line band, and at 2690.76 MHz and 2700 MHz. At 2700 MHz, unintended radiation was detected in 76.9 percent of all observations of the relevant satellite version. ATCA followup measurements confirm flux densities up to eleven orders of magnitude brighter than typical astronomical sources, well in excess of levels that saturate radio astronomy receivers.

### [B] 61.1 — Gravitational-wave parameter estimation with machine-learning generated surrogate waveforms
- **arXiv:** [2608.20222](https://arxiv.org/abs/2608.20222)
- **Primary category:** gr-qc
- **Categories:** gr-qc, astro-ph.IM, cs.LG
- **Top topics:** ism_methods_data (61.1), turbulence (52.8), magnetic_fields (48.0)
- **Current keyword baseline:** NO
- **BM25 max:** 39.2
- **Semantic max:** 69.2
- **Abstract:** The worldwide network of gravitational-wave detectors have detected more than 350 binary coalescence events till date. Future third-generation detectors, like Einstein telescope, are expected to detect orders-of-magnitude more signals from sources with more complicated characteristics, including eccentric orbits and high-mass ratio binaries. It is well-established that the computational cost of parameter estimation for signals from these kinds of sources will be extremely high. In particular, the process could be sped-up if generating theoretical waveform predictions, used for likelihood calculation becomes faster. Recently, various machine-learning techniques has been proposed to this end. In this work, we propose a two-stage deterministic conditional-autoencoder model for generating four-parameter SEOBNRv4 waveforms. The first-stage of the model generates amplitude and phase series of the waveform, while the second-stage calibrates the residual error in the predictions. Our model achieves a median mismatch of around $10^{-2}$ with the target polarization waveforms, while the calibrated amplitude/phase series achieve $10^{-6}$ level cosine distance error. We then propose a waveform conditioning step to enable use of these surrogate waveforms for downstream parameter estimation tasks. Finally, we perform extensive parameter estimation tests, with ML and EOB waveform injections and try to recover posterior estimates for the source parameters. We find that when ML waveforms are used to recover EOB target parameter estimates, the inferred posterior have some systematic bias. This inherent bias can be estimated and corrected for, and then importance reweighting of posterior samples can enable use of low-accuracy surrogate waveforms at low SNRs.

### [B] 61.1 — The H$α$ specific angular momentum of dwarf galaxies
- **arXiv:** [2608.16089](https://arxiv.org/abs/2608.16089)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (61.1), star_formation (59.8), galactic_ism_surveys (58.8)
- **Current keyword baseline:** NO
- **BM25 max:** 46.9
- **Semantic max:** 76.3
- **Abstract:** The relationship between a galaxy's specific angular momentum $j$ and its mass $M$, parameterised by $j \propto M^α$ and known as the Fall relation, has emerged as a fundamental scaling relation reflecting key physical and morphological properties of galaxies. This relation has been well studied for galaxies with masses above $10^{9}$ $M_{\odot}$. However, whether or not it holds for the low-mass dwarf galaxies, especially given their varied morphologies, remains uncertain. Here we use H$α$ observations of 49 star-forming dwarf galaxies from the SH$α$DE survey, as well as 20 high-mass `control' galaxies, to investigate the stellar $j_{*}$-$M_{*}$ relation down to masses below $10^{6}$ M$_{\odot}$. We find that the star-forming dwarf galaxies follow the same $j_{*}$-$M_{*}$ relation as high-mass disk-like galaxies, with $α= 0.53 \pm{0.4}$, demonstrating that the relation holds across 5 orders of magnitude in mass. We then select a matching sample from the IllustrisTNG cosmological simulation and create mock observations resembling the SH$α$DE survey. We find that the simulated dwarf galaxy population follows the extrapolated $j_{*}$-$M_{*}$ relation with a flattening and significant scatter towards lower $j_{*}$ values. Following the evolution of these galaxies, we find that dwarf galaxies experience a gradual loss in $j_{*}$ with time, while high-mass galaxies experience a sudden jump in $j_{*}$ before settling into a stable state. This dynamical evolution leads to a redshift dependence in $α$, with $α= 0.45$ at $z = 2$ and 0.55 at $z = 0$. Despite the apparent simplicity in the present-day $j_{*}$-$M_{*}$ relation over a wide mass range, the evolution of $j$ leading to this relation is complex and dynamic.

### [B] 61.1 — An open-source data processing pipeline for Keck / NIRC2-Polarimetry
- **arXiv:** [2608.14864](https://arxiv.org/abs/2608.14864)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** magnetic_fields (61.1), ism_methods_data (54.0), molecular_clouds (52.2)
- **Current keyword baseline:** NO
- **BM25 max:** 41.6
- **Semantic max:** 69.3
- **Abstract:** The Keck/NIRC2 infrared imager was recently upgraded with a new suite of polarimetric observing modes. This polarimetry upgrade (referred to as NIRC2-Pol) will open up a wide range of new astronomical studies, including investigations of exoplanets, the Galactic center, active galactic nuclei and the solar system. Astronomical polarimeters require sophisticated data reduction, especially for quantitative polarimetry requiring the use of a Mueller Matrix model for instrumental polarization calibration. This work presents the design of a flexible, user-friendly, open-source data processing pipeline intended for use with NIRC2-Pol, summarizing its key steps and details of its ongoing implementation.

### [B] 61.1 — The Evolution of the ACIS Contamination Layer on the Chandra X-ray Observatory from 2010 to 2026
- **arXiv:** [2608.14363](https://arxiv.org/abs/2608.14363)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.IM
- **Top topics:** star_formation (61.1), feedback_bubbles (55.7), astrochemistry (54.0)
- **Current keyword baseline:** NO
- **BM25 max:** 38.7
- **Semantic max:** 76.4
- **Abstract:** The Chandra X-ray Observatory (CXO) was launched over 27 years ago and has been delivering spectacular science over the course of its mission. The Advanced CCD Imaging Spectrometer (ACIS) is the prime instrument on the satellite, conducting over 90% of the observations. The CCDs operate at a temperature of $-$120$^\circ$C and the optical blocking filter (OBF) in front of the CCDs is at a temperature of approximately $-$60$^\circ$C. The surface of the OBF has accumulated a layer of contamination over the course of the mission, as it is the coldest surface exposed to the interior to the spacecraft. We have been characterizing the thickness, chemical composition, and spatial distribution of the contamination layer as a function of time over the mission. The contamination model has required several revisions over the course of the mission as the properties of the contamination layer have changed and our understanding of the layer has improved. In this paper, we evaluate the performance of the current contamination model (N0016 released in CalDB 4.12.3 on 16 December 2025) using the most recent calibration observations conducted from 2023 to 2026 by using the standard model spectrum for the supernova remnant 1E 0102.2-7219 (E0102) developed by the International Astronomical Consortium for High Energy (IACHEC), spectral data from the cluster of galaxies known as Abell 1795, and high resolution X-ray spectra of Mrk 421. This evaluation has been complicated by the decreasing observed counts at low energies, especially the O VII He$α$ line complex and the O VIII Ly$α$ line from E0102 which are no longer useful for this purpose. The analyses of the E0102, Abell 1795, and Mrk 421 data show that the current model of the contamination adequately predicts the additional absorption through mid-2026.

### [B] 61.1 — Assessing Planetary Stability and Long-Term Habitability in Nearby Stellar Binaries: 70 Oph, 36 Oph, $γ$ Leo
- **arXiv:** [2608.13243](https://arxiv.org/abs/2608.13243)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** star_formation (61.1), astrochemistry (57.4), feedback_bubbles (56.1)
- **Current keyword baseline:** NO
- **BM25 max:** 39.2
- **Semantic max:** 76.4
- **Abstract:** Binary stars are common and have the potential to host habitable planets, which may reside in more complex habitable zones as compared to planets orbiting single stars. In this work, we use numerical simulations to assess the possibility that bright, nearby stellar multiples 36 Oph, 70 Oph, and $γ$ Leo could host habitable planets. We find that for the 36 Oph A/B system and for the 70 Oph A/B system, the stars can support planets residing in permanently habitable zones with low ejection rates and moderate eccentricity oscillations. The habitable zones around the red giants in the $γ$ Leo system exhibit severe dynamical instability due to the high binary eccentricity, eliminating the habitable zones around both stars. In these two systems, we find that planets in the habitable zone with orbits coplanar to that of the binary become uninhabitable due to interactions with the binary only 1.5% - 1.8% of the time, while planets with orbits 45 degrees misaligned to the plane of the binary experience larger oscillations in orbital eccentricity and as a result become uninhabitable 4.8% - 5.4% of the time. Our results identify 36 Oph and 70 Oph as promising targets for future missions such as the Habitable Worlds Observatory and SHERA, while suggesting that the stars in $γ$ Leo are unlikely to host any habitable planets. Our methods can be applied more generally to other binary stellar systems to refine target lists for upcoming habitable planet searches.

### [B] 61.0 — Reconstructing orbits of galaxies in extreme regions (roger v2.0): an extension to intermediate mass systems
- **arXiv:** [2608.19429](https://arxiv.org/abs/2608.19429)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (61.0), ism_methods_data (60.1), molecular_clouds (59.4)
- **Current keyword baseline:** NO
- **BM25 max:** 38.8
- **Semantic max:** 76.2
- **Abstract:** In this paper, we present an updated version of the roger code, called roger v2.0, developed to perform the orbital classification of galaxies residing in and around galaxy groups and clusters. In addition to the projected phase-space coordinates, the new version incorporates the host halo mass as an additional input parameter. Although the inclusion of the halo mass leads to only modest changes in the classification, it contributes to improving the overall robustness of the method. We also extend the range of host halo masses over which roger can be applied, enabling the analysis of systems with masses down to $10^{13.5} h^{-1} M_{\odot}$. We further provide a Python implementation of the new code, which will be made publicly available. This implementation enables users to efficiently and robustly classify arbitrary galaxy samples using either version of the method. Moreover, it allows users to train a customized classifier on an alternative training set, providing the flexibility to adapt the method to different datasets and scientific applications.

### [B] 61.0 — The Production of Electron-Capture Elements in Thermonuclear Supernovae: Theory vs. Observations
- **arXiv:** [2608.13432](https://arxiv.org/abs/2608.13432)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.HE, nucl-th, physics.plasm-ph
- **Top topics:** star_formation (61.0), turbulence (57.4), ism_methods_data (52.2)
- **Current keyword baseline:** NO
- **BM25 max:** 55.3
- **Semantic max:** 65.2
- **Abstract:** Type Ia supernovae (SNe Ia) explosively destroy carbon-oxygen white dwarfs (WDs) in multiple stellar systems. They produce approximately 50% of the iron-group elements in the Universe, synthesize electron-capture (EC) elements, drive nuclear physics experiments, and underpin high-precision cosmology. To first order, the outcome is governed by nuclear physics, a property often described as stellar amnesia. Recently, this stellar amnesia has begun to be broken by the nearly universal detection of EC elements with JWST. These elements trace high-density burning, largely ruling out the currently popular helium-triggered, sub-Mch detonation models as the dominant channel. Instead, the ubiquitous presence of EC is shifting back the focus to dynamical and secular mergers, and near-Mch explosions similar to the deflagration model W7, but in which the nuclear flame undergoes a deflagration-to-detonation transition. The early deflagration phase is especially important because spherical simulations identify the central WD density, and thus the WD mass, as a key parameter governing the explosion. Here, we present detailed magneto-hydrodynamical simulations. We find that small-scale, pre-existing turbulence expected from the pre-explosion smoldering phase is essential for overcoming the fundamental challenges imposed by the intrinsic 3D physics. This turbulence systematically reduces the production of EC elements by about a factor of two, implying the need for WD central densities closer to those associated with accretion-induced collapse to a neutron star. We also demonstrate the effect of magnetic fields near the saturation field strength and highlight the need for higher-precision EC rates at low Ye.

### [B] 61.0 — The low luminosity end of Galactic HMXBs with eROSITA: Establishing a luminosity floor for accreting BeXRBs
- **arXiv:** [2608.13259](https://arxiv.org/abs/2608.13259)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** galactic_ism_surveys (61.0), star_formation (55.4), massive_star_formation (54.4)
- **Current keyword baseline:** NO
- **BM25 max:** 66.6
- **Semantic max:** 69.2
- **Abstract:** We present a first look at the Galactic population of heretofore known HMXBs as observed by SRG/eROSITA during its first four surveys. eROSITA's sensitivity of $\sim10^{-13}\,\mathrm{erg}\,\mathrm{s}^{-1}\,\mathrm{cm}^{-2}$, translating to $10^{32}$-$10^{34},\mathrm{erg}\,\mathrm{s}^{-1}$ in luminosity for most known HMXBs in the Milky Way, has thus far never been reached by any wide-area survey instrument. We present the extended log N-log L distribution of known HMXBs reaching down to $10^{32}\,\mathrm{erg}\,\mathrm{s}^{-1}$ using eROSITA, and show the large scatter that can be induced by source intrinsic variability. We present sub-type resolved luminosity distributions, showing that the Supergiant X-ray binaries (SgXBs) and Be X-ray binaries (BeXRBs) occupy different parts of the overall distribution, and reanalyse RXTE/ASM data and MAXI for comparison to eROSITA. The luminosity regime uncovered by eROSITA allows a systematic study of the "transient" BeXRBs, which are typically below the detection threshold of monitors outside of outburst, and whose low luminosity behavior has been a longstanding question. Signatures of stable accretion at low luminosities have been observed with pointed instruments for a fraction of the overall sample, so far. With the eROSITA results, we posit that accretion outside of outburst is likely the norm, since a vast majority (> 80%) of BeXRBs are detected at luminosities at least an order of magnitude higher than expected for the most X-ray luminous Be stars. We discuss the observed luminosity in the context of cold disk accretion and the "propeller" mechanism. We highlight a small subpopulation of "isolated" Be-stars that reach luminosities comparable to the least luminous BeXRBs, hinting at the presence of compact object companions.

### [B] 61.0 — Optical concept model of the future cosmology project BISOU
- **arXiv:** [2608.13257](https://arxiv.org/abs/2608.13257)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.CO
- **Top topics:** ism_methods_data (61.0), astrochemistry (54.7), molecular_clouds (45.9)
- **Current keyword baseline:** NO
- **BM25 max:** 50.6
- **Semantic max:** 69.2
- **Abstract:** We present an optical analysis of BISOU (Balloon Interferometer for Spectral Observations of the primordial Universe), an astronomical balloon-borne pathfinder spectrometer developed as part of a preparatory study for a future space mission aiming at measuring spectral distortions of the cosmic microwave background (CMB). The BISOU optical system is based on a differential polarizing Fourier Transform Spectrometer (FTS) that receives inputs from both a sky-facing telescope and an internal calibration source. The FTS focal planes are equipped with bolometric detectors coupled to multimode feed horns, with distinct focal planes dedicated to the low (90 - 300GHz) and high (0.3 - 1.5THz) frequency bands. The optical analysis first relies on ray-tracing simulations to establish the overall configuration of the system, before proceeding to more advanced Gaussian beam and physical optics analyses.

### [B] 60.8 — How X-rays heat the IGM in different 21-cm simulation codes: a comparison between Licorice and Beorn
- **arXiv:** [2608.14423](https://arxiv.org/abs/2608.14423)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (60.8), atomic_ism (54.3), feedback_bubbles (52.7)
- **Current keyword baseline:** NO
- **BM25 max:** 62.2
- **Semantic max:** 68.9
- **Abstract:** Any interpretation of the 21-cm signal of neutral hydrogen using Bayesian inference methods can only be as accurate as the underlying simulation code used to model the state of the intergalactic medium (IGM). 3D radiative transfer (RT) simulation codes may capture complex physics, but are computationally expensive and, therefore, faster, more approximate codes have been developed. To improve our understanding of the convergence of simulation codes in the 21-cm science community, we present a comparison of the X-ray heating of the IGM modelled in Licorice, a 3D RT simulation code, and Beorn, a 1D RT code. We use Beorn to process sources extracted from Licorice simulations, using the same physics of the sources, in order to obtain two versions of the temperature of the IGM heated by X-rays. We observe a good agreement between the luminosity fields, mean temperatures, and global 21-cm signal of the two setups, but discrepancies in the distribution of temperature and 21-cm signal, which result in a $\sim 30\%$ difference in the 21-cm power spectrum. We attempt to isolate the approximations that lead to these differences and find that common approximations used in 1D RT codes produce effects of that magnitude. Using an emulator of the Licorice power spectra in an MCMC pipeline, we translate these differences between power spectra into differences between posterior distributions over the astrophysical parameters. We observe a typical bias between 1D posteriors of $\gtrsim 1 σ$ (with a noise level corresponding to 100h of SKA observations).

### [B] 60.7 — Giant exoplanets are not fully mixed
- **arXiv:** [2608.15717](https://arxiv.org/abs/2608.15717)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** astrochemistry (60.7), feedback_bubbles (52.0), massive_star_formation (45.4)
- **Current keyword baseline:** NO
- **BM25 max:** 39.3
- **Semantic max:** 75.9
- **Abstract:** The interior structure and bulk composition of giant planets are not directly observable and must be inferred from models. Under the common assumption of a well-mixed, adiabatic envelope, the measured atmospheric metallicity is taken as a proxy for the metallicity of the entire envelope, and hence for the planet's heavy-element budget. JWST now provides precise atmospheric metallicities for a growing number of warm giants, allowing this assumption to be tested for the first time. We quantify the difference between envelope and bulk metallicities of warm giants to assess the evidence for compositional stratification. We assembled eleven warm giants with atmospheric metallicities from published JWST retrievals, computed tailored interior and thermal evolution model grids for each, and performed MCMC retrievals to infer the bulk metallicity consistent with the measured mass, radius, system age, and atmospheric metallicity. Envelope metallicities are smaller than bulk metallicities throughout the sample, with mixing ratios from about 0.02 to 0.90. Eight of the eleven planets have mixing ratios below 0.50, and ten are inconsistent with a fully mixed interior to within one sigma. We tentatively identify a significant anti-correlation between planetary mass and envelope metallicity, but no correlation between envelope and bulk metallicity, nor between envelope and host-star metallicity. Atmospheric metallicity is therefore not a reliable proxy for the bulk composition of warm giants, and incomplete mixing (possibly composition gradients) appears common among the planets accessible to JWST. Bulk composition estimates assuming a homogeneous envelope substantially underestimate the total heavy-element mass. That the solar-system giants are unremarkable within this sample suggests dilute or partially mixed interiors may be a generic outcome of giant planet formation.

### [B] 60.6 — Don't Cut Corners: How Training Outside the Prior Makes Simulation-Based Inference More Robust
- **arXiv:** [2608.12470](https://arxiv.org/abs/2608.12470)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, stat.ML
- **Top topics:** ism_methods_data (60.6), turbulence (54.3), star_formation (53.1)
- **Current keyword baseline:** NO
- **BM25 max:** 30.5
- **Semantic max:** 75.8
- **Abstract:** Large astrophysical simulation campaigns often generate training data by sampling parameters across a Uniform prior box. Due to the proposal's sharp edge, neural posterior estimators struggle to learn accurate approximations near the boundaries. We propose Tailed-Uniform, a family of hybrid proposal distributions for sampling training simulations for robust simulation-based inference. By padding the original hard-truncated training box with decaying tails, Tailed-Uniform-trained networks yield more accurate posteriors near and beyond the edges. We demonstrate these improvements on a family of tail shapes, including a widened Uniform box as a control. Our results suggest that additional simulations near the prior boundary better constrain the networks as it approaches the edge of the training box, even for Uniform assumed priors. We show these advantages on a toy problem and cosmological parameter inference from the matter power spectrum. These benefits increase in high dimensions, where boundaries dominate parameter space volume.

### [B] 60.5 — Complex Energy-Dependent Behaviour of Quasi-Periodic Oscillation Observed in GRS 1915+105
- **arXiv:** [2608.13068](https://arxiv.org/abs/2608.13068)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** turbulence (60.5), star_formation (56.4), molecular_clouds (53.6)
- **Current keyword baseline:** NO
- **BM25 max:** 42.7
- **Semantic max:** 75.7
- **Abstract:** We present complex energy-resolved properties of quasi-periodic oscillations (QPOs) in the black hole X-ray binary GRS 1915+105 using an observation from the LAXPC instrument onboard AstroSat. Power density spectra (PDSs) are constructed in multiple energy bands and modeled with multi-Lorentzian components to investigate the energy dependence of QPO properties. The QPO frequency shows a modest increase with energy. Dynamic PDS analysis does not reveal clear evidence for time-dependent evolution of the QPO frequency, suggesting that the observed frequency shift is not primarily driven by temporal variability. We perform simultaneous fitting of energy-resolved PDSs and find that a model in which the QPO feature is described by two Lorentzian components provides a better fit. The two components exhibit different evolution in fractional root mean square amplitude as a function of energy. We further examine the phase-lag properties by simultaneously modeling the PDS and the real and imaginary parts of the cross-spectrum and find distinct phase-lag behavior for the two components. Overall, these results indicate that the apparent energy-dependent evolution of the QPO feature may be a result of the presence of more than one variability component.

### [B] 60.0 — General relativistic hydrodynamics of stellar tidal disruptions in Kerr spacetime: methods, validation, and first applications
- **arXiv:** [2608.16986](https://arxiv.org/abs/2608.16986)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (60.0), star_formation (57.0), turbulence (53.2)
- **Current keyword baseline:** NO
- **BM25 max:** 41.4
- **Semantic max:** 75.0
- **Abstract:** The disruption of a star by the tidal field of a super-massive black hole may provide insights into dormant and otherwise hard-to-study galactic nuclei. State-of-the-art numerical tools have not converged on the importance of the strong relativistic effects in the disruption of stars by potentially spinning black holes. We present a specialised numerical tool to perform global hydrodynamic simulations of stellar tidal disruptions in curved spacetimes. We quantify the role of impact strength and black hole spin onto the stellar structures and mass fallback rates. We adapted the code SPHINCS_BSSN to perform General Relativistic Smoothed-Particle Hydrodynamics (GRSPH) simulations of stellar tidal disruptions in Kerr metric. We coupled the code with a Newtonian self-gravity module, and we added the option to use an entropy evolution formulation to handle numerically challenging situations. Besides describing the implementation and code validation, we present a set of 18 simulations of parabolic tidal disruptions of stellar polytropes to investigate the effect of impact strength and black hole spin. We demonstrate that SPHINCS is capable of performing GRSPH simulations, reproducing benchmark tests to machine precision. Our stellar tidal disruption simulations show that the fallback rates agree with state-of-the-art modelling. Deep events result into structures where self-gravity plays no role, the mass fallback rates peak at lower values, and rise-to-peak timescales decrease with impact strength. In these cases the black hole spin affects noticeable these quantities increasing (decrease) both fallback rate peak and rise-to-peak timescale for prograde (retrograde) spin. Last, fallback rates tend to decay with the characteristic $t^{-5/3}$ on long timescales. The results show that SPHINCS can simulate high-resolution stellar tidal disruptions in Kerr metric at a reasonable computational time.

### [C] 59.9 — Observational Manifestations of Primordial Objects in the Early Universe Through the Hydrogen Subordinate Lines
- **arXiv:** [2608.15481](https://arxiv.org/abs/2608.15481)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** massive_star_formation (59.9), star_formation (57.7), feedback_bubbles (55.4)
- **Current keyword baseline:** NO
- **BM25 max:** 57.4
- **Semantic max:** 74.9
- **Abstract:** A new mechanism for the formation of spectral--spatial distortions in cosmic microwave background radiation near primordial massive compact objects (such as primordial black holes) at redshifts from $z \sim 1000$ to $\sim$100 is proposed. After hydrogen recombination, the radiation from these objects leads to a significant increase in the population of hydrogen subordinate levels in their surrounding environment. Consequently, this allows for the observation of a Fraunhofer-like absorption spectrum in the cosmic microwave background. Such a distortion is formed due to the temperature difference between matter and relic radiation at the corresponding epoch. Ultimately, we should observe circular absorption or emission features around the objects with small angular sizes. These subordinate hydrogen lines currently lie in the radio wavelength range. Estimates indicate that the effect under consideration is accessible for the observations with planned large radiotelescopes. The possibility of the proposed mechanism lies in the ability of an object (e.g., accretion disk around black hole) to emit few-eV photons that populate the $n=2,3,4$ and higher levels of hydrogen, enabling the required excitation.

### [C] 59.9 — XRISM reveals sloshing-driven gas motions in the core of Abell 2029
- **arXiv:** [2608.14415](https://arxiv.org/abs/2608.14415)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** star_formation (59.9), turbulence (59.6), galactic_ism_surveys (58.9)
- **Current keyword baseline:** YES
- **BM25 max:** 83.6
- **Semantic max:** 74.8
- **Abstract:** We investigate the velocity structure of the intracluster medium (ICM) in the core of the relaxed cool-core cluster Abell 2029 using XRISM Resolve spectroscopy. We analyze combined XRISM Resolve observations and divide the central region into several subregions. To account for photon mixing caused by the XRISM point spread function, we perform a spatial-spectral mixing analysis. We detect an ordered line-of-sight bulk-velocity gradient across the cluster core: the northern regions are blueshifted relative to the brightest cluster galaxy (BCG), while the southern regions are close to zero velocity or slightly redshifted. The maximum velocity difference is about $280~{\rm km\,s^{-1}}$. In contrast, the turbulent velocity dispersion is smaller, with measured values and upper limits of $\lesssim150~{\rm km\,s^{-1}}$, implying a non-thermal pressure fraction below $\sim2.5\%$. The velocity pattern is consistent with gas sloshing associated with the spiral structure seen in Chandra X-ray images. Averaged over all regions, the inferred turbulent heating rate is below the radiative cooling rate, indicating that turbulent dissipation alone is insufficient to offset cooling in the entire core. These results reveal that A2029 is not kinematically featureless: sloshing-induced bulk motions are present, while the observed line-of-sight velocity dispersion indicates only a limited contribution to pressure support and core heating.

### [C] 59.8 — The UKIRT M33 Monitoring Project: A 15-Year Near-Infrared Variable Star Catalogue for the Central Kiloparsec, and Prospects for Star Formation History and Dust Return
- **arXiv:** [2608.19657](https://arxiv.org/abs/2608.19657)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (59.8), star_formation (59.2), astrochemistry (56.9)
- **Current keyword baseline:** NO
- **BM25 max:** 100.0
- **Semantic max:** 74.8
- **Abstract:** We present results from the UKIRT M33 Monitoring Project, a near-infrared survey of variable red giants in the Local Group spiral galaxy M33. Combining four independent photometric datasets spanning UIST (2003), UFTI (2005), WFCAM (2005-2007), and a new UKIRT Hemisphere Survey epoch (2018), we construct a homogenised 15.11-year $K$-band light-curve catalogue for 847 stars in the central kiloparsec, of which 771 (91 per cent) are variable. Cross-matching with archival Spitzer photometry identifies 120 dust-enshrouded AGB candidates. We compare the spatial coverage of this central catalogue with the earlier UIST-only (Paper I) and disc-wide WFCAM (Paper IV) variable-star surveys. Building on this catalogue, two forthcoming papers will (i) measure individual pulsation periods to reconstruct the star formation history of the central kiloparsec, and (ii) refine dust and gas mass-loss rates across the disc using the extended time baseline.

### [C] 59.8 — How mergers shape galaxy morphology in the IllustrisTNG simulation
- **arXiv:** [2608.13996](https://arxiv.org/abs/2608.13996)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** galactic_ism_surveys (59.8), star_formation (57.8), feedback_bubbles (52.5)
- **Current keyword baseline:** NO
- **BM25 max:** 52.3
- **Semantic max:** 74.7
- **Abstract:** How galaxy mergers drive morphological evolution remains an open question. Traditional views hold that major mergers produce elliptical galaxies, while minor mergers form dispersion-dominated components such as galactic bulges. However, more recent work has challenged this simple picture, suggesting a more complex evolutionary scenario. In this study, we use the IllustrisTNG cosmological simulation to investigate how mergers shape galaxy morphology, across a broad range of galaxy masses and merger mass ratios. Our results show that the post-merger galaxy morphology is primarily determined by three factors: collision angle $\overlineθ$, cold gas fraction $f_\mathrm{cold\,gas}$, and pre-merger galaxy morphology $\mathrm{(B/T)_{*,pre}}$. Specifically, spiral-in mergers with large $\overlineθ$ increase the rotational support of the system, allowing the gas to settle into an extended disk. When the system is rich in cold gas, star formation within the newly formed gas disk can further strengthen the disk-dominated structure of the remnant. On the other hand, head-on mergers with small $\overlineθ$ typically disrupt ordered galactic motion, producing more dispersion-supported remnants. Overall, we interpret our results within a unified picture of merger-driven morphological transformation in galaxies.

### [C] 59.6 — A Statistical Mechanics Model for Stable Rings Outside the Roche Limit
- **arXiv:** [2608.17004](https://arxiv.org/abs/2608.17004)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** star_formation (59.6), turbulence (59.2), molecular_clouds (54.1)
- **Current keyword baseline:** NO
- **BM25 max:** 42.5
- **Semantic max:** 74.4
- **Abstract:** Stellar occultations have revealed two rings around the dwarf planet Quaoar outside the Roche limit. Simulations suggest that the rings are sustained by large velocity dispersions. We present the first analytical, first-principles theory that extends the Roche limit to describe planetary rings with large velocity dispersion. The underlying principle is an analogy between a liquid/gas phase transition and the moon/ring transition: just as high temperatures can boil a liquid under pressure, high velocity dispersions can stabilize ring systems beyond the Roche limit. We employ statistical mechanics to derive a modification to the Roche limit that treats rings with nonzero velocity dispersion. We demonstrate the new model's consistency with previous simulations of Quaoar's outermost ring. We also note that dense regions of the ring experience negative pressure, which would cause them to shrink over time if the assumptions of the model continue to hold. This could help explain the rings' azimuthal asymmetry.

### [C] 59.5 — Triggered Fragmentation in Self-Gravitating Protoplanetary discs: Cooling, Mass Movement and Instability
- **arXiv:** [2608.17857](https://arxiv.org/abs/2608.17857)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** feedback_bubbles (59.5), molecular_clouds (53.0), star_formation (51.0)
- **Current keyword baseline:** NO
- **BM25 max:** 57.2
- **Semantic max:** 74.4
- **Abstract:** Previous three-dimensional hydrodynamical simulations of gravitationally unstable discs have shown that the formation of a single fragment can trigger the formation of subsequent fragments. This behaviour was attributed to changes in the surface mass density caused by the interaction between the first fragment and the disc material. This study reanalyses those simulations to see if the surface mass density was the sole driver. Our results reveal that both surface mass density and sound speed can contribute to the formation of additional fragments. Beyond the general cooling typical of such discs, the inwards movement of cool material from the outer disc, driven by the formation of the first fragment, can enhance fragmentation in the inner regions. We also identify that interactions between the midplane gas and the cooler upper layers of the disc can facilitate additional cooling. Triggered fragmentation can create a unique planet-formation environment by redistributing material across the disc, potentially leading to chemically distinct fragments from those formed in-situ.

### [C] 59.4 — Effects of Pebble Accretion Isolation Mass on Observable Exoplanet Properties
- **arXiv:** [2608.13639](https://arxiv.org/abs/2608.13639)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** feedback_bubbles (59.4), star_formation (56.9), magnetic_fields (52.5)
- **Current keyword baseline:** NO
- **BM25 max:** 43.2
- **Semantic max:** 67.2
- **Abstract:** The Kepler Mission has discovered a plethora of planetary systems with super-Earth sized planets. These systems exhibit many properties, from widely-spaced planets with non-negligible eccentricities and inclinations, to tightly-spaced, coplanar, and nearly circular multi-planet systems. The observable properties of these systems, such as planet-planet spacings, multiplicity and orbital morphology, can be strongly influenced by the initial conditions of formation. These conditions affect the early growth of planetary embryos in the gas disk phase through pebble and/or planetesimal accretion, which then affects the final growth of planets during the giant impact stage. In this work, we investigate how assumptions of different limiting embryo isolation masses during early stages of planet formation affect the final properties of super-Earth planets within the inner disk, comparing our mock-observed results to each other, as well as to the Kepler sample. We test several models of pebble accretion isolation mass, including pebble isolation, flow isolation, and migration feedback isolation and otherwise adopt the same parameters for the gas disk. We find that while each model can match at least one distribution of observables in the Kepler catalog, they fall short of matching all distributions simultaneously, even with extreme reweighting. Our inability to match all observations suggests that the initial conditions and/or modeled effects in our simulations that we held fixed should be investigated. This exploration sheds light on how planetary systems evolve and the processes that influence the wide range of system parameters we observe today, helping place our own Solar System in context.

### [C] 59.2 — Finding Habitable Exoplanets with Binary Relative Astrometry: Planet Detection and Characterization with the Microarcsecond Astrometric Retrieval Algorithm (MARA)
- **arXiv:** [2608.19444](https://arxiv.org/abs/2608.19444)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.IM
- **Top topics:** astrochemistry (59.2), ism_methods_data (59.1), star_formation (50.7)
- **Current keyword baseline:** NO
- **BM25 max:** 43.8
- **Semantic max:** 74.0
- **Abstract:** Binary relative astrometry is a technique to search for rocky planets in the habitable zone of nearby binary stars using 1D relative astrometry at the microarcsecond level. This unprecedented precision would allow a custom-designed space telescope to directly measure the occurrence rate of these planets. The success of such a mission depends on our ability to recover and characterize planets from the unique format of extreme precision binary relative astrometry data. We present MARA, the Microarcsecond Astrometric Retrieval Algorithm, specifically designed for these data. We describe the design and format of the MARA pipeline, and demonstrate its accuracy and performance with a series of validation tests on simulated data, using the SHERA SMEx mission concept as an example. Our injection/recovery tests show that with these data, MARA is able to detect and characterize rocky planets in the habitable zone of alpha Cen A, down to a coplanar mass of about 1 Earth mass in 1 year orbits. Expanding to a range of input planet masses and periods for the same example mission, we find that the results from these injection/recovery tests generally agree with the analytic predictions of binary relative astrometry sensitivity. We use MARA to map out the expected completeness as a function of planet mass and period, which in this case reaches down to about 0.5 M Earth masses at 3 year orbits around alpha Cen A. These depth-of-search calculations will be a vital ingredient in demographics calculations from the final data from a binary relative astrometry mission.

### [C] 59.2 — Stellar Abundances as Probes of Rocky Exoplanet Interiors: The Mantle Composition and Mineralogy of GJ 486b
- **arXiv:** [2608.18457](https://arxiv.org/abs/2608.18457)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** astrochemistry (59.2), ism_methods_data (58.5), feedback_bubbles (57.1)
- **Current keyword baseline:** YES
- **BM25 max:** 47.9
- **Semantic max:** 74.0
- **Abstract:** Over the past three decades, hundreds of rocky exoplanets have been discovered. Some of these show atmospheric signatures indicative of diverse chemical compositions. Interpreting these atmospheres requires a physically grounded understanding of planetary interiors, as interior composition and mineralogy govern the formation and evolution of secondary atmospheres. Rocky terrestrial exoplanets are expected to inherit the refractory composition of their host stars, providing a direct pathway to constrain their bulk composition and mineralogy. However, a large fraction of these planets orbit M-type stars, whose compositions remain poorly constrained because of limited and uncertain stellar abundance measurements. Here, we present a physically consistent framework that connects stellar abundances to the interior structure and mineralogy of rocky exoplanets by combining stellar abundance inference, devolatilization modeling to estimate bulk and mantle elemental abundances, interior structure calculations to derive pressure-temperature profiles, and thermodynamic equilibrium modeling of mantle mineralogy. We first benchmark the framework against Earth and then apply it to the super-Earth GJ 486b using chemically consistent abundances derived from ensembles of similar M-dwarf hosts. We find that GJ 486b likely hosts an iron-rich and silica-poor mantle relative to Earth while preserving the major mantle phase transitions. Sensitivity analyses show that the overall mineralogical structure is robust to variations in bulk composition and pressure-temperature profiles, with temperature primarily modulating phase proportions near key transitions. Finally, our results show that stellar-abundance inference combined with devolatilization models constrains the interior composition of rocky exoplanets and provides a foundation for linking planetary interiors to atmospheric characterization.

### [C] 58.9 — Informing spectral models for dense plasmas with K-edge absorption measurements of warm dense copper
- **arXiv:** [2608.19382](https://arxiv.org/abs/2608.19382)
- **Primary category:** physics.plasm-ph
- **Categories:** physics.plasm-ph, astro-ph.HE
- **Top topics:** molecular_clouds (58.9), massive_star_formation (55.0), ism_methods_data (49.0)
- **Current keyword baseline:** NO
- **BM25 max:** 85.5
- **Semantic max:** 73.6
- **Abstract:** Warm dense matter remains a challenging regime to characterize experimentally and to model with predictive accuracy. Recent experimental platforms have been developed to generate, characterize, and diagnose uniform warm dense matter, enabling detailed comparisons with models. Here, we present experiments conducted at the OMEGA laser facility that compress and heat a buried layer target to warm dense matter conditions, where the targets are heated to temperatures of approximately 20 eV and compressed to densities of 25 g/cm^3. We probe the warm dense plasma using x-ray absorption spectroscopy, using the K-edge and bound-bound absorption features to constrain the temperature and charge state distribution of the plasma. We compare these measurements with two types of models: collisional-radiative models with detailed electronic structure and ad-hoc density effects, and a multi-ion model based on density functional theory in combination with excited-state projector augmented-wave potentials. Neither approach fully reproduces the observed data, We show that the broad structure and position of the K-edge region can be modeled using density functional theory in combination with excited-state projector augmented-wave potentials. The density functional theory results are contrasted with a collisional-radiative model approach that incorporates ad-hoc density effects, which show incomplete agreement with the experimental observations, highlighting a need for improved density-dependent atomic modeling in warm dense plasmas.

### [C] 58.9 — CosmoPyro: Gradients for Gravitational-Wave Cosmology
- **arXiv:** [2608.18281](https://arxiv.org/abs/2608.18281)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc, hep-ph
- **Top topics:** ism_methods_data (58.9), turbulence (58.6), star_formation (54.1)
- **Current keyword baseline:** NO
- **BM25 max:** 39.3
- **Semantic max:** 73.6
- **Abstract:** Gravitational-wave (GW) observations of stellar-mass compact binary coalescences directly measure the source luminosity distance. Combined with the source redshift, these measurements constrain the current expansion rate of the Universe, the Hubble constant, $H_0$, or $h=H_0 / [100 \,{\rm km \,s^{-1} \, Mpc^{-1}}]$. For most GW signals no electromagnetic redshift measurement is expected, but the GW signal itself depends on the redshifted (detector-frame) masses. Assuming a source-frame mass distribution therefore enables a redshift estimate for each source. Combining the redshift estimates with the distance measurements provides a weak constraint on $H_0$ for each individual source that tightens with the number of sources in the catalog. However, the shape of the source-frame mass distribution is not known a priori, and previous work has relied on parametric models (piecewise power-laws with Gaussian components), and one-dimensional Gaussian processes. Here, we introduce CosmoPyro, a fully differentiable hierarchical Bayesian inference code that models the mass distribution using either one- or two-dimensional Gaussian processes. With the latest GW transient catalog (GWTC-5) we find $h = 0.66^{+0.17}_{-0.20}$ and $h = 0.57^{+0.20}_{-0.15}$ (median with $1σ$ uncertainty), for the one- and two-dimensional case, respectively. Despite the noticeably different inferred mass distributions, both models yield $H_0$ values consistent with the latest LVK measurements within $1 σ$. While our main results marginalize over the Gaussian-process power-spectrum hyperparameters, the measurement is also robust against fixing these hyperparameters over a range comparable to their measured uncertainty.

### [C] 58.9 — Formation of heavy double neutron stars II: the role of heavy first-born neutron stars and low metallicity
- **arXiv:** [2608.17430](https://arxiv.org/abs/2608.17430)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA, astro-ph.HE
- **Top topics:** star_formation (58.9), astrochemistry (52.9), galactic_ism_surveys (47.0)
- **Current keyword baseline:** NO
- **BM25 max:** 55.1
- **Semantic max:** 66.5
- **Abstract:** The high total mass of GW190425 challenges our understanding of double neutron star (DNS) formation, as no such heavy ($\ge 3$\, M$_\odot$) DNS system has been observed in the Milky Way disk. Numerous formation scenarios have been proposed to explain its formation. We test these within a self-consistent binary evolution framework calibrated to the Galactic DNS population. In Paper~I of this series, we studied the evolution of a $1.4$\,M$_\odot$ neutron star (NS) in a binary with a $2.5$--$10$\,M$_\odot$ helium star at solar metallicity ($Z = Z_\odot$), assuming Eddington-limited accretion onto the NS using \texttt{MESA}. In this paper, we consider the evolution of NS-He star binaries with a broad range of NS masses from $1.1$--$1.9$\,M$_\odot$ at $Z=Z_\odot$, 0.1\,$Z_\odot$ and 0.01\,$Z_\odot$. We find that the formation of heavy DNSs is rare, accounting for only $\sim 0.5$ per cent of DNSs. The majority of these are formed through the `standard formation' channel, widely believed to form GW170817 and observed Galactic DNSs. We find no contribution through the `fast-merger' channel at solar metallicity, but systems at low metallicity predominantly form through unstable mass transfer. Furthermore, we find no significant dependence of the heavy DNS formation fraction on metallicity over the range considered here. We conclude that heavy DNSs do not form a separate subpopulation and merely represent the high-mass tail of the standard DNS population.

### [C] 58.8 — Constraining Cosmic-Ray Acceleration and Escape in Middle-Aged Supernova Remnants with GeV-TeV Gamma-Ray Observations
- **arXiv:** [2608.18954](https://arxiv.org/abs/2608.18954)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (58.8), galactic_ism_surveys (54.2), ism_methods_data (49.4)
- **Current keyword baseline:** NO
- **BM25 max:** 62.5
- **Semantic max:** 67.7
- **Abstract:** In this work, we perform a systematic, time-dependent study of the gamma-ray emission from four representative middle-aged SNRs (W51C, IC~443, W44, W28), incorporating both CRs within the remnant shells and escaped CRs interacting with surrounding molecular clouds. We compare our results with GeV--TeV gamma-ray observations from Fermi-LAT, H.E.S.S., MAGIC, and LHAASO, including a dedicated analysis of the Fermi-LAT data for regions A and B associated with W28. We find that the observed spectra favor steeper CR injection spectra with indices of \(α\sim4.2\)--\(4.3\), maximum proton energies of $\sim$ \(100\)--\(300\) TeV, diffusion coefficients below the Galactic average, and CR acceleration efficiencies from a few to tens of percent. In particular, the VHE emission detected by LHAASO from W51C is more naturally explained by escaped CRs interacting with a nearby molecular cloud. We also investigate the contribution of escaped CRs to the VHE emission from IC~443, W44, and W28. We further demonstrate that escaped CRs can substantially enhance the TeV neutrino flux from middle-aged SNRs, improving their prospects as potential neutrino sources. These results provide new constraints on CR acceleration and escape in middle-aged SNRs and highlight the important role of escaped CRs in shaping their high-energy gamma-ray and neutrino emission.

### [C] 58.8 — The high entropy of the UHECR arrival direction distribution favors a light composition
- **arXiv:** [2608.17801](https://arxiv.org/abs/2608.17801)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** astrochemistry (58.8), magnetic_fields (56.2), ism_methods_data (55.4)
- **Current keyword baseline:** NO
- **BM25 max:** 54.3
- **Semantic max:** 73.5
- **Abstract:** We analyze the constraints on the composition of ultra-high-energy cosmic rays (UHECRs), and on the density and distribution of their sources, that may be inferred from their arrival-direction distribution, using a novel semi-analytical description of the propagation energy loss of atomic nuclei ($A>4$) with energy $>2\times10^{19}~\text{eV}$, that allows generating UHECR arrival maps faster than by using detailed propagation simulations and yields insights to the impact of propagation energy loss. We show that the anisotropy of the UHECR arrival direction distribution due to the large-scale structure (LSS) of matter distribution is larger for heavy nuclei composition compared to protons, despite their larger deflections by magnetic fields, due to their shorter propagation distance and weaker dependence of rigidity on observed energy. Identifying the LSS anisotropy signal is hampered for heavy nuclei due to their large deflections by the uncertain Galactic magnetic field (GMF). We introduce a new measure of anisotropy, an "entropy" of the arrival-direction distribution, that is largely independent of the GMF configuration and has strong discriminating power between heavy- and light-composition models. Analyzing the public $>3.2\times10^{19}$~eV Auger data, we show that the correlation with the LSS on large angular scales is weak and requires a low source density, $s_0\le10^{-4}{\rm Mpc}^{-3}$, to allow masking the LSS signature by "cosmic-variance" ($s_0=10^{-2}{\rm Mpc}^{-3}$ is ruled out at $>99\%$ confidence level (CL)). The high entropy of the distribution is consistent with proton models and inconsistent with heavy nuclei models at $>96\%$ CL for $s_0\ge10^{-5}{\rm Mpc}^{-3}$. Reducing the absolute energy calibration uncertainty may allow detection of the LSS correlation for proton models (increased exposure alone will not suffice due to the dominance of cosmic variance).

### [C] 58.8 — Characterizing Stellar Flares in Ariel Targets: Activity Analysis and Transit Contamination
- **arXiv:** [2608.16301](https://arxiv.org/abs/2608.16301)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.EP
- **Top topics:** ism_methods_data (58.8), feedback_bubbles (53.4), astrochemistry (52.8)
- **Current keyword baseline:** NO
- **BM25 max:** 43.6
- **Semantic max:** 73.5
- **Abstract:** Stellar flares are sudden releases of magnetic energy that can distort exoplanet transit photometry and transmission spectroscopy, biasing planet radius estimates, transit timings, and atmospheric characterization. Understanding flare activity in Ariel targets is therefore essential to identify stars where flares may compromise observations and to characterize the radiation environment affecting atmospheric escape and photochemistry. We analyzed 290 Ariel target stars using TESS light curves. Flares were identified via iterative Gaussian process detrending, and their energy distributions were modeled with two-segment power laws. We performed injection-recovery tests by adding synthetic flares to detrended light curves and running the full pipeline to quantify completeness and detection biases. We detected 15,857 flares across 1,638 TESS sectors, with 2-86 events per sector. We defined a normalized flare index GF.01 to compare activity across stellar luminosities. Near 3% of the sample exhibits enhanced flare activity (GF.01 > 1). AU Mic and HD 28109 show a high likelihood of flare contamination during transit observations. GF.01 correlates negatively with stellar bolometric luminosity, indicating higher relative flare output in lower-luminosity stars. AU Mic is an extreme case: four of five observed transits of AU Mic b are affected by flares, consistent with statistical expectations. We validate the framework by comparing predicted flare-contamination probabilities with observed flare occurrences in a representative subset of transits, finding agreement within uncertainties. These results confirm that energetic flares can significantly impact transit observations and provide quantitative guidance for Ariel target selection and analysis strategies.

### [C] 58.7 — Testing Matter Diffusion with Late-Time Cosmological Observations
- **arXiv:** [2608.15950](https://arxiv.org/abs/2608.15950)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (58.7), astrochemistry (47.5), galactic_ism_surveys (45.7)
- **Current keyword baseline:** NO
- **BM25 max:** 37.4
- **Semantic max:** 73.4
- **Abstract:** We investigate a class of late-time cosmological models derived from the phenomenological framework of variable matter diffusion. In these scenarios, energy-momentum conservation requires a continuous energy exchange between matter and an effective scalar-field dark-energy component, $φ$. We consider a baseline constant-diffusion scenario alongside four non-linear power-law parametrizations, in which the diffusion coefficient evolves as a function of the scale factor, matter density, scalar-field density, or Hubble expansion rate. To assess their cosmological viability, we implement these models within \texttt{SimpleMC} and constrain them using late-time observations, including cosmic chronometers, baryon acoustic oscillation measurements, Type Ia supernovae with and without the local SH0ES calibration. In the absence of the local calibration, the diffusion models yield only modest improvements in the fit ($Δχ^2 \approx -4$), performing comparably to the CPL parametrization while exhibiting negative Bayesian log-evidence differences relative to $Λ$CDM. In contrast, including SH0ES leads to a dramatic reduction in the minimum $χ^2$ ($Δχ^2 \approx -22$) and decisive Bayesian evidence in favor of the diffusion framework ($Δ\ln\mathcal{Z} \approx 9$). Remarkably, the single-parameter constant-diffusion model accounts for virtually all the statistical improvement, outperforming the CPL parametrization by more than 10 units in $χ^2$ and more than 8 units in $Δ\ln\mathcal{Z}$. The four non-linear extensions provide only negligible additional improvements ($Δχ^2 \approx -1$), indicating that current late-time background observations favor the presence of a non-vanishing matter-diffusion interaction over $Λ$CDM, while providing no statistically significant evidence for a specific time-dependent functional form of the diffusion coefficient.

### [C] 58.6 — Asgard/NOTT: Status of laboratory nulling performance
- **arXiv:** [2608.18951](https://arxiv.org/abs/2608.18951)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** molecular_clouds (58.6), ism_methods_data (54.5), star_formation (52.6)
- **Current keyword baseline:** NO
- **BM25 max:** 34.2
- **Semantic max:** 73.2
- **Abstract:** Nulling interferometry enables the direct detection of faint companions and circumstellar structures at angular separations unresolvable by classical, diffraction-limited imagers, whilst dramatically improving the measurable contrast. The Asgard/NOTT nulling instrument aims to achieve a contrast performance of 10^-5 in the L' wavelength band (3.5 - 4.0 μm), enabling observation and characterization of young giant exoplanets near the snowline and hot exozodiacal dust. Previous studies have verified the nulling capabilities, of the chip in ambient conditions and of the test bench in cryogenic conditions. This work aims to add the first ambient performance assessment of the test bench with spectrally dispersed light. Necessary revisions are made to the data acquisition and calibration pipeline and fringe scans are carried out, modeled and fitted. The splitting ratios of the 4-telescope nulling beam combiner, a photonic Gallium Lanthanum Sulfide (GLS) chip, are moreover characterized on the bench, showing tentative agreement with previous chip characterization. The null performance has worsened, the achieved contrast of ~ 10^-1 being one order of magnitude higher than what earlier characterized performance showed. Multiple future changes to the test bed and to the approach taken promise an improved characterization of performance. In particular, the input beam intensities will be deliberately mismatched to account for the imbalanced splitting ratios of the directional couplers. With the installation of the final cryostat and camera, the developed tools will be leveraged to re-assess the performance in ambient and cryogenic conditions.

### [C] 58.6 — Population-Level Verification of the Black-Hole Area Law with First- and Second-Generation Black Holes
- **arXiv:** [2608.16563](https://arxiv.org/abs/2608.16563)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, gr-qc
- **Top topics:** feedback_bubbles (58.6), galactic_ism_surveys (52.3), star_formation (46.6)
- **Current keyword baseline:** NO
- **BM25 max:** 46.3
- **Semantic max:** 73.3
- **Abstract:** Hawking's area theorem states that the total event-horizon area of classical black holes (BHs) can never decrease. Existing gravitational-wave tests analyze single loud events (GW150914, GW230814, GW250114) and therefore certify the law only for the specific mergers observed. Here we perform the {\it first} population-level test, exploiting the recent decomposition of the GWTC-5 BBHs into a low-spin subpopulation of stellar-collapse origin and a high-spin subpopulation formed through hierarchical mergers of the former. If the high-spin BHs are merger remnants (i.e., second-generation BHs), the area law requires their horizon areas to statistically exceed the total pre-merger areas of the low-spin binaries. Using inspiral-only parameter estimation for 241 events, independent of merger-ringdown modeling, we find that both peaks in the horizon-area distribution of second-generation BHs lie above their first-generation counterparts, with probabilities of $0.9995$ ($3.3σ$) and $0.983$ ($2.1σ$), respectively. The area law thus holds statistically for the quasicircular, moderately spinning mergers that dominate current catalogs, which in turn underpins the robustness of our classification of stellar-collapse and hierarchical-merger BHs.

### [C] 58.5 — Probing the $γ$-ray emission region and the connection to jet ejections in NRAO 150 with VLBI
- **arXiv:** [2608.16981](https://arxiv.org/abs/2608.16981)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** molecular_clouds (58.5), magnetic_fields (51.1), galactic_ism_surveys (51.1)
- **Current keyword baseline:** NO
- **BM25 max:** 83.3
- **Semantic max:** 73.1
- **Abstract:** Relativistic jets launched by active galactic nuclei are fundamental for understanding the physics of accreting supermassive black holes and their immediate environments, yet the origin of these jets remains an open question. NRAO 150 is a blazar with a complex relativistic jet morphology that evolves on short timescales due to strong projection effects, enabling detailed kinematic analysis. In this study, we utilise data by the Very Long Baseline Array and the European VLBI Network from 2010 until 2019 at 43 GHz, to understand the formation and launching processes of the jet in NRAO 150. We study the $γ$-ray and radio light-curves, together with total intensity and linear polarisation information to probe the connection between flaring events, $γ$-ray emission, and the ejection of new jet features. Furthermore, we investigate the magnetic field configuration in the innermost jet region, as captured in polarised light, to gain insights about its configuration before, during, and after a $γ$-ray flare. Our results indicate a close temporal link between the $γ$-ray flaring activity and the ejection of new VLBI jet components, suggesting that the high-energy emission is produced downstream of the VLBI core. The combined kinematic and polarimetric evidence further points to a toroidal magnetic field in the inner jet, highlighting the key role of magnetic fields in governing both jet dynamics and high-energy emission in NRAO 150.

### [C] 58.5 — Forecast for the detectability of patchy hydrogen reionization in WEAVE-QSO measurements of the Lyman-$α$ forest power spectrum at redshift $z \geq 4$
- **arXiv:** [2608.13153](https://arxiv.org/abs/2608.13153)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** turbulence (58.5), galactic_ism_surveys (57.0), feedback_bubbles (55.3)
- **Current keyword baseline:** NO
- **BM25 max:** 60.3
- **Semantic max:** 71.3
- **Abstract:** We present the first detailed forecasts for the detectability of patchy hydrogen reionization in the one-dimensional Ly$α$ forest power spectrum to be measured by the WEAVE-QSO survey. Using the Sherwood-relics reionization simulations and a WEAVE-QSO survey configuration, we generate mock spectra in four redshift bins, $z=4.0,4.2,4.4,$ and $4.6$, in which relic ionization and temperature fluctuations from patchy hydrogen reionization enhance the Ly$α$ forest power spectrum on large scales (i.e., at wavenumber $k\sim 10^{-3},\mathrm{s\,km^{-1}}$). Our Ly$α$ forest pipeline forecasts the power spectrum covariance by considering sample size, spectral resolution, noise subtraction, continuum placement, metal contamination, and damping wings from high-column density absorbers. Applying our covariance forecast within a Bayesian parameter inference framework, we find that the signature of patchy hydrogen reionization should be detectable at a significance of $\simeq 4.5σ$. The forthcoming WEAVE-QSO 1D power spectrum measurements should therefore be able to directly detect and characterize the large-scale relic imprint of patchy hydrogen reionization in the Ly$α$ forest power spectrum at $z\geq 4$.

### [C] 58.4 — Halo Mass of ULIRGs at Cosmic Noon
- **arXiv:** [2608.16667](https://arxiv.org/abs/2608.16667)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (58.4), astrochemistry (50.7), massive_star_formation (48.4)
- **Current keyword baseline:** NO
- **BM25 max:** 47.7
- **Semantic max:** 73.0
- **Abstract:** We present a clustering analysis of $\sim 3000$ ultraluminous infrared galaxies (ULIRGs) at $z\sim 2$, uniformly selected by $24μ{\rm m}$ flux and IRAC colors in the COSMOS and BOOTES fields. We measure the angular correlation functions of ULIRGs in both fields and fit them with galaxy clustering models. Linear theory modeling shows that these ULIRGs reside in dark matter halos with characteristic masses of $\log M_{\rm h} /({h^{-1}\rm M_{\odot}}) = 12.64\pm 0.50$ in COSMOS and $12.72\pm 0.13$ in BOOTES. The halo occupation distribution (HOD) modeling yields occupation-weighted effective halo masses of $\log M_{\rm eff} /({h^{-1}\rm M_{\odot}}) =12.50^{+0.26}_{-0.28}$ for COSMOS and $12.89^{+0.11}_{-0.12}$ for BOOTES. These host halos are expected to evolve into halos with masses of $\sim 10^{13.6-13.9}\ {h^{-1}\rm M_{\odot}}$ at $z=0$. The HOD fits allow for a non-negligible satellite contribution to the clustering of galaxies in the BOOTES field, but the satellite fraction derived in the COSMOS field appears nearly zero.

### [C] 58.3 — SPT-3G+: A Cosmic Microwave Background Experiment for the South Pole Telescope
- **arXiv:** [2608.20236](https://arxiv.org/abs/2608.20236)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (58.3), magnetic_fields (54.7), star_formation (48.0)
- **Current keyword baseline:** NO
- **BM25 max:** 57.8
- **Semantic max:** 61.3
- **Abstract:** SPT-3G+ is the next survey receiver planned to be installed in early 2029 on the 10-meter South Pole Telescope (SPT). This new receiver will feature 6,020 polarization-sensitive dichroic pixels with transition-edge sensors observing in frequency bands centered at 90 GHz and 150 GHz. The 24,080 detectors in the SPT-3G+ receiver will be cooled to 100 mK by a dilution refrigerator and read out using microwave SQUID multiplexing. The optical design of the receiver enables a 4 degree diameter field of view, which is broken up into 14 individual optics tubes each containing cryogenic alumina, silicon, and nylon lenses. These technology choices will allow the SPT-3G+ receiver to improve on the mapping speed of the currently operating SPT-3G receiver by nearly an order of magnitude. Once deployed, the SPT-3G+ receiver will observe for 6-years an area overlapping with the BICEP survey to achieve a combined (90 GHz and 150 GHz) CMB map depth of 0.5 uK-arcmin. Data from these observations will be used to create unprecedentedly deep CMB lensing maps, discover new galaxy clusters, and detect astrophysical transients. The lensing map produced by SPT-3G+ will be used to remove or "delens" foreground B modes, where large-scale structure gravitationally lenses the CMB and converts E modes into B-mode polarization, with the goal of revealing inflationary B modes. Together with data from the BICEP Array as part of the South Pole Observatory, SPT-3G+ data will be used to constrain the tensor-to-scalar ratio $r$ with a goal of achieving a measurement of $σ(r) = 0.001$

### [C] 58.3 — The second Arcminute Microkelvin Imager - Large Array Gamma-ray burst radio afterglow catalog
- **arXiv:** [2608.13697](https://arxiv.org/abs/2608.13697)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** molecular_clouds (58.3), feedback_bubbles (53.8), turbulence (50.3)
- **Current keyword baseline:** NO
- **BM25 max:** 32.6
- **Semantic max:** 72.9
- **Abstract:** Radio observations of gamma-ray burst afterglows provide insight in to the different emitting regions within the jet, its hydrodynamics and burst environment. In this paper, we present the second iteration of the Arcminute Microkelvin Imager - Large Array (AMI-LA) Gamma-ray burst (GRB) radio afterglow catalog. The catalog consists of 1035 observations of 210 bursts. Our observations range from 0.04 to 900days post-burst. We detect radio emission associated with 19 events with flux densities spanning 0.1-40mJy, and present a detailed analysis of six events whose light curves have not been published elsewhere. In our individual afterglow analyses, we find that our radio counterparts show evidence of reverse shock emission 60% of the time. Two of the detected afterglows show evidence of scintillation which we use to place source size limits at tens of days. Of the whole catalog, 50 events have redshift measurements which we use to find the radio afterglow luminosity distribution for our sample. Our luminosity distribution spans five orders of magnitude, a larger range than seen in optical and X-ray bands, indicative of the strong dependence of the radio counterparts on the GRB's physical parameters.

### [C] 58.2 — Optical-NIR Multi-band Photometric Analysis and Characterization of Giant Exoplanets with CPI-C
- **arXiv:** [2608.16215](https://arxiv.org/abs/2608.16215)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.IM
- **Top topics:** ism_methods_data (58.2), astrochemistry (57.7), molecular_clouds (56.4)
- **Current keyword baseline:** NO
- **BM25 max:** 47.7
- **Semantic max:** 72.8
- **Abstract:** We present a multi-band photometric approach to characterize giant exoplanets, which represents one of the anticipated core scientific outcomes of Cool Planet Imaging Coronagraph (CPI-C). CPI-C operates with two observational channels covering visible and near-infrared wavelengths, each equipped with four broadband filters. The planet--star flux ratio integrated over each filter bandpass is calculated for photometric analysis. For cool planets observed in the visible bands, the data are primarily used to fit the overall spectral shape and methane-induced modulation, providing sensitivity to metallicity- and cloud-dependent spectral variations while constraining the reflected-light spectral shape and the combined scaling involving planet radius, orbital separation, and orbital phase. In the near-infrared bands, which probe thermal emission, the data help to better constrain fundamental planetary parameters including the effective temperature, radius, surface gravity and mass. For a synthetic giant planet with measurable reflected-light and thermal-emission components, the combined VIS4+NIR4 data provide tighter same-target constraints than either filter set alone, especially for the planet radius and cloud sedimentation parameter. Our simulations incorporate realistic instrument throughput, detector noise, and residual speckle noise. The results demonstrate that the eight-band design spanning visible to near-infrared wavelengths supports reflected-light diagnostics, thermal-emission characterization, and joint optical--NIR analysis of giant exoplanets within CPI-C science observations.

### [C] 58.1 — The impact of recombination during tidal disruption events
- **arXiv:** [2608.18201](https://arxiv.org/abs/2608.18201)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** molecular_clouds (58.1), star_formation (55.9), turbulence (52.2)
- **Current keyword baseline:** NO
- **BM25 max:** 57.4
- **Semantic max:** 72.7
- **Abstract:** During a tidal disruption event, the resulting debris stream cools down adiabatically due to the tidal stretching. As the temperature drops, the gas is expected to undergo chemical processes, which can release thermal energy into the stream, potentially affecting the subsequent gas evolution. For the first time, we investigate in detail this effect and its dynamical impact on the early-time evolution of the stream by making use of three dimensional hydrodynamic simulations coupled with a realistic equation of state. We find that a few days after disruption, the energy injected by hydrogen recombination and molecular hydrogen formation causes the stream thickness to grow much more rapidly. In the bound debris, this effect stops the stream's confinement by self-gravity before the gas reaches apocentre. As a result, the maximum stream thickness increases by a factor that ranges from a few, for the most bound gas, to a few tens for the near-parabolic gas, reaching $\approx 30 \, R_{\star} $ around the peak of the mass fallback rate. We discuss how this accelerated stream expansion may affect the subsequent evolution of the gas, estimate the luminosity powered by recombination in the unbound debris, and evaluate the potential influence of non-ideal magneto-hydrodynamic effects. By characterizing the thermodynamic and hydrodynamic properties of the stream before its return near pericentre, our results provide physically motivated initial conditions to self-consistently model the later stages of tidal disruption events, offering a promising pathway to unveiling the physical origins of their observed emission.

### [C] 58.1 — A stochastic forward model for the intergalactic dispersion-measure distribution of Fast Radio Bursts
- **arXiv:** [2608.17658](https://arxiv.org/abs/2608.17658)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, astro-ph.HE, astro-ph.IM
- **Top topics:** galactic_ism_surveys (58.1), turbulence (52.8), ism_methods_data (49.0)
- **Current keyword baseline:** NO
- **BM25 max:** 47.6
- **Semantic max:** 72.6
- **Abstract:** Fast Radio Bursts probe ionised baryons through their observed dispersion measures. We present \turbofrb, a semi-analytic stochastic forward model for the intergalactic dispersion-measure distribution, $P({\rm DM}_{\rm IGM}\mid z)$, that resolves the diffuse IGM, halo, and filament contributions as explicit physical channels, with the halo and filament encounter rates coupled by a latent line-of-sight environmental variable. Only four effective parameters are calibrated against hydrodynamical ray-traced IllustrisTNG benchmark. The model matches the benchmark mean DM to the percent level and yields a per-redshift Jensen-Shannon divergence of at most $5\times10^{-3}$ across $z = 0.5$-$2.5$. The per-sightline channel decomposition makes explicit what closed-form parametric descriptions cannot show: the diffuse IGM sets the body of the distribution, while halos and filaments populate the high-DM tail. Applied to representative localised FRBs, the forward likelihood quantifies host-excess events independently of their astrophysical signatures and recovers the injected $H_0$ within $1σ$ in a closed-loop consistency test. The \turbofrb package is available at \href{https://github.com/jefersonfortunato/turbofrb}{github.com/jefersonfortunato/turbofrb}.

### [C] 58.1 — Density-induced dark-baryon conversion in $Δ-$admixed hypernuclear neutron stars
- **arXiv:** [2608.17409](https://arxiv.org/abs/2608.17409)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, hep-ph, nucl-th
- **Top topics:** ism_methods_data (58.1), astrochemistry (50.6), turbulence (46.9)
- **Current keyword baseline:** NO
- **BM25 max:** 43.0
- **Semantic max:** 72.7
- **Abstract:** We investigate density-induced conversion of neutrons into a neutral dark baryon $χ$ in cold, charge-neutral, $β$-equilibrated neutron-star matter containing hyperons and all $Δ(1232)$ quartet. The hadronic sector is modeled within a density-dependent covariant density-functional framework using the DDME2 parametrization. A scalar Higgs portal is included as a possible interaction channel between the visible and dark sectors, although its mean-field contribution is negligible for the couplings adopted here. Unlike fixed dark-matter admixture models or scenarios in which nucleon-to-DM conversion is driven by Higgs exchange, the $χ$ abundance is determined self-consistently from chemical equilibrium and baryon-number conservation. We find that hyperons and $Δ$ resonances alter the neutron chemical potential, delay the onset of $χ$, and suppress its abundance relative to nucleonic matter. This competition induces characteristic changes in the equation of state, particle fractions, sound speed, and adiabatic index. For $m_χ=1250$, $1300$, and $1400$ MeV, the maximum masses of the complete $N+Y+Δ+χ$ configurations are $1.806$, $1.899$, and $2.024,M_\odot$, respectively, indicating that the massive-pulsar constraint disfavors the lighter dark-baryon benchmarks. The radial profiles further show that for $m_χ=1400$ MeV, $χ$ is confined to the inner core of the most massive stars, while canonical configurations remain essentially unaffected. Thus, the stellar modifications arise primarily from conversion-induced rearrangement of the equilibrium composition rather than from Higgs-mediated interactions. These results highlight the importance of treating conventional non-nucleonic degrees of freedom and density-generated dark baryons on an equal footing when assessing the astrophysical viability of dark-sector extensions of dense matter.

### [C] 58.1 — Detection and Characterization of Microlensing Events due to Isolated Black Holes towards the Magellanic Clouds in the Rubin Observations
- **arXiv:** [2608.16448](https://arxiv.org/abs/2608.16448)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** feedback_bubbles (58.1), ism_methods_data (56.7), galactic_ism_surveys (56.2)
- **Current keyword baseline:** NO
- **BM25 max:** 42.3
- **Semantic max:** 72.6
- **Abstract:** Gravitational microlensing surveys potentially discover isolated black holes (IBHs) at large distances through their gravitational effects on apparent brightness and motion of collinear stars. Here, we study detecting and characterizing IBHs within the mass range $[3,~5000]M_{\odot}$ with either stellar or dark matter origins in the upcoming observations by Vera~C.~Rubin Observatory towards the Large and Small Magellanic Clouds (LMC and SMC). We consider four lens mass functions (MFs:~$dN/dM\propto M^{-β}$ for $β=0,~0.5,~1,~2$), and generate long-duration microlensing events due to IBHs detectable by Rubin. By assuming the fraction of IBHs's mass in total Galactic mass as $\mathcal{F}$, Rubin potentially detects $\sim0.3,~\rm{and}~2$ microlensing events towards SMC and LMC due to IBHs if $β=1,~\rm{and}~\mathcal{F}=5\times10^{-3}$. These IBHs are inside our galaxy with the probability $\gtrsim70\%$. These events have on average $θ_{\rm{E}}\sim30-50~\rm{mas}$, so that the probabilities of resolving their lensing-induced images through the Rubin astrometric observations are $\sim1.4,~\rm{and}~16.3\%$ towards LMC and SMC. In $\sim1,~5.2\%$ of these events their astrometric deflections are realizable. The probabilities of discerning their parallax are $\sim40,~25\%$. We evaluate relative errors with simulating synthetic data points and by assuming the true models as the best-fitted ones. We conclude for a log-uniform MF for $\lesssim0.1,~\rm{and}~0.3\%$ of photometrically detectable microlensing events towards in LMC and SMC the relative errors in the lens mass, distance and velocity are $\lesssim3\%$. We calculate the number of detectable IBHs versus by assuming their complete contribution of compact objects in halos' darkmatter, and conclude Rubin specifies $95\%$~C.L. upper-limit on IBHs exclusion by masses $\lesssim208,~8M_{\odot}$ for $\mathcal{F}\simeq4\times10^{-3}$.

### [C] 58.1 — Unknown Unknowns: Model Misspecification in Machine Learning for Physics
- **arXiv:** [2608.13633](https://arxiv.org/abs/2608.13633)
- **Primary category:** physics.data-an
- **Categories:** physics.data-an, astro-ph.CO, astro-ph.GA, cs.LG, hep-ex, hep-ph
- **Top topics:** ism_methods_data (58.1), molecular_clouds (55.1), turbulence (54.3)
- **Current keyword baseline:** NO
- **BM25 max:** 32.7
- **Semantic max:** 72.7
- **Abstract:** Machine learning is now a central tool for solving inverse problems in particle physics and astronomy. Models are trained on simulation and deployed on real data, raising the question not just of whether they fit, but of whether they are wrong in ways we did not anticipate: the unknown unknowns. This challenge of model misspecification is not unique to machine learning. In physics, misspecification is sometimes exactly what we want to find: new discoveries appear as failures of existing models. At other times, we want such effects absorbed into the analysis without biasing the measurement. A robust analysis is one that absorbs the misspecifications we are not interested in, while preserving sensitivity to the ones we are. Machine learning can both amplify misspecification and provide new tools to address it. We discuss the challenges of model misspecification, diagnostics for detecting it, and strategies for mitigation. No single diagnostic can confirm that a model is correctly specified: detection and mitigation are two halves of an iterative loop, in which a battery of complementary diagnostics is applied, the model is updated, and the process repeated. Robustness against unknown unknowns is ultimately less about any single technique than about a disposition: a willingness to suspect one's own model, and to design analyses that can survive being wrong in ways one did not anticipate.

### [C] 58.0 — A Prediction for DESI Full-Shape: Increasing Tomographic $Ω_m(z)$ Trend
- **arXiv:** [2608.19883](https://arxiv.org/abs/2608.19883)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** astrochemistry (58.0), ism_methods_data (56.9), galactic_ism_surveys (51.0)
- **Current keyword baseline:** NO
- **BM25 max:** 55.4
- **Semantic max:** 72.5
- **Abstract:** To confirm $Λ$CDM deviations are due to missing physics (not systematics), one should demonstrate that the model fitting parameters exhibit qualitatively similar redshift drift across independent observables. This is the only way one guarantees new physics. Here, we show that a recent Dark Energy Spectroscopic Instrument (DESI) DR2 Full-Shape (FS) modelling Lyman-$α$ constraint at $z_{\rm eff} = 2.33$ combined with earlier DR1 FS modelling constraints with $0.295 \leq z_{\rm eff} \leq 1.491$ leads to a straight line $Ω_m(z) = m z + c$ with slope $m = 0.022 \pm 0.012$, $1.8 σ$ removed from constant $Ω_m$. Akaike Information Criterion and Bayesian evidence confirm that constant $Ω_m$ and increasing $Ω_m(z)$ are statistically indistinguishable. Through the $Om(z)$ diagnostic, we review how increasing and decreasing $Om(z)$ map to phantom and quintessence dark energy (DE) regimes, respectively. While FS modelling constraints map to phantom DE, the decreasing and increasing $Ω_m(z)$ trends in DESI BAO and DESI with external data make a phantom crossing inevitable. Since dynamical DE is but one interpretation for $Ω_m(z)$ trends, it is imperative that different datasets converge on their $Ω_m(z)$ trends before one jumps to physical conclusions. We forecast how DESI FS modelling $Ω_m$ constraints will improve up to the final data release and explore the implications for model selection.

### [C] 58.0 — Radio Properties of Narrow-Line and Broad-Line Seyfert 1 Galaxies
- **arXiv:** [2608.13303](https://arxiv.org/abs/2608.13303)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** star_formation (58.0), galactic_ism_surveys (57.6), ism_methods_data (56.6)
- **Current keyword baseline:** NO
- **BM25 max:** 55.4
- **Semantic max:** 72.0
- **Abstract:** Narrow-line Seyfert 1 (NLS1) galaxies host active galactic nuclei (AGN) with narrow optical emission lines of the broad-line region. This is often explained with a relatively lower mass of the central supermassive black hole and super-Eddington accretion. We compared the radio properties of large samples of NLS1 and broad-line Seyfert 1 (BLS1) galaxies compiled from the Sloan Digital Sky Survey. We cross-matched the NLS1 and BLS1 samples with the Faint Images of the Radio Sky at Twenty-Centimeters (FIRST) sky survey at 1.4 GHz and the first and second epoch data of the Very Large Array Sky Survey (VLASS) at 3 GHz. We calculated the radio spectral indices, the 1.4-GHz radio power, and the radio loudness. We found lower 1.4-GHz radio detection rates for the NLS1 galaxies. The median radio loudness values, the fraction of radio-loud AGN, and the median 1.4-GHz radio power are also lower for the NLS1 sample. The median spectral indices imply a slightly steeper radio spectrum for the NLS1 sample than for the BLS1 sample. Comparison of the star formation rates estimated from the radio data and the infrared measurements of the Wide-field Infrared Survey Explorer satellite indicated that more than half of the FIRST- and VLASS-detected NLS1 and BLS1 galaxies contain radio-emitting AGN.

### [C] 57.9 — Physical Optics Analysis of Polarization Effects in SO LAT Reflectors
- **arXiv:** [2608.18998](https://arxiv.org/abs/2608.18998)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (57.9), molecular_clouds (53.2), magnetic_fields (52.6)
- **Current keyword baseline:** NO
- **BM25 max:** 48.6
- **Semantic max:** 65.2
- **Abstract:** We present a physical-optics analysis of the polarization response of the reflective optical of the Simons Observatory Large Aperture Telescope (SO LAT). Far-field co-polar and cross-polar beam patterns are simulated for representative feedhorn positions, and the corresponding polarization-angle offsets are evaluated. The results show that the crossed-Dragone reflector system has good polarization performance. Off-axis feed positions introduce small, position-dependent offsets in the far-field polarization orientation, with a maximum value of 0.23 degrees, due to optical asymmetry. The relative polarization-angle offset under feedhorn polarization rotation, however, remains consistent with zero. No significant frequency dependence is found over the frequencies considered. These results provide a practical reference for polarization-angle calibration and for assessing reflector-induced polarization systematics in the SO LAT.

### [C] 57.9 — Discovery of an Eccentric Hot Super-Jupiter Leaving the Transiting Geometry of the Early-A-type star TOI-1355
- **arXiv:** [2608.17387](https://arxiv.org/abs/2608.17387)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** star_formation (57.9), astrochemistry (55.6), ism_methods_data (54.2)
- **Current keyword baseline:** NO
- **BM25 max:** 36.0
- **Semantic max:** 72.3
- **Abstract:** Hot Jupiters orbiting hot stars ($T_\mathrm{eff} > 7000$ K) are suggested to have experienced high-eccentricity migration, often evidenced by the tendency for misaligned orbits, despite their circular orbits. In this paper, we present the discovery of TOI-1355 b: an eccentric ($e\sim0.22$) hot Jupiter with a mass of $m_{\mathrm{p}}\sim5.8M_J$ and a radius of $R_{\mathrm{p}}\sim 1.4R_J$ orbiting an A-type star with a period of about $2.17$ days, identified from the TESS transit survey and subsequent follow-up observations. We measured the stellar parameters using the data from the high-resolution spectrograph Seimei/GAOES-RV and obtained the planetary parameters from the photometric data acquired by TESS and ground-based telescopes. This is one of the rare eccentric hot Jupiters around hot stars. This system could be undergoing high-eccentricity migration. We detected nodal precession by measuring the change in its impact parameter. This implies that its transit will no longer be observable from the middle of 2033. Nevertheless, TOI-1355 b is anticipated to be a compelling target for future atmospheric observations, given the hint of atmospheric variability detected in this study.

### [C] 57.9 — Cryogenic characterisation for the Nulling Interferometry Cryogenic Experiment (NICE)
- **arXiv:** [2608.16291](https://arxiv.org/abs/2608.16291)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** molecular_clouds (57.9), star_formation (39.6), ism_methods_data (34.8)
- **Current keyword baseline:** NO
- **BM25 max:** 37.0
- **Semantic max:** 72.4
- **Abstract:** The Nulling Interferometry Cryogenic Experiment (NICE) is an experimental testbed for the beam combiner of the Large Interferometer For Exoplanets (LIFE) space mission. Until now, progress on NICE has been confined to an ambient bench, where we have recorded progress in deep ($<10^{-5}$) nulls at wavelengths between 4 and 5 microns at 300 K. However, the ultimate goal and requirement of NICE is to repeat these measurements at the sensitivity levels expected for a planetary system, requiring deep cryogenic conditions at 15 K. Here, we describe the ``Ice Cube'' cryostat, a small version of the future NICE cryostat that is used for component and subsystem level cryogenic testing. This is interfaced with a measurement setup using a segmented aperture interferometer and a wavefront sensor. We will also describe the testing campaign for understanding the material and mounting challenges that will be faced when translating the warm bench to cryogenic operations.

### [C] 57.9 — Modelling the nonlinear matter power spectrum in Hu-Sawicki $f(R)$ gravity with the Web-Halo Model
- **arXiv:** [2608.15635](https://arxiv.org/abs/2608.15635)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** turbulence (57.9), galactic_ism_surveys (53.8), star_formation (52.0)
- **Current keyword baseline:** NO
- **BM25 max:** 39.6
- **Semantic max:** 67.2
- **Abstract:** We develop a semi-analytic extension of the Web-Halo Model (WHM) to Hu-Sawicki $f(R)$ gravity, with the aim of linking nonlinear matter clustering to the successive stages of cosmic-web collapse. The cylindrical sheet and filament windows of the original WHM are replaced by axisymmetric ellipsoidal top-hat windows, yielding a modest improvement around the perturbative-to-nonlinear transition without introducing additional fitting parameters. Modified gravity is incorporated through environment-dependent chameleon spherical collapse, from which the collapse threshold and virial overdensity are obtained and propagated through the sheet, filament, and halo contributions. For $|f_{R0}|=10^{-5}$ and $10^{-6}$, the predicted nonlinear enhancement is broadly consistent with the scale-, redshift-, and field-strength dependence seen in the e-MANTIS emulator, with closer agreement for the weaker field and at higher redshift. The component responses show that sheets and filaments contribute substantially around the transition regime, while the halo response becomes increasingly important at smaller scales. As complementary diagnostics, no displacement of the BAO peak is resolved, whereas tomographic weak-lensing spectra retain a percent-level response to the modified matter power spectrum. The extended WHM therefore provides a physically interpretable framework for tracing screened modified-gravity effects across the cosmic-web collapse hierarchy.

### [C] 57.9 — Hemispheric Asymmetry of Solar Active Regions Arises from a Nested Population
- **arXiv:** [2608.12263](https://arxiv.org/abs/2608.12263)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** feedback_bubbles (57.9), magnetic_fields (56.8), ism_methods_data (54.5)
- **Current keyword baseline:** NO
- **BM25 max:** 55.3
- **Semantic max:** 72.3
- **Abstract:** We investigate the longitude--time distribution of NOAA active regions (ARs) during Solar Cycles 22--24 and find statistically significant North--South asymmetry in AR emergence. Using an activity-nest identification algorithm, we show that this asymmetry is concentrated in the subset of ARs that participate in nests. Nest-member ARs exhibit substantially larger hemispheric asymmetry than either the full AR population or the non-nest population, and the asymmetry is largely removed when nest-member ARs are excluded. Monte Carlo tests with randomized longitudes and temporal perturbations show that the observed nesting and asymmetry exceed random expectations, implying that $\sim$6--18\% of ARs participate in a non-random, hemispherically asymmetric nesting component. This asymmetry is associated with temporally offset bursts of activity and distinct longitudinal clustering between the hemispheres, leading to reduced cross-equatorial coherence in the longitude--time distribution of solar ARs. Intervals of enhanced nesting activity and hemispheric asymmetry broadly coincide with enhanced hemispheric quasi-biennial variability and temporal evolution of the large-scale solar magnetic field, suggesting a possible connection between intermediate-timescale dynamo variability and the hemispheric organization of solar activity.

### [C] 57.6 — The intrinsic luminosity-decay correlation in subsamples of GRB X-ray afterglows
- **arXiv:** [2608.19332](https://arxiv.org/abs/2608.19332)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (57.6), molecular_clouds (56.0), galactic_ism_surveys (55.2)
- **Current keyword baseline:** NO
- **BM25 max:** 36.3
- **Semantic max:** 72.0
- **Abstract:** The intrinsic luminosity-decay correlation in gamma-ray burst (GRB) afterglows, between the early-time luminosity and the average rate of decay past this time, has previously been observed in the radio, optical/UV, X-ray and GeV wavebands and quantitatively shows that more luminous afterglows tend to have higher average rates of decay. We have compiled an updated sample of 427 X-ray afterglows with measured redshifts, observed with Swift/XRT over 20 years. For each GRB, we measure the luminosity at 200 seconds in the rest frame, $L_{\mathrm{X,200s}}$, and the average rate of decay from this time, $α_{X,>200s}$. We find these parameters are correlated with a Spearman's rank coefficient ($R_\mathrm{sp}$) of $0.54\pm0.04$ at a significance of $\geq3σ$ and a linear regression slope of $0.18\pm0.02$. We separate our sample into subsamples, including 395 long GRBs (LGRBs) and 32 short GRBs (SGRBs) and find evidence of the $L_{\mathrm{X,200s}}$-$α_{X,>200s}$ correlation at a significance of $\geq3σ$ in LGRBs but not in SGRBs, consistent with previous studies. In a subsample of 102 LGRBs with well-sampled light curves and late end times, we find that scatter in the correlation is significantly reduced and the strength increases to $R_\mathrm{sp}=0.80\pm0.04$ whilst the slope remains consistent with the full sample. We discuss our results and, briefly, their potential implications on constraining the cause of the correlation. Possible causes include geometric effects due to the angle between the observer and the jet-axis, or some mechanism that regulates the rate at which energy is released by the GRB central engine.

### [C] 57.5 — The comets discovered from New Zealand, and the astronomers who found them
- **arXiv:** [2608.19636](https://arxiv.org/abs/2608.19636)
- **Primary category:** physics.hist-ph
- **Categories:** physics.hist-ph, astro-ph.EP
- **Top topics:** star_formation (57.5), molecular_clouds (55.6), ism_methods_data (42.9)
- **Current keyword baseline:** NO
- **BM25 max:** 30.2
- **Semantic max:** 71.9
- **Abstract:** Eleven comets were discovered by six New Zealanders from New Zealand shores. New Zealand's important geographical position south of the Equator is highlighted. This location allows observers to discover and observe comets that would be difficult to see from the Northern Hemisphere. The lives of these comet discoverers are explored, as well as the discovery circumstances and an analysis of the morphological changes of their comets. We find that numerous New Zealand observers made many observations of these comets, however, relatively few were included in international publications, this possibly being due to papers about them not being submitted to overseas journals. We also note an interesting trend in that the number of New Zealand newspaper articles relating to these comet discoveries plummeted after the 1946 discovery by Albert Jones. We speculate as to why this may have happened.

### [C] 57.5 — First demonstration of a multimode-to-multimode photonic lantern for astronomy
- **arXiv:** [2608.18912](https://arxiv.org/abs/2608.18912)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** ism_methods_data (57.5), molecular_clouds (44.2), star_formation (39.5)
- **Current keyword baseline:** NO
- **BM25 max:** 36.4
- **Semantic max:** 64.8
- **Abstract:** Photonic lanterns have been widely used in astronomy as low-loss multiplexing devices, typically coupling light from a multimode input into several single-mode outputs. In this work, we present the first multimode-to-multimode photonic lantern specifically designed to combine light from several multimode fibers into a single multimode waveguide. We fabricated and characterized the devices at multiple wavelengths to evaluate the performance of the adiabatic multimode transition. The measured efficiencies exceed $90\ \%$, demonstrating low-loss multimode propagation and efficient modal transfer through the lantern structure. This architecture enables efficient multimode beam combination and represents a significant step toward scalable modular telescope concepts without requiring diffraction-limited injection.

### [C] 57.5 — Ejecta clumps revealed by study of reverse-shocked ejecta through MUSE integral field spectroscopy of SNR 0509-67.5
- **arXiv:** [2608.17465](https://arxiv.org/abs/2608.17465)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA, astro-ph.HE
- **Top topics:** astrochemistry (57.5), molecular_clouds (56.1), feedback_bubbles (55.7)
- **Current keyword baseline:** YES
- **BM25 max:** 35.5
- **Semantic max:** 71.9
- **Abstract:** We report the discovery of a spatially resolved clumpy ejecta structure in the reverse-shocked ejecta of SNR 0509-67.5, revealed through multiple faint and broad forbidden coronal emission lines in deep MUSE observations. We also identify two new broad coronal emission lines not reported before in this remnant, [Fe xi] 7894 A and [Fe x] 6374.5 A , which extend the set of previously reported [Fe xv] 7059.59 A, [Fe xiv] 5302.86 A , [Fe ix] 8236.55 A , [Ca xv] 5695 A, and [S xii] 7611.0 A. Near-continuous ionisation states of Fe allow us to follow the ionisation progression behind the reverse shock. We use a 1D analytical model to evolve Fe charge states following reverse shock interaction to compare with observations, indicating the need for preshock clumping or over-density in order to reproduce the observed surface brightness of the [Fe xiv] line. Additionally, we report the spatially resolved distribution of ejecta clumps and show that reverse-shock interaction drives their compression and fragmentation. We also find a clear trend of decreasing velocity width with increasing Fe ionisation state, from the broadest [Fe ix] emission to the narrowest [Fe xv], with intermediate-ionisation species ([Fe x], [Fe xi], [Fe xiv]) showing intermediate widths. Finally, we compare our observations to a dynamically driven double-degenerate double detonation (D6) 3D remnant model at similar Fe and S ionisation states and conclude that the observed clumps are predominantly due to Rayleigh-Taylor instabilities.

### [C] 57.4 — Universal Relations for Neutron Stars from Asymptotic Analysis
- **arXiv:** [2608.19939](https://arxiv.org/abs/2608.19939)
- **Primary category:** gr-qc
- **Categories:** gr-qc, astro-ph.HE, hep-ph
- **Top topics:** ism_methods_data (57.4), star_formation (54.9), astrochemistry (41.7)
- **Current keyword baseline:** NO
- **BM25 max:** 38.5
- **Semantic max:** 71.7
- **Abstract:** Dimensionless observables of neutron stars, such as the moment of inertia, the tidal deformability, the spin-induced quadrupole moment, and the compactness, satisfy the I--Love--Q and Love--$C$ universal relations to percent-level accuracy over a wide range of equations of state. We investigate analytically the origin of this insensitivity in the stellar structure equations. We derive asymptotic expansions of these relations directly from the differential equations and boundary conditions for slowly rotating, tidally deformed stars described by a general piecewise-polytropic equation of state. Although the differential equations allow several forms of the asymptotic expansion, we find that only one class is consistent with the observed universality, and we use this class to analyze the universal relations. Because the observables are determined at the stellar surface, information about the deep-interior equation of state can enter them only through the parameters that survive in the asymptotic expansion at the surface. We find that the universal relations depend only on three parameters: two integration constants and one polytrope index of the outermost segment. By determining how these parameters deform the relations, we show that, throughout the region of parameter space occupied by realistic equations of state, the resulting deviations remain at the percent level, consistent with the observed accuracy of the universal relations. Within the same formalism, we classify violations of universality according to the additional degrees of freedom or input data responsible for them. Since the construction relies only on the underlying differential equations and boundary conditions, the same procedure can be applied to other systems once the corresponding equations and boundary conditions are specified.

### [C] 57.4 — Quantifying uncertainty in the neutron-star equation of state using point estimates and posterior distributions
- **arXiv:** [2608.19019](https://arxiv.org/abs/2608.19019)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, hep-ph, hep-th, nucl-th
- **Top topics:** ism_methods_data (57.4), star_formation (46.8), turbulence (43.4)
- **Current keyword baseline:** NO
- **BM25 max:** 31.7
- **Semantic max:** 71.8
- **Abstract:** We investigate uncertainty quantification for the neutron-star equation of state (EOS) by comparing point-estimation and distributional inference approaches using the same Chebyshev and piecewise-linear parameterizations. We combine neutron-star mass--radius and gravitational-wave tidal-deformability information within Bayesian, multilayer-perceptron (MLP), and normalizing-flow frameworks. Although the methods yield similar mean EOS behavior, the deterministic MLP produces substantially narrower uncertainty bands at high densities. We show that this behavior is associated with the point-estimation objective, which maps degenerate solutions toward the conditional mean rather than representing the full parameter posterior. By contrast, the normalizing flow yields distributions more consistent with the Bayesian inference. Our results demonstrate that reliable uncertainty quantification of the high-density EOS requires methods that represent conditional probability distributions rather than only point estimates.

### [C] 57.4 — TIC 433545934: The first 2+2 type doubly eclipsing binary with extra, mutual eclipses
- **arXiv:** [2608.13034](https://arxiv.org/abs/2608.13034)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** astrochemistry (57.4), star_formation (55.8), feedback_bubbles (54.2)
- **Current keyword baseline:** YES
- **BM25 max:** 42.8
- **Semantic max:** 71.7
- **Abstract:** In this work we identify and photodynamically analyze TIC 433545934, the very first doubly eclipsing 2+2-type quadruple stellar system, which shows outer eclipses, too. One such outer eclipse was discovered with TESS, which triggered a special interest in this system. Most of the data for this study come from TESS observations, but we also obtained supplemental ground-based photometric measurements for this quadruple system. The eclipse timing variation curves extracted from the TESS and ground-based follow-up data, the photometric light curves, and the spectral energy distribution are combined in a complex photodynamical analysis to yield the stellar and orbital parameters of this dynamically interesting system. The periods of the two inner, eclipsing binaries were found to be $P_A=2.07$d and $P_B=1.41$d, while the outer period is $P_{AB}=224.5$d. The outer period alone makes this system the fifth most compact known 2+2-type quadruple. Moreover, what really makes TIC 433545934 unique is that TESS observed a triple-dipped extra eclipsing event when the stars of binary B eclipsed the two components of binary A. We identified similar extra eclipsing events in the archival, ground-based data of ASAS-SN and ATLAS, as well. We found, however, that these extra events occur only once during an outer revolution, that is, binary A does not eclipse the stars of binary B. This is in accord with our finding that the outer eccentricity is quite high, being $e_{AB}=0.62$. Our analysis reveals that binary A consists of two quite similar, but slightly evolved late A-type stars ($q_A=0.92$), while in the case of binary B, the primary star, whose mass is between the masses of the two stars of binary A, is quite dominant, with $q_B=0.60$. The system was found to be substantially flat, with mutual inclination angles below $\approx2\degr$.

### [C] 57.3 — Understanding the Energy Input Required for Methane Emission on CWISEP J193518.59-154620.3: A Comprehensive Analysis
- **arXiv:** [2608.17016](https://arxiv.org/abs/2608.17016)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** astrochemistry (57.3), feedback_bubbles (54.9), ism_methods_data (54.1)
- **Current keyword baseline:** NO
- **BM25 max:** 48.8
- **Semantic max:** 68.6
- **Abstract:** The Y dwarf WISE 1935 exhibits a thermal inversion in its radiative atmosphere, producing methane emission features in its JWST spectrum, but the physical mechanism responsible for this inversion remains unknown. Using the open-source radiative--convective equilibrium code PICASO, we model atmospheric heating with Chapman energy deposition profiles to reproduce the observed thermal inversion and methane emission feature. Our models require heating rates of approximately 10^5-10^6 erg cm^-2 s^-1. We show that the atmospheric response depends primarily on the integrated heating deposited in the observable atmosphere, revealing a degeneracy between heating magnitude, vertical extent, and emitting surface fraction. Disequilibrium chemistry lowers the required energy input by lowering CH$_4$ opacity and strengthening the inversion. Comparison with recent electron-beam heating models indicates that reproducing the thermal inversion in W1935 requires substantially greater energy deposition than currently predicted for brown dwarf auroral heating, while the observed methane emission favors energy deposition near 10^-3-10^-2 bar. Our models also predict a prominent methane emission feature near 7.8 microns, along with energy-sensitive ammonia features near 6 microns, implying a bolometric luminosity greater than that yet measured. Finally, we investigate potential sources of the inferred upper-atmospheric heating. We find that Joule heating would require a strong magnetic field and large electron densities, the latter supported by external ionization from an unidentified source. We also consider cometary impacts as a possible source of atmospheric heating.

### [C] 57.3 — Testing a Sign-Switch Cosmological Model with Curvature through Latest Planck 2018, DESI DR2 and PantheonPlus\&SH0ES Observational Data
- **arXiv:** [2608.15167](https://arxiv.org/abs/2608.15167)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc
- **Top topics:** feedback_bubbles (57.3), ism_methods_data (55.8), astrochemistry (53.2)
- **Current keyword baseline:** NO
- **BM25 max:** 37.6
- **Semantic max:** 69.7
- **Abstract:** We investigate the spatial geometry of the Universe within the framework of a sign-switch dark energy scenario by extending the recently proposed $Λ_{\rm s}$CDM model to include a free curvature parameter $Ω_k$.In this framework, the effective cosmological constant undergoes a transition from a negative to a positive value at a characteristic redshift $z_{\dagger}$. Using the latest Planck 2018 cosmic microwave background (CMB) data, DESI DR2 baryon acoustic oscillation (BAO) measurements, and the PantheonPlus\&SH0ES Type Ia supernova sample, we derive joint constraints on the spatial curvature parameter $Ω_k$ and other cosmological parameters. We find that Planck data itself slightly favors a closed universe within both the $Λ_{\rm s}$CDM$+Ω_k$ and $Λ$CDM$+Ω_k$ frameworks, although spatial flatness remains well within the allowed uncertainties. When low-redshift probes were included, the curvature constraints were significantly tightened. In particular, the full Pk18+DR2+PP\&SH0ES dataset yields $Ω_k = 0.0001 \pm 0.0014$ for the $Λ_{\rm s}$CDM model, indicating a universe that is remarkably consistent with spatial flatness. We further analyzed the correlations between $Ω_k$, $H_0$, and $S_8$, finding that the inclusion of curvature and a sign-switch dark energy component helps stabilize cosmological parameter estimates while remaining compatible with current observational constraints. Model comparison using AIC and Bayesian evidence shows that the $Λ_{\rm s}$CDM model receives inconclusive/weak observational support relative to $Λ$CDM.

### [C] 57.3 — Cosmic Structures in CDM and SIDM
- **arXiv:** [2608.13070](https://arxiv.org/abs/2608.13070)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (57.3), ism_methods_data (56.4), feedback_bubbles (56.2)
- **Current keyword baseline:** NO
- **BM25 max:** 54.1
- **Semantic max:** 71.6
- **Abstract:** The standard $Λ$ Cold Dark Matter ($Λ$CDM) model has achieved remarkable success in explaining the formation and evolution of cosmic structures on large scales, supported by a wide range of observations, including the cosmic microwave background, large-scale structure surveys, and galaxy clusters. However, discrepancies between theoretical predictions and observations on small scales, have motivated the exploration of alternative dark matter models, including the self-interacting dark matter (SIDM) scenario. This review provides an overview of the theoretical foundations of CDM structure formation, the small-scale challenges, and the solutions proposed within the SIDM framework. We summarize recent theoretical developments in the SIDM framework and discuss current observational constraints on the dark matter self-interaction cross-section with particular emphasis on galaxy clusters.

### [C] 57.1 — Galaxy Morphology Classification: Uncertainty Modeling and Out of Distribution Detection
- **arXiv:** [2608.16654](https://arxiv.org/abs/2608.16654)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** galactic_ism_surveys (57.1), star_formation (54.3), molecular_clouds (53.8)
- **Current keyword baseline:** NO
- **BM25 max:** 35.0
- **Semantic max:** 71.4
- **Abstract:** We present a comprehensive framework for galaxy morphology classification that combines enhanced ``out-of-distribution (OOD)'' detection with improved uncertainty quantification. Using ``Galaxy Zoo DECaLS'', we trained a ResNet-34 architecture under three configurations: standard cross-entropy loss as a baseline, IsoMaxPlus loss function for OOD detection, and hybrid IsoMaxPlus+MonteCarlo Dropout for enhanced uncertainty quantification. IsoMaxPlus replaces the conventional SoftMax logits with distance-based class representations, preserving inter-class separability and enabling reliable OOD detection, without requiring additional architectural modifications or hyperparameter tuning. Coalescing IsoMaxPlus with MC Dropout provides a fast Bayesian approximation by performing multiple stochastic forward passes during inference. Our results show that IsoMaxPlus substantially improves OOD detection, increasing TNR@TPR95 by nearly $90\%$ relative to the cross-entropy baseline, while maintaining a competitive accuracy of 97\% across nine morphological classes. Additionally, with MC Dropout, the model yields more stable predictions and a reduction in calibration error, providing more reliable uncertainty estimates. The Expected Calibration Error (ECE) is reduced from $0.0095$ to $0.0026$ ($\approx73\%$) for IsoMaxPlus and $0.0033$ ($\approx65\%$) when combined with MC Dropout, compared to the baseline. Misclassified or underconfident predictions exhibit higher predictive entropy and lower minimum distance scores, providing an interpretable metric for identifying unreliable predictions. These methods are well-suited for current and upcoming large-scale surveys, where reliable automated morphological classification and awareness of uncertainty are essential for identifying rare or previously unseen galaxy morphologies.

### [C] 57.0 — Discovery of Three Glitches in the previously quiet pulsar PSR J1637$-$4642
- **arXiv:** [2608.19555](https://arxiv.org/abs/2608.19555)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.SR, nucl-th
- **Top topics:** ism_methods_data (57.0), star_formation (56.6), feedback_bubbles (51.6)
- **Current keyword baseline:** NO
- **BM25 max:** 32.7
- **Semantic max:** 70.7
- **Abstract:** We present the discovery and analysis of three rotational glitches in the young pulsar PSR J1637$-$4642. The timing observations span from 19 February 2009 to 6 October 2024 (MJD 54881$-$60589) from the Murriyang radio telescope of the Parkes Observatory. The first and strongest glitch occurred around MJD 58352 with a fractional frequency change of $Δν/ν\sim 2.7 \times 10^{-6}$, while two additional smaller glitches were detected at MJD 59443 and MJD 60445 with fractional changes of $2.2 \times 10^{-9}$ and $2.8 \times 10^{-8}$, respectively. Prior to this, the pulsar had shown no glitch activity since its discovery in the Parkes Multibeam survey. Only the first glitch exhibits detectable exponential recovery, with a decay timescale of $\sim$100 days and a small recovery fraction $\approx 0.015$, accompanied by a permanent increase in the magnitude of the spin-down rate. Modeling the post-glitch evolution of $\dotν$ within the vortex-creep framework using Bayesian inference gives a superfluid moment-of-inertia fraction $\approx 0.0187$, consistent with the inner-crust superfluid. These results reinforce the standard superfluid glitch paradigm and demonstrate that even ``quiet'' pulsars can still host substantial glitch activity.

### [C] 57.0 — The SAMI Galaxy Survey: Linking Tidal Features and Orbit Populations Using Schwarzschild Modelling
- **arXiv:** [2608.14012](https://arxiv.org/abs/2608.14012)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** feedback_bubbles (57.0), star_formation (55.6), ism_methods_data (53.7)
- **Current keyword baseline:** NO
- **BM25 max:** 50.2
- **Semantic max:** 69.5
- **Abstract:** The evolution of angular momentum in galaxies is shaped by a combination of internal secular processes and external mechanisms such as mergers. Orbit-superposition based dynamical modelling provides a powerful means of linking the intrinsic orbital structures of galaxies to their global properties and merger histories. We construct Schwarzschild orbit-superposition models of massive ($\log(M/M_{\odot})>10$) SAMI galaxies using the DYNAMITE code, utilising deep KiDS photometry to accurately reproduce each galaxy's luminosity distribution. We find that the fractions of hot, cold, warm, and counter-rotating orbits all show significant correlations with the spin parameter proxy $λ_{R_e}$, with the strongest correlation arising from the combined hot plus counter-rotating fraction. When controlling for stellar mass and environment, we find that the fraction of hot and cold orbits show significant correlations with stellar age, whereas warm orbits do not. We further find that the lower values of $λ_{R_e}$ for young galaxies with shell merger features as compared to the full sample is driven by an excess of hot orbits and a deficit of cold orbits, with no dependence on warm orbits. We suggest that the kinematic transformation in this SAMI sample proceeds through stars transitioning directly from cold to hot orbits. As warm orbits are expected to arise from secular heating processes, these findings indicate that merger-driven heating is the dominant mechanism governing the redistribution of angular momentum and the reduction of rotational support in massive galaxies.

### [C] 56.9 — Multi-scale Memory and Regime Shift in the Hyperactive Repeating FRB 20240114A
- **arXiv:** [2608.19713](https://arxiv.org/abs/2608.19713)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (56.9), turbulence (56.8), molecular_clouds (53.3)
- **Current keyword baseline:** NO
- **BM25 max:** 36.7
- **Semantic max:** 71.1
- **Abstract:** We present a statistical analysis of FRB~20240114A, a hyperactive repeating fast radio burst, based on 11,553 bursts detected by FAST over 214 days. Our main findings are fourfold. (1) On the most active day (MJD~60381, 3,197 bursts in 4.38 hr), event-rate coherence analysis reveals persistent correlated activity extending up to 3600~s, the longest reported for any repeating FRB, showing memory persists even in intense bursting epochs. (2) The waiting-time distribution on this day is well described by three exponentials, whereas the full 214-day sample develops a threshold power-law tail, indicating burst statistics depend on the observational baseline, with long-range correlations emerging only over longer timescales, a hallmark of self-organized criticality. (3) Rescaled range (R/S) analysis of waiting times reveals a broken power law, with Hurst exponents $H_1=0.63\pm0.02$ (short-lag weak memory) and $H_2=1.04\pm0.02$ (long-lag non-stationary drift). The break corresponds to $\sim$1 hour, consistent with the 3600~s coherence limit. R/S analysis of energies similarly exhibits a break ($H_1=0.60\pm0.01$, $H_2=1.10\pm0.05$) at a different lag, reinforcing that non-stationarity affects both temporal and energetic properties. (4) Energy distributions exhibit waiting-time-dependent slopes that are consistent with the full and daily samples, and the high-energy cutoff remains constant across waiting-time groups, suggesting that the maximum energy scale is an intrinsic source property. Together, these results establish a multi-scale memory framework: the source behaves stochastically on short timescales but exhibits systemic non-stationarity over months, providing benchmarks for burst models and highlighting the need for long-term, high-cadence monitoring to capture temporal complexity.

### [C] 56.9 — Revisiting the Growth Rate of the Relativistic Tearing Instability: The Role of the Non-ideal MHD Structure
- **arXiv:** [2608.19645](https://arxiv.org/abs/2608.19645)
- **Primary category:** physics.plasm-ph
- **Categories:** physics.plasm-ph, astro-ph.HE
- **Top topics:** magnetic_fields (56.9), turbulence (45.4), feedback_bubbles (43.1)
- **Current keyword baseline:** NO
- **BM25 max:** 73.9
- **Semantic max:** 64.0
- **Abstract:** Magnetic reconnection in magnetically dominated pair plasmas is a key process in high-energy astrophysical systems. We revisit the relativistic tearing instability in a Harris current sheet and derive an improved analytical expression for its linear growth rate and the most unstable wavenumber. The key modification is the treatment of the vector potential perturbation in the non-ideal magnetohydrodynamic (MHD) region. Instead of the conventional constant-A approximation, we use an extrapolated-A approximation, in which the ideal-MHD solution is linearly extrapolated into the non-ideal region. Comparison with two-dimensional particle-in-cell simulations shows that the revised theory improves the prediction of the most unstable wavenumber. The improvement is most pronounced at low particle drift velocities, where the particle gyroradius is smaller than the current-sheet thickness and the fastest-growing mode shifts to longer wavelength. The resulting analytical expressions provide an updated benchmark for magnetically dominated reconnection and its applications to high-energy astrophysical plasmas, including gamma-ray bursts and fast radio bursts.

### [C] 56.9 — The Roman Coronagraph Community Participation Program: data reduction pipeline astrometric calibration
- **arXiv:** [2608.17985](https://arxiv.org/abs/2608.17985)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** astrochemistry (56.9), molecular_clouds (56.4), ism_methods_data (56.2)
- **Current keyword baseline:** NO
- **BM25 max:** 30.6
- **Semantic max:** 71.2
- **Abstract:** The Nancy Grace Roman Space Telescope will be equipped with a Technology Demonstration Coronagraph Instrument that will push the current limits of high contrast imaging for exoplanets ($10^{-9}$ contrast). The Roman Coronagraph Community Participation Program has developed corgidrp, a python-based data reduction pipeline for the Roman Coronagraph Instrument that will perform essential data processing and calibration steps for coronagraphic observations. The astrometric calibration function within corgidrp allows us to understand the on-sky angular size and distance scale of science observations by characterizing essential detector parameters: boresight, plate scale, north angle, and optical distortion. Measuring these astrometric calibration products not only helps us understand the science output of our data, but it is what allows us to point the Roman coronagraph accurately at our science target in the first place. Here, we describe the techniques used within the astrometric calibration and demonstrate that our algorithm meets Technology Demonstration Threshold Requirements: (1) compute the on-sky location of the center of CGI EXCAM detector to better than 30 [mas] and (2) compute the on-sky position angles of the camera axes to within 0.3 [deg].

### [C] 56.8 — An invariant energy release hierarchy in a repeating fast radio burst
- **arXiv:** [2608.18455](https://arxiv.org/abs/2608.18455)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (56.8), magnetic_fields (55.5), star_formation (54.6)
- **Current keyword baseline:** NO
- **BM25 max:** 44.7
- **Semantic max:** 71.0
- **Abstract:** Fast radio bursts (FRBs) are luminous millisecond radio transients whose physical origin remains unsettled. A key diagnostic is whether their burst-energy distributions retain characteristic physical scales that are intrinsic and temporally stable within an individual engine. Here we report a 3.2-year monitoring campaign of the hyperactive repeater FRB~20220529 with FAST and Parkes, yielding more than 1,300 bursts spanning nearly five orders of magnitude in spectral energy density. The cumulative burst-rate distribution is described by an exponential-plus-power-law (EXP+PL) form, linking a low-energy exponential component with characteristic scale (E_0) to a scale-free bright-end tail. This scale remains invariant despite the burst rate declining by more than an order of magnitude, revealing a stable dissipation scale decoupled from the source's macroscopic trigger activity. Within a magnetar interpretation, this phenomenology is consistent with localized sub-critical reconnection episodes coexisting with plasmoid-mediated magnetic avalanches in a twisted magnetosphere. The invariant (E_0) constrains the dissipation region to the inner-to-middle magnetosphere and reveals a robust energy-release hierarchy beneath the variable activity of repeating FRBs, providing an observational benchmark for relativistic reconnection in an ultra-magnetized neutron-star environment.

### [C] 56.8 — The Tidal Venus Phenomenon: Demographics and Case Studies
- **arXiv:** [2608.18290](https://arxiv.org/abs/2608.18290)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** feedback_bubbles (56.8), astrochemistry (50.9), star_formation (49.9)
- **Current keyword baseline:** NO
- **BM25 max:** 34.4
- **Semantic max:** 71.0
- **Abstract:** The demographics of terrestrial planets and their orbits reveal a vast diversity in overall planetary energy budgets. Terrestrial exoplanets in short-period or eccentric orbits can experience intense tidal heating that, combined with stellar irradiation, may trigger runaway greenhouse conditions analogous to Venus. We calculate tidal heating rates for 143 terrestrial-sized exoplanets with measured eccentricities and find that, under adopted archive default eccentricities and constant-$Q$ assumptions, 70% exceed the extreme volcanism threshold in tidal flux and 96% exceed the runaway greenhouse limit in total zero-albedo flux. We develop a three-category taxonomy of tidal influence on climate: flux-driven Venus analogs, tidally dominated planets, and historically compromised Habitable Zone (HZ) worlds, and apply this framework to five case studies. TOI-6716 b and TOI-912 b may have exceptionally high tidal fluxes, potentially serving as examples where tidal dissipation alone causes them to exceed the runaway greenhouse threshold. TOI-700 d and LHS 1140 b, though currently below the threshold, were exposed to above-threshold stellar irradiation during their host stars' $\sim$0.5--3~Gyr pre-main-sequence phases; whether their atmospheres survived is testable with JWST. GJ 12 b, already above the threshold from stellar flux alone, experiences a tidal heat flux of $\sim$5~W/m$^2$ (comparable to Io) that drives an independent volcanic pathway to a runaway greenhouse. Three-dimensional climate simulations show that a temperate atmosphere for GJ 12 b fails to achieve radiative balance, while a Venus-like CO$_2$-dominated atmosphere converges to a stable state. We consider observational prospects for these systems and connections to forthcoming Venus in-situ missions.

### [C] 56.8 — Numerical Model Simulation of the Carruthers GCI Images
- **arXiv:** [2608.13516](https://arxiv.org/abs/2608.13516)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** molecular_clouds (56.8), astrochemistry (53.4), ism_methods_data (47.4)
- **Current keyword baseline:** NO
- **BM25 max:** 50.3
- **Semantic max:** 71.0
- **Abstract:** The Carruthers Geocorona Observatory, launched in September 2025, is NASA's first mission devoted to investigating the fundamental nature of Earth's exosphere from its distant vantage in halo orbit around the Earth-Sun Lagrange (L1) point. Its primary payload, the GeoCoronal Imager, consists of two coaligned photometric imagers that measure the radiance of ultraviolet emission at 121.6 nm (Lyman-$α$, or Ly-$α$) from exospheric hydrogen atoms simultaneously at wide and narrow fields of view. In order to validate the calibration and hydrogen density retrieval algorithms used in the Carruthers data processing pipeline, we developed a comprehensive numerical simulator to produce realistic images similar to those collected by the actual imagers on orbit. This paper details the algorithms used to simulate the exospheric emissions, background scene components, and instrument measurement model necessary to produce synthetic raw images.

### [C] 56.8 — Revisiting gravitational instability in protostellar discs with improved radiative cooling models
- **arXiv:** [2608.13058](https://arxiv.org/abs/2608.13058)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.GA, astro-ph.SR
- **Top topics:** star_formation (56.8), feedback_bubbles (55.8), molecular_clouds (50.6)
- **Current keyword baseline:** YES
- **BM25 max:** 74.6
- **Semantic max:** 69.7
- **Abstract:** Young discs are expected to be significantly more massive than those observed at $>1$ Myr and it is at this earliest stage that planet formation likely begins. Such massive discs may be susceptible to the gravitational instability (GI), therefore we need to determine the disc and stellar properties for which the GI is active to understand its role in early disc evolution and planet formation. Prior work has been limited by model assumptions and inaccuracies due to the complex nature of the thermodynamics of protostellar discs so we now revisit this question using an improved method to approximate radiative cooling within hydrodynamics simulations. We have explored a wide parameter space, representative of young protostellar discs of 0.1 to 1 M$_{\odot}$ and include irradiation from the host star. The parameters for which discs form spirals and fragment were found to differ to those obtained from earlier simulations. The outer regions of discs with radii of 50 au may be susceptible to fragmentation, meaning that GI-driven planet formation is not restricted to only the most extended discs. The additional thermal support due to stellar irradiation increases the disc mass that remains stable against GI: discs may reach up to $\gtrsim 0.4$ M$_*$ without fragmenting, providing a considerable quantity of material for building planets. Large scale spiral arms only developed for $M_*\lesssim$ 0.3 M$_{\odot}$, except in the most compact discs. Furthermore, the long-lived spiral structures that form tend to be flocculent and compact, indicating that large-scale spiral arms should not be considered a typical outcome of GI.

### [C] 56.7 — Origin of nucleosynthetic isotope variability in the NC reservoir: Evidence from Ti, Cr, and Mo isotopes
- **arXiv:** [2608.19786](https://arxiv.org/abs/2608.19786)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** astrochemistry (56.7), molecular_clouds (44.2), star_formation (40.5)
- **Current keyword baseline:** NO
- **BM25 max:** 47.0
- **Semantic max:** 70.8
- **Abstract:** Nucleosynthetic isotope anomalies allow distinguishing between non-carbonaceous (NC) and carbonaceous (CC) type meteorites, and have revealed correlated isotope variations especially among NC bodies. Understanding the origin of this NC trend is important for identifying the processes that produced the NC isotope heterogeneity, and for using these isotope anomalies to reconstruct the early evolution of the solar protoplanetary disk. We report mass-independent Ti, Cr, and Mo isotope compositions for a comprehensive set of previously not or only poorly investigated meteorites, as well as acid leachates obtained from the sequential digestion of primitive ordinary chondrites. Some of the samples investigated in this study fill previously identified apparent gaps in the NC trend, suggesting these gaps reflect unrepresentative sampling of a more continuous isotopic trend. Bulk meteorites and leachates exhibit distinct isotope systematics, indicating that the NC isotope variability does not reflect selective thermal processing of presolar carriers in the disk. The NC trend also cannot reflect the continuous addition of CC dust from the outer to the inner disk, because early- and late-formed NC meteorites display largely overlapping isotopic compositions. Instead, we find that the NC isotope heterogeneity is best accounted for by fractionation and mixing among chemically and isotopically distinct dust components, similar to the processes that produced the isotopic variability among carbonaceous chondrites. On this basis we argue for the presence of substructures in the inner disk, which facilitated fractionation and mixing among distinct dust components, and helped preserve a long-lived dust reservoir from which NC planetesimals accreted over an extended period of time.

### [C] 56.6 — MORFEO control strategy
- **arXiv:** [2608.13728](https://arxiv.org/abs/2608.13728)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (56.6), molecular_clouds (52.0), ism_methods_data (45.3)
- **Current keyword baseline:** NO
- **BM25 max:** 38.6
- **Semantic max:** 70.8
- **Abstract:** The ESO Extremely Large Telescope (ELT) will offer unprecedented sensitivity and resolution in the near-infrared, marking a new era for ground-based astronomy. Among its key imaging instruments is MORFEO coupled with MICADO. MORFEO (Multi-conjugate adaptive Optics Relay For ELT Observations), formerly known as MAORY, is the largest astronomical adaptive optics system ever designed. It features 12 wavefront sensors and three deformable mirrors, for a total of over 20,000 subapertures and over 6,000 actuators. MORFEO represents one of the greatest upcoming challenges in the field of astronomical adaptive optics. While the design builds upon the heritage of previous AO systems, several architectural choices are entirely new, driven by the unique scale and requirements of this instrument. One of the main challenges is delivering high and uniform wavefront correction across the MICADO field of view. To meet this goal, the MORFEO control strategy adopts a specific approach: sodium laser guide stars are used to sense modes above focus only, since differences in beacon altitude can introduce significant aberrations. Natural guide stars are instead employed to measure and correct for tip, tilt, plate scale variations, and field-averaged focus. In this work, we present the MORFEO control strategy and provide performance estimates across different observing scenarios.

### [C] 56.5 — Addressing position anomalies in the Strong Gravitational Lensing System HS~0810+2554 through Dark Matter Subhalos
- **arXiv:** [2608.15554](https://arxiv.org/abs/2608.15554)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, hep-ph
- **Top topics:** galactic_ism_surveys (56.5), ism_methods_data (53.3), astrochemistry (47.9)
- **Current keyword baseline:** NO
- **BM25 max:** 41.1
- **Semantic max:** 70.6
- **Abstract:** Self-bounded dark matter (DM) subhalos are predicted to populate galactic halos in great abundance in the Cold Dark Matter (CDM) scenario. These substructures can leave observable imprints in strong gravitational lensing and have shown the ability to account for flux-ratio and position anomalies in multiply imaged systems. In this paper, we utilize the DM subhalos to address the image position anomalies of the two radio quads of HS 0810+2554 observed with the Very Long Baseline Interferometry. We model the lens using an elliptical power-law macro-lens supplemented by a population of CDM subhalos from numerical simulations and perform a dual-source reconstruction to fit all eight radio images simultaneously. We find that subhalos below $10^{6}M_\odot$ induce astrometric shifts smaller than the measurement uncertainties, whereas more massive subhalos naturally generate the required milliarcsecond perturbations without significantly altering the global lens configuration. Including CDM subhalos improves the fit from $χ^2=60.38$ for the pure macro-lens to $χ^2=1.61$. Our results show that the position anomalies of HS~0810+2554 can be explained within the CDM framework and do not by themselves necessarily require non-standard scenarios like fuzzy DM or angular complexity in the macro-lens. Instead, they provide a sharp and testable manifestation of the subhalo population predicted by CDM.

### [C] 56.5 — The sensitivity of TESS to transiting planets in TOIs with close-in stellar companions
- **arXiv:** [2608.13527](https://arxiv.org/abs/2608.13527)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** star_formation (56.5), feedback_bubbles (53.7), ism_methods_data (52.4)
- **Current keyword baseline:** NO
- **BM25 max:** 31.7
- **Semantic max:** 70.7
- **Abstract:** High resolution imaging with optical speckle interferometry has revealed that many transiting exoplanet host stars possess close-in stellar companions. The objective of this study is to quantify how the presence of these companions impacts the ability of TESS to detect the transits of small planets. We accomplish this by examining 2052 TESS Objects of Interest (TOIs) that appear to be single-star systems based on speckle interferometric observations as well as 188 TOIs in unresolved ($< 1.2\arcsec$) stellar binaries. For each planet, we take its transit signal-to-noise ratio (SNR), radius, and orbital period from the TOI catalog and, for planets in stellar binaries, we correct the radius for dilution by the companion. By applying a scaling relation to the measured transit SNR of each TOI in our sample, we determine the detectability of transits in each TOI as a function of both planet radius and orbital period. When applied to the full sample, this procedure elucidates the sensitivity of TESS to transiting planets as a function of binarity, host-star spectral type, planet radius, and planet orbital period. These sensitivity grids quantify the bias against the detection of small planets in unresolved binaries by TESS and show that there is a particularly low sensitivity to planets transiting secondary stars in unresolved binaries, especially as the magnitude difference between the stars increases. These sensitivity grids are available for download to facilitate their use in other studies.

### [C] 56.4 — Asymmetric Aerosol Distribution on the Terminators of the Warm Saturn WASP-69 b Revealed by JWST NIRISS/SOSS
- **arXiv:** [2608.19756](https://arxiv.org/abs/2608.19756)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** feedback_bubbles (56.4), astrochemistry (51.8), star_formation (44.8)
- **Current keyword baseline:** NO
- **BM25 max:** 58.3
- **Semantic max:** 70.6
- **Abstract:** How aerosols form, are transported, and cycle between condensation and evaporation across exoplanet temperature regimes remains poorly understood. Recent models and observations suggest that warm giant planets near $800$--$1000$ K may span a transition between homogeneous and longitudinally heterogeneous aerosol distributions. We present a robust detection of aerosol asymmetry in a giant planet with $T_{\rm eq}\lesssim1000$ K, using the $0.86$--$2.82~μ$m JWST NIRISS/SOSS transmission spectrum of WASP-69 b. The evening limb shows prominent 1.4 $μ$m H$_2$O absorption ($Δ\mathrm{BIC}_{\rm H_2O}=+22.7$), whereas H$_2$O is not detected on the morning limb ($Δ\mathrm{BIC}_{\rm H_2O}=-8.7$). Atmospheric retrievals reveal significant aerosol opacity on both limbs, with high-altitude, optically thick clouds muting molecular features on the morning limb and lower cloud opacity allowing H$_2$O to emerge on the evening limb. The evening terminator is hotter by $304^{+62}_{-91}$ K, consistent with morning-limb condensates partially evaporating during transport toward the evening limb. This mechanism is independently verified with 3D general circulation models. Stellar contamination or aerosols dominated by photochemical haze do not readily explain the asymmetry. From a limb-resolved analysis, we infer a stellar-to-superstellar atmospheric metallicity, with $\rm[M/H]=0.11^{+0.40}_{-0.46}$ from the equilibrium retrieval and [O/H]$=1.38^{+0.44}_{-0.79}$ from the free retrieval. We also detect an escaping metastable-helium tail extending to $3.08^{+0.50}_{-0.45}\,R_p$. WASP-69 b anchors the cooler edge of the emerging population of planets with asymmetric aerosol distributions and suggests that substantial aerosol opacity may persist on both limbs across this transition.

### [C] 56.4 — Asteroseismology of the multiperiodic field SX Phe pulsator BL Camelopardalis
- **arXiv:** [2608.19076](https://arxiv.org/abs/2608.19076)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** molecular_clouds (56.4), magnetic_fields (55.5), astrochemistry (53.3)
- **Current keyword baseline:** YES
- **BM25 max:** 57.6
- **Semantic max:** 70.5
- **Abstract:** BL Camelopardalis (BL Cam) is the most metal-poor SX Phoenicis star known in the Galactic field, making it an excellent test bed for studies of Population II stellar structure and evolution, as well as for investigating the formation channels of blue straggler stars. We aim to constrain fundamental stellar parameters and pulsational properties of BL Cam and identify the nature of its observed oscillation modes. We analysed high-precision space-based data from the TESS mission and long-term ground-based observations from the Zwicky Transient Facility (ZTF) survey. The ZTF data were primarily used to derive the orbital parameters of the system, while the TESS light curves enabled us to extract a rich oscillation spectrum. We identified multiple pulsation frequencies and performed seismic modelling using a Bayesian approach. We detected numerous pulsation frequencies, including a dominant radial mode and additional non-radial components. We predicted all fitted modes in our seismic models as excited. The models reproduced the two highest amplitude-independent frequencies (i.e. the radial fundamental mode and a dipole mode) and suggested the possible presence of additional radial overtones. The inferred stellar parameters confirm the extremely low metallicity of BL~Cam. We also confirm its binary nature, with an orbital period of 144 days. BL Cam provides a valuable benchmark for testing stellar models of metal-poor pulsators. The combination of space-based photometry and Bayesian seismic modelling enables robust constraints to be placed on its internal structure and pulsation properties.

### [C] 56.4 — Simulation of advective accretion flows around black holes under various outer boundary conditions
- **arXiv:** [2608.18860](https://arxiv.org/abs/2608.18860)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (56.4), star_formation (49.1), turbulence (48.3)
- **Current keyword baseline:** NO
- **BM25 max:** 32.8
- **Semantic max:** 70.5
- **Abstract:** We simulated various accretion disc structures with viscous hydrodynamic (HD) flow around a black hole (BH). We found that the structure of the accretion disc is significantly influenced by changes in the physical parameters of the initial inflowing gases. These physical parameters can be called outer boundary conditions (OBCs) at the outer-accretion boundary and represented on an OBC plane, which is primarily divided into hot-mode and cold-mode inflowing gases. We found smooth and shocked flows in the simulation, which follow the semi-analytical solutions with their OBCs. Interestingly, we observed that certain types of OBCs can produce shocks with jet-like features in the accretion flow. However, other OBCs can produce smooth or shock-free accretion flow, which may or may not have outflows. The smooth flows can display both the lowest and highest angular momentum distributions among the advective flows, depending on the OBCs. Additionally, the nature of the accretion flows can be either steady or quasi-steady, also influenced by the OBCs. We also observed that solutions corresponding to hot-mode gases have a greater tendency to generate outflows compared to those with the cold-mode. Therefore, this qualitative study of OBCs is crucial for understanding accretion physics, which can aid in modeling accretion discs, similar to the quantitative studies (which involve only changing mass accretion rates) of the inflowing gases. Thus, we assert that an accretion model should be based on both the qualitative and quantitative aspects of the initial inflowing gases.

### [C] 56.4 — Accurately simulating gain and clock-induced charge production in the EMCCD gain register
- **arXiv:** [2608.17842](https://arxiv.org/abs/2608.17842)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP
- **Top topics:** astrochemistry (56.4), molecular_clouds (54.1), star_formation (53.8)
- **Current keyword baseline:** NO
- **BM25 max:** 47.9
- **Semantic max:** 67.6
- **Abstract:** An electron-multiplying charge-coupled device (EMCCD) is capable of precise detections in low-signal environments, able to detect a single photon through electron multiplication. It has many applications, such as faint-target astronomy, quantum optics, molecule tracing, and others, and it will be used for faint companion detection in the Roman Telescope's coronagraph instrument. In an EMCCD, photons hit the pixels, and photo-electrons are created; these are multiplied via impact ionization as they travel through the gain register from one gain stage to the next. A high gain means a high multiplication factor, and this is achieved through a high voltage difference across a gain stage. If the gain is high enough, the chance of clock-induced charge (CIC) production in the gain register increases. The probability distribution function governing the gain process typically used only accounts for charge multiplication if one or more electrons enter the gain register. I discuss my implementation of the simulation of this effect and its customization in emccd_detect, the EMCCD detector simulator used for the Roman Telescope. In addition, the simulator has been updated to use the exact binomial distribution for EM gain instead of the approximate Gamma distribution usually used in the literature, which is only valid for large counts. I also examine some EMCCD data and show through maximum likelihood estimation with CIC_gain_register that the data conform better to the binomial distribution versus the approximate Gamma/Erlang distribution. The use of the modified distribution would in principle improve the fidelity of Roman's testing and lead to better EMCCD calibration and more accurate signal extraction from a frame.

### [C] 56.1 — The initial evolution of SN 2011dh: The importance of inhomogeneities
- **arXiv:** [2608.17736](https://arxiv.org/abs/2608.17736)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** magnetic_fields (56.1), feedback_bubbles (54.8), molecular_clouds (48.4)
- **Current keyword baseline:** NO
- **BM25 max:** 66.5
- **Semantic max:** 63.0
- **Abstract:** SN 2011dh is rather unique in that it offered detailed observations of the initial phase in the radio as well as optical regimes. This makes possible a comparison between models used to deduce properties of the outer envelope of the supernova ejecta. It is shown that a consistent description suggests the forward shock to have started in the piston phase with constant velocity, and only later, around 50 days, transitioned to the standard model, which is independent of initial conditions. In addition, observations imply that the radio source is inhomogeneous with a covering factor of, approximately, 50%. It is emphasised that the deduced properties of the synchrotron source are very sensitive to the presence of inhomogeneities; for example, a covering factor of 50% increases the ratio of the energy densities of relativistic electrons and magnetic field by several orders of magnitude as compared to a homogeneous source. The shallow density gradient in the envelope causes substantial deceleration of the forward shock. This is used to argue that the magnetic field strength scales inversely with radius rather than inversely with time; this is similar to SN 1993J. Attention is also drawn to the similarities between the flat spectra of compact, extragalatic radio sources and the evolution of radio supernovae; e.g., the scaling of the magnetic field and the constant brightness temperature.

### [C] 56.1 — VERaiPHY -- Validation & Evaluation for Robust AI in PHYsics
- **arXiv:** [2608.17724](https://arxiv.org/abs/2608.17724)
- **Primary category:** hep-ph
- **Categories:** hep-ph, astro-ph.CO, hep-ex, physics.data-an, stat.ML
- **Top topics:** ism_methods_data (56.1), turbulence (52.4), feedback_bubbles (41.4)
- **Current keyword baseline:** NO
- **BM25 max:** 43.1
- **Semantic max:** 70.1
- **Abstract:** Modern machine learning is leading to substantial gains in precision, flexibility, and computational efficiency in fundamental physics. Statistical validation, uncertainty quantification, and robustness assessment are less systematically addressed. The VERaiPHY initiative (Validation & Evaluation for Robust AI in PHYsics) is a series of articles developed within the PHYSTAT programme, aimed at establishing statistical standards for the development, evaluation, and deployment of ML techniques. Each article focuses on a specific methodological domain from a statistics perspective and clarifies statistical questions, tests, and the interpretation of results. This opening article establishes the probabilistic, statistical, and machine learning foundations that the later contributions assume, together with the notation used throughout.

### [C] 55.9 — Climates of Gl 514 b
- **arXiv:** [2608.12457](https://arxiv.org/abs/2608.12457)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** molecular_clouds (55.9), star_formation (54.0), magnetic_fields (52.0)
- **Current keyword baseline:** NO
- **BM25 max:** 35.5
- **Semantic max:** 67.5
- **Abstract:** The continuous discovery of exoplanets, each with distinctive stellar and planetary properties, along with the development of higher resolution ground and space telescopes has positioned climate evolution as a fundamental component of the study of habitability. In particular, the planet Gl 514 b, located within the habitable zone of an M0.5 dwarf star 7.62 pc from Earth, is a candidate for direct observations with future ground and space-based telescopes and therefore worthy of climate modeling. One notable aspect of this planet is its eccentricity of $e = 0.45^{+0.15}_{-0.14}$, which could affect the seasonal climate by inducing large swings in instellation over the course of an orbit. Hence, we simulate a plausible range of climates on this planet to assess the likelihood that its surface is habitable as well as estimate the surface ice coverage, which could affect the photometric signal. To perform these simulations, we use an energy balance model to explore the parameter space permitted by the observations and the allowed ranges of the obliquity, eccentricity, atmospheric CO$_2$, precession angle, land fraction, and land distribution. We find the planet is most likely to be in either a snowball or ice free state, but about 1.27% of our simulations contain polar ice caps or an ice belt. A partial pressure of CO$_2$ in the range of 7.25-9.5 bar permits the planet's surface to be habitable. These results constrain the orbital, rotational, and physical conditions required for surface habitability of Gl 514 b and will help guide future direct-imaging surveys of this and similar planets.

### [C] 55.8 — Radar observations of Europa in 2011-2024: New insights into radar scattering properties
- **arXiv:** [2608.17689](https://arxiv.org/abs/2608.17689)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** magnetic_fields (55.8), ism_methods_data (52.8), molecular_clouds (50.4)
- **Current keyword baseline:** NO
- **BM25 max:** 49.3
- **Semantic max:** 63.0
- **Abstract:** Three of Jupiter's Galilean satellites - Europa, Ganymede, and Callisto - are of particular scientific interest due to their icy shells and suspected subsurface oceans. However, the radar properties of the icy satellites have not been measured since observations in 1987-1991. Because radio waves can penetrate pure ice to considerable depths, radar observations provide a powerful means of characterizing the subsurface properties of the icy shells of these satellites, offering key insights into planetary evolution. We have observed Europa using the Goldstone 3.5-cm Solar System Radar and the Green Bank Telescope (GBT) in 2011-2024 in order to address a longstanding gap in the radar studies of these moons. In this paper, we present the most longitudinally comprehensive set of radar measurements of Europa to date and describe its disk-integrated radar properties. On the basis of monostatic Goldstone data, we find radar albedo values in two circular polarizations of $\hatσ_{\rm OC}$ = 0.92 $\pm$ 0.11 and $\hatσ_{\rm SC}$ = 1.35 $\pm$ 0.13 (unweighted mean and root-mean-square dispersion), with a circular polarization ratio of $μ_c$ = 1.44 $\pm$ 0.12 (weighted mean and root-mean-square dispersion). Values obtained bistatically at the GBT are similar. The $μ_c$ values suggest a leading-vs-trailing side dichotomy in radar scattering properties on Europa. Our results support the existence of the coherent backscatter opposition effect (CBOE), currently the most widely accepted physical mechanism that explains the unusual radar scattering properties of the icy Galilean satellites. Because we observed Europa with a bistatic configuration, we can place a lower bound on the width of Europa's CBOE peak equal to 36 arcsec, which provides an upper bound of 32 m ($\sim$1000 wavelengths) on the penetrating depth of X-band radar waves at Europa.

### [C] 55.8 — Merging Galaxy Clusters and the Search for New Physics of Dark Matter: A Review
- **arXiv:** [2608.16987](https://arxiv.org/abs/2608.16987)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** massive_star_formation (55.8), star_formation (54.3), turbulence (53.3)
- **Current keyword baseline:** NO
- **BM25 max:** 40.5
- **Semantic max:** 69.8
- **Abstract:** Merging galaxy clusters represent one of the most powerful macroscopic laboratories in the Universe for searching for new physics within the dark sector. High-velocity cosmic collisions inherently separate the dark matter and stellar components from the highly collisional, X-ray-emitting intracluster gas. These massive systems provide an ideal environment to probe the fundamental nature of dark matter, specifically testing whether it behaves as a strictly collisionless particle or exhibits non-zero self-interactions. While pioneering systems like the Bullet Cluster historically demonstrated the macroscopic decoupling of dark and ordinary matter, the field has evolved into a sophisticated discipline driven by multi-disciplinary methodologies. This review synthesizes recent theoretical and empirical advances in interpreting post-collision dynamics. It examines how the synergy of combined approaches---integrating multi-wavelength observations from gravitational lensing and X-ray mapping with high-fidelity N-body hydrodynamical simulations---allows the translation of macroscopic spatial observables into stringent constraints on microscopic particle properties. Through this synthesis, the work evaluates how leveraging heterogeneous merger ensembles can reliably advance the ongoing search for physics beyond the standard cosmological model.

### [C] 55.7 — From Earth Meteors to Mars: Predicting Where to See the First Martian Meteors
- **arXiv:** [2608.16558](https://arxiv.org/abs/2608.16558)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** molecular_clouds (55.7), ism_methods_data (54.2), feedback_bubbles (49.5)
- **Current keyword baseline:** NO
- **BM25 max:** 30.6
- **Semantic max:** 69.6
- **Abstract:** Predictions of optical meteors at Mars have largely relied on classical single-body ablation models, despite high-resolution terrestrial observations showing that mm-sized meteoroids frequently fragment. This study quantifies how fragmentation alters the predicted brightness and peak-luminosity altitudes of sporadic mm-sized meteoroids in the Martian atmosphere and evaluates the single-body approximation as a reference baseline. Physical properties were inferred for 144 sporadic meteoroids observed on Earth using dynamic nested sampling with the erosion-fragmentation model. The resulting best-fit meteoroids were then re-simulated under Martian atmospheric conditions to generate predicted light curves. Because the physical trigger of fragmentation onset remains uncertain, three hypotheses were tested based on atmospheric mass density, dynamic pressure, and total accumulated heat. The results were also compared with predictions from a single-body ablation model. The data-driven simulations predict peak absolute magnitudes of $M_{\rm peak}\sim$ 2 - 7 for Martian meteors spanning diameters of 0.4 - 10 mm and entry speeds of 10 - 56 km/s. We find most events are luminous between $\sim$ 55 and 110 km heights. Relative to the single-body ablation baseline, the fragmentation-based predictions are brighter by $\sim$ 0.8 mag at peak brightness and concentrate luminosity within a narrower vertical range ($\sim$ 17 km instead of 36 km). The modelling accounting for fragmentation also produce shorter luminous trails ($\sim$ 20 km instead of 45 km). The resulting altitude-brightness maps provide observation-ready guidance for future Mars missions, while the fragmentation-based framework supports the interpretation of meteoroid-related ionospheric metal layers and improvements to Mars meteoroid-environment models.

### [C] 55.7 — A NICE (Nulling Interferometry Cryogenic Experiment) update: Beyond 1e-5 and towards cryogenic operation
- **arXiv:** [2608.16297](https://arxiv.org/abs/2608.16297)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** molecular_clouds (55.7), star_formation (43.1), ism_methods_data (42.7)
- **Current keyword baseline:** NO
- **BM25 max:** 29.1
- **Semantic max:** 69.6
- **Abstract:** The Nulling Interferometry Cryogenic Experiment (NICE) is a mid-infrared laboratory testbed at ETH Zürich that aims to not only reproduce the deep ($<1\times10^{-5}$) broadband nulls of the nulling testbeds of the early 2000s, but also at the required sensitivity levels expected for the LIFE space mission. This sensitivity enforces the experiment to go cryogenic at temperatures around 15 K; an ambitious task for an ultra-precise interferometer. We share our results of the ambient precursor experiment, demonstrating repeatable $<1\times10^{-5}$ nulls at a single wavelength and high throughput, and investigations into the nulling performance across a broader bandpass and with dual polarisation states. We will also highlight the push towards cryogenic operation, with the instalment of a new 15 K test cryostat that will inform our choices of materials and optomechanical mounting techniques.

### [C] 55.7 — Adapting the 23m LST-North mechanical structure design for the strong Chile seismic environment
- **arXiv:** [2608.15201](https://arxiv.org/abs/2608.15201)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (55.7), ism_methods_data (53.8), molecular_clouds (45.2)
- **Current keyword baseline:** NO
- **BM25 max:** 42.7
- **Semantic max:** 69.6
- **Abstract:** The 23-meter-diameter Large-Sized Telescope (LST) is the largest size telescope of the next generation Cherenkov Telescope Array (CTA). The first telescope, LST-1, was installed at the Roque de los Muchachos Observatory (ORM) on La Palma at an altitude of 2,250 m in 2018 and has been in operation since 2019. Its ultra-lightweight structure (110 tons) enables extremely rapid repositioning (180° in 18 seconds) and has been designed to withstand extreme environmental conditions, including storms and winds exceeding speed up to 200 km/h. To deploy the same solid telescope design at the CTA Southern Observatory in Chile, the structure must be adapted to the significantly higher seismic demands of the site. To address this challenge, the Max Planck Institute for Physics (MPP) has proposed the integration of a seismic isolation system with the proven LST-1 structural design. This approach substantially reduces seismic loads and dynamic amplification, thereby avoiding extensive structural modifications and enabling the existing telescope design to be transferred to the Chilean site with only minor adaptations. In this contribution, we present the proposed seismic isolation concept and its feasibility studies. MPP is responsible for the mechanical structure of the LST and has validated the concept through detailed finite-element analyses and long-term structural lifetime assessments.

### [C] 55.4 — The Gamma-ray Burst Jet Energy Distribution Suggests A Quasi-universal, Weakly Magnetized Jet Evolving Over Cosmic Time
- **arXiv:** [2608.16991](https://arxiv.org/abs/2608.16991)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (55.4), molecular_clouds (52.6), turbulence (51.8)
- **Current keyword baseline:** NO
- **BM25 max:** 36.4
- **Semantic max:** 69.2
- **Abstract:** We present distributions of gamma-ray burst observed and inferred properties for those GRBs with redshifts. We show that the isotropic energy distribution, which spans over four orders of magnitude, can be reproduced reasonably well under a simplistic assumption that every observed GRB originates from a quasi-universal jet with roughly the same decreasing power-law profile of energy as a function of angle, with a power-law index of $ 3 \lesssim ζ\lesssim 4$. The spread in the observed distribution can be explained by the variation in observer viewing angle alone. Furthermore, this power-law jet structure provides an even better fit to both the isotropic energy and luminosity distributions if the isotropic energy normalization evolves as a function of redshift in a manner that has been suggested by a range of previously published studies. The relatively steep power-law index of this jet is consistent with the structure predicted by simulations of weakly magnetized jets in collapsars, whereas simulations of hydrodynamic jets predict a structure shallower than what we find here. The predicted afterglow light curves within this model framework show steepening behavior at times commensurate with observed jet break times.

### [C] 55.4 — The detection prospects of the polarizations in the plateau phase of GRB afterglow by eXTP
- **arXiv:** [2608.15485](https://arxiv.org/abs/2608.15485)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (55.4), magnetic_fields (51.7), molecular_clouds (49.2)
- **Current keyword baseline:** NO
- **BM25 max:** 46.1
- **Semantic max:** 62.2
- **Abstract:** Approximately (20-50)$\%$ of the gamma-ray burst (GRB) X-ray afterglows exhibit the shallow decay features. Two popular energy-injection models had been proposed to interpret such observational phenomenons, the relativistic wind bubble (RWB) model with a Poynting-flux injection and the structured ejecta (SE) model with a dynamical energy injection. Polarization predictions of the two models had been investigated and can be used as a test of the two models. However, the impacts of the parameters on the model predictions were not studied and the comparisons with the detection ability of the forthcoming mission, enhanced X-ray Timing and Polarimetry (eXTP), had not been discussed. We considered the above issues and found that influences of the model parameters on the predicted polarizations of the two models are very limited. To perform a feasible polarization detection during the plateau phase, the priority ToO response is required. The detection probability of the GRB plateau phase is about $1/3$ for one pointing under the priority ToO. The polarization detection probability would depend on the ratio between the Poynting-flux injection to the dynamical energy injection, which is unclear currently. The predicted flux density and polarization degree (PD) of the RWB model could be well above the threshold flux and minimal detectable polarization degree of the polarimetry focusing array (PFA) on board eXTP, while the predicted PDs of the SE model would be difficult to be detected by eXTP/PFA. Therefore, a detection of a significant polarization signal during the GRB plateau phase would prefer the RWB model and the injected energy would be in the form of the Poynting flux, while a non detection of the polarized signal would indicate a dynamical energy injection of the SE model.

### [C] 55.3 — No Persistent Helium Absorption in LHS 1140 b: Four JWST/NIRISS SOSS Transits and Multi-epoch Stellar He I Variability
- **arXiv:** [2608.19120](https://arxiv.org/abs/2608.19120)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** star_formation (55.3), astrochemistry (54.1), molecular_clouds (52.8)
- **Current keyword baseline:** NO
- **BM25 max:** 68.5
- **Semantic max:** 69.1
- **Abstract:** The search for atmospheres on temperate terrestrial planets is important for understanding how these objects form and evolve, and their potential habitability. Recent transit observations of LHS 1140 b, a temperate ($T_{\rm eq}=226$ K) planet straddling the radius valley ($R_{\rm p}\approx1.7 R_\oplus$), with the WINERED high-resolution spectrograph yielded a detection of planetary atmospheric escape through the measurement of excess absorption ($1.24\pm0.23\%$) in the metastable helium triplet, although a later second visit resulted in a non-detection. We analyze four transits of LHS 1140 b and two of LHS 1140 c observed with JWST/NIRISS SOSS. We find no evidence of helium absorption in either planet, with all amplitudes consistent with zero within $1σ$. For LHS 1140 b, we derive $3σ$ upper limits of $0.72$--$1.21\%$. Individual visits disfavor the reported WINERED absorption at $2.6$--$3.7σ$, while their joint constraint disfavors a persistent signal at $4.5σ$. We find that the stellar He I line of LHS 1140 varies substantially between NIRPS and WINERED epochs, with both its strength and fractional variability consistent with the behavior of other M dwarfs. We also identify a moderate correlation between the 2024 He I depth and seeing, suggesting a possible seeing-dependent instrumental contribution. If the high-resolution detection is indeed planetary, the rate of such atmospheric loss events must be relatively low ($f=22_{-12}^{+17}\%$). Alternatively, stellar He I variability may contribute to the reported excess absorption. Additional high-resolution observations, both in and out of transit, are required to distinguish between these scenarios.

### [C] 55.3 — Machine Learning in Application to Automatic Noise Processing of Solar Spectrograms
- **arXiv:** [2608.16392](https://arxiv.org/abs/2608.16392)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, physics.optics
- **Top topics:** ism_methods_data (55.3), molecular_clouds (54.5), turbulence (45.8)
- **Current keyword baseline:** YES
- **BM25 max:** 48.0
- **Semantic max:** 69.1
- **Abstract:** In this paper, a machine learning approach for processing solar spectral data were developed. Its performance was demonstrated using the example of the limb solar flare on July 17th, 1981. The results indicated that machine learning can be effectively utilized to transform between differently digitized spectra, fill gaps in unique experimental data, and undertake spectrum cleaning. Specifically, convolutional neural networks were devised to transform between reflective and transmissive scans of a solar flare spectrogram. This can be a convenient technique for treating the spectrograms of unique solar events, most notably increasing the proportion of observational spectra that can be further analyzed. Namely, in subsequent research, we will be able to confidently incorporate data such as that captured on the edges of spectrograms, which was previously deemed insufficiently reliable due to limitations of available processing techniques. This will consequently increase the number of spectral lines studied for certain observed events, which is paramount for constructing physical models, as the spectral peculiarities are expected to manifest consistently across different spectral lines. The developed approach also notably facilitates the detection and removal of impurities in the spectrograms. Previously, each distinct feature in the spectra was manually scrutinized to check its integrity in order to be excluded if identified as an impurity, such as a scratch or a dust particle. By employing the suggested protocol for treating the spectrogram, which includes scanning the spectrogram using multiple distinct techniques and then leveraging machine learning for comparison, the process of excluding impurities can now be automated. Furthermore, the spectrum areas affected by such exclusions can be restored, enabling further analysis.

### [C] 55.3 — Jet Power, Bulk Lorentz Factor, Black Hole Spin, and Magnetic Field of Accretion Disk in Jetted Active Galactic Nuclei: A Large Gamma-Ray Emission Sample
- **arXiv:** [2608.15498](https://arxiv.org/abs/2608.15498)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (55.3), turbulence (49.9), magnetic_fields (49.2)
- **Current keyword baseline:** NO
- **BM25 max:** 76.1
- **Semantic max:** 69.1
- **Abstract:** We present a catalog of physical parameters for powerful jet-accretion disk-black hole systems in one of the largest samples of gamma-ray emitting jetted active galactic nuclei (AGNs), including jet kinetic and radiative powers, jet radiative efficiencies, bulk Lorentz factors, black hole spins, accretion-disk magnetic fields and Compton dominance. Comparing jet kinetic power estimators for blazars, values derived from spectral energy distribution (SED) fitting tend to exceed those estimated via cavity power and other scaling relations. For radiatively efficient AGNs, most sources are inferred to possess high spins; for radiatively inefficient AGNs, many potentially have high spins, though some may differ. This indicates that black hole spin does not effectively distinguish radiatively efficient from inefficient jetted AGNs. Our results suggest accretion-disk magnetic field strength as a key discriminator, proposing a tentative dividing value of $\approx 10^{3.9}$ Gauss between radiatively efficient and inefficient populations. Jet power and bulk Lorentz factor exhibit significant correlations with black hole mass in radiatively efficient AGNs, while weak-to-moderate correlations are observed in radiatively inefficient AGNs within narrow accretion-rate bins. Our analysis reveals that jet power correlates with both disk luminosity and magnetic field strength. Furthermore, correlations linking Eddington ratio and Compton dominance with jet properties are consistent with the jet-accretion connection. Finally, jet radiative power and bulk Lorentz factor show a potential dependence on black hole spin. These results are consistent with the scenario in which jets are powered and accelerated by energy extraction from rapidly spinning black holes via accretion-disk magnetic fields.

### [C] 55.3 — Optical development of the BISOU breadboard
- **arXiv:** [2608.13225](https://arxiv.org/abs/2608.13225)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.CO
- **Top topics:** ism_methods_data (55.3), astrochemistry (51.8), magnetic_fields (46.6)
- **Current keyword baseline:** NO
- **BM25 max:** 50.3
- **Semantic max:** 64.8
- **Abstract:** BISOU (Balloon Interferometer for Spectral Observations of the primordial Universe) is an astronomical balloon-borne pathfinder developed as part of a preparatory study for a future space mission aimed at measuring spectral distortions of the cosmic microwave background (CMB). A laboratory breadboard of the instrument is being developed at the Institut d'Astrophysique Spatiale (IAS), enabling the characterization of subsystems and instrument systematic effects, particularly in the optical system. The optical system is based on a differential polarizing Fourier Transform Spectrometer (FTS) that receives inputs from both a sky-facing telescope and an internal calibration source. The FTS focal planes include sub-K detectors coupled to multimode feed horns. The full spectral band, spanning between 90 and 1500 GHz, is sub-divided into two frequency sub-bands, thanks to the use of a dichroic. The optical analysis first relies on ray-tracing simulations to establish the overall configuration of the system, before proceeding to more advanced Gaussian beam and physical optics analyses.

### [C] 55.2 — A generalized quadratic balance relation for nonradial nonadiabatic pulsations
- **arXiv:** [2608.18697](https://arxiv.org/abs/2608.18697)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** star_formation (55.2), ism_methods_data (51.7), turbulence (47.9)
- **Current keyword baseline:** NO
- **BM25 max:** 38.1
- **Semantic max:** 69.0
- **Abstract:** We derive a generalized quadratic balance relation for linear nonadiabatic, nonradial stellar pulsations, starting from a sesquilinear amplitude analogue of the pressure-volume-rate work. The derivation requires neither weak nonadiabaticity nor averaging over a pulsation cycle. The relation is expressed in terms of work, generalized norm and boundary contributions and is subsequently recast into kinetic-energy-power form $\mathcal{P}+ΔB=2\Re(σ)E_{\rm kin}$. The volume power is decomposed into a thermodynamic exchange term and response terms associated with compression, horizontal-area deformation and gravitational stratification effects. The equivalent forms of the relation provide diagnostics for checking the computed eigenfrequencies and estimating mode excitation rates. The properties of the balance relation for various types of modes in an envelope of a model AGB star are examined. We analyze the terms entering the power $\mathcal{P}$ for radial and nonradial p-modes, strange modes as well as examples of low frequency outer-envelope gravity modes and thermal modes. The results show that the magnitude of mode driving is not determined solely by the thermodynamic work term.

### [C] 55.1 — The Roman Coronagraph Community Participation Program: Using the Zernike wavefront sensor for a full characterisation of the Roman Space Telescope and the Coronagraph Instrument
- **arXiv:** [2608.17740](https://arxiv.org/abs/2608.17740)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** molecular_clouds (55.1), ism_methods_data (49.7), magnetic_fields (46.2)
- **Current keyword baseline:** NO
- **BM25 max:** 37.4
- **Semantic max:** 68.9
- **Abstract:** The Roman Space Telescope Coronagraph Instrument (CGI) will demonstrate a series of technologies and techniques to enable the direct detection of reflected-light planets with space-based observatories. Among the several available observing modes and coronagraphic devices embarked in CGI, there is the transmissive dual-path Zernike wavefront sensor (ZWFS) that could be used to directly measure optical aberrations in the system. The dual-path ZWFS is currently unsupported, but in this work we advocate for the commissioning of this unique observing mode. We investigate the sensitivity of the ZWFS using CGI simulator and other tools developed and supported by the Roman community participation program (CPP). This type of analysis is crucial for understanding the stability of the Roman observatory and to prepare the path towards HWO.

### [C] 55.0 — Stability Mapping of the New Uranian Moon S/2025 U1 with Updated Masses for Cordelia, Ophelia, and Cressida
- **arXiv:** [2608.16078](https://arxiv.org/abs/2608.16078)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** magnetic_fields (55.0), astrochemistry (47.1), feedback_bubbles (46.5)
- **Current keyword baseline:** NO
- **BM25 max:** 42.8
- **Semantic max:** 68.8
- **Abstract:** We investigate the dynamics of Uranus's inner satellite system considering three recent updates: the inclusion of the new moon S/2025~U1, revised mass estimates for Cordelia, Ophelia, and Cressida, and updated zonal harmonic coefficients (J$_2$, J$_4$, and J$_6$). Using numerical integrations, mean-motion resonance analysis, and Frequency Map Analysis (FMA), we explore their impact on orbital stability. For the first time, we analyze the dynamics of the newly discovered moon S/2025~U1 and find that it follows a stable orbit, exhibiting smooth variations in its orbital elements over 250,000~years. Depending on the adopted radius, the gravitational influence of S/2025~U1 on the surrounding region is more compatible with a body of approximately 5-7 km radius, producing diffusion maps associated with a regular orbital evolution. Furthermore, the case $R = 7$ km shows a reduction in the diffusion of neighboring satellites, suggesting a possible local stabilizing effect on the system's orbital evolution. We also identified inner and outer regions of low diffusion around its orbit, suggesting that the dynamical environment is compatible with survival of coorbital particles or additional small satellites. In contrast, very high radius values, particularly $R = 20$ km, tend to increase diffusion among neighboring satellites, making this scenario less compatible with a dynamically stable orbital configuration. We further explore the survival of hypothetical satellites near S/2025~U1. Our results show that bodies with masses up to $3\times$ that of S/2025~U1 can remain stable in both the interior (between S/2025~U1 and Ophelia) and the exterior (between S/2025~U1 and Bianca) of its orbit. Finally, Cressida, Desdemona, Juliet, and Portia are most sensitive to updated parameters. Most resonances circulate, while Belinda-Perdita 44:43 confines the system with reduced libration amplitude.

### [C] 55.0 — Determining low-$\ell$ p-mode frequency shifts in Sun-like stars: Enhancing the cross-correlation technique with filters
- **arXiv:** [2608.15364](https://arxiv.org/abs/2608.15364)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, physics.data-an
- **Top topics:** turbulence (55.0), magnetic_fields (54.0), ism_methods_data (49.6)
- **Current keyword baseline:** NO
- **BM25 max:** 49.3
- **Semantic max:** 68.7
- **Abstract:** Acoustic mode frequencies in the Sun and Sun-like stars change due to magnetic activity, on time-scales much larger than the star's rotation and much smaller than its evolution. Given the poor S/N of the observed stellar p-modes, it is challenging to measure the changes of individual mode frequencies. Typically, power spectra of different time series segments are cross-correlated to estimate a mean p-mode frequency change, which ends up averaging over the individual mode contributions. We seek to enhance the cross-correlation method, by introducing a novel and computationally cheap method, thus enabling us to disentangle p-mode frequency changes for different spherical harmonic degree $\ell$. Assuming that the inclination angle and rotation rate are already measured, filters are designed, which enable the isolation of $δω_\ell$, frequency changes of modes with a given $\ell$, while preventing bias creeping in from neighbouring modes. Monte-Carlo simulations are performed to quantify uncertainty in the estimation of $δω_\ell$. We validate our method against well-studied solar data (SOHO/VIRGO and BiSON) and demonstrate its applicability to the solar-like Kepler star KIC 8006161.

### [C] 54.9 — The Shape of the Vertical Action Distribution Locates the Scatterers that Heat the Galactic Disc
- **arXiv:** [2608.12156](https://arxiv.org/abs/2608.12156)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.IM
- **Top topics:** molecular_clouds (54.9), star_formation (53.5), galactic_ism_surveys (51.7)
- **Current keyword baseline:** YES
- **BM25 max:** 60.5
- **Semantic max:** 66.9
- **Abstract:** The Milky Way's stellar disc is thicker than the cold gas layer from which its stars form. What scatters stars onto orbits with greater vertical motion remains unresolved. Scatterers could fill the disc volume, as bending waves or dark substructure would, or could be confined to the midplane, as giant molecular clouds are. Scattering from a midplane layer occurs only during the fast plane-crossing phase and becomes less effective as that speed increases, whereas a volume-filling perturbation remains effective near the slow turning points. We derive the distribution of vertical action this leaves behind, for any height distribution of scatterers. The geometry turns out to enter only through the logarithmic slope of the diffusivity in action, $D\propto J_z^{b}$, and solving the Fokker-Planck equation gives $p(J_z)\propto\exp[-(J_z/J_0)^{2-b}]$. Scatterers that fill the volume give $b=1$ and an exponential, a thin layer at the midplane gives $b=1/2$ and a sharper cutoff: the shape of $p(J_z)$ records where the scatterers sit, the growth of its scale how strongly they scatter. We fit this model to 7589 low-$α$ red clump stars of Ting & Rix (2019) between 5 and 10 kpc and 2 and 8 Gyr old, leaving the heating history free. This yields $b=0.51^{+0.06}_{-0.07}$, consistent with the thin-layer prediction but not the volume-filling one. Comparing the 2-4 Gyr heating amplitude with the present molecular surface density gives an effective scatterer mass of $2.7\times10^{6}\,M_\odot$. Older stars have experienced more of the Galaxy's gas-richer past; correcting for that history brings all four age bins to $(1.9-2.8)\times10^{6}\,M_\odot$, inside the range cloud catalogues and mass functions give. The Milky Way's disc is heated near the plane, by an evolving population of objects of giant-molecular-cloud mass.

### [C] 54.8 — Dynamics of tidal dwarf galaxies in the system Arp 72
- **arXiv:** [2608.18385](https://arxiv.org/abs/2608.18385)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (54.8), turbulence (52.2), feedback_bubbles (49.5)
- **Current keyword baseline:** NO
- **BM25 max:** 70.2
- **Semantic max:** 68.5
- **Abstract:** Some interactions between galaxies produce tidal tails primarily composed of material from their disks. Within these tails, concentrations of gas and stars can form, resembling dwarf galaxies. These tidal objects often begin to form stars and become dynamically independent of their parent galaxies, leading to their classification as Tidal Dwarf Galaxies (TDGs). By definition, TDGs should consist solely of baryonic material, with a negligible dark matter fraction. In this study, we analyze the dynamics of two TDGs in the Arp 72 system using high-resolution Hα observations obtained with the MEGARA multi-spectrograph at the GTC (Gran Telescopio Canarias) and neutral hydrogen (HI) data from the GMRT (Giant Metrewave Radio Telescope). The HI data were also used to determine the gas mass. We derived the rotation curves and velocity dispersion from the kinematic data, which allowed us to estimate the dynamical mass of the systems. The TDGs were modeled through 3D fitting as rotating disks with additional pressure support, assuming a mass distribution following an exponential law. The gas mass was combined with the stellar mass to determine the total baryonic mass. Under specific dynamical considerations, we established the relationship between the dynamical mass and the baryonic mass. Additionally, we used the pressure-support corrected circular velocity to compare the behavior of TDGs in the context of the baryonic Tully-Fisher relation (BTFR) with the literature, showing how detached TDGs fall off the relation. The two studied objects are consistent with the expected properties of a TDG.

### [C] 54.6 — On coordinate frames relevant for pulsar physics
- **arXiv:** [2608.18501](https://arxiv.org/abs/2608.18501)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** magnetic_fields (54.6), molecular_clouds (45.8), star_formation (44.0)
- **Current keyword baseline:** NO
- **BM25 max:** 35.1
- **Semantic max:** 68.2
- **Abstract:** Pulsars can be either isolated or binary (or even in triple) systems. Observational features of pulsars are used to probe various aspects of fundamental physics, including emission mechanism, gravitational physics, etc. Theoretical models of various phenomena need different coordinate frames. Often different physical processes affect each other and we need to use multiple coordinate frames and relations between those. This short review presents an extensive set of coordinate frames and relations between those.

### [C] 54.6 — Direct Imaging and Gradient-Based Analysis of the 12 August 2026 Partial Solar Eclipse from a Freely Rotating High-Altitude Balloon
- **arXiv:** [2608.16257](https://arxiv.org/abs/2608.16257)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (54.6), magnetic_fields (52.3), molecular_clouds (50.3)
- **Current keyword baseline:** NO
- **BM25 max:** 55.6
- **Semantic max:** 68.3
- **Abstract:** We report a proof-of-concept observation of the partial solar eclipse of 12 August 2026 using a freely rotating high-altitude balloon launched from Oldenburg, northern Germany. The payload carried two Insta360 ONE RS cameras equipped with 4K Boost wide-angle lenses; covered by filter material taken from a BRESSER eclipse viewing glass. Interval photographs were acquired every 10 s at ISO 800 and 1/1000 s. Of approximately 1,300 images, 21 contained a directly visible image of the eclipsed Sun, spanning 19:19:15-20:38:21 CEST and both sides of the local eclipse maximum. To test whether quantitative eclipse information could be recovered from these small, non-stabilized wide-angle images, the visible solar area was estimated using a two-dimensional gradient-based solar edge analysis and normalized to the first observation. The image-derived obscuration followed the independently calculated eclipse geometry with Pearson r = 0.959, a mean absolute difference of 9.5 percentage points, and an RMSE of 11.5 percentage points. Systematic deviations are consistent with the limitations of an uncalibrated action-camera system, including point-spread function, field-dependent lens response, filter geometry, and camera-to-camera differences. The results demonstrate that passive payload rotation can yield both visually useful and semi-quantitative direct eclipse observations without active solar pointing, and define a calibration strategy for future balloon-borne eclipse measurements.

### [C] 54.5 — Multi-zone Modeling of Blazar Jets: Constraints from GeV-Optical Correlation and Short-Timescale Variability
- **arXiv:** [2608.18707](https://arxiv.org/abs/2608.18707)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** galactic_ism_surveys (54.5), molecular_clouds (51.1), feedback_bubbles (48.4)
- **Current keyword baseline:** NO
- **BM25 max:** 78.7
- **Semantic max:** 68.1
- **Abstract:** We have developed a multi-zone model of blazar jet emission, in which the emission region contains many cells with individual magnetic fields and electron energy distributions. Nonthermal emission from radio to $γ$-rays is generated by electrons accelerated by shocks passing through the region via synchrotron and inverse-Compton (IC) processes. The optical and GeV variability at days-to-months time-scale simulated from our model are strongly correlated with no significant time lag, as observed in most blazars and indicated by the standard shock-in-jet model. However, the mechanism of the shorter time-scale variability has been less explored, although such fluctuations at X-rays, $γ$-rays and optical bands have been observed regularly in recent years. In our model, the hr time-scale variability of the synchrotron radiation is due to the spatial fluctuation of the magnetic field in the emission region. We found that to reproduce the short-timescale variability of the observed synchrotron emission in blazars, the required fluctuations of the magnetic field are in the range $1-2\%$ to $25-30\%$. Similar variability of the IC emission, which does not depend on the magnetic field, may be reproduced in our model by implementing equipartition of energy between the magnetic field and particles. We found that orphan flares in the optical or GeV band, or optical-GeV correlation with a significant time delay, as observed occasionally, may be reproduced in certain special conditions related to the orientation of the magnetic field in the cells.

### [C] 54.5 — Nuclear Drip Line and the Composition of Supernova Matter
- **arXiv:** [2608.16778](https://arxiv.org/abs/2608.16778)
- **Primary category:** nucl-th
- **Categories:** nucl-th, astro-ph.HE, astro-ph.SR, nucl-ex, physics.comp-ph
- **Top topics:** feedback_bubbles (54.5), star_formation (53.0), astrochemistry (50.5)
- **Current keyword baseline:** YES
- **BM25 max:** 44.0
- **Semantic max:** 63.1
- **Abstract:** The nuclear drip line plays a crucial role in determining the composition of matter under extreme astrophysical conditions. In core-collapse supernovae and neutron-star crusts, matter is driven far from saturation density and nuclear stability; nuclei coexist with a sea of free neutrons, an effect that is present even at zero temperature in neutron-star crusts and becomes more pronounced in the hotter, neutron-rich supernova environment. This makes a careful treatment of drip-line physics essential for a realistic description of the equation of state and composition. In this work, the influence of the nuclear drip line on the baryonic composition of supernova matter is investigated within the framework of nuclear statistical equilibrium (NSE). The composition is evaluated in terms of free nucleons, light clusters, and heavy nuclei at finite temperature and global sub-saturation densities. The results indicate that, at low proton fractions and higher densities, the inclusion of nuclei beyond the drip line enhances the formation of extremely neutron-rich light clusters, leading to a significant reduction in the free-neutron density and the charge fraction of heavy nuclei. These findings demonstrate that drip-line physics has a significant impact on the composition of supernova matter and should be carefully incorporated in supernova modeling and nucleosynthesis studies.

### [C] 54.3 — SN 2021pfs: A Type Ia Supernova Likely Affected by Progenitor Metallicity, as Revealed by Comparison with Its Twin Counterpart
- **arXiv:** [2608.19929](https://arxiv.org/abs/2608.19929)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, astro-ph.GA, astro-ph.HE
- **Top topics:** star_formation (54.3), feedback_bubbles (53.8), astrochemistry (50.4)
- **Current keyword baseline:** NO
- **BM25 max:** 46.7
- **Semantic max:** 67.8
- **Abstract:** We present extensive photometric and spectroscopic observations of the normal type Ia supernovae (SNe Ia) 2021pfs, which occurred in the Seyfert 2 galaxy NGC 5427 at a redshift 0.009. SN 2021pfs reached an absolute \textit{B}-band peak magnitude of $M_{\rm max}(B)=$-19.28 $\pm$ 0.40 mag. The mag and a post-peak decline rate of $Δm_{15}(B)=$1.13 $\pm$ 0.06 mag. The observed properties of this nearby SN Ia closely resemble those of SN 2011fe, including the main optical spectroscopic features and photometric evolution. Despite their similar decline rates, SN 2021pfs rose more rapidly in the $U$ band but more slowly in the $r$ and $i$ bands compared to SN 2011fe in very early phases. This photometric difference, particularly at short wavelengths, can introduce a systematic uncertainty of up to $\sim$12% in distance estimates. Analysis of the host galaxy's local and global environment shows an environment consistent with producing a higher-metallicity progenitor for SN 2021pfs than that of SN 2011fe.This higher progenitor metallicity may explain the observed photometric discrepancy and the resulting distance between SN 2021pfs and SN 2011fe, though a larger sample of such "twin" SNe Ia is needed to confirm this trend and assess its impact on cosmological measurements.

### [C] 54.2 — Hydrogen Engulfment into Sub-Neptune Cores through Magma Ocean Convective Surface Renewal
- **arXiv:** [2608.14518](https://arxiv.org/abs/2608.14518)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** feedback_bubbles (54.2), star_formation (46.8), astrochemistry (43.1)
- **Current keyword baseline:** NO
- **BM25 max:** 34.8
- **Semantic max:** 67.8
- **Abstract:** A convective surface renewal explanation for ingassing of hydrogen from H2-rich envelopes into molten cores of growing planets is presented, with particular application to sub-Neptunes. The ingassing of hydrogen occurs at a moving front comprising the upper boundary of the magma ocean that engulfs hydrogen from the envelope above as it moves. The mechanism of engulfment is surface renewal as the upper diffusive boundary layer is diluted by convection. Surface renewal results in ingassing even where the stabilizing buoyancy of the low-density hydrogen neutralizes the destabilizing thermally-driven buoyancy. It is ultimately driven by cooling. Beginning during the gaseous disk phase, when hydrogen is effectively available in infinite supply, sub-Neptunes can acquire enough hydrogen to permit global core-envelope equilibrium. The structures are therefore consistent with hydrogen-rich, supercritical magma oceans overlain by hydrogen-rich envelopes. The process of surface renewal has implications for other magma ocean - atmosphere interactions in general.

### [C] 54.1 — A metallicity sweet spot for disc fragmentation and planet formation
- **arXiv:** [2608.18830](https://arxiv.org/abs/2608.18830)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** massive_star_formation (54.1), feedback_bubbles (53.6), molecular_clouds (52.3)
- **Current keyword baseline:** YES
- **BM25 max:** 37.5
- **Semantic max:** 67.6
- **Abstract:** Fragmentation of gravitationally unstable discs offers an alternate formation mechanism for gas giant planets and brown dwarfs on wide orbits. Metallicity plays a key role in disc evolution from the onset of gravitational instability to the formation of planets. We aim to determine the effect of metallicity on disc fragmentation and on the properties of disc-instability planets. We model gravitationally unstable discs with varying metallicity ($0.01-10 \,\rm Z_{\odot}$) using the Smoothed Particle Hydrodynamics code PHANTOM. Our simulations reveal a "sweet spot" for fragmentation at $0.3 \,\rm Z_{\odot}$, where cooling is most efficient, with fragmentation also happening less vigorously at higher and lower metallicities. However, further away from the sweet spot, fragmentation becomes more difficult and is eventually suppressed at extreme low and high metallicities ($0.01 \,\rm Z_{\odot}$ and $10 \,\rm Z_{\odot}$, respectively), where the disc cools inefficiently. Discs with metallicities close to the sweet spot form more planets per disc, faster, and with lower initial masses than fragmenting discs with higher or lower metallicities. Our results may explain the slight overabundance of wide-orbit giant planets observed around metal-poor stars; these planets may have formed via disc fragmentation.

### [C] 54.0 — Validating direct solvers for Newton's gravitational N-body problem, and the systematic comparison between IEEE floating point and Posits
- **arXiv:** [2608.17032](https://arxiv.org/abs/2608.17032)
- **Primary category:** physics.comp-ph
- **Categories:** physics.comp-ph, astro-ph.IM, cs.PL, nlin.CD
- **Top topics:** star_formation (54.0), ism_methods_data (45.8), molecular_clouds (45.6)
- **Current keyword baseline:** NO
- **BM25 max:** 36.8
- **Semantic max:** 67.5
- **Abstract:** We present a systematic comparison between arbitrary precise arithmetic and integration, IEEE-754 compliant floating point arithmetic (fp16, bfp16, fp32, double precision fp64, and quadruple precision fp128), and two implementations of Posits (type III unum) for solving Newton's chaotic N-body problem. Each implementation is benchmarked with arbitrary precise calculations to objectively evaluate their performance in precision as well as speed. We rely on hardware and compiler implementations for fp64, and software implementations for arbitrary-precision arithmetic and Posits. Half precision arithmetic (fp16, bfp16, and Posits$<16,1>$) are insufficiently precise for solving Newton's equations of motion. Single precision (fp32, and Posits$<32,2>$) could be used for statistical ensemble calculations, but lead to relatively large errors in any individual strong encounter. All 64-bit implementations fp64 as well as Posits (Posits$<64,3>$) experience difficulty in our tests. One of the implementations of Posits (Universal) gives precision comparable to fp64 but is slow (by at least an orders of magnitude compared to fp64 after correcting for the more efficient hardware support for the latter). The other (CPPPosits) has a speed comparable to fp64 but has systematically larger errors (by about an order of magnitude compared to fp64 with excesses exceeding two orders of magnitude). As a consequence, this implementation leads to a systematic drift in the result space and has difficulty resolving close encounters. Posits and fp64 have difficulty when integrating a dynamical system in a moving reference frame; testing Galileo invariancy. In their current implementation, Posits do not seem to be the ideal alternative for fp64 when integrating chaotic or stiff ordinary differential equations, such as Newton's equations of motion.

### [C] 53.8 — Altitude-Dependent Near-Source Spectral Filtering of Meteor Infrasound Above 80 km and Consequences for Period-Based Energy Estimates
- **arXiv:** [2608.13853](https://arxiv.org/abs/2608.13853)
- **Primary category:** physics.ao-ph
- **Categories:** physics.ao-ph, astro-ph.EP, physics.geo-ph, physics.space-ph
- **Top topics:** molecular_clouds (53.8), turbulence (53.0), star_formation (52.0)
- **Current keyword baseline:** NO
- **BM25 max:** 37.0
- **Semantic max:** 67.3
- **Abstract:** Infrasound signal period is widely used as a proxy for source energy in bolide studies, but the reliability of period-yield relations for small, high-altitude regional meteors has not been systematically evaluated. We analyze 90 infrasound detections from well-constrained regional meteoroid events (source altitudes 20-111 km, ranges 47-268 km) and demonstrate a strong, monotonic decrease in receiver dominant frequency with increasing source altitude (Spearman r_{s} = -0.629, p = 3.3 x 10^11). No detections above 80 km retain dominant frequencies exceeding 3 Hz, and 75% of detections above 100 km are dominated by sub-1 Hz content. Partial correlation analysis indicates this is primarily an altitude effect, not a propagation distance artifact. Near-source dissipation modeling using the generalized Burgers equation supports a physical mechanism: the exponential increase in kinematic viscosity with altitude drives the acoustic Reynolds number downward, imposing frequency-dependent molecular absorption that selectively attenuates high-frequency content within the first 5 km below the source. Our results suggest that this atmospheric low-pass filter systematically modulates the observed period and can bias period-based energy estimates upward by one to two orders of magnitude for sources above 80-90 km when uncorrected period-yield relations are applied. These findings are relevant to any high-altitude infrasound source, including space debris and controlled reentries.

### [C] 53.8 — Explosions from Rotating Very Massive Star Collapses to Black Holes: Effects of Nuclear Burning
- **arXiv:** [2608.13642](https://arxiv.org/abs/2608.13642)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, gr-qc
- **Top topics:** star_formation (53.8), feedback_bubbles (51.9), ism_methods_data (51.2)
- **Current keyword baseline:** NO
- **BM25 max:** 73.4
- **Semantic max:** 64.8
- **Abstract:** We investigate the collapse of rotating very massive and supermassive stellar cores using numerical relativity simulations including an alpha-chain nuclear reaction network and neutrino cooling. Our main survey focuses on newly constructed models with initial core masses of $2 \times {10}^{3}-5\times 10^4M_\odot$. The collapse is triggered either by pair instability in lower-mass cores or by general-relativistic instability in higher-mass cores. We find that higher-mass cores undergo a nearly homologous collapse, whereas lower-mass cores show a more runaway-like collapse because neutrino cooling becomes more efficient at their higher densities and temperatures. Consequently, the black hole formed in lower-mass models initially contains a smaller fraction of the core mass, and disk formation occurs while a larger amount of matter remains outside the black hole. The lower compactness of pair-unstable cores also allows larger dimensionless angular momentum, favoring the formation of rapidly rotating black holes and massive disks. The disk bounce drives mass ejection with ejecta masses of order $10-10^3M_\odot$ and kinetic energies of order $10^{53}-10^{55}\,\mathrm{erg}$. Significant $^{56}$Ni production in the disk-bounce ejecta occurs only in the lowest-mass models. For selected models, we further follow the viscous evolution of the disk and find that viscosity enhances the ejecta mass and kinetic energy. In models with $\lesssim10^4M_\odot$, the viscosity-driven ejecta can originate from disk matter that has reached nuclear statistical equilibrium and can therefore become rich in $^{56}$Ni. These results suggest that rotating very massive star collapses can produce massive, energetic ejecta and, for sufficiently low core masses, substantial iron-group elements.

### [C] 53.6 — Quasi-periodic Eruptions from Recurrent Satellite Black Hole Transits through Magnetized Galactic Nucleus Accretion Disks
- **arXiv:** [2608.19796](https://arxiv.org/abs/2608.19796)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA
- **Top topics:** feedback_bubbles (53.6), molecular_clouds (46.9), galactic_ism_surveys (44.4)
- **Current keyword baseline:** NO
- **BM25 max:** 77.1
- **Semantic max:** 67.0
- **Abstract:** Quasi-periodic eruptions (QPEs) are recurrent soft X-ray flares from galactic nuclei, but their origin remains uncertain. The delayed ultraviolet (UV) counterpart detected in Ansky provides a new constraint on viable models. We present a two-channel model in which a satellite black hole (sBH) repeatedly crosses a nuclear accretion disk threaded by a large-scale magnetic field. Gravitational focusing and dynamical drag generate hot, optically thick ejecta whose expansion and photon diffusion power the soft X-ray QPE. For fiducial Bondi-scale parameters, the model yields a characteristic X-ray duration of $\sim10^3\ \mathrm{s}$ and luminosity of $\sim10^{42}\ \mathrm{erg\,s^{-1}}$; at lower orbital inclinations, the duration extends to the day-long scale observed in Ansky. Simultaneously, the sBH motion compresses and bends the background magnetic field, triggering in-disk reconnection. The dissipated energy then emerges after photon diffusion as a broader, delayed UV response. The resulting thermal power is comparable to the variable UV luminosity of Ansky. Unfavorable magnetic fields or diffusion times longer than the QPE recurrence period can weaken or smear out the UV signal, potentially explaining the lack of clear UV counterparts in other QPE sources.

### [C] 53.6 — Massive cold hybrid stars in a modified Polyakov-Nambu-Jona-Lasinio model
- **arXiv:** [2608.12653](https://arxiv.org/abs/2608.12653)
- **Primary category:** hep-ph
- **Categories:** hep-ph, astro-ph.HE, gr-qc, nucl-th
- **Top topics:** turbulence (53.6), star_formation (53.3), ism_methods_data (52.5)
- **Current keyword baseline:** NO
- **BM25 max:** 46.4
- **Semantic max:** 67.0
- **Abstract:** We propose a modified Polyakov-loop Nambu--Jona-Lasinio (mPNJL) model in which the Polyakov potential is given by an explicit dependence on the quark chemical potential, allowing it to remain finite at zero temperature and thus to describe the confinement-deconfinement transition in cold dense matter. Combining this modified quark sector with hadronic equations of state via a Maxwell construction, we find that, depending on the model parameters, the equation of state can exhibit either two phase transitions, from hadronic matter to confined (quarkyonic) quark matter and subsequently to deconfined quark matter, or a single transition directly from hadronic to deconfined quark matter or from hadronic to quarkyonic quark matter. Stable massive cold hybrid stars with only quarkyonic and/or deconfined quark phase are obtained. We systematically examine how the parameters of the modified Polyakov potential and the quark vector interactions control the location of these transitions, and find that repulsive vector interactions are essential to obtain a stable quark core. Hybrid stars with quarkyonic and/or a deconfined core can reach maximum masses above $2M_\odot$, provided a sufficiently stiff hadronic equation of state is used at low density. In the core of the maximum-mass configurations, the speed of sound exceeds the conformal limit, $c_s^2 = 1/3$, for the quarkyonic core stars. This work establishes the qualitative role of each model parameter in shaping hybrid-star structure.

### [C] 53.5 — Astro-Hunters: Machine Learning for Exoplanet Transit Detection in TESS Photometry
- **arXiv:** [2608.18172](https://arxiv.org/abs/2608.18172)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.IM
- **Top topics:** star_formation (53.5), astrochemistry (48.5), molecular_clouds (48.1)
- **Current keyword baseline:** NO
- **BM25 max:** 31.2
- **Semantic max:** 66.8
- **Abstract:** Finding planets beyond the Solar System is now largely a data-analysis problem: photometric surveys return far more stellar light curves than can be inspected by eye, and machine learning is increasingly asked to recognise the faint, periodic dimming of a transiting planet. Whether such a detector works turns on a choice that is seldom reported: how its training labels were made. No catalogue disposes the individual measurements a per-cadence detector must classify, so the annotation has to be derived, and this paper asks what that costs. We present Astro-Hunters, an end-to-end pipeline over TESS two-minute photometry: retrieval, detrending, seven sliding-window statistics per cadence, and gradient-boosted classification. These components are deliberately conventional. What is new is the treatment of label provenance as an experimental variable, a corpus of 189,279 cadences from twelve confirmed hosts annotated from published ephemerides rather than from the photometry, and a physical bound on what the task permits. Six classifier families are compared under a star-disjoint protocol. Holding features, model and protocol fixed, precision--recall performance spans a factor of 29 across label sources against 1.8 across architectures. Labels from an isolation forest fitted to the classifier's own features give an apparent AUC of 0.9915 that measures circularity; an unconverted transit epoch drives performance to chance; correct annotation gives AUC 0.788 at 5.3 times the prevalence baseline. The ceiling is observational, not architectural: a median single-cadence signal-to-noise ratio of 2.10 caps per-cadence AUC at 0.932. A Box Least Squares baseline recovers eight of twelve orbital periods from one sector. Phase-folding, not classifier capacity, is what makes the transit signal accessible.

### [C] 53.5 — Prospects for Direct Detection of Ultralight Dark Matter candidates in deci-Hz Band with IndIGO-D
- **arXiv:** [2608.15240](https://arxiv.org/abs/2608.15240)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc, hep-ex, hep-ph, hep-th
- **Top topics:** ism_methods_data (53.5), turbulence (43.3), galactic_ism_surveys (42.6)
- **Current keyword baseline:** NO
- **BM25 max:** 47.6
- **Semantic max:** 66.9
- **Abstract:** We investigate the sensitivity of IndIGO-D, a proposed space-based decihertz gravitational-wave interferometer, to different classes of ultralight dark matter. IndIGO-D will probe the $\sim0.01$--$10~\mathrm{Hz}$ frequency band between those accessible to current ground- and future space-based gravitational-wave interferometers, providing access to ultralight dark-matter masses beyond the reach of existing instruments. We consider two complementary signatures: interferometric displacements induced by coherently oscillating scalar (dilaton), vector (dark-photon, $U(1)_B$ and $U(1)_{B-L}$ gauge groups), and tensor fields with masses $m_{\rm DM}\sim10^{-17}$--$10^{-14}~\mathrm{eV}$; and changes in laser polarization induced by pseudoscalar axion dark matter at higher masses, around $m_a\sim10^{-12}~\mathrm{eV}$. For the dilatons, dark photons and tensors, we compute the expected sensitivities using two pipelines -- cross-correlation and BSD excess-power -- assuming L-shaped and triangular interferometer layouts and three representative noise power spectral densities (S1, S2, S3), each for two years of continuous observation. We find that the projected sensitivities agree to within a factor of order unity across the search pipelines and interferometer geometries. In particular, we show that IndIGO-D could open previously unconstrained coupling parameter space for vector and tensor dark matter across $m_{\rm DM}\sim10^{-16}$--$10^{-14}~\mathrm{eV}$, bridging the sensitivity of space- and ground-based experiments. For axion dark matter, we demonstrate that a complementary detection for laser light polarization shifts, limited primarily by photon shot noise, could probe the axion-photon coupling $g_{aγ}$ at masses around $m_a\sim10^{-12}~\mathrm{eV}$ at a level potentially better than that of other future experiments without degrading sensitivity to gravitational waves.

### [C] 53.5 — Cross-spectral Analysis of the Type-C Quasi-periodic Oscillation Shoulder Component in GX 339-4
- **arXiv:** [2608.12966](https://arxiv.org/abs/2608.12966)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** molecular_clouds (53.5), star_formation (48.6), turbulence (47.4)
- **Current keyword baseline:** NO
- **BM25 max:** 48.1
- **Semantic max:** 66.9
- **Abstract:** We revisit Rossi X-ray Timing Explorer (RXTE) observations of GX~339$-$4 during the rising phase of its 2006/2007 outburst and apply a joint power-density-spectrum (PDS)--cross-spectrum (CS) decomposition to the type-C quasi-periodic oscillation (QPO) region. Within this framework, the QPO region is described by a narrow QPO fundamental and a neighboring high-frequency shoulder, whose amplitudes and phase lags can be measured separately. The shoulder is first detected at MJD~54142.04, mainly through the imaginary part of the CS and a narrow local structure in the phase-lag spectrum, before becoming a resolved high-frequency shoulder in the PDS. It follows the QPO frequency evolution on the high-frequency side, with $R_ν=ν_{\rm sh}/ν_{\rm QPO}\simeq1.04$--$1.18$. The QPO lag remains small, typically below $\sim0.17$~rad, whereas the shoulder carries a larger hard lag of $\sim0.5$--$0.8$~rad. Energy-resolved fits show the same separation: the QPO lag is close to zero or only weakly positive across most of the energy band, while the shoulder lag is systematically larger and generally increases with photon energy. The two components have broadly similar rms--energy shapes, although their relative strengths evolve during the observed sequence. Although the shoulder remains broad, with $Q\sim2$--$4$, its lag and rms--energy behavior resemble those of the type-B QPO detected shortly after our observations. This similarity raises the interesting possibility that the shoulder is related to an earlier, broader stage of the variability later seen as the type-B QPO.

### [C] 53.4 — Hybrid disc geometry for shocked accretion flows: Unveiling QPOs in black hole X-ray binaries
- **arXiv:** [2608.18615](https://arxiv.org/abs/2608.18615)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** molecular_clouds (53.4), star_formation (51.3), feedback_bubbles (49.1)
- **Current keyword baseline:** NO
- **BM25 max:** 36.5
- **Semantic max:** 66.7
- **Abstract:** We investigate the efficacy of semi-analytical global accretion solutions in capturing the flow properties observed in two-dimensional numerical simulations of shocked accretion onto black holes. A comparative analysis reveals that no single disc geometry adequately matches the simulation profiles across the entire radial domain. The pre-shock region exhibits closer agreement with the conical disc geometry, while the post-shock region is better described by the vertical equilibrium disc, where enhanced thermal pressure leads to substantial vertical expansion. Motivated by these complementary behaviours, we introduce a hybrid disc geometry in which the pre-shock flow follows the conical solution and the post-shock flow attains vertical equilibrium. This hybrid model satisfactorily reproduces both dynamical and thermodynamical properties of shocked accretion flows with the predicted Mach number and temperature profiles closely matching the simulations and the inferred shock location differing by $\sim10\%$. Within this framework, we delineate the shock parameter space spanned by the energy ($\mathcal{E}$) and angular momentum ($λ$) of the flow for weakly and rapidly rotating black holes and investigate the possible origin of Quasi-periodic Oscillations (QPOs) in black hole X-ray binaries (BH-XRBs). We constrain flow parameters that reproduce observed QPO centroid frequencies ($ν_{\rm QPO}$) demonstrating that oscillations of the shock front provide a self-consistent mechanism for both low and high frequency QPOs. Extending the analysis to ten Galactic BH-XRBs, we demonstrate that the observed $ν_{\rm QPO}$ are reproduced within physically plausible parameter ranges, which establishes shocked global accretion solutions as a potentially compelling framework for interpreting accretion driven temporal variability.

### [C] 53.4 — A Population View of the Cosmic-Ray Knee: The Role of Variance in Supernova Maximum Rigidities
- **arXiv:** [2608.15892](https://arxiv.org/abs/2608.15892)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** ism_methods_data (53.4), feedback_bubbles (52.8), turbulence (50.6)
- **Current keyword baseline:** NO
- **BM25 max:** 36.6
- **Semantic max:** 66.8
- **Abstract:** The broad shape of the Galactic cosmic-ray knee challenges source models in which all supernova remnants share a nearly universal, sharp maximum rigidity. We investigate whether the knee can instead arise as a population effect, produced by source-to-source variations in the maximum energy of Galactic supernova remnants. We derive the population-averaged spectrum for sources with sharp individual cutoffs and distributed $E_{\max}$, showing that it is given by an underlying propagated power law multiplied by the survival probability of the cutoff distribution. A lognormal distribution of $E_{\max}$ naturally produces a smooth, continuously curving knee, while a power-law tail gives an approximately constant post-knee steepening. We then connect the lognormal width to supernova-remnant physics through maximum-energy scalings with explosion energy and ambient density, finding that the expected variance is mainly driven by the spread in explosion energies. Fitting the measured proton spectrum with a two-component lognormal-cutoff model, we find that the PeV component requires $σ_{\log_{10}E_{\max}}\simeq 0.24$. This width is substantially smaller than the variance expected for the full Galactic remnant population, indicating that the PeV component must originate from a more restricted and comparatively homogeneous subset of remnants. Our results show that the knee can be understood as the gradual exhaustion of a heterogeneous population of PeV-capable supernova remnants, without requiring a universal maximum rigidity.

### [C] 53.4 — Are Hot Jupiters Tidally Disrupted During Stellar Main Sequence?
- **arXiv:** [2608.12790](https://arxiv.org/abs/2608.12790)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.GA, astro-ph.IM
- **Top topics:** star_formation (53.4), astrochemistry (51.3), feedback_bubbles (50.0)
- **Current keyword baseline:** YES
- **BM25 max:** 46.2
- **Semantic max:** 66.7
- **Abstract:** Once hot Jupiters (HJs) reach their very close orbits, they are expected to experience orbital decay due to tidal interactions with their host star. However, the strength of tidal dissipation is highly uncertain, and it remains an open question whether HJs are tidally disrupted during the stellar main sequence. A previous study found that HJ hosts have a smaller Galactic total velocity dispersion than their field star counterparts, which they interpreted as evidence of tidal disruption. We revisit this study and find that, after using the more reliable vertical velocity dispersion ($σ_W$) as the age indicator and accounting for the heterogeneity and anisotropy of their HJ sample, the kinematic age difference between their HJ hosts and matched field stars is significantly reduced. As an independent check, we collect HJs newly discovered by TESS and find that their $σ_W$ is statistically similar to that of matched field stars. We also find no statistically significant $σ_W$ difference between the field stars and the theoretically vulnerable ultra-hot Jupiters with $P<2$ d. Our results suggest that, after accounting for systematics in the age--velocity dispersion relation, there is no statistically strong evidence from the stellar kinematics that a large fraction of hot Jupiters around Sun-like stars are tidally destroyed during the stellar main sequence.

### [C] 53.3 — Cosmic Ray Diffusion and the Origin of Very High Energy Gamma-Ray Emission in Young Massive Stellar Clusters
- **arXiv:** [2608.14547](https://arxiv.org/abs/2608.14547)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (53.3), magnetic_fields (49.3), turbulence (47.9)
- **Current keyword baseline:** NO
- **BM25 max:** 70.2
- **Semantic max:** 59.6
- **Abstract:** The search for Galactic sources capable of accelerating cosmic rays (CRs) to PeV energies has advanced significantly in recent years. High-energy observatories such as LHAASO have detected extended gamma-ray halos around several sources, suggesting that CRs escape their acceleration sites through anomalously slow diffusion. Theoretical studies propose that magnetic mirror diffusion combined with pitch-angle scattering in turbulent flow can naturally suppress CR transport. Here, we first show how mirror diffusion combined with scattering suppresses cosmic-ray transport, leading to an energy-dependent diffusion coefficient $D(E)\propto E^{1/3}$. We then combine a 3D magnetohydrodynamic (MHD) simulation of a young massive stellar cluster (YMSC) with Monte Carlo CR propagation calculations (CRPropa). The model includes the background gas density, magnetic field, stellar blackbody and dust emission, the cosmic microwave background, and the Galactic interstellar radiation field. Using the YMSC W43 as a benchmark, we compare two CR injection geometries: a central source and a spherical shell representing the cluster's collective wind shock. We show that mirror+scattering diffusion $D(E)\propto E^{1/3}$, combined with a CR injection spectrum $E^{-2}$, reproduces the gamma-ray spectrum observed by Fermi and LHAASO. In contrast, stronger energy-dependent diffusion requires a harder CR injection spectrum, $\sim E^{-1.6}$, to match the data. The relative contributions of leptonic inverse-Compton and hadronic emission depend sensitively on the diffusion regime. Finally, the resulting spectra show little dependence on the CR injection location, aside from a lower injection luminosity in the central-source case. Overall, our results indicate that the observed gamma-ray emission is shaped primarily by the diffusive propagation regime rather than by the precise location of the CR source.

### [C] 53.2 — Detection of possible burst oscillation in the neutron star low-mass X-ray binary 4U 1323-62
- **arXiv:** [2608.14010](https://arxiv.org/abs/2608.14010)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (53.2), astrochemistry (53.2), ism_methods_data (51.0)
- **Current keyword baseline:** NO
- **BM25 max:** 30.1
- **Semantic max:** 66.5
- **Abstract:** Burst oscillations observed during thermonuclear X-ray bursts arise from asymmetric brightness patterns on the neutron star surface and provide a direct probe of the neutron star spin frequency. We present a detailed timing analysis of the neutron star low-mass X-ray binary 4U 1323-62 using 2024 observations with XMM-Newton and NuSTAR observatories. We identify nine thermonuclear X-ray bursts in the XMM-Newton/EPIC-pn data, along with eclipsing dips in the light curve. One of the XMM-Newton bursts exhibits a rare doublet structure. In addition, NuSTAR detects six bursts, four of which occur simultaneously with those observed with XMM-Newton. We identify a possible burst oscillation signal at $\sim$611.5 Hz in the XMM-Newton data. The strongest oscillation, detected during the primary burst of the doublet burst, reaches a maximum $Z_1^{2}$ power of $\sim35$. An analytical estimate accounting for the searched frequency and time intervals gives a significance of $\sim3.0σ$, whereas independent Monte Carlo simulations yield a more robust global significance of only $\sim2.4σ$. We therefore interpret the signal as a tentative detection of burst oscillation. The folded pulse profile in the 0.5-10 keV band is well described by a sinusoid, with a fractional rms amplitude of $\sim30\pm6$%. The oscillation frequency corresponds to a neutron-star spin period of $\sim$1.635 ms, suggesting that 4U 1323-62 may harbor a rapidly rotating millisecond neutron star.

### [C] 53.1 — A blind spot in transverse BAO calibration
- **arXiv:** [2608.20296](https://arxiv.org/abs/2608.20296)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (53.1), galactic_ism_surveys (47.0), astrochemistry (46.6)
- **Current keyword baseline:** NO
- **BM25 max:** 39.0
- **Semantic max:** 66.4
- **Abstract:** Transverse baryon acoustic oscillation (BAO) measurements are increasingly used for cosmological inference, and carry a calibration that no such inference can constrain. A constant error in the transverse BAO scale is exactly degenerate with the combination $r_{\rm d} h$: it leaves the goodness of fit unchanged and the recovered parameters plausible, and is therefore invisible to any analysis that uses these measurements alone. The radial BAO sector removes this degeneracy, supplying $D_{\rm M}/r_{\rm d}$ by integration without reference to $H_0$ or to any model for the expansion rate. In flat Friedmann--Lemaître--Robertson--Walker (FLRW) geometry the relation between the two sectors is an identity, so the sound horizon and the dark-energy equation of state cancel as well. An integrated form of this identity reduces the consistency test to a straight line, whose slope measures a relative transverse calibration $\varepsilon$. A departure from $\varepsilon = 1$ cannot be produced by any dark-energy model, nor by spatial curvature: it indicates an inconsistency in the measurement chain rather than in the cosmology. We apply the test to the two main SDSS transverse BAO compilations, which give $\varepsilon = 1.073 \pm 0.021$ and $1.021 \pm 0.029$. The first differs from unity at $3.8σ$ using the published independent errors, while the second is consistent with unity. The two compilations themselves differ by $(5.4 \pm 1.4)\%$, or $3.9σ$, and the offset is constant in redshift. The test provides a direct diagnostic for current and future angular BAO measurements.

### [C] 53.0 — Design and Realization of the LST Main Structure for the Cherenkov Telescope Array
- **arXiv:** [2608.15204](https://arxiv.org/abs/2608.15204)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (53.0), molecular_clouds (47.2), ism_methods_data (43.2)
- **Current keyword baseline:** NO
- **BM25 max:** 46.0
- **Semantic max:** 66.2
- **Abstract:** The 23 m diameter Large Size Cherenkov Telescope (LST) for CTA, located at 2250 m a.s.l. on the Canary Island of La Palma, is the next-generation Cherenkov telescope following MAGIC, H.E.S.S., and VERITAS. To enable rapid repositioning (180° in 18 s) for gamma-ray burst observations, the mechanical structure was designed to be ultra- lightweight (110 tons). The space-frame structure consists of slender struts made of carbon fibre, aluminium (dish and camera mast), and steel. The telescope is designed to withstand extreme environmental conditions at the ORM observatory on La Palma, including wind speeds up to 200 km/h, uplift forces, and ice loads of up to 30 tons. We present the structural design developed to meet these functional and environmental requirements. MPP Munich is responsible for the telescope's mechanical structure together with partner institutes in France (LAPP) and Spain (IFAE). The prototype, LST-1, has been operational since 2019, and three additional LSTs are curre1ntly under construction.

### [C] 52.9 — The Challenge of Observing Patchy Reionization with CMB Optical-Depth Fluctuations
- **arXiv:** [2608.19307](https://arxiv.org/abs/2608.19307)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** astrochemistry (52.9), turbulence (49.1), galactic_ism_surveys (46.6)
- **Current keyword baseline:** NO
- **BM25 max:** 43.0
- **Semantic max:** 59.0
- **Abstract:** Spatial fluctuations in the Thomson optical depth encode information about the inhomogeneous nature of cosmic reionization. We compute the optical-depth angular power spectrum, $C_\ell^{ττ}$, using past lightcones constructed from five Cosmic Reionization on Computers (CROC) radiation-hydrodynamical simulations. By decomposing the electron-density field into patchy and density components, we quantify the separate contributions of ionization-fraction and baryon-density fluctuations to the optical-depth anisotropy. Because the simulations end at $z\approx5$, we supplement the reionization-era signal with an analytic estimate of the fully ionized low-redshift contribution. We find that baryon-density fluctuations dominate the high-redshift signal over most angular scales, while the accumulated low-redshift contribution exceeds the high-redshift signal across the full multipole range considered. Our results demonstrate that a significant fraction of the optical-depth power is not uniquely associated with reionization morphology, implying that future interpretations of $C_\ell^{ττ}$ must account for the density contribution in addition to patchy ionization.

### [C] 52.7 — Broadband Properties of the Harmonic of Type-C Quasi-periodic Oscillation in MAXI J1348-630
- **arXiv:** [2608.16648](https://arxiv.org/abs/2608.16648)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (52.7), molecular_clouds (49.6), massive_star_formation (46.2)
- **Current keyword baseline:** NO
- **BM25 max:** 26.4
- **Semantic max:** 65.9
- **Abstract:** Harmonics are common features of quasi-periodic oscillations (QPOs) in black hole X-ray binaries; however, their physical origins remain poorly understood. Using broadband Insight-HXMT data, we investigated the Type-C QPO harmonic in MAXI J1348-630. The harmonic is significantly detected exclusively during the hard intermediate state and displays prominent energy-dependent properties: while it is strong in the soft X-ray band (< 10 keV) with its fractional rms amplitude even exceeding that of the fundamental QPO, it is much weaker in the hard X-ray band (> 10 keV), where its rms amplitude is generally several times lower than that of the fundamental. Furthermore, the harmonic shows no significant phase coupling with the fundamental in the soft X-ray band, whereas strong coupling is present in the hard X-ray band. These features point to a complex, energy-dependent origin for the harmonic. We propose that the hard X-ray harmonic may arise from nonlinear distortion of the fundamental waveform within the corona, while the soft X-ray harmonic is likely produced via a distinct physical process, such as the reflection emission from the inner disk.

### [C] 52.6 — Bayesian Forecasts on Cosmic Superstring Searches with LISA
- **arXiv:** [2608.19406](https://arxiv.org/abs/2608.19406)
- **Primary category:** hep-ph
- **Categories:** hep-ph, astro-ph.CO, gr-qc, hep-th
- **Top topics:** ism_methods_data (52.6), turbulence (50.3), galactic_ism_surveys (49.4)
- **Current keyword baseline:** NO
- **BM25 max:** 47.6
- **Semantic max:** 65.7
- **Abstract:** Cosmic superstrings are well-motivated early-Universe sources of stochastic gravitational waves, with phenomenology controlled by the string tension $Gμ$ and the intercommutation probability $P$. We study whether LISA can reconstruct these parameters and distinguish different superstring signal models in the presence of instrumental noise and astrophysical foregrounds. We consider two phenomenological models. In Model I, reduced intercommutation acts only as an amplitude enhancement of a cusp-dominated spectrum, $Ω_{\rm SS}^{\rm I}=P^{-β}Ω_{\rm cusp}$. In Model II, the signal is a cusp--kink mixture, $Ω_{\rm SS}^{\rm II} =P^{-β}[p_cΩ_{\rm cusp}+(1-p_c)Ω_{\rm kink}]$, so that $P$ controls both amplitude and spectral shape. Using simulated LISA data, we perform Bayesian inference with noise uncertainties, unresolved extragalactic compact-binary backgrounds, and a flexible Galactic double-white-dwarf foreground. We compare the models using Bayesian evidences and map the $(Gμ,P)$ posterior geometry with marginalized widths, correlations, covariance anisotropy, principal eigenvalues, posterior area, and bias. We find that reduced intercommutation generically produces strong $Gμ$--$P$ correlations, because the data often constrain an amplitude-like combination. However, when the cusp--kink spectral difference lies in the LISA band and the signal is sufficiently loud, Model II can be favored and the posterior can retain genuine shape information. As an optimistic foreground scenario, we also compute the Bayes factor using a reduced tanh Galactic foreground template, finding improved model discrimination when the foreground shape is constrained.

### [C] 52.6 — SST-1M: Recent results and prospects for observation of the Galactic Center region
- **arXiv:** [2608.17599](https://arxiv.org/abs/2608.17599)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.IM
- **Top topics:** star_formation (52.6), molecular_clouds (52.3), ism_methods_data (51.8)
- **Current keyword baseline:** NO
- **BM25 max:** 46.4
- **Semantic max:** 65.8
- **Abstract:** The Galactic Center is a crowded region containing powerful particle accelerators and objects producing non-thermal radiation, including the diffuse very-high-energy (VHE) gamma-ray component known as the `Ridge', whose hard spectrum suggests particle acceleration up to PeV energies. The relevant processes can be tested, and the source parameters can be constrained via Cherenkov telescope observations. Two Single-Mirror Small-Size Cherenkov Telescopes (SST-1M) are currently operated in stereoscopic mode at the Ondřejov Observatory. Their future relocation is being considered, including a site with excellent visibility of the Galactic Center. We present recent observations demonstrating SST-1M capabilities for detecting extended emission and discuss prospects for probing the Galactic Center region, including searches for a spectral cut-off above 10 TeV. We show that the large field-of-view and good VHE sensitivity make SST-1M an ideal instrument for the search for PeVatrons.

### [C] 52.6 — Cosmicflows-4 and the Cosmological Consistency of Large-Scale Motions
- **arXiv:** [2608.14265](https://arxiv.org/abs/2608.14265)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (52.6), astrochemistry (48.9), feedback_bubbles (47.3)
- **Current keyword baseline:** NO
- **BM25 max:** 44.4
- **Semantic max:** 65.7
- **Abstract:** We study coherent flows in Cosmicflows-4 (CF4) and its constituent catalogs. We fit monopole and dipole moments in nonoverlapping radial bins using a log-distance radial-velocity estimator. For each sample, the Planck 2018 $Λ$CDM prediction accounts for the actual positions, statistical weights, velocity covariance, and measurement covariance. Across six bins extending to $300,h^{-1},\mathrm{Mpc}$, the All Individual sample is broadly consistent with $Λ$CDM, with dipole and joint deviations of $2.29σ$ and $2.36σ$. The strongest localized feature occurs at $120$--$160,h^{-1},\mathrm{Mpc}$, where $|V_{\rm dip}|=628\pm82,\mathrm{km,s^{-1}}$ and the dipole deviation reaches $3.40σ$. The excess is concentrated toward negative supergalactic X and depends strongly on the survey window. TFR and 6dFGS favor larger dipoles, while SDSS and SN favor smaller ones. Removing 6dFGS reduces the upper-bin dipole deviation to $1.56σ$, while removing SN raises it to $3.77σ$. Nevertheless, the SN and 6dFGS dipoles remain mutually consistent when their covariance is included. SDSS is consistent with $Λ$CDM through $160,h^{-1},\mathrm{Mpc}$ but shows a separate rise at larger radii whose significance depends on the treatment of the monopole and shared distance-scale covariance. Overall, CF4 does not show uniformly anomalous motion across its full radial range. Instead, it contains localized and window-dependent features that should be tested with selection-matched mock catalogs and correlated calibration uncertainties.

### [C] 52.5 — An axion constraint from the diffuse supernova neutrino background indicated by Super-Kamiokande
- **arXiv:** [2608.17681](https://arxiv.org/abs/2608.17681)
- **Primary category:** hep-ph
- **Categories:** hep-ph, astro-ph.CO, astro-ph.HE
- **Top topics:** feedback_bubbles (52.5), ism_methods_data (42.8), galactic_ism_surveys (41.1)
- **Current keyword baseline:** NO
- **BM25 max:** 32.2
- **Semantic max:** 58.5
- **Abstract:** Recently, the Super-Kamiokande Collaboration reported an indication of the diffuse supernova neutrino background (DSNB) with a statistical significance of $2.6σ$. Motivated by this possible discovery, we investigate the impact of axion cooling on the DSNB flux on the basis of long-term neutrino-radiation hydrodynamic simulations. We compare the observed flux and our models and obtain a $1σ$ upper limit $|g_{ap}|<1.3\times10^{-9}$ on the axion-proton coupling constant, which is comparable to the conventional limit based on the SN 1987A neutrino burst. In contrast to the SN 1987A bound, the DSNB constraint does not rely on the properties of a single observed supernova, because the DSNB represents the cumulative neutrino emission from a cosmic population of core-collapse events. More generally, this approach can be applied to other feebly interacting particles that modify protoneutron-star cooling.

### [C] 52.5 — A novel technique for reflection coefficient measurement in precision cosmology
- **arXiv:** [2608.17010](https://arxiv.org/abs/2608.17010)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.CO
- **Top topics:** ism_methods_data (52.5), astrochemistry (52.2), molecular_clouds (45.5)
- **Current keyword baseline:** NO
- **BM25 max:** 52.8
- **Semantic max:** 65.6
- **Abstract:** The detection of the global 21-cm signal from the Cosmic Dawn and Epoch of Reionisation remains a challenge to experiments worldwide. Emitted at a rest-frame frequency of 1420.405~MHz, this signal from the early Universe is redshifted to 40-200~MHz with a maximum brightness temperature of a few 100~mK. Efforts to detect this sky-averaged signal include experiments such as the Shaped Antenna measurement of the background RAdio Spectrum (SARAS) and Probing ReionizATion of the Universe using Signal from Hydrogen (PRATUSH). Detecting this faint signal requires precise calibration of the antenna, which includes a high-precision measurement of its reflection coefficient. This measurement must be performed \textit{in situ} at the observation site, as the antenna characteristics vary significantly with the environment. PRATUSH, a space-based radiometer, faces the additional challenge of structural distortions induced by thermal cycling, necessitating multiple measurements of the reflection coefficient. This work highlights the development of an \textit{in situ} Vector Network Analyser, which utilises a novel noise source-based calibration scheme and a cross-correlation spectrometer to perform magnitude and phase measurements of the complex reflection coefficient of the antenna. Further, we demonstrate the performance of the designed network analyser using independent measurements from a precision network analyser and reflection coefficient modelling of the device under test. We find the level of non-smooth calibration systematics, which need critical control for 21-cm signal detection, to be about $10^{-5}$. Finally, we study the impact of reflection coefficient correction on sky measurements, highlighting its usability for precision 21-cm observations.

### [C] 52.3 — Sub-Pixel Calibration of CMOS Sensors for Precision Astrometry
- **arXiv:** [2608.14874](https://arxiv.org/abs/2608.14874)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (52.3), molecular_clouds (45.6), astrochemistry (44.5)
- **Current keyword baseline:** NO
- **BM25 max:** 22.0
- **Semantic max:** 65.4
- **Abstract:** Many sources of systematic error are important to centroid the position of a star below the level of $10^{-4}$ of the FWHM of the stellar image. One of the more important sources of centroiding error is the imperfect position of the pixels in a focal plane array. In this paper, we discuss the calibration of pixel position of multiple commercial CMOS detectors. Focal plane arrays are semiconductor devices fabricated with 10's nanometer precision. However, the effective location of a pixel can be biased if there's a QE gradient across the pixel. We typically see pixel position variations of 1--3\% of a pixel in most CMOS imagers. This paper describes how we measure the position of each pixel below the $10^{-3}$ pixel level. We also describe how this information might be used in a least square fitting of an airy spot to obtain a higher accuracy position of the centroid of the PSF.

### [C] 52.2 — Strangeness Transport in Binary Neutron Star Mergers
- **arXiv:** [2608.15527](https://arxiv.org/abs/2608.15527)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, gr-qc
- **Top topics:** turbulence (52.2), feedback_bubbles (44.4), star_formation (43.8)
- **Current keyword baseline:** NO
- **BM25 max:** 48.1
- **Semantic max:** 65.3
- **Abstract:** The presence of hyperons in the cores of neutron stars opens fast strangeness equilibration channels that can produce bulk-viscous dissipation during binary inspiral. Because these reactions coexist with electron $β$-equilibration, tidal compression can drive the two coupled chemical imbalances far beyond linear response. We construct the first reaction network that self-consistently evolves the electron and strangeness fractions with a four-dimensional strangeness-dependent chiral mean-field (CMF) equation of state, including nucleonic and hyperonic Urca processes and non-leptonic hyperon reactions. For periodic density perturbations, representative of inspiral oscillations, we find that rapid strangeness conversion can generate a large $β$-imbalance, after which slow $β$-equilibration bottlenecks strangeness relaxation. Rather than decaying exponentially, the coupled system consequently exhibits dynamically important algebraic decay in a far-from-equilibrium regime. At the $\rm keV$ temperatures expected during inspiral, this nonlinear response produces a broad enhancement of the effective bulk viscosity, reaching $\sim10^{31}\,\mathrm{g\,cm^{-1}\,s^{-1}}$ for $320$ Hz oscillations. A phenomenological estimate of continuous inspiral dissipation yields gravitational-wave phase shifts up to $\sim0.14$ rad for neutron stars with hyperonic cores. Self-consistent, far-from-equilibrium strangeness transport may therefore provide a dynamical probe of hyperons in neutron-star interiors.

### [C] 52.0 — Extreme-Mass-Ratio Inspirals in Gaseous Disks
- **arXiv:** [2608.17003](https://arxiv.org/abs/2608.17003)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, gr-qc
- **Top topics:** star_formation (52.0), ism_methods_data (48.9), feedback_bubbles (47.5)
- **Current keyword baseline:** NO
- **BM25 max:** 43.7
- **Semantic max:** 61.1
- **Abstract:** Gravitational waves from extreme mass ratio inspirals (EMRIs) are precise probes of the environment of the supermassive black holes (SMBHs) they orbit. If an SMBH is actively accreting, the surrounding gaseous disk can impart hydrodynamic torques on and assist the formation of EMRIs within it. Such disk-EMRI interactions could leave measurable imprints on future observations by the Laser Interferometer Space Antenna (LISA), and potentially provide a route to constrain disk properties using gravitational wave observations. We present herein a detailed relativistic analysis of these hydrodynamic interactions using linear theory. We first derive a Lagrangian governing the evolution of spiral density waves in the disk and use it to formulate a balance law for the transfer of angular momentum between the EMRI and disk. We then develop a stable numerical scheme which can be used to treat corotation resonances and find modal solutions in thin disks up to very large azimuthal numbers. Using this numerical scheme, we explore how SMBH spins, EMRI semi-major axes, disk scale heights, sound speed gradients, and surface density gradients affect the interaction between accretion disks and circular EMRIs. Our results show that relativistic effects substantially alter disk-EMRI interactions once the secondary orbit is within $\mathcal{O}(25)$ Schwarzschild radii from the SMBH. Comparing our numerical results with recent analytical models suggests that the impact of pressure gradients and softening of the gravitational potential is important for disks with finite thickness and cannot be captured by tuning the torque cutoff parameters in the analytical models. The framework provided here will help analyze the formation scenarios of EMRIs and build relativistically accurate waveform models of disk-EMRI interactions.

### [C] 52.0 — A statistical relation of energy injection plateaus in multi-band afterglows of gamma-ray bursts
- **arXiv:** [2608.15918](https://arxiv.org/abs/2608.15918)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (52.0), molecular_clouds (45.9), star_formation (44.5)
- **Current keyword baseline:** NO
- **BM25 max:** 38.6
- **Semantic max:** 65.1
- **Abstract:** The origin of the plateau phase in gamma-ray burst (GRB) afterglows remains under debate, with the energy injection model being one of the most competitive explanations. If the plateau is truly driven by energy injection, the average X-ray and optical luminosities during the plateau phase, $L_{\rm X, plat, ave}$ and $L_{\rm opt, plat, ave}$, should naturally be correlated. Moreover, under this scenario, the scaling relations between the luminosities during the plateau and the normal decay phase are expected to be consistent since they share the same origin, i.e., synchrotron radiation from the external forward shock. Therefore, simultaneous multi-band observations are essential to verify this mechanism. In this work, we select a sample of 47 GRBs with simultaneous plateaus in both bands. We calculate their time-averaged isotropic luminosities for the plateau and the subsequent normal decay phases. We find a moderate positive correlation $\log L_{\rm X, plat, ave}=m\log L_{\rm opt, plat, ave}+c$ with a slope $m = 0.86 \pm 0.11$ for the plateau phase. This correlation supports the energy injection origin and offers a promising diagnostic approach to test the model. Furthermore, we obtain a similar slope $m = 1.05 \pm 0.05$ for the normal decay phase, which reinforces the idea that both phases share the same physical origin. Notably, the post-plateau data exhibit a systematic downward shift in luminosity, which may indicate the cessation of the central engine.

### [C] 52.0 — High-energy neutrino signatures of embedded GRB jets in AGN disks: a dynamic jet-propagation framework
- **arXiv:** [2608.12217](https://arxiv.org/abs/2608.12217)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (52.0), feedback_bubbles (48.0), turbulence (45.6)
- **Current keyword baseline:** NO
- **BM25 max:** 40.7
- **Semantic max:** 60.0
- **Abstract:** Relativistic jets embedded in active galactic nucleus (AGN) accretion disks are promising high-energy neutrino sources, but their emission is often estimated from a single representative jet state. We develop a time-dependent framework that follows jet-head propagation, evolving reverse-shock conditions, and particle cooling until the jet chokes or breaks out, and apply it to the SG and TQM disk models. For the representative choked cases, neutrino emission is dominated by the high-dissipation phase near jet stalling, allowing a stalling-state approximation to reproduce the trajectory-integrated, detector-weighted event yield within approximately $14\%$. In breakout cases, however, rapid jet-head acceleration across steep disk-density gradients suppresses reverse-shock dissipation and can cause single-state estimates to overpredict the fluence, even after accounting for the available energy budget. Full trajectory integration also reshapes the high-energy spectral tail and produces distinct detectability patterns across SMBH mass and disk radius for the two disk models. Some lower-density outer-disk cases develop harder tails extending into the 10--100 PeV range, motivating future ultra-high-energy neutrino searches. Resolving jet propagation dynamics is therefore indispensable for evaluating embedded transients across AGN disk environments and avoiding systematic biases in multi-messenger modeling.

### [C] 51.8 — Effect of ion temperature on lunar photoelectron sheath
- **arXiv:** [2608.19926](https://arxiv.org/abs/2608.19926)
- **Primary category:** physics.plasm-ph
- **Categories:** physics.plasm-ph, astro-ph.EP, physics.space-ph
- **Top topics:** turbulence (51.8), molecular_clouds (51.3), star_formation (42.5)
- **Current keyword baseline:** NO
- **BM25 max:** 51.6
- **Semantic max:** 64.8
- **Abstract:** Observations suggest that the solar wind ions impinging on the lunar surface possess a finite temperature. The effect of ion temperature on the plasma sheath over the lunar surface is investigated in this paper. To account for thermal effects, a thermal pressure term has been added to the ion-flow force equation. Quantitative estimation of sheath characteristics has been performed by solving the Poisson equation, accounting for photoelectrons, solar wind electrons, and warm ions. Notably, the presence of warm ions within the sheath, i) changes the potential, field, sheath population density structures, ii) changes the sheath thickness, iii) reduces the photoelectron trapping, and iv) reduces solar wind electron reflection, compared to cold ions. The effect is more prominent at high lunar latitudes, which in turn may significantly modulate the dust dynamics.

### [C] 51.6 — Tradeoff between segment density and IWA for high-contrast imaging of exoplanets with a large segmented space mission
- **arXiv:** [2608.16479](https://arxiv.org/abs/2608.16479)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** star_formation (51.6), molecular_clouds (50.1), galactic_ism_surveys (49.7)
- **Current keyword baseline:** NO
- **BM25 max:** 43.7
- **Semantic max:** 64.5
- **Abstract:** Imaging Earth-like exoplanets with coronagraphs on future large segmented space telescopes such as the Habitable Worlds Observatory requires contrasts down to $10^{-10}$ at separations below 100 mas, imposing segment phasing control down to a few picometers. We evaluate how this constraint can be relaxed by optimizing telescope and instrument design, quantifying the impact on performance stability under segment phasing aberrations. We propose a system-level approach, adjusting the primary mirror segmentation and the focal-plane mask size (inner working angle). We compare the passive robustness to segment phasing errors across systems, and the ability of a Zernike low-order wavefront sensor to reconstruct aberrations and recover target performance. Increasing the focal-plane mask radius or decreasing segment count improves both passive robustness and sensor reconstruction: Increasing the mask radius from 3.5 to 6.5λ/D relaxes phasing constraints by up to a factor 4 near the IWA, and reducing the segment count from 85 (5 rings) to 7 (1 ring) relaxes them by up to a factor 2; The same mask radius increase also doubles, on average, the sensor's sensitivity to photon noise across segment piston, tip, and tilt modes. To conclude, jointly optimizing the segmentation scheme and mask size, so the low-order PSD envelope is blocked by the mask, can significantly relax phasing requirements, complementing active correction, with direct implications for HWO.

### [C] 51.5 — Confining density functional approach to the QCD phase diagram at low temperatures and thermal twin stars
- **arXiv:** [2608.18038](https://arxiv.org/abs/2608.18038)
- **Primary category:** nucl-th
- **Categories:** nucl-th, astro-ph.SR, hep-ph
- **Top topics:** star_formation (51.5), turbulence (37.2), molecular_clouds (35.7)
- **Current keyword baseline:** NO
- **BM25 max:** 39.1
- **Semantic max:** 57.3
- **Abstract:** We present a density functional-based equation of state for warm, dense nuclear matter with a transition to deconfined quark matter for applications to simulations of supernova explosions and neutron star mergers, but also for the cosmological evolution of Q-balls. For the quark matter equation of state, we employ a recently developed confining density functional approach while nuclear matter is described within a relativistic density functional model of the DD2 class. The phase transition is obtained by a Maxwell construction at constant entropy per baryon. We discuss the solutions of TOV equations for isentropic hybrid stars for the hybrid equation of state model DDf-SFM (DD2-$χ$CDF) without (with) color superconductivity and find that at finite temperatures above a critical value of entropy per baryon sequences of disconnected third family branches ("thermal twin stars") may appear for the DDf-SFM model, while they are absent for the color superconducting model and at $T=0$. We discuss the relation of this critical entropy per baryon to the Seidov criterion of gravitational instability for $T=0$ and find that it is a good guide. We suggest that the presence of thermal twin stars may be regarded as an indicator for the core-collapse supernova explodability of massive blue supergiant stars and thus serve as a new criterion for the reliability of hybrid equation of state models. By this argument, strong color superconductivity shall be excluded and it remains to be shown whether models with moderate diquark pairing could fulfill the thermal twin constraint. For the case of symmetric matter, we compare the resulting hybrid EOS with the flow constraint by Danielewicz et al. and find a a sensitivity of the onset density for deconfinement on the presence or absence of color superconductivity.

### [C] 51.3 — Controlling artificial surface heating in neutron star simulations: Application to hybrid equations of state
- **arXiv:** [2608.16945](https://arxiv.org/abs/2608.16945)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, gr-qc
- **Top topics:** feedback_bubbles (51.3), star_formation (48.6), magnetic_fields (39.4)
- **Current keyword baseline:** NO
- **BM25 max:** 36.9
- **Semantic max:** 64.1
- **Abstract:** The treatment of the stellar surface in binary neutron star simulations is crucial for the accuracy of the numerical evolution and the physical reliability of the predicted observables. Numerical artifacts associated with the treatment of steep gradients near the stellar surface can produce spurious heating during the inspiral, leading to an artificial increase of the internal energy and an unphysical expansion of the neutron star. In this work, we investigate the effectiveness of the entropy-based flux-limiting (EFL) scheme in mitigating these numerical effects within the finite-difference code BAM. We perform simulations of both isolated neutron stars and binary neutron star inspirals employing a representative set of hybrid equations of state. We show that the EFL scheme significantly reduces artificial surface heating. This reduction is observed consistently across all stellar models and binary configurations considered, demonstrating that the reduction of numerical heating is a robust feature of the EFL method.

### [C] 51.3 — Transport properties in binary neutron star mergers: Effect of magnetic field
- **arXiv:** [2608.12091](https://arxiv.org/abs/2608.12091)
- **Primary category:** nucl-th
- **Categories:** nucl-th, astro-ph.HE, hep-ph
- **Top topics:** magnetic_fields (51.3), turbulence (47.3), ism_methods_data (44.5)
- **Current keyword baseline:** NO
- **BM25 max:** 96.8
- **Semantic max:** 59.2
- **Abstract:** In extreme environments such as binary neutron star mergers, temperatures as high as $50$ MeV and magnetic fields up to $10^{17}$ G, reach a regime where neutrino transport governs the macroscopic thermodynamic and chemical evolution. Existing merger simulations rely on zero magnetic field neutrino emissivity and opacity, potentially missing critical transport physics in highly magnetized neutron star cores. We present an exact framework for computing charged current Urca emissivity and neutrino opacity at finite temperature and magnetic field. We employ the Nucleon Width Approximation framework to account for the collisional broadening effects dominant in the high-density core. Our calculations demonstrate that extreme magnetic fields significantly enhance charged current neutrino opacity, effectively reducing the mean free path for thermal neutrinos.

### [C] 51.2 — Laser-micromachined silicon-platelet feedhorns for large-scale submillimeter and millimeter-wave focal planes
- **arXiv:** [2608.12577](https://arxiv.org/abs/2608.12577)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, physics.optics
- **Top topics:** molecular_clouds (51.2), galactic_ism_surveys (36.0), turbulence (35.2)
- **Current keyword baseline:** NO
- **BM25 max:** 43.6
- **Semantic max:** 64.0
- **Abstract:** We present the fabrication and characterization of the first silicon-platelet feedhorn arrays produced using laser micromachining. First, we present a demonstration of the technology for the millimeter-wave band of 80~GHz to 170~GHz, i.e. covering the 90/150~GHz bands typical of CMB experiments. Next, we expand the technology to large-scale production on 150~mm wafers and demonstrate operation at submillimeter wavelengths. This feedhorn array is optimized for operation in a band centered at 350~GHz (330~GHz to 370~GHz) and is being deployed as one of the focal plane elements of the CCAT 350~GHz module of Prime-Cam. We present the design and fabrication processes for these feedhorn arrays and compare the optical performance directly to simulation and to feedhorns of identical design but produced using traditional deep reactive-ion etching (DRIE). We conclude with a discussion of future expansions of this technology, including the potential of sidewall control and using thicker (and thus fewer) wafers, which could significantly reduce production costs and labor.

### [C] 51.1 — Hydrodynamics modeling of the water snow line in young protoplanetary disks with dust-size-dependent opacities
- **arXiv:** [2608.17921](https://arxiv.org/abs/2608.17921)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.SR
- **Top topics:** molecular_clouds (51.1), feedback_bubbles (49.9), star_formation (48.9)
- **Current keyword baseline:** YES
- **BM25 max:** 56.3
- **Semantic max:** 63.8
- **Abstract:** Aims. We investigated the properties of the water snow line during the early stages of disk evolution, paying particular attention to the effects of gravitational instability and dust growth on the snow line's shape and position. Methods. We used the FEOSAD numerical hydrodynamics code to simulate the disk formation and evolution in the thin-disk limit. The simulations incorporate the coevolution of gas, dust, and volatiles, including dust growth, volatile phase transitions, and dust-size-dependent opacities. Results. The position of the water snow line is highly nonsteady during the considered disk evolution period, first moving outward during the disk build-up and then retreating back as the disk cools. Its form in the disk midplane deviates strongly from a circular shape in the early gravitationally unstable phase of disk evolution. An increase in the amounts of grown dust and water ice as well as in the maximum dust size just beyond the snow line, as is readily observed in one-dimensional viscous disk evolution models, in our hydrodynamic models occurs only after gravitational instability diminishes. Dust-growth-induced opacity changes have a profound effect on the position of the water snow line, shifting it closer to the star by almost a factor of two compared to models that do not take this effect into account. Conclusions. The shape, position, and properties of the water snow line in young, gravitationally unstable disks differ from those of older, axisymmetric disks. Our results highlight the importance of taking into account the dependence of opacity on dust size when studying disk evolution.

### [C] 51.0 — The Most Probable Outer Density Profile from Excursion Set Theory
- **arXiv:** [2608.13347](https://arxiv.org/abs/2608.13347)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** star_formation (51.0), massive_star_formation (46.7), galactic_ism_surveys (44.3)
- **Current keyword baseline:** NO
- **BM25 max:** 42.1
- **Semantic max:** 63.7
- **Abstract:** Measurements of the turnaround radius around galaxy clusters can be used to break the degeneracy between measurements of the present day energy density of matter and dark energy. Korkidis & Pavlidou showed that the turnaround radius coincides with the first point of deviation between outer density profiles in N-body simulations and the analytic profile predicted by excursion set theory. However, their analytic profile relied on a number of simplifying assumptions, which may each introduce systematic error. We evaluate the effect of these assumptions on the shape of the analytic profile and its correspondence with simulated outer density profiles. We relax the key simplifying assumptions and re-derive the mode of the outer density profile from excursion set theory. We then numerically resolve the double distribution (DD) across a range of masses and clustering parameters, and compare the numerical mode estimate to the re-derived analytic profile. We find excellent agreement between our analytic profile and the numerically-realized DD. However, our analytic profiles diverge from N-body profiles, and this divergence grows as we relax successive assumptions. We relate this mismatch to the differing window functions used in the analytic and simulation-based approaches, which respectively yield Markovian and correlated density trajectories. We conclude that the analytic profile proposed by Korkidis & Pavlidou should only be used as a few-parameter effective description of the most-probable outer density profile, with parameters fitted to results of cosmological simulations.

### [C] 50.8 — Collisionless Shock Driven by a Supersonic Velocity Shear
- **arXiv:** [2608.16656](https://arxiv.org/abs/2608.16656)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, physics.plasm-ph
- **Top topics:** turbulence (50.8), molecular_clouds (39.2), feedback_bubbles (32.3)
- **Current keyword baseline:** NO
- **BM25 max:** 64.4
- **Semantic max:** 56.4
- **Abstract:** The long-term evolution of a relativistic collisionless velocity shear in an unmagnetized electron-positron plasma is investigated using a first-principle particle-in-cell simulation. The Alves instability converts the shear kinetic energy into thermal and magnetic field energy. The resulting pressures push the plasma, leading to the formation of collisionless shocks. The generated collisionless shocks would accelerate high energy particles, which is a possible solution to the injection problem of shear acceleration. In addition, the collisionless shocks generate a magnetic field turbulence that is required for the shear acceleration to work.

### [C] 50.6 — Inclination Diffusion in Relativistic Loss Cones
- **arXiv:** [2608.16779](https://arxiv.org/abs/2608.16779)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, astro-ph.GA, gr-qc
- **Top topics:** star_formation (50.6), molecular_clouds (44.8), magnetic_fields (38.5)
- **Current keyword baseline:** NO
- **BM25 max:** 30.7
- **Semantic max:** 63.2
- **Abstract:** Relativistic capture and tidal disruption around a spinning black hole depend on both the magnitude and direction of the star's angular momentum, yet loss-cone models often assume fixed orbital inclinations by ignoring the associated diffusion. We show that this is not justified: for isotropic two-body relaxation near a small loss threshold, angular-momentum magnitude $L$ and inclination $x = L_{z}/L$ diffuse on comparable timescales, $t_{E} \gg t_{L} \sim t_{x}$. For Kerr capture, retaining inclination diffusion significantly amplifies the prograde--retrograde contrast while leaving the total inclination-integrated flux nearly unchanged. An almost correct integrated flux can hide a badly wrong angular distribution. The three-dimensional diffusion problem nevertheless retains enough angular structure to permit analytic treatment. By representing pericenter removal as a continuous sink, we obtain a closed-form loss flux solution for a nearly linear Kerr tidal-disruption boundary, finding close agreement with phase-resolved calculations. Inclination-dependent loss therefore requires inclination-resolved diffusion even when integrated rates appear robust.

### [C] 50.4 — Stress-Testing DANTE under Detector Domain Shift: a Representation-Coherent Reanalysis of LIGO O4a
- **arXiv:** [2608.15166](https://arxiv.org/abs/2608.15166)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, gr-qc
- **Top topics:** ism_methods_data (50.4), astrochemistry (46.1), molecular_clouds (41.3)
- **Current keyword baseline:** NO
- **BM25 max:** 35.8
- **Semantic max:** 57.6
- **Abstract:** This sixth version of the Domain-Adaptive Network for Transient Evaluation (DANTE) preprint stress-tests an unsupervised transient-noise pipeline under representation mismatch and observing-run adaptation. We reanalyse 10,429 detector-time strain candidates from 42 LIGO O4a sessions using frozen DINOv2 patch embeddings and a Top-k multiple-instance score. Candidate and native-background Q-transforms share Q in [4,64], and detector-specific thresholds are calibrated from 5,000 run-native windows by temporal-block bootstrap. The coherent analysis yields 6,365 ROBUST, 1,275 AMBIGUOUS, and 2,789 BACKGROUND statistical dispositions; 4,676 of 10,372 paired historical dispositions differ from the cross-representation v5 analysis. Direct controls resolve an O3b-O4a score shift and reduction after native adaptation for H1, but not L1, while known-glitch separation is detector- and morphology-dependent. Replicated studies quantify population-dependent sensitivity to background draw, clustering seed, dictionary size, and whitening, demonstrate native-index absorption, and identify conditional low-Q blindness. A conservative H1-L1 max-shift screen yields 13/8,806 values above threshold, but its on-source values and pooled per-event null maxima are not exchangeable. The primary two-null PEM endpoint shows no resolved ROBUST-BACKGROUND enrichment (p=1.000), and two catalogue overlaps are consistent with a circular-shift coverage proxy (p=0.651). Simulation-only compact-binary controls show detector- and distance-dependent disagreement between novelty, native disposition, and physical coincidence. We withdraw the v5 discovery, rate-limit, catalogue-recall, and survey-wide stability interpretations. The supported result is a measured set of failure modes and validity conditions for unsupervised detector characterization, not a new glitch class or an astrophysical search.

### [C] 50.2 — Exact spherical-wave forward model for radio reflection from stratified media
- **arXiv:** [2608.15989](https://arxiv.org/abs/2608.15989)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.HE, hep-ex, physics.class-ph, physics.ins-det
- **Top topics:** ism_methods_data (50.2), feedback_bubbles (48.4), turbulence (44.6)
- **Current keyword baseline:** NO
- **BM25 max:** 33.1
- **Semantic max:** 62.8
- **Abstract:** Radio detection of ultra-high energy particles ($\gtrsim10^{18}$ eV) depends on how broadband radio pulses reflect from natural media boundaries. We extend the spherical-wave (Sommerfeld--Weyl) treatment of a single homogeneous interface to stratified media by replacing the Fresnel coefficient of each plane-wave component with the characteristic-matrix reflection coefficient of a layered medium, evaluated in the local tangent plane on the spherical surface. The calculation reduces to the single-boundary result at machine precision when the layer contrast is removed and agrees with the published spherical-surface calculation to better than $1.1\%$ at ten HiCal-2 elevation angles, with a mean deviation of $0.6\%$. We apply the formalism to shallow firn stacks proposed as explanations for anomalous-polarity ANITA events. For realistic firn contrasts, layering changes the reflected amplitude but does not reverse the pulse polarity over $150$--$850$ MHz for the elevations studied. In a reference $s$-polarized two-layer model, a coefficient sign change requires buried refractive index $n_2\simeq2.56$, $2.04$, and $1.79$ at local elevations of $8^\circ$, $15^\circ$, and $25^\circ$, respectively. We also test the specular factorization used in fast propagation models, finding $0.2\%$ agreement with the full angular integral for high-altitude balloon geometries, while near-boundary sources require the full integral. The calculated reflected pulses reproduce the expected polarity inversion in $101$ of $106$ HiCal-1 direct/reflected pulse pairs. Because the medium enters through its complex refractive index, the framework applies to ice, lunar regolith, and conducting media.

### [C] 50.0 — Intrinsic Alignments in Redshift Space I: Symmetries
- **arXiv:** [2608.17078](https://arxiv.org/abs/2608.17078)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** ism_methods_data (50.0), turbulence (46.5), galactic_ism_surveys (44.2)
- **Current keyword baseline:** NO
- **BM25 max:** 48.2
- **Semantic max:** 62.4
- **Abstract:** Galaxy shapes are unique tensor tracers of large-scale structure, providing a promising avenue to both enhance current cosmological programs and detect new physics beyond the scalar sector. We develop a general formalism to describe the full 3D structure of galaxy shapes and their statistics, including the breaking of isotropy by the line of sight and redshift space distortions. We constructively show that the redshift-space mapping generates a kinematic basis whose form factors are strictly polynomial in the line-of-sight angle $μ= \hat{k} \cdot \hat{n}$, and that parity selection rules restrict scalar-tensor and tensor-tensor correlators to 3 and 13 independent form factors, respectively, with the latter further reduced to 9 by exchange symmetry. We show that this polynomiality is preserved transforming into a total helicity basis denoted by total angular momentum $M$---sourced to be nonzero by powers of the line-of-sight $\hat{n}$---and that this is equivalent to the form factors having spin weights $(1 - μ^2)^{|M|/2}$ and described by associated Legendre polynomials $P^{|M|}_\ell$. We construct estimators for form factors in the normalized total-helicity basis that provide the optimal angular weighting to extract shape information, and connect the full tensor basis to projected shape statistics. To validate our formalism, we study the above tensor form factors within a toy model, showing that all allowed channels are generated even within simplified assumptions, and apply our estimators to halo shape statistics in N-body simulations wherein all channels up to total angular momentum $|M| \leq 2$ are detected. We anticipate that the methods developed here will have applications ranging from optimal extraction of intrinsic-alignments in hydrodynamical simulations to identifying new physics in tensor channels forbidden by selection rules in the standard model of cosmology.

### [C] 50.0 — Parameter estimation in differential equations: Mathematical foundation for satellite gravimetry, review and perspectives
- **arXiv:** [2608.15148](https://arxiv.org/abs/2608.15148)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM, astro-ph.EP, math-ph, math.DS
- **Top topics:** star_formation (50.0), magnetic_fields (41.4), ism_methods_data (40.2)
- **Current keyword baseline:** NO
- **BM25 max:** 39.0
- **Semantic max:** 62.4
- **Abstract:** Satellite gravimetry has become essential in many areas of earth science. However, the resolution of satellite gravitational models remains low at scales of a few hundreds km and no gravity recovery methods can take full advantages of unprecedented high accuracy of satellite tracking measurements. We first provide a unified theoretical framework of parameter estimation in differential equations for satellite gravimetry and then briefly review the mathematical methods to compute the gravity field of the Earth from satellite tracking. We focus on the collocation method, Kaula linear perturbations, two-point boundary value problems and orbit-energy-based methods. The numerical integration method is also included in this review, though it has been proved to be mathematically incorrect and physically not permitted. The reason is that it has become the standard method to routinely produce global gravitational models from satellite tracking data, which have been widely applied in many different areas of earth science. Because it is not clear how the incorrect foundation would affect gravity products from satellite tracking, we do not review any applications of these products. We then present a measurement-based perturbation theory to estimate the gravity field of the Earth, which can fully utilize both precise satellite orbits of arbitrary length and unprecedented high accuracy of satellite and inter-satellite tracking. The method is theoretically free of modeling errors, is capable of extracting any small forces from satellite and inter-satellite tracking data and provides a guarantee for high-precision and high-resolution global gravity models. Finally, we assume a reference gravity model and derive local solutions to the Newton's nonlinear governing differential equations of satellite motion for scattered tracking data that can still be important in some applications.

### [C] 49.7 — Millimeter-wave adaptive optics: Demonstrating closed-loop correction for lowest Zernike modes
- **arXiv:** [2608.16548](https://arxiv.org/abs/2608.16548)
- **Primary category:** astro-ph.IM
- **Categories:** astro-ph.IM
- **Top topics:** molecular_clouds (49.7), magnetic_fields (46.4), ism_methods_data (44.4)
- **Current keyword baseline:** NO
- **BM25 max:** 27.3
- **Semantic max:** 62.1
- **Abstract:** We report on a five-element prototype wavefront sensor for millimeter-wave adaptive optics (MAO), enabling closed-loop correction of tip-tilt and defocus via secondary mirror (M2) displacement. MAO is essential for large ground-based millimeter/submillimeter telescopes to maintain surface accuracy under wind and thermal distortions. Our sensor, based on radio interferometry, measures excess path lengths from the primary mirror to a focal-plane receiver. A previous two-element prototype achieved < 10 um accuracy at the Nobeyama 45 m telescope. The new five-element system, operating at 20 GHz, was installed on the same telescope. A ``Moon-edge'' experiment confirmed detection of wavefront gradients through strong correlation with continuum flux. Implementing a PI controller closed the sensor-M2 loop, stably suppressing the lowest Zernike modes. This approach establishes a foundation for metrology in future large-aperture submillimeter facilities such as AtLAST/LST.

### [C] 49.7 — Cosmogenic neutrinos from FRII galaxies as potential origin of the ultra-high-energy KM3-230213A event
- **arXiv:** [2608.16540](https://arxiv.org/abs/2608.16540)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** galactic_ism_surveys (49.7), feedback_bubbles (42.5), ism_methods_data (41.8)
- **Current keyword baseline:** NO
- **BM25 max:** 41.0
- **Semantic max:** 62.2
- **Abstract:** Aim : We investigate whether the ultra-high-energy neutrino KM3-230213A can be interpreted as a cosmogenic neutrino produced by ultra-high-energy cosmic rays (UHECRs) accelerated in the lobes of FRII radio galaxies. Method : We model the UHECR, cosmogenic neutrino and photon fluxes expected at Earth using a recent luminosity-dependent density evolution of radio galaxies, empirical relations between radio luminosity and jet kinetic power, and standard assumptions for the UHECR output of FRII lobes. The FRII contribution to the UHECR population is derived self-consistently from the observed luminosity function, rather than imposed as a fixed normalization. The propagation of UHECRs and the production of secondary particles are computed with well-established numerical tools. Results : The predicted cosmogenic neutrino flux is compatible with that inferred from the detection of KM3-230213A, while remaining consistent with current UHECR and gamma-ray constraints. According to our models, the full GRAND observatory ($200\,000~\rm km^2$) should detect between $\sim50$ and $\sim135$ neutrinos above $10^{17}$~eV in ten years, allowing the diffuse UHE neutrino spectrum to be characterized. In contrast, the detection of individual FRII sources or statistically significant correlations with FRII catalogs is likely to remain challenging. At the highest energies, UHECR composition and anisotropy measurements, in particular those related to the nearby radio galaxy Cygnus~A, should provide complementary tests of this scenario. More generally, progress will likely rely on the combination of multimessenger observations with improved astrophysical constraints on particle acceleration and jet composition in FRII radio galaxies.

### [C] 49.7 — Gaia parallax bias via spherical harmonics: A Python tool and discussion of possible causes
- **arXiv:** [2608.12619](https://arxiv.org/abs/2608.12619)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.CO, astro-ph.SR
- **Top topics:** astrochemistry (49.7), star_formation (48.7), feedback_bubbles (46.7)
- **Current keyword baseline:** NO
- **BM25 max:** 35.6
- **Semantic max:** 62.2
- **Abstract:** Parallaxes in Gaia DR3 are known to suffer from a complex set of sky-correlated and magnitude-dependent offsets or biases at the level of a few tens of $μ$as. Estimated from a sample of one million distant quasars and AGNs from the CRF catalog, the average offset is negative, but the actual distribution of this important parameter shows significant variations on the sky. We propose a practical method to evaluate the parallax correction as a function of sky position and, optionally, of $G$ magnitude using a spherical harmonic series, and supply a tested Python tool {\tt varpi3.py} available on Zenodo\footnote{ https://zenodo.org/records/21708614}. We find that only the constant $Y_{00}$ term is significantly dependent on magnitude, while the other 80 harmonic terms are either close to zero or flat with magnitude. The directions of the smallest and largest parallax offsets are $(l,b)\simeq(220\degr,+43\degr)$ and $(l,b)\simeq(45\degr,-45\degr)$, which are close to the orientation of the quasar density dipole reported in recent publications. Motivated by this curious coincidence, we review possible physical effects resulting in a negative bias of measured parallaxes, including an anisotropic universe with a positive curvature and an orbital aberration component. The proposed method of parallax correction is tested using independent asteroseismology data for four different areas on the sphere. Finally, we show that the parallax zero-point propagates into the CRF proper-motion field through the parallax--proper-motion covariance, biasing the vector spherical harmonic determination of the secular-aberration glide, and hence the Galactocentric acceleration, at the microarcsecond-per-year level.

### [C] 49.2 — Sudden emergence of a low-frequency hard X-ray lag in the Seyfert 1 galaxy Mrk 1044
- **arXiv:** [2608.17292](https://arxiv.org/abs/2608.17292)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** molecular_clouds (49.2), star_formation (49.1), astrochemistry (35.9)
- **Current keyword baseline:** NO
- **BM25 max:** 49.7
- **Semantic max:** 61.5
- **Abstract:** Hard X-ray lags, where low frequency variations in the hard X-ray band lag behind those in the soft band, have been detected in many active galactic nuclei (AGNs) and are generally attributed to the inward propagation of accretion-flow fluctuations through an extended corona. In a long XMM-Newton observation of the Seyfert 1 galaxy Mrk 1044, we found a remarkable transition in the lag behavior within a single exposure, while the X-ray flux and spectral shape remained largely unchanged. During the first 60 ks, no significant hard X-ray lag was detected, whereas in the subsequent 60 ks, a pronounced lag emerged. The lag was so prominent that a large-amplitude flux variation event during the lag-detected interval, characterized by a gradual dimming followed by recovery, produced a remarkable clockwise loop in the flux-softness diagram. The sudden appearance of the hard X-ray lag suggests that the X-ray corona underwent a rapid transition from a compact to an extended configuration. This scenario is further supported by two independent observational signatures: (1) the variability became noticeably smoother, with a redder power spectral density (PSD), during the lag-detected interval, and (2) the broad Fe K$α$ line profile became narrower and the reflection continuum weaker. These findings highlight the diagnostic power of tracking rapid changes in hard X-ray lags for probing the physical structure and evolution of AGN coronae, and demonstrate that identifying prominent loops in the flux-softness diagram provides an effective way to locate intervals with significant hard X-ray lags.

### [C] 48.5 — A posteriori correction of Gaia CRF proper motions using conditional probability and zero-parallax prior
- **arXiv:** [2608.16767](https://arxiv.org/abs/2608.16767)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA
- **Top topics:** astrochemistry (48.5), molecular_clouds (46.6), ism_methods_data (46.3)
- **Current keyword baseline:** NO
- **BM25 max:** 35.1
- **Semantic max:** 60.6
- **Abstract:** Precision of proper motions and positions given in the Gaia Celestial Reference Frame (CRF) catalog can be statistically improved introducing conditional probability based on the prior knowledge of zero parallax for these extremely distant sources. The method developed in this study produces statistically conditioned proper-motion estimates under the assumed per-source Gaussian covariance model. It is demonstrated that thus corrected proper motion vectors of 1.2 million CRF objects in Gaia DR3 show a tighter distribution around zero and a general reduction in the rate of outliers by approximately 15\%. A general vector spherical harmonic fit to degree 4 is produced with the corrected data for a filtered subset of CRF quasars with redshifts between 1 and 1.5. This application, predicated on the unknown stochastic component of the global parallax field, shows a 3-sigma change in the estimated magnitude of the Galactocentric acceleration of the solar system barycenter, quantifying the sensitivity of this fundamental determination to the proposed conditioning of proper motions.

### [C] 48.2 — First Observational Evidence for QPO-like Coevolution between Characteristic Damping Timescales and X-ray Time Lags among AGNs
- **arXiv:** [2608.19610](https://arxiv.org/abs/2608.19610)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** molecular_clouds (48.2), star_formation (48.0), feedback_bubbles (45.6)
- **Current keyword baseline:** NO
- **BM25 max:** 40.5
- **Semantic max:** 60.2
- **Abstract:** Quasi-periodic oscillations (QPOs) and stochastic variability provide complementary probes of the inner accretion flow around supermassive black holes in active galactic nuclei (AGNs). Previous multi-epoch studies of narrow-line Seyfert 1 galaxy RE~J1034+396 revealed a coevolution between the QPO frequency and the X-ray time lag, but whether the stochastic variability participates in the same structural evolution has remained unclear. We analyze the multi-epoch XMM-Newton observations of RE~J1034+396 and model the soft (0.3--1~keV) and hard (1--4~keV) light curves separately using a damped random walk process. We obtain reliable characteristic damping timescales (CDTs) for 17 observations, with the soft-band CDT consistently longer than its hard-band counterpart. When combined with the X-ray time lag, the hard-band CDT traces a counterclockwise closed loop that closely resembles the previously reported QPO-frequency--time-lag loop, whereas the soft-band CDT exhibits more complex trajectory. Under plausible dynamical, thermal, and viscous interpretations, the hard-band CDT is associated with characteristic scales in the inner hot accretion flow/corona. The observed loops may represent different projections of a common cyclic evolution of the inner accretion flow/corona, as the three timing observables may respond to its dynamical, stochastic, and radiative properties on different timescales. These results provide the first observational support among AGNs for the physical picture in which changes in the spatial extent of the hot inner flow/corona simultaneously affect QPO and stochastic variability.

### [C] 48.2 — Are Near Resonant Multiple-planet Systems from Kepler Young?
- **arXiv:** [2608.12786](https://arxiv.org/abs/2608.12786)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.GA
- **Top topics:** astrochemistry (48.2), feedback_bubbles (46.4), star_formation (42.5)
- **Current keyword baseline:** YES
- **BM25 max:** 44.8
- **Semantic max:** 60.3
- **Abstract:** Recent studies have claimed that Kepler multi-planet systems hosting near-resonant planet pairs---particularly those near second-order mean-motion resonances (MMRs)---exhibit smaller stellar velocity dispersions than the general population of Kepler planet hosts. Interpreting velocity dispersion as an age indicator, these works concluded that near-resonant systems are systematically younger. We revisit this claim, but we explicitly account for contamination by thick disk stars, which are kinematically hotter and follow a different age-velocity dispersion relation (AVR) than thin disk stars. Using the kinematic criterion to separate thin and thick disk stars, we show that systems classified as having plausible second-order resonant pairs are preferentially hosted by brighter, closer stars and are therefore less contaminated by thick disk stars than the overall sample. After applying a cut to remove probable thick disk contaminants (${\rm TD/D}<0.1$), the vertical velocity dispersion of near-resonant systems becomes statistically indistinguishable from that of the overall Kepler multi-planet sample. We conclude that the apparent kinematic youth of near-resonant systems in Kepler may not be due to a genuine age difference, but rather arises from observational selection effects linked to host star properties and planet detectability. We also comment on the kinematic ages of ultra-short-period planets (USPs).

### [C] 47.5 — Does Early Dark Energy Absorb the DESI Late-Time Dynamics Signal? A Combined Analysis
- **arXiv:** [2608.19432](https://arxiv.org/abs/2608.19432)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc
- **Top topics:** astrochemistry (47.5), ism_methods_data (38.1), galactic_ism_surveys (32.0)
- **Current keyword baseline:** NO
- **BM25 max:** 27.7
- **Semantic max:** 59.4
- **Abstract:** While the recent Baryon Acoustic Oscillation (BAO) measurements from the Dark Energy Spectroscopic Instrument (DESI) collaboration are largely consistent with a flat $Λ$CDM cosmology, the preferred parameters are in mild tension with those determined from the cosmic microwave background (CMB). A late-time dynamical dark energy (DDE) solution has been proposed by the DESI collaboration to address this tension. In this work, we investigate whether the statistical preference for DDE is a genuine late-time phenomenon or an artifact of unresolved early-universe physics. To do so, we simultaneously allow for both early- and late-time modifications to the expansion history by combining the Early Dark Energy (EDE) framework with the Chevallier-Polarski-Linder (CPL) parametrization. Excluding the DESI BAO measurements, our joint analysis of the CMB+Pantheon+ datasets demonstrates that within an EDE-extended framework, the CPL parameters remain statistically consistent with the standard $Λ$CDM model. This supports the hypothesis that a DDE signal at low redshifts can be effectively accounted for by an EDE component within the $Λ$CDM background. However, upon the inclusion of the DESI BAO measurements in the joint analysis, a statistically significant deviation from a cosmological constant emerges. Within this combined framework, the best-fit CPL parameters robustly indicate a departure from the standard $Λ$CDM model, favoring a phantom-to-quintessence transition in the DE equation of state. This demonstrates that the DESI preference for the late-time DDE is a robust signature that cannot be absorbed by modifying the physics of the early Universe.

### [C] 47.5 — Scaling of microcraters with molten rims derived from laser-induced cratering experiments
- **arXiv:** [2608.15068](https://arxiv.org/abs/2608.15068)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.IM
- **Top topics:** molecular_clouds (47.5), ism_methods_data (30.9), massive_star_formation (26.0)
- **Current keyword baseline:** NO
- **BM25 max:** 34.7
- **Semantic max:** 59.4
- **Abstract:** Microcraters with molten rims are widely observed in returned samples from the Moon and asteroids. These features reflect the conditions of small-scale impact events, but the impact velocities required for their formation are not well understood. In this study, we use well-controlled laser irradiation on rock surfaces as an experimental analog to investigate the formation of these molten-rim craters. Specifically, we derive a scaling relation between crater volume, total irradiation energy, and energy loss associated with thermal diffusion. The experimental results indicate that molten-rim structures of microcraters can be formed in the range of $10^2$--$10^3$~m/s impact velocity. This value is consistent with some previous studies which suggested that the origin of microcraters is secondary impact events. These findings provide experimental constraints on the formation mechanisms of molten-rim microcraters and offer a new perspective on impact processes recorded on planetary surfaces. The estimated result is also consistent with the impact velocity required to produce the observed wavy rim protrusions due to a Rayleigh-Taylor hydrodynamic instability ($\sim 10^2$~m/s).

### [C] 47.5 — Blazar Boosted Dark Matter in IceCube
- **arXiv:** [2608.14549](https://arxiv.org/abs/2608.14549)
- **Primary category:** hep-ph
- **Categories:** hep-ph, astro-ph.HE
- **Top topics:** ism_methods_data (47.5), feedback_bubbles (41.0), galactic_ism_surveys (39.5)
- **Current keyword baseline:** NO
- **BM25 max:** 38.3
- **Semantic max:** 59.4
- **Abstract:** We study the sensitivity of IceCube to blazar-boosted dark matter in a fermionic dark matter model with a massive vector mediator coupling to quarks. To this aim, we compute the diffuse flux arising from a sample of 324 blazars with proton spectra inferred from multiwavelength observations, adopting conservative dark matter spike profiles around the central supermassive black holes and consistently accounting for attenuation effects during propagation through the Earth. The dark matter-nucleon scattering cross section is evaluated by including elastic, resonant single pion production, and deep inelastic contributions, with particular emphasis on resonant single-pion production channels in order to smoothly cover the transition between the elastic and deep inelastic regimes. Using IceCube neutrino data, we derive constraints on the parameter space of the model and show that this detection strategy can surpass the sensitivity of conventional direct-detection experiments for dark matter masses below $\sim 1$ GeV. We find that the signal is dominated by deep inelastic scattering and is therefore more sensitive to comparatively heavy mediators, while resonance processes provide a reduction of the event rate, reaching up to about $9\%$ near the experimental threshold. Our results demonstrate that IceCube constitutes a powerful probe of sub-GeV dark matter scenarios through the observation of blazar-boosted dark matter.

### [C] 47.4 — Looking for TRAPPIST-1 external planets' emission in JWST archival data
- **arXiv:** [2608.18626](https://arxiv.org/abs/2608.18626)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** feedback_bubbles (47.4), molecular_clouds (41.4), astrochemistry (39.8)
- **Current keyword baseline:** NO
- **BM25 max:** 35.9
- **Semantic max:** 59.3
- **Abstract:** The TRAPPIST-1 system has been thoroughly observed with JWST. Unfortunately, stellar contamination issues strongly limit the interpretation of transit observations. As for emission observations, only the two closest planets have been observed through five dedicated JWST programs. We gathered all these emission observations and tried to detect the combined emission of the external planets in previous JWST MIRI observations of TRAPPIST-1; this paper presents our approach and our results. We could not achieve sufficient precision to detect the thermal emission of the outer planets and to discriminate between an all-bare rocks and an all-atmospheres scenario. However, we show that a~60 hours continuous observations at a specific phase range, when the gradient of thermal flux from the outer planets is maximum, could allow us to achieve this goal.

### [C] 47.4 — Atmospheric Reconnaissance of TRAPPIST-1 f with JWST NIRISS SOSS: No Evidence for the Transit Light Source Effect
- **arXiv:** [2608.17207](https://arxiv.org/abs/2608.17207)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP
- **Top topics:** ism_methods_data (47.4), feedback_bubbles (44.8), molecular_clouds (44.6)
- **Current keyword baseline:** NO
- **BM25 max:** 29.0
- **Semantic max:** 59.3
- **Abstract:** In just over three years of operation, JWST has observed all seven planets of the TRAPPIST-1 system. The two innermost planets were found to have little to no atmosphere, barring the presence of high-altitude aerosols. Here we present the first JWST transit spectra of the habitable-zone exoplanet TRAPPIST-1 f, which were obtained with NIRISS SOSS over the course of five transits. At least one stellar flare occurred in each visit, but unlike observations of closer-in TRAPPIST-1 planets, no evidence for contamination of the transit spectra from unocculted stellar surface heterogeneities was found. This non-detection does not guarantee the absence of unocculted heterogeneities in all future transit observations of this planet, and it could be explained by the transit chord of TRAPPIST-1 f having properties similar to the average, out-of-transit, visible stellar hemisphere at the time of observation. The transit spectra exhibit slopes ranging from -365 ppm/um down to 15 ppm/um, which we attribute to stellar variability, that is, flares and/or smaller-scale events. The visits least affected by flares rule out H2/He-dominated atmospheres with surface pressures higher than about 20 mbar at 95% confidence. For high-mean-molecular-mass atmospheres, the exact upper limits on surface pressures depend on the reduction pipeline and on the treatment of the residual slopes in the transit spectra.

### [C] 47.4 — Unveiling Neutrino Nature with the Diffuse Supernova Background
- **arXiv:** [2608.14785](https://arxiv.org/abs/2608.14785)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE, hep-ph
- **Top topics:** feedback_bubbles (47.4), astrochemistry (46.4), turbulence (44.1)
- **Current keyword baseline:** NO
- **BM25 max:** 65.0
- **Semantic max:** 58.0
- **Abstract:** The true nature of neutrinos--whether Dirac or Majorana--is a foundational, unresolved question. We demonstrate that the diffuse supernova neutrino background (DSNB) offers an untapped avenue to resolve this issue, provided neutrino magnetic moments are $\gtrsim 10^{-14}μ_B$. The intense magnetic fields characteristic of a subset of collapsing massive stars can trigger resonant chirality flips. This flavor conversion physics alters DSNB fluxes in measurable ways that depend on the neutrino nature. A $20$~yr combined exposure at Hyper-Kamiokande loaded with gadolinium and JUNO can unravel this signature at $90\%$ ($99\%$) confidence if the fraction of magnetorotational events exceeds $12\%$ ($20\%$) of cosmic core collapses. This result holds independent of the mass ordering and establishes the DSNB as a critical gateway to unveiling the true identity of the neutrino.

### [C] 47.3 — Correlations with Magnetic Activity in the Solar Near-Surface Shear Layer. I. Rotation
- **arXiv:** [2608.19438](https://arxiv.org/abs/2608.19438)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR
- **Top topics:** magnetic_fields (47.3), galactic_ism_surveys (41.8), astrochemistry (39.2)
- **Current keyword baseline:** NO
- **BM25 max:** 64.7
- **Semantic max:** 52.3
- **Abstract:** We used data from the Helioseismic and Magnetic Imager to determine the rotation rate of the near-surface shear layer and its time variation. We applied the ring-diagram analysis technique allowing us to probe the layer between the depths of 1 Mm and 17 Mm. We find that the rotation rate increases inwards; it reaches values consistent with those inferred from global helioseismic analyses in the deeper layers, however, there are differences in the rotation rate of the northern and southern hemispheres. We show that the time variation of the rotation rate can be determined even without subtracting the time-averaged rotation rate from each epoch; however, such a subtraction is needed to get the canonical ``torsional oscillation'' signal. We find that even at depths as shallow as 1 Mm, the rotation rate shows the typical torsional oscillation pattern. The cumulative zonal displacement inferred from the residual flows exhibits a pronounced high-latitude hemispheric asymmetry and varies on solar-cycle timescales; at $75^\circ$ it shows an apparent temporal association with the polar magnetic field. We find significant correlations between the cumulative displacement and magnetic activity at a subset of latitudes, with multi-year lags: the displacement leads activity by ~5 years near $15^\circ$, whereas at higher latitudes activity leads by ~4 years. At mid to high latitudes, the inferred lags show a hemispheric dependence, with activity tending to lead in the north and lag in the south, suggesting possible hemispheric differences in the timing of cycle evolution and motivating longer time series to test cycle-to-cycle variation.

### [C] 47.0 — Interacting stellar winds feeding Sgr A*: from the system of mass-losing stars to the binary IRS 16SW
- **arXiv:** [2608.16993](https://arxiv.org/abs/2608.16993)
- **Primary category:** astro-ph.GA
- **Categories:** astro-ph.GA, astro-ph.HE
- **Top topics:** astrochemistry (47.0), molecular_clouds (43.3), turbulence (42.8)
- **Current keyword baseline:** YES
- **BM25 max:** 49.3
- **Semantic max:** 58.8
- **Abstract:** The discovery of cold structures around Sgr A* has challenged our understanding of the gas dynamics and thermodynamic state of the plasma in its vicinity. This work aims to constrain the conditions for the formation of such structures, namely the cold disc-like structure and the recently discovered G-1-2-3 complex. We conduct hydrodynamic simulations of the observed Wolf-Rayet stars feeding Sgr A*. Our simulations show that the plasma chemical composition is crucial for determining the medium properties. We demonstrate that the formation of a cold disc is possible for chemical compositions that are consistent with observational constraints. However, it is not possible to reproduce all the properties of the observed disc which might suggest the interaction with another structure. Additionally, we present our first results on the hydrodynamic modelling of IRS 16SW as a colliding-wind binary. This is the first step to develop a realistic model on the formation of the G-1-2-3 complex.

### [C] 46.9 — Probing Sub-GeV Dark Matter with the Migdal Effect at JUNO
- **arXiv:** [2608.18609](https://arxiv.org/abs/2608.18609)
- **Primary category:** hep-ph
- **Categories:** hep-ph, astro-ph.CO
- **Top topics:** astrochemistry (46.9), ism_methods_data (42.2), feedback_bubbles (40.8)
- **Current keyword baseline:** NO
- **BM25 max:** 51.4
- **Semantic max:** 52.7
- **Abstract:** We discuss the sensitivity of the JUNO neutrino detector to the Migdal ionization signal triggered by nuclear scattering events produced by sub-GeV weakly interacting massive particles (WIMPs). Exploiting JUNO's large target mass and the annual modulation effect we find that the aggregate rate from many independent and indistinguishable WIMP events in JUNO's liquid scintillator can be isolated from the total dark rate of the photomultipliers, potentially providing for spin-dependent interactions a world-leading sensitivity across the sub-GeV mass range.

### [C] 46.7 — Cosmology without the cosmological principle: A study of the large-scale structure effects in the background universe
- **arXiv:** [2608.15983](https://arxiv.org/abs/2608.15983)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc
- **Top topics:** galactic_ism_surveys (46.7), feedback_bubbles (39.3), ism_methods_data (39.2)
- **Current keyword baseline:** NO
- **BM25 max:** 42.9
- **Semantic max:** 58.3
- **Abstract:** Recent studies strongly suggest that the $Λ$CDM model may no longer serve as the definitive standard model in cosmology, given the increasing tensions between different cosmological observables. Some researchers have described this situation as a "crisis in cosmology." The $Λ$CDM model relies on two fundamental assumptions: the isotropy of the universe (supported by observational evidence) and the Copernican principle (a philosophical postulate). Together, these assumptions lead to the well-known Cosmological Principle, with the homogeneity of the universe emerging as a direct consequence. In this thesis, I review the cosmological consequences of relaxing some of these assumptions, exploring inhomogeneous and anisotropic universe models, as well as tilted cosmologies, which consider observers in motion relative to the Hubble flow. We examine methods to study these effects using existing cosmological data. First, we explore a variety of models that describe inhomogeneous and anisotropic universes, including different metric theories, perturbative analyses, averaging effects, tilted scenarios, and cosmographic approaches. We then apply this theoretical framework to analyze SNIA data and the local peculiar velocity field, aiming to constrain key parameters.

### [C] 46.6 — Stochastic Schwinger Effect: de Sitter and beyond
- **arXiv:** [2608.19378](https://arxiv.org/abs/2608.19378)
- **Primary category:** hep-th
- **Categories:** hep-th, astro-ph.CO, gr-qc, hep-ph
- **Top topics:** feedback_bubbles (46.6), star_formation (40.8), turbulence (38.2)
- **Current keyword baseline:** NO
- **BM25 max:** 47.6
- **Semantic max:** 58.2
- **Abstract:** We develop a stochastic formulation of the Schwinger effect in de Sitter spacetime using the Schwinger--Keldysh (in-in) formalism, tailored to particle production by non-stationary gauge backgrounds in the early Universe. Treating the gauge field as a prescribed classical stochastic ensemble, we integrate out massless charged matter and derive the corresponding influence functional and particle-production kernel to leading non-trivial order in the gauge coupling. Conformal invariance allows the result to be extended directly from de Sitter to generic spatially flat FLRW spacetimes, without relying on asymptotic out states. We establish the infrared safety and classicality conditions of the stochastic description and clarify its relation to the conventional static Schwinger effect. We further extend the framework to massless conformally coupled scalars and to weakly coupled non-Abelian gauge sectors, including Standard Model and hidden-sector examples, in regimes where thermal corrections are negligible. Our results provide a general framework for matter creation by stochastic gauge fields in inflation, preheating, and non-thermal BSM sectors, connecting quantum field theory in curved spacetime with early-Universe and high-energy phenomenology.

### [C] 46.4 — Testing MOND-like modifications to gravity using growth-rate measurements and one-loop corrections to the matter power spectrum
- **arXiv:** [2608.18229](https://arxiv.org/abs/2608.18229)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc
- **Top topics:** ism_methods_data (46.4), turbulence (46.0), feedback_bubbles (40.3)
- **Current keyword baseline:** NO
- **BM25 max:** 47.0
- **Semantic max:** 58.0
- **Abstract:** We develop a perturbative framework for structure formation in a broad class of MOND-like theories characterized by a generalized nonlinear Poisson equation. We derive the modified evolution equations governing matter perturbations and obtain the corresponding linear growth equation, extending the analysis into the mildly nonlinear regime through one-loop corrections to the matter power spectrum. Beyond the theoretical framework, we perform a cosmological analysis based on two phenomenological scenarios: one parametrized by a quantity controlling the degree of nonlinearity in the generalized Poisson equation, and another describing the interplay between the MOND acceleration scale and the cosmological acceleration associated with the background expansion. We constrain these scenarios using recent measurements of the growth rate of structure, $fσ_8$, DESI-DR2 baryon acoustic oscillation data, and Type Ia supernova compilations. We find no statistically significant evidence for departures from the standard $Λ$CDM cosmology. The inferred constraints are fully consistent with the GR + $Λ$CDM scenario within the current observational uncertainties. At nonlinear scales, we note that MOND-like modifications can alter $P_{\rm NL}(k)$ and leave signatures that current and future high-precision large-scale-structure observations may probe. Our results establish a systematic connection between MOND-like gravitational dynamics and large-scale structure observations, providing a consistent framework to assess the phenomenological viability of MOND-inspired modifications of gravity in a cosmological context.

### [C] 46.4 — Confirmation of the Finch Flatter-Fainter Relation for the Quadruple Images of Lensed Point Sources
- **arXiv:** [2608.17116](https://arxiv.org/abs/2608.17116)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** galactic_ism_surveys (46.4), feedback_bubbles (45.8), star_formation (44.8)
- **Current keyword baseline:** NO
- **BM25 max:** 18.6
- **Semantic max:** 58.1
- **Abstract:** Finch et al (2002) derived relations for the summed absolute magnifications of quadruply lensed images that vary inversely with flattening in two alternative isothermal gravitational potential models. However, they did not elaborate on the selection effects this "flatter-fainter'' relation induces in actual lensed systems. We test the relation against the Luhtaru et al (2021) sample of 39 quadruply lensed quasars (38 of which we model successfully), using predicted rather than observed magnifications to avoid the complication of microlensing. We found that the summed predicted magnification decreases by a factor of ten over the observed range of flattening.

### [C] 46.2 — Photospheric Kelvin--Helmholtz Vortices as Possible Drivers of Coronal Heating: Implications of the DKIST Observations
- **arXiv:** [2608.12796](https://arxiv.org/abs/2608.12796)
- **Primary category:** astro-ph.SR
- **Categories:** astro-ph.SR, physics.space-ph
- **Top topics:** magnetic_fields (46.2), molecular_clouds (42.4), feedback_bubbles (41.2)
- **Current keyword baseline:** NO
- **BM25 max:** 64.6
- **Semantic max:** 57.7
- **Abstract:** The Daniel K. Inouye Solar Telescope (DKIST) has resolved Kelvin--Helmholtz (KH) vortices at photospheric magnetic-flux boundaries with a characteristic wavelength of 65 km. I estimate whether these vortices can supply the photospheric driver for cross-scale plasma heating through reconnection across different heights from photosphere to low-corona. Using the simulated MURaM shear, density contrast, and 500 km vertical extent, together with a representative photospheric density, gives a shear-energy density of $1.35\times10^{2}$ J m$^{-3}$ and $2.2\times10^{24}$ erg per characteristic vortex. Magnetic fields $1^\circ$--$7^\circ$ from the exact perpendicular orientation ($ {\bf{B}}\perp{\bf{k}}$) remain KH unstable in an idealized calculation and provide an in-plane component that can be wound or compressed into current layers. The limiting case, in which the center-of-momentum shear reservoir becomes new magnetic free energy, gives $b_{\rm cs}=184$ G, identical to the ideal marginal-stability field and equivalent to a $7.6^\circ$ effective twist. This stores at most 135 J m$^{-3}$ in the layers. Using empirical collisionless reconnection heating fractions of 0.28--0.44, the same twist mapped to weakly collisional heights gives ion heating from $\approx$20 eV at the photosphere to $\approx$1.4 keV in the low corona. For an illustrative, snapshot-based KH-active surface fraction of 0.03, quiet-Sun and coronal-hole losses require 5--8\% and 14--21\%, respectively, of the shear reservoir to become reconnecting magnetic free energy that reaches such heights. Active regions likely require a separate guide-field twist and helicity reservoir. The required upward transport has not been measured by DKIST, but it is directly testable.

### [C] 45.8 — A Radon-Transform Perspective on Exoplanet Transits
- **arXiv:** [2608.13163](https://arxiv.org/abs/2608.13163)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.IM
- **Top topics:** ism_methods_data (45.8), molecular_clouds (34.1), star_formation (33.3)
- **Current keyword baseline:** NO
- **BM25 max:** 45.9
- **Semantic max:** 57.2
- **Abstract:** Transit light curves are usually analyzed under the assumption that the transiting planet has a circular sky-projected silhouette. However, planetary rotation, tides, rings, or atmospheric inhomogeneities can produce non-circular silhouettes. This raises the question of what information transit light curves can provide about the underlying two-dimensional attenuation map. In this paper, we show that, in a simple and transparent limit, the time derivative of the transit light curve during ingress or egress can be interpreted as a Radon-transform measurement of the planetary attenuation map, with the projection direction set by the local normal to the stellar limb. This viewpoint makes the information content of a single transit clear. Ingress and egress provide at most two projection angles, so the data constrain the Fourier transform of the attenuation map only along at most two radial slices, leaving a large null space. Physical constraints on the attenuation values and shape priors can reduce the range of viable solutions, but non-uniqueness generally remains. We further examine how realistic effects modify this picture. In particular, small stellar-limb curvature introduces weak sensitivity to transverse Fourier-space structure around the ideal slices, a sensitivity that is absent in the strict Radon-transform limit. These results provide a framework for understanding what transit light curves can and cannot reveal about non-circular planetary silhouettes.

### [C] 45.5 — Diffractive-Sail Single-Impulse Reachable Set for Interplanetary Transfer Design
- **arXiv:** [2608.19654](https://arxiv.org/abs/2608.19654)
- **Primary category:** astro-ph.EP
- **Categories:** astro-ph.EP, astro-ph.IM
- **Top topics:** ism_methods_data (45.5), star_formation (45.0), magnetic_fields (32.9)
- **Current keyword baseline:** NO
- **BM25 max:** 46.1
- **Semantic max:** 56.9
- **Abstract:** Interest in planetary exploration has renewed, and the design of interplanetary transfers has attracted remarkable attention. This paper considers the interplanetary transfer design using a diffractive sail. Considering a nonzero departure hyperbolic excess velocity, the interplanetary transfer problem is transformed into the problem of computing single-impulse reachable sets. Then, based on previous work, a complementary computational method for reachable sets under arbitrary dynamics is proposed using differential algebra combined with adaptive grid refinement. The adaptive grid refinement considers two types of merit scores that reveal dynamical properties and the truncation error of the differential algebra propagation. The proposed method is applied to compute the diffractive-sail reachable sets, and the results verify the effectiveness of the method and merit scores. Finally, a preliminary design of the interplanetary transfers, specified as the Earth-Mars transfers, is performed based on the diffractive-sail reachable sets. The design results are presented. The effects of the corresponding parameters, including transfer time, diffractive angle, and type of diffractive sails, on transfer characteristics are analyzed, providing further insight into parameter selection for interplanetary transfer design.

### [C] 45.4 — Revisiting neutrino event epochs for the blazar PKS 0735+178 with TESS
- **arXiv:** [2608.17651](https://arxiv.org/abs/2608.17651)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** feedback_bubbles (45.4), ism_methods_data (44.5), astrochemistry (40.0)
- **Current keyword baseline:** NO
- **BM25 max:** 41.0
- **Semantic max:** 56.7
- **Abstract:** We present here the results of the optical light curve variability analysis of the blazars PKS 0735+178, in weeks-scale flare state, observed in three sectors with the Transiting Exoplanet Survey Satellite (TESS). The TESS observations in this study coincide with a well-known neutrino emission phase detected with four different neutrino observatories at multiple epochs in a narrow time window. We segmented the rising and decaying parts of the flare and individually analyzed their flux distribution, excess variance, variability timescale, and the power spectral density (PSD). The source displayed an elevated excess variance of ~25%, with a multi-modal flux distribution (coherent in the rising and distorted in the decaying phase). The variability timescale analysis highlights a much faster decay than the rising scale, and the PSDs depict a nominal change in the power spectral slope. We discuss a likely connection in the optical variations and the neutrino events, and briefly explain a possible physical scenario for the observed optical flux behavior in view of previously discovered radio-band results.

### [C] 45.4 — Automatic detection of fast oscillations of dark matter scalar field and updated cosmological constraints on QCDM
- **arXiv:** [2608.13346](https://arxiv.org/abs/2608.13346)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO
- **Top topics:** feedback_bubbles (45.4), galactic_ism_surveys (41.6), turbulence (41.5)
- **Current keyword baseline:** NO
- **BM25 max:** 35.4
- **Semantic max:** 56.8
- **Abstract:** It is well known that a scalar field dark matter with a quadratic potential undergoes fast oscillations when the time period represented by the mass scale in the Klein-Gordon equation becomes much smaller than that set by the Hubble parameter. This makes a solution to the equation numerically intractable. Many works in the literature have addressed the problem by either switching between solving the Klein-Gordon equation in the well-behaved regime to solving the fluid equations at the onset of oscillations, or by introducing a new set of variables that can absorb these oscillations. Despite being successful, these techniques rely on an estimate of when the oscillations start. For large scale scans of a model's parameter space, this can become cumbersome. Furthermore, the techniques have been used mainly for non-interacting dark matter models. In this work, we introduce an averaging technique with an automatic detection of the onset of oscillations, capable of capturing the non-interacting as well as the interacting dark matter scenarios. The technique, implemented in \texttt{CLASS}, is tested on the QCDM model and shows excellent detection and averaging abilities. We also update the cosmological constraints on the model using the most recent public data.

### [C] 45.4 — Temperature effects on white dwarfs in modified gravity
- **arXiv:** [2608.12992](https://arxiv.org/abs/2608.12992)
- **Primary category:** gr-qc
- **Categories:** gr-qc, astro-ph.SR
- **Top topics:** feedback_bubbles (45.4), star_formation (42.1), astrochemistry (42.0)
- **Current keyword baseline:** NO
- **BM25 max:** 44.0
- **Semantic max:** 56.7
- **Abstract:** In this article we analyze the effects of a finite temperature equation of state on the equilibrium structure of white dwarfs in massive Brans-Dicke theory as well as the symmetron and dilaton screening mechanisms. We compute and present the numerically obtained mass-radius relation, effective gravitational constant as well as radial profiles of the scalar field, pressure and metric within the star. We show that assuming a non-zero temperature effectively results in a larger radius while leaving the total mass of the star essentially unchanged, and discuss the interplay between the effective gravitational constant, central density, and radius of the star.

### [C] 45.1 — Dark Energy in the $w-c_s^2$ Plane
- **arXiv:** [2608.17208](https://arxiv.org/abs/2608.17208)
- **Primary category:** astro-ph.CO
- **Categories:** astro-ph.CO, gr-qc
- **Top topics:** turbulence (45.1), astrochemistry (33.2), ism_methods_data (32.5)
- **Current keyword baseline:** NO
- **BM25 max:** 51.0
- **Semantic max:** 56.4
- **Abstract:** We introduce a unified framework for dark energy diagnostics based on the joint phase space of the equation of state $w$ and the sound speed $c_s^2$. The resulting $w-c_s^2$ plane provides a minimal extension beyond background cosmology, capturing both the expansion history and perturbative properties within a single representation. Building on this framework, we define the microphysical flow parameter $F=dc_s^2/dw$, which encodes the dynamical relation between background evolution and perturbative response. We derive a direct connection between the present-day value $F_0$, $H_0$, and $σ_8$, and show that the microphysical flow parameter enables a hierarchy of increasingly stringent consistency tests that substantially reduce the viable dark energy theory space. We further demonstrate how trajectories in the $w-c_s^2$ plane distinguish models that are nearly degenerate at the level of $w(a)$, including canonical quintessence, Chaplygin gas models, and noncanonical scalar field realizations. This framework provides a compact phenomenological bridge between dark energy microphysics and future perturbation-sensitive observations, establishing $F_0$ as a useful discriminator of the kinetic structure underlying cosmic acceleration.

### [C] 45.0 — Impact of Neutrino Flavour Conversion on the Diffuse Neutrino Background from Neutrino-dominated Accretion Flows
- **arXiv:** [2608.12177](https://arxiv.org/abs/2608.12177)
- **Primary category:** astro-ph.HE
- **Categories:** astro-ph.HE
- **Top topics:** star_formation (45.0), galactic_ism_surveys (38.1), feedback_bubbles (37.9)
- **Current keyword baseline:** NO
- **BM25 max:** 35.5
- **Semantic max:** 47.6
- **Abstract:** Neutrino-dominated accretion flows (NDAFs) are believed to form during the fallback accretion phase of some core-collapse supernovae (CCSNe). Such systems produce copious neutrino emission, whose cumulative contribution over cosmic history forms the diffuse NDAF neutrino background (DNNB). As neutrinos propagate from the source to Earth, flavour conversion can significantly modify the observed neutrino spectra and consequently the detectability of the DNNB. In this work, based on fallback CCSN simulations, we investigate the effects of progenitor mass, metallicity, and initial explosion energy on neutrino emission from NDAFs. We calculate the heavy-lepton neutrino ($ν_x$) spectra from NDAFs and incorporate them into DNNB predictions. We find that the unoscillated $ν_x$ spectra are more than an order of magnitude lower than those of electron antineutrinos $\barν_e$. Using the latest neutrino oscillation parameters reported by the Jiangmen Underground Neutrino Observatory (JUNO), we evaluate the impact of flavour conversion on the DNNB and derive the corresponding spectra for both the normal and inverted mass orderings. We further estimate the expected event numbers in JUNO and Hyper-Kamiokande. We find that the predicted DNNB signal is strongly dependent on the neutrino mass ordering. While the DNNB may be detectable in the normal ordering with next-generation neutrino detectors, the signal is significantly suppressed in the inverted ordering, making detection considerably more challenging.

## Disagreement set: current keyword selected, hybrid skipped

- None in this run.

## Disagreement set: hybrid A/B, current keyword missed

- **[A] 89.7 — CHANG-ES XL: Magnetic Field Structures in the Disk and Halo of NGC 891** [2608.12275](https://arxiv.org/abs/2608.12275)
- **[A] 88.5 — Theoretical emission lines and metallicity calibrations of H II regions in ASTRID simulation** [2608.15572](https://arxiv.org/abs/2608.15572)
- **[A] 87.3 — Differential Reddening and Extinction Law Analyses of Galactic Open Clusters** [2608.13313](https://arxiv.org/abs/2608.13313)
- **[A] 85.7 — Wide field Slitless Spectroscopy with JWST's MIRI** [2608.15430](https://arxiv.org/abs/2608.15430)
- **[A] 83.8 — Star Formation in the H II Region Sh 2-205: 3D Morphology and Kinematics from Young Stars and Molecular Gas** [2608.16179](https://arxiv.org/abs/2608.16179)
- **[A] 82.9 — Trace the Self-Gravitating Gas Using CO Isotopologues** [2608.12473](https://arxiv.org/abs/2608.12473)
- **[A] 82.7 — ALMA observations of pre-JWST z ~ 10 galaxy candidates: A CO(J = 9-8) line from a ULIRG at z = 2.54 and revisit of the photometric redshifts with JWST photometry** [2608.12708](https://arxiv.org/abs/2608.12708)
- **[A] 81.3 — OutThere Survey: Addressing $\mathrm{ξ_{ion}}$ and $\mathrm{f_{esc}}$ with a population of average galaxies at z$\sim$2** [2608.19687](https://arxiv.org/abs/2608.19687)
- **[A] 81.2 — High-Redshift Type Ia Supernovae Exhibit Enhanced Calcium Abundances** [2608.18342](https://arxiv.org/abs/2608.18342)
- **[A] 81.2 — CO rotational line emission in very red carbon stars in the Magellanic Clouds** [2608.16456](https://arxiv.org/abs/2608.16456)
- **[A] 80.7 — Abundant Heavy Black Hole Seeds from Moderate Lyman-Werner Radiation** [2608.13656](https://arxiv.org/abs/2608.13656)
- **[A] 80.4 — The Roman Coronagraph Community Participation Program: calibration strategy for the Mueller matrix using on-sky sources** [2608.17369](https://arxiv.org/abs/2608.17369)
- **[A] 80.0 — Outflows in steep density gradients: diversity of behavior and implications for tidal disruption events and luminous fast blue optical transients** [2608.19512](https://arxiv.org/abs/2608.19512)
- **[A] 80.0 — Generalized Non-linear Bayesian Pulsar Timing with Enterprise** [2608.18047](https://arxiv.org/abs/2608.18047)
- **[A] 80.0 — Aromatics and Aliphatics in Local Star-Forming Galaxies as Probed by AKARI** [2608.14989](https://arxiv.org/abs/2608.14989)
- **[A] 79.8 — Chromospheric heating and magnetic topology above the shared penumbra of a delta-spot: Multi-line inversions and multi-height magnetic-field extrapolations** [2608.19983](https://arxiv.org/abs/2608.19983)
- **[A] 79.7 — A Cross-Band (X-ray $\times$ Optical) Periodicity Search for Supermassive Black Hole Binaries: A Null Result and the First Completeness-Corrected Constraint** [2608.16787](https://arxiv.org/abs/2608.16787)
- **[A] 79.7 — Elemental Composition Evolution during the 2024 September 30 Solar Eruption: A Comparison of Hot and Cool Plasma Components with Solar Orbiter/SPICE, Hinode/EIS, and Chandrayaan-2/XSM** [2608.12881](https://arxiv.org/abs/2608.12881)
- **[A] 79.4 — The efficient star-forming regions of stripped-envelope supernovae** [2608.18897](https://arxiv.org/abs/2608.18897)
- **[A] 79.2 — Enhancing the performance and capabilities of the MIRI instrument on JWST** [2608.13873](https://arxiv.org/abs/2608.13873)
- **[A] 79.1 — The Roman Coronagraph Community Participation Program: target database and tools** [2608.17152](https://arxiv.org/abs/2608.17152)
- **[A] 79.1 — The Low-Mass Baryon Cycle in QUEST Dwarf Galaxies I: Sample definition and first results** [2608.15782](https://arxiv.org/abs/2608.15782)
- **[A] 78.6 — Old Disks Die Hard: How Does AGN Feedback Suppress Disk Formation in Milky Way Mass Galaxies?** [2608.13718](https://arxiv.org/abs/2608.13718)
- **[A] 78.5 — Cosmography with DESI-DR1 Cosmic Chronometers: Direct H(z) measurements from Luminous Red Galaxy ages** [2608.13178](https://arxiv.org/abs/2608.13178)
- **[A] 78.4 — Multiphase turbulence as the origin of OH+, H2O+ and H3+ column density scatter in the local ISM** [2608.15633](https://arxiv.org/abs/2608.15633)
- **[A] 78.2 — VAPOLA - A multiyear, multiband polarization survey of AGNs and Sgr A* at millimeter wavelengths with ALMA II. Spectropolarimetric properties and their evolution from 2017 to 2023** [2608.14900](https://arxiv.org/abs/2608.14900)
- **[A] 78.1 — The Cross-Survey Decade: A Call to Action** [2608.19272](https://arxiv.org/abs/2608.19272)
- **[A] 77.8 — Towards Quantum-Dot Detectors as Barcodes for Dark Matter Interactions** [2608.18204](https://arxiv.org/abs/2608.18204)
- **[A] 77.4 — From Cluster Cores to the Low-Density Field: Strong Environmental Quenching of Galaxy Star Formation at Low Redshift** [2608.12301](https://arxiv.org/abs/2608.12301)
- **[A] 77.1 — A Radio-Bright Local Little Red Dot Analog** [2608.16200](https://arxiv.org/abs/2608.16200)
- **[A] 77.1 — Improved Cosmological Constraints from Morphology-Based Marked Correlation Functions** [2608.15083](https://arxiv.org/abs/2608.15083)
- **[A] 76.9 — A NuSTAR Reflection-Spectroscopy Survey of Cygnus X-1** [2608.15902](https://arxiv.org/abs/2608.15902)
- **[A] 76.6 — The VariableTNG project: mass-dependent regulation of galaxy morphology by baryonic feedback** [2608.19543](https://arxiv.org/abs/2608.19543)
- **[A] 76.6 — Deep Earth imaging through neutrino and seismic tomography** [2608.15231](https://arxiv.org/abs/2608.15231)
- **[A] 76.5 — CLASSY. XV. Kinematics and Spatial Distributions of Outflows in Local Highly Star-Forming Galaxies** [2608.12482](https://arxiv.org/abs/2608.12482)
- **[A] 76.4 — The Stellar Population of NGC 346 in the Small Magellanic Cloud with JWST** [2608.17875](https://arxiv.org/abs/2608.17875)
- **[A] 76.2 — SPURS: Massive Stars, Dense Gas, and Ly$α$ Escape in GN-z11 at $z = 10.6$** [2608.12699](https://arxiv.org/abs/2608.12699)
- **[A] 75.8 — The first comprehensive spectral and timing study of the ultra-compact X-ray binary 4U 1812-12 with NICER and NuSTAR** [2608.16841](https://arxiv.org/abs/2608.16841)
- **[A] 75.8 — 3D Radiative Transfer of Lyman-series Lines with SKIRT** [2608.12527](https://arxiv.org/abs/2608.12527)
- **[A] 75.5 — Diffuse HI emission in the circumgalactic medium of NGC891 and NGC4565 - III: azimuthal profiles** [2608.19186](https://arxiv.org/abs/2608.19186)
- **[A] 75.5 — Polarization of GRB standard X-ray afterglow and its detection prospects by eXTP** [2608.15503](https://arxiv.org/abs/2608.15503)
- **[A] 75.4 — Diversity of Ionized Gas Structures in Nearby Metal-poor Dwarf Galaxies** [2608.19667](https://arxiv.org/abs/2608.19667)
- **[A] 75.2 — Identifying Cost-Favorable Locations for Cosmic Explorer** [2608.19114](https://arxiv.org/abs/2608.19114)
- **[B] 74.9 — Large eROSITA X-ray sources as 2MRS galaxy groups** [2608.17732](https://arxiv.org/abs/2608.17732)
- **[B] 74.9 — AT 2020afjz (TSS2020a): The First Fast Extragalactic Transient Discovered by TESS** [2608.17242](https://arxiv.org/abs/2608.17242)
- **[B] 74.7 — Impact of Upstream Clumpiness on Supernova Remnant Forward Shock Evolution in Molecular Cloud Environments** [2608.17477](https://arxiv.org/abs/2608.17477)
- **[B] 74.7 — The deepest color-magnitude diagrams for the benchmark open cluster NGC 2437 from Gaia and VVVX** [2608.14514](https://arxiv.org/abs/2608.14514)
- **[B] 74.4 — Tracing Lyman alpha escape in the CRISTAL-02 galaxy at z~5.3** [2608.19439](https://arxiv.org/abs/2608.19439)
- **[B] 74.4 — Tracking nonlinear solar-wind dynamics over three solar cycles using Wind observations** [2608.17037](https://arxiv.org/abs/2608.17037)
- **[B] 74.2 — The Mass Function of Neutron Stars from Core-Collapse Supernova Simulations** [2608.18198](https://arxiv.org/abs/2608.18198)
- **[B] 74.2 — X-ray thread/Nonthermal Radio Filament associations: Evidence for Interstellar Magnetic Reconnection** [2608.14830](https://arxiv.org/abs/2608.14830)
- **[B] 74.0 — Observations of Disrupted CME Material Falling Back Into the Low Corona** [2608.17951](https://arxiv.org/abs/2608.17951)
- **[B] 74.0 — RIOJA. Environmental Effects on Stellar Populations and Ionized Gas in a Protocluster at $z=7.88$** [2608.16343](https://arxiv.org/abs/2608.16343)
- **[B] 73.8 — Millimeter and sub-millimeter characterization of polymers used for infrared filters in high-sensitivity cryogenic microwave telescopes** [2608.18793](https://arxiv.org/abs/2608.18793)
- **[B] 73.8 — OH Line Detections in Southern Galaxies of the IRAS Revised Bright Galaxy Sample** [2608.14473](https://arxiv.org/abs/2608.14473)
- **[B] 73.8 — High-Energy Neutrinos from Supernova Shock Breakouts in Circumstellar Media: Light Curves, Spectra, and Contribution to the Extragalactic Neutrino Background** [2608.13680](https://arxiv.org/abs/2608.13680)
- **[B] 73.8 — Recycled Gas Dominates the Metal-rich Fuel of Supermassive Black Holes** [2608.12462](https://arxiv.org/abs/2608.12462)
- **[B] 73.5 — Quasar Impostors: Two Extremely UV-Bright ($M_{\rm UV}\approx-23.5$) Reionisation-Epoch Galaxies Powered by Very Massive Stars** [2608.18212](https://arxiv.org/abs/2608.18212)
- **[B] 73.4 — Infrared Lines from Sterile-Neutrino Transition Magnetic Moments at JWST** [2608.17679](https://arxiv.org/abs/2608.17679)
- **[B] 73.4 — Resolving Nearby Supermassive Black Holes with the Black Hole Explorer** [2608.16983](https://arxiv.org/abs/2608.16983)
- **[B] 73.3 — Serendipitous discovery of an almost-dark galaxy in the Virgo Cluster** [2608.19326](https://arxiv.org/abs/2608.19326)
- **[B] 73.2 — EON-SII: Design of a transportable picosecond stellar intensity interferometer for compact-star astrophysics** [2608.17444](https://arxiv.org/abs/2608.17444)
- **[B] 73.2 — H-$α$ Integral Carrington Synoptic Maps Produced by NSO/NISP** [2608.13812](https://arxiv.org/abs/2608.13812)
- **[B] 73.2 — Observational Constraints on Horizonless Compact Objects from Thermal Emission in AGNs** [2608.13645](https://arxiv.org/abs/2608.13645)
- **[B] 73.2 — Interacting Supernovae: a Radio and X-ray Strategy to Constrain the Structure of the Circumstellar Medium** [2608.12464](https://arxiv.org/abs/2608.12464)
- **[B] 73.1 — The VariableTNG project: how baryonic mechanisms shape galaxy properties** [2608.17272](https://arxiv.org/abs/2608.17272)
- **[B] 73.1 — Why is GN-z11 Bright, Compact, and Nitrogen Enhanced? Insights from UV Absorption and Emission Diagnostics** [2608.12466](https://arxiv.org/abs/2608.12466)
- **[B] 73.0 — The THESAN-ZOOM project: clumpiness of high-redshift galaxies and its connection to bursty star formation** [2608.19308](https://arxiv.org/abs/2608.19308)
- **[B] 73.0 — Sr and Ba yields of the First Generation(s) of stars: Constraints from metal-poor stars** [2608.17001](https://arxiv.org/abs/2608.17001)
- **[B] 72.9 — The Atacama Cosmology Telescope: Passband Measurements with an Analysis of Systematic Errors** [2608.18348](https://arxiv.org/abs/2608.18348)
- **[B] 72.7 — The Roman Coronagraph Community Participation Program: corgisim - a simulation suite for the Nancy Grace Roman Space Telescope Coronagraph Instrument** [2608.17257](https://arxiv.org/abs/2608.17257)
- **[B] 72.6 — The galaxies' energy balance problem solved** [2608.14023](https://arxiv.org/abs/2608.14023)
- **[B] 72.4 — A deep learning algorithm for black hole spin estimation using hot-spot secondary images** [2608.18208](https://arxiv.org/abs/2608.18208)
- **[B] 72.2 — The Ĝ Infrared Search for Extraterrestrial Civilizations with Large Energy Supplies. V. When Galaxies Glow with Industry** [2608.12458](https://arxiv.org/abs/2608.12458)
- **[B] 72.1 — The Effects of M Star Age Dependent Ultraviolet Emission on Detecting and Interpreting Exoplanet Biosignatures** [2608.19328](https://arxiv.org/abs/2608.19328)
- **[B] 72.1 — The X-Ray Continuum Emission Region in the Lensed Quasar SDSS J133907.23+131038.6 is Much Smaller than the Accretion Disk** [2608.17041](https://arxiv.org/abs/2608.17041)
- **[B] 72.1 — Two domains of extended Lyman-alpha emission around galaxies: from local radiation to environmental regulation** [2608.16665](https://arxiv.org/abs/2608.16665)
- **[B] 72.0 — Towards independent event horizon imaging of the supermassive black holes in M87 and the Milky Way** [2608.19675](https://arxiv.org/abs/2608.19675)
- **[B] 72.0 — The Viability of Life in Helium-Dominated Exoplanet Atmospheres** [2608.15679](https://arxiv.org/abs/2608.15679)
- **[B] 71.7 — A Systematic Gaia--ZTF Search for Short-Period Blue Compact-Binary Candidates** [2608.19493](https://arxiv.org/abs/2608.19493)
- **[B] 71.7 — The segmented spiral structure of the Solar neighbourhood traced by young clustered populations** [2608.17887](https://arxiv.org/abs/2608.17887)
- **[B] 71.3 — 3D simulations of magnetospheric accretion in T Tauri stars: I. Disk truncation, stellar torques, and application to observations** [2608.17869](https://arxiv.org/abs/2608.17869)
- **[B] 71.3 — X-ray Flaring and Variability in NGC 1275, the Heart of the Perseus Cluster** [2608.13281](https://arxiv.org/abs/2608.13281)
- **[B] 71.2 — Identifying AGNs from X-ray detections$-$II: Metallicity calibrations for the $\rm N_2O_2$ and $\rm N_2S_2$ diagnostics** [2608.16825](https://arxiv.org/abs/2608.16825)
- **[B] 71.0 — Inferring the Dark from the Observable: Estimating Halo Masses Using Galaxy Properties** [2608.19154](https://arxiv.org/abs/2608.19154)
- **[B] 70.8 — A JWST/MIRI Study of Dust in a Sample of Normal Type IIP Core Collapse Supernovae** [2608.16979](https://arxiv.org/abs/2608.16979)
- **[B] 70.8 — ATLAS. IV. A JWST+MUSE Demographic Study of Ly$α$ Profiles in Little Red Dots** [2608.14534](https://arxiv.org/abs/2608.14534)
- **[B] 70.7 — The Total and Polarized Radio Emission from the Innermost Jets of a High-Redshift Quasar and a Candidate at Parsec-Scale Resolution** [2608.18691](https://arxiv.org/abs/2608.18691)
- **[B] 70.6 — A chemo-dynamical search for planet-candidate hosts of possible extragalactic origin** [2608.13895](https://arxiv.org/abs/2608.13895)
- **[B] 70.6 — JWST Detects a Dusty AGB-like Source Before the Type Ia-CSM Supernova 2026sqf** [2608.13321](https://arxiv.org/abs/2608.13321)
- **[B] 70.5 — No Evidence for Nearby Circumstellar Material in the Type Ia Supernova 2025rbs** [2608.13655](https://arxiv.org/abs/2608.13655)
- **[B] 70.5 — Evidence for the First Globular Cluster Stellar Stream beyond the Milky Way** [2608.12254](https://arxiv.org/abs/2608.12254)
- **[B] 70.4 — Low Ly$α$ Visibility in Galaxy Overdensities: Reionization Topology and Neutral-Fraction Ceilings from DIVER over $4.8<z<11$** [2608.19311](https://arxiv.org/abs/2608.19311)
- **[B] 70.4 — Candidates for the most [$O_{III}$] $\lambda5007$-luminous planetary nebula in the Milky Way. I. Integrated light properties of NGC 6572, NGC 6884, and M 1-71** [2608.17380](https://arxiv.org/abs/2608.17380)
- **[B] 70.3 — The Ultrafast Line-Driven Wind from the Double-Degenerate Merger Remnant WD J005311** [2608.19037](https://arxiv.org/abs/2608.19037)
- **[B] 70.3 — Safe Domain Adaptation for Physics: Overcoming Nuisances, Label Shifts, and Simulation Priors** [2608.18190](https://arxiv.org/abs/2608.18190)
- **[B] 70.2 — A dual-polarization whitened-template trigger for real-time radio detection of extensive air showers** [2608.19898](https://arxiv.org/abs/2608.19898)
- **[B] 70.2 — Optical Spectroscopy of TeV-emitting BL Lac Candidates** [2608.14412](https://arxiv.org/abs/2608.14412)
- **[B] 70.0 — Wet Removal and Cloud Enhancement: The Microphysics of Cloud-Haze Interactions on Sub-Neptunes** [2608.19100](https://arxiv.org/abs/2608.19100)
- **[B] 70.0 — Eclipse Timing of the Eccentric Planet HD 80606b with JWST: Constraints on a Second Planet and other Dynamical Effects** [2608.16816](https://arxiv.org/abs/2608.16816)
