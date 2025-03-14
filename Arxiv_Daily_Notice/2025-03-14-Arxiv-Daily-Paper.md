# Showing new listings for Friday, 14 March 2025
Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.


阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送

See `Usage.md` for instructions on how to personalize the repo. 


Keyword list: ['star formation', 'molecular cloud', 'interstellar medium', 'cloud', 'clump', 'core', 'filament', 'atomic gas', 'N-PDF', 'bubble', 'shell', 'HI']


Excluded: ['galaxies', 'galaxy cluster', 'AGN']


### Today: 29papers 
#### Title:
          Parameter estimation of gravitational-wave signals with frequency-dependent antenna responses and higher-modes
 - **Authors:** Pratyusava Baral, Soichiro Morisaki, Ish Gupta, Jolien Creighton
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We implement frequency-dependent antenna responses and develop likelihood classes (standard likelihood, multibanded likelihood, and the relative binning (RB) likelihood) capable of handling the same within the framework of \texttt{Bilby}. We validate the approximate likelihoods by comparing them with the exact likelihood for a GW170817-like signal (signal-to-noise ratio ~ 1900) containing higher-order modes of radiation. We use the relative-binning likelihood to perform parameter estimation (PE) for a GW170817-like signal, including Earth-rotation effects, detector-size effects, and higher-order modes. We study the system in several detector networks consisting of a single 40 km Cosmic Explorer, a 20 km CE and a present-generation detector at A+ sensitivity. The PE runs with RB take around a day to complete on a typical cluster.
#### Title:
          GPU-accelerated Subcycling Time Integration with the Einstein Toolkit
 - **Authors:** Liwei Ji, Roland Haas, Yosef Zlochower, Steven R Brandt, Erik Schnetter, Allen Wen
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc); Computational Physics (physics.comp-ph)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Adaptive Mesh Refinement (AMR) with subcycling in time enables different grid levels to advance using their own time steps, ensuring finer grids employ smaller steps for accuracy while coarser grids take larger steps to improve computational efficiency. We present the development, validation, and performance analysis of a subcycling in time algorithm implemented within the CarpetX driver in the Einstein Toolkit framework. This new approach significantly improves upon the previous subcycling implementation in the Carpet driver by achieving higher-order convergence -- fourth order in time instead of second order -- and enhanced scaling performance. The key innovation lies in optimizing the exchange of ghost points at refinement boundaries, limiting it to the same number as those at inter-process boundaries using dense output from coarser levels, thereby reducing computational and communication overhead compared to the implementation in Carpet, which required a larger number of buffer zones. To validate the algorithm, we first demonstrate its fourth-order convergence using a scalar wave test. We then apply the algorithm to binary black hole (BBH) simulations, confirming its robustness and accuracy in a realistic astrophysical scenario. The results show excellent agreement with the well-established LazEv code. Scaling tests on CPU (Frontera) and GPU (Vista) clusters reveal significant performance gains, with the new implementation achieving improved speed and scalability compared to the Carpet-based version.
#### Title:
          WIggle Corrector Kit for NIRSpEc Data: WICKED
 - **Authors:** Antoine Dumont, Nadine Neumayer, Anil C. Seth, Torsten Böker, Michael Eracleous, Kameron Goold, Jenny E. Greene, Kayhan Gültekin, Luis C. Ho, Jonelle L. Walsh, Nora Lützgendorf
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The point-spread function of the integral-field unit (IFU) mode of the JWST's NIRSpec is heavily under-sampled, creating resampling noise seen as low-frequency sinusoidal-like artifacts, or "wiggles". These artifacts in the data are not corrected in the JWST data pipeline, and significantly impact the science that can be achieved at a single-pixel level. We present WICKED (WIggle Corrector Kit for NIRSpEc Data), a tool designed to empirically remove wiggles. WICKED uses the Fast Fourier Transform to identify wiggle-affected spaxels across the data cube. Spectra are modeled with a mix of integrated aperture and annular templates, a power-law, and a second-degree polynomial. The method works across all medium- and high-resolution NIRSpec gratings: F070LP, F100LP, F170LP, and F290LP. WICKED can recover the true overall spectral shape up to a factor of 3.5x better compared to uncorrected spectra. It recovers the equivalent width of absorption lines within 5% of the true value-~3x better than uncorrected spectra and ~2x better than other methods. WICKED significantly improves kinematic measurements, recovering the line-of-sight velocity (LOSV) within 1% of the true value -- more than 100x better than uncorrected spectra at S/N ~40. As a case study, we applied WICKED to G235H/F170LP IFU data of the elliptical galaxy NGC5128, finding good agreement with previous studies. In wiggle-affected regions, the uncorrected spectrum showed stellar LOSV and velocity dispersion differences compared to the WICKED-cleaned spectrum, of ~17x and ~36x larger than the estimated uncertainties, respectively. Wiggles in NIRSpec IFU data can introduce severe biases in spectral shape, line measurements, and kinematics to values larger than the typical uncertainties. WICKED provides a robust, user-friendly solution, enabling precise single-pixel studies and maximizing JWST's potential.
#### Title:
          Low 4.5 μm Dayside Emission Disfavors a Dark Bare-Rock scenario for the Hot Super-Earth TOI-431 b
 - **Authors:** Christopher Monaghan, Pierre-Alexis Roy, Björn Benneke, Ian J. M. Crossfield, Louis-Philippe Coulombe, Caroline Piaulet-Ghorayeb, Laura Kreidberg, Courtney D. Dressing, Stephen R. Kane, Diana Dragomir, Michael W. Werner, Vivien Parmentier, Jessie L. Christiansen, Farisa Y. Morales, David Berardo, Varoujan Gorjian
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The full range of conditions under which rocky planets can host atmospheres remains poorly understood, especially in the regime of close-in orbits around late-type stars. One way to assess the presence of atmospheres on rocky exoplanets is to measure their dayside emission as they are eclipsed by their host stars. Here, we present Spitzer observations of the 4.5 $\mu$m secondary eclipses of the rocky super-Earth TOI-431 b, whose mass and radius indicate an Earth-like bulk composition (3.07 $\pm$ 0.35 M$_{\oplus}$, 1.28 $\pm$ 0.04 R$_{\oplus}$). Exposed to more than 2000 times the irradiation of Earth, dayside temperatures of up to 2400K are expected if the planet is a dark bare-rock without a significant atmosphere. Intriguingly, despite the strong stellar insolation, we measure a secondary eclipse depth of only 33 $\pm$ 22 ppm, which corresponds to a dayside brightness temperature of $1520_{-390}^{+360}$K. This notably low eclipse depth disagrees with the dark bare-rock scenario at the 2.5$\sigma$ level, and suggests either that the planet is surrounded by an atmosphere, or that it is a bare-rock with a highly reflective surface. In the atmosphere scenario, the low dayside emission implies the efficient redistribution of heat to the nightside, or by molecular absorption in the 4-5 $\mu$m bandpass. In the bare-rock scenario, a surface composition made of a high-albedo mineral species such as ultramafic rock can lead to reduced thermal emission consistent with low eclipse depth measurement. Follow-up spectroscopic observations with the James Webb Space Telescope hold the key to constraining the nature of the planet.
#### Title:
          Exploring the formation environment of multiple stellar populations in Globular Clusters through binary systems
 - **Authors:** E. Bortolan, J. Bruce, A. P. Milone, E. Vesperini, E. Dondoglio, M. V. Legnardi, F. Muratore, T. Ziliotto, G. Cordoni, E. P. Lagioia, A. F. Marino, M. Tailo
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Globular Clusters (GCs) are known to host distinct stellar populations, characterized by different chemical compositions. Despite extensive research, the origin of these populations remains elusive. According to many formation scenarios, the second population (2P) originated within a compact and denser region embedded in a more extended first population (1P) system. As a result, 2P binaries should be disrupted at a larger rate than 1P binaries. For this reason, binary systems offer valuable insight into the environments in which these stellar populations formed and evolved. In this research, we analyze the fraction of binaries among 1P and 2P M dwarfs in the outer region of NGC 288 using Hubble Space Telescope data. We combine our results with those from a previous work, where we inferred the fraction of 1P and 2P binaries in the cluster center. In the outer region, we find a predominance of 1P binaries ($97^{+1}_{-3}\%$) compared to 2P binaries ($3\pm1\%$) corresponding to an incidence of binaries with a mass ratio (i.e., the ratio between the masses of the primary and secondary star) greater than 0.5 equal to $6.4\pm 1.7\%$ for the 1P population and $0.3\pm 0.2\%$ for the 2P population. These binary fractions and incidences differ from those found in the cluster$'$s central region, where the 1P and 2P populations exhibit similar binary incidences and fractions. These results are in general agreement with the predictions of simulations following the evolution of binary stars in multiple-population GCs, starting with a dense 2P subsystem concentrated in the central regions of a 1P system.
#### Title:
          The Shamrock code: I- Smoothed Particle Hydrodynamics on GPUs
 - **Authors:** Timothée David--Cléris, Guillaume Laibe, Yona Lapeyre
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Distributed, Parallel, and Cluster Computing (cs.DC)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We present Shamrock, a performance portable framework developed in C++17 with the SYCL programming standard, tailored for numerical astrophysics on Exascale architectures. The core of Shamrock is an accelerated parallel tree with negligible construction time, whose efficiency is based on binary algebra. The Smoothed Particle Hydrodynamics algorithm of the Phantom code is implemented in Shamrock. On-the-fly tree construction circumvents the necessity for extensive data communications. In tests displaying a uniform density with global timesteping with tens of billions of particles, Shamrock completes a single time step in a few seconds using over the thousand of GPUs of a super-computer. This corresponds to processing billions of particles per second, with tens of millions of particles per GPU. The parallel efficiency across the entire cluster is larger than $\sim 90\%$.
#### Title:
          The dearth of high-mass hydrogen-atmosphere metal-polluted white dwarfs within 40 pc
 - **Authors:** Tim Cunningham, Pier-Emmanuel Tremblay, Mairi O'Brien, Evan B. Bauer, Mark A. Hollands, Detlev Koester, Scott J. Kenyon, David Charbonneau, Dimitri Veras, Muhammad Furqaan Yusaf
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR); Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We present a population synthesis model which addresses the different mass distributions of the metal-polluted and non-metal-polluted hydrogen-atmosphere white dwarfs identified in volume-limited samples. Specifically, metal-pollution has been observed to be rare in white dwarfs more massive than $\approx$0.7 $M_{\odot}$. Our population synthesis model invokes episodic accretion of planetary debris onto a synthetic population of white dwarfs. We find that the observed difference can be explained in the regime where most debris disks last for $10^4$$-$$10^6$ years. This is broadly consistent with observational estimates that disk lifetimes are on the order 10$^5$$-$10$^7$ years. We also invoke an alternate model which explores an upper limit on planetary system formation and survival around the intermediate-mass progenitors of the more massive white dwarfs. In this scenario, we find an upper limit on the polluted white dwarf mass of $M_{\rm wd}<0.72^{+0.07}_{-0.03}$ M$_{\odot}$. This implies an empirical maximum progenitor mass of $M_{\rm ZAMS}^{\rm max}=2.9^{+0.7}_{-0.3}$ M$_{\odot}$. This value is consistent with the maximum reliable host star mass of currently known exoplanet systems. We conclude by imposing these two results on the sample of He-atmosphere white dwarfs within 40\,pc. We find that both scenarios are capable of providing a consistent solution to the full sample of H- and He-atmosphere white dwarfs.
#### Title:
          Cosmological tensions and $\mathcal{Q}_{\rm CDM}$ as an alternative to $Λ$CDM
 - **Authors:** Amin Aboubrahim, Pran Nath
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The Standard Model of cosmology, $\Lambda$CDM, while enormously successful, is currently unable to account for several cosmological anomalies the most prominent of which are in the measurements of the Hubble parameter and $S_8$. Additionally, the inclusion of the cosmological constant is theoretically unappealing. This has lead to extensions of the model such as the use of fluid equations for interacting dark matter and dark energy which, however, are ad hoc since they do not appear to arise from a Lagrangian. Recently, we have proposed $\mathcal{Q}_{\rm CDM}$ as an alternative to $\Lambda$CDM which is a dynamical model of a quintessence field interacting with dark matter within a field theoretic approach. In this approach, we analyze the effect of the dark matter mass, the dark matter-dark energy interaction strength and the dark matter self-interaction on the cosmological parameters. Further, within $\mathcal{Q}_{\rm CDM}$ we investigate the possible alleviation of the Hubble tension and the $S_8$ anomaly and the nature of dark energy.
#### Title:
          Constraints on the X-ray and Very High Energy $γ$-ray Flux from Supernova Remnant W44
 - **Authors:** A. Archer, P. Bangale, J. T. Bartkoske, W. Benbow, J. H. Buckley, Y. Chen, J. L. Christiansen, A. J. Chromey, A. Duerr, M. Errando, M. Escobar Godoy, S. Feldman, Q. Feng, J. Foote, L. Fortson, A. Furniss, W. Hanlon, O. Hervet, C. E. Hinrichs, J. Holder, T. B. Humensky, W. Jin, M. N. Johnson, P. Kaaret, M. Kertzman, M. Kherlakian, D. Kieda, T. K. Kleiner, N. Korzoun, S. Kumar, S. Kundu, M. J. Lang, G. Maier, M. Lundy, M. J. Millard, C. L. Mooney, P. Moriarty, R. Mukherjee, W. Ning, R. A. Ong, M. Pohl, E. Pueschel, J. Quinn, P. L. Rabinowitz, K. Ragan, P. T. Reynolds, D. Ribeiro, E. Roache, L. Saha, M. Santander, G. H. Sembroski, R. Shang, D. Tak, A. K. Talluri, J. V. Tucci, D. A. Williams, S. L. Wong, J. Woo
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Observations of GeV gamma-ray emission from the well-studied mixed-morphology supernova remnant (SNR) W44 by Fermi-LAT and AGILE imply that it is a site of significant cosmic ray acceleration. The spectral energy distribution (SED) derived from the GeV data suggest that the gamma-ray emission likely originates from the decay of neutral pions generated by cosmic-ray interactions. It is essential to measure the SED of W44 in the X-ray and very high energy (VHE) gamma-ray bands to verify the hadronic origin of the emission and to gauge the potential contributions from leptonic emission. We report an upper-limit of the nonthermal X-ray flux from W44 of 5 $\times$ 10$^{-13}$ erg cm$^{-2}$ s$^{-1}$ in the 0.5 - 8.0 keV band based on $\sim$ 300 ks of XMM-Newton observations. The X-ray upper limit is consistent with previously estimated hadronic models, but in tension with the leptonic models. We estimate the VHE flux upper limit of $\sim$ 1.2 $\times$ 10$^{-12}$ erg s$^{-1}$ cm$^{-2}$ in the 0.5 - 5.0 TeV range from W44 using data from the Very Energetic Radiation Imaging Telescope Array System (VERITAS). Our non-detection of W44 at VHE wavlengths is in agreemnent with observations from other imaging atmospheric Cherenkov telescopes (IACTs) and is perhaps consistent with the evolutionary stage of the SNR.
#### Title:
          Results from NASA's First Radio Telescope on the Moon: Terrestrial Technosignatures and the Low-Frequency Galactic Background Observed by ROLSES-1 Onboard the Odysseus Lander
 - **Authors:** Joshua J. Hibbard, Jack O. Burns, Robert MacDowall, Natchimuthuk Gopalswamy, Scott A. Boardsen, William Farrell, Damon Bradley, Thomas M. Schulszas, Johnny Dorigo Jones, David Rapetti, Jake D. Turner
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Cosmology and Nongalactic Astrophysics (astro-ph.CO); Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Radiowave Observations on the Lunar Surface of the photo-Electron Sheath instrument (ROLSES- 1) onboard the Intuitive Machines' Odysseus lunar lander represents NASA's first radio telescope on the Moon, and the first United States spacecraft landing on the lunar surface in five decades. Despite a host of challenges, ROLSES-1 managed to collect a small amount of data over fractions of one day during cruise phase and two days on the lunar surface with four monopole stacer antennas that were in a non-ideal deployment. All antennas recorded shortwave radio transmissions breaking through the Earth's ionosphere -- or terrestrial technosignatures -- from spectral and raw waveform data. These technosignatures appear to be modulated by density fluctuations in the Earth's ionosphere and could be used as markers when searching for extraterrestrial intelligence from habitable exoplanets. After data reduction and marshaling a host of statistical and sampling techniques, five minutes of raw waveforms from the least noisy antenna were used to generate covariances constraining both the antenna parameters and the amplitude of the low-frequency isotropic galactic spectrum. ROLSES- 2 and LuSEE-Night, both lunar radio telescopes launching later in the decade, will have significant upgrades from ROLSES-1 and will be set to take unprecedented measurements of the low-frequency sky, lunar surface, and constrain the cosmological 21-cm signal. ROLSES-1 represents a trailblazer for lunar radio telescopes, and many of the statistical tools and data reduction techniques presented in this work will be invaluable for upcoming lunar radio telescope missions.
#### Title:
          Modified gravity constraints with Planck ISW-lensing bispectrum
 - **Authors:** Anton Chudaykin, Martin Kunz, Julien Carron
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); High Energy Physics - Phenomenology (hep-ph)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We present updated constraints on modified gravity by including the Integrated Sachs-Wolfe (ISW) effect from CMB lensing-CMB temperature cross-correlations, based on the latest Planck PR4 maps. Utilizing the Effective Field Theory of dark energy approach and adopting the $w_0w_a$CDM background cosmological model, we find that including the CMB ISW lensing cross-correlations tighten constraints on the modified gravity parameters by approximately $20\%$, reducing the viable parameter space by $50$-$80\%$. We derive constraints from Planck CMB, Planck and ACT CMB lensing, DESI DR1 BAO, CMB ISW-lensing, and type Ia supernovae (SN Ia) data. Our results are consistent with General Relativity (GR) at the $95\%$ CL. The modified gravity model shows a mild preference for an evolving dark energy at the $1.8\sigma$, $2.6\sigma$ and $3.2\sigma$ levels for the combinations with Pantheon+, Union3 and DESY5 supernova datasets. We find that using the latest likelihoods $\texttt{HiLLiPoP}+\texttt{LoLLiPoP}$ alleviates the departure of modified gravity parameters from the GR-values compared to results using Planck 2018 data. This paper underlines the importance of the ISW lensing probe in constraining late-time modifications of gravity.
#### Title:
          Improved Carbon and Nitrogen Isotopic Ratios for CH$_3$CN in Titan's Atmosphere Using ALMA
 - **Authors:** J. Nosowitz, M. A. Cordiner, C. A. Nixon, A. E. Thelen, Z. Kisiel, N. A. Teanby, P. G. J. Irwin, S. B. Charnley, V. Vuitton
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Titan, Saturn's largest satellite, maintains an atmosphere composed primarily of nitrogen (N$_2$) and methane (CH$_4$) that leads to a complex organic chemistry. Some of the nitriles (CN-bearing organics) on Titan are known to have substantially enhanced $^{15}$N abundances compared to Earth and to Titan's dominant nitrogen (N$_2$) reservoir. The $^{14}$N/$^{15}$N isotopic ratio in Titan's nitriles can provide better constraints on the synthesis of nitrogen-bearing organics in planetary atmospheres as well as insights into the origin of Titan's large nitrogen abundance. Using high signal-to-noise ratio ($>13$), disk-integrated observations obtained with the Atacama Large Millimeter/submillimeter Array (ALMA) Band 6 receiver (211-275 GHz), we measure the $^{14}$N/$^{15}$N and $^{12}$C/$^{13}$C isotopic ratios of acetonitrile (CH$_3$CN) in Titan's stratosphere. Using the Nonlinear optimal Estimator for MultivariatE spectral analySIS (NEMESIS), we derived the CH$_3$CN/$^{13}$CH$_3$CN ratio to be 89.2 $\pm$ 7.0 and the CH$_3$CN/CH$_3$$^{13}$CN ratio to be 91.2 $\pm$ 6.0, in agreement with the $^{12}$C/$^{13}$C ratio in Titan's methane, and other Solar System species. We found the $^{14}$N/$^{15}$N isotopic ratio to be 68.9 $\pm$ 4.2, consistent with previously derived values for HCN and HC$_3$N, confirming an enhanced $^{15}$N abundance in Titan's nitriles compared with the bulk atmospheric N$_2$ value of $^{14}$N/$^{15}$N = 168, in agreement with chemical models incorporating isotope-selective photodissociation of N$_2$ at high altitudes.
#### Title:
          From Non-Detection to Detection: Atacama Compact Array Mosaic Observations of Faint Extended [C I] Emission in NGC 7679
 - **Authors:** Tomonari Michiyama, Toshiki Saito, Kouichiro Nakanishi, Daisuke Iono, Ken-ichi Tadaki, Juan Molina, Bumhyun Lee, Ming-Yang Zhuang, Junko Ueda, Takuma Izumi, Luis C. Ho
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We report the detection of [C I] $^3P_1$--$^3P_0$ emission in the nearby galaxy NGC 7679 using the Atacama Compact Array (ACA) of the Atacama Large Millimeter/submillimeter Array (ALMA). In Michiyama et al. (2021), [C I] $^3P_1$--$^3P_0$ emission in NGC 7679 was reported as undetected based on ACA observations conducted in 2019 (ALMA Cycle 6). These observations had ~1 minute on-source time and used a single pointing with a field of view (FoV) of ~20 arcsec. In 2023 (Cycle 9), we carried out mosaic observations using seven pointings with an FoV of ~27 arcsec and 4-5 minutes on-source per pointing. The additional data have significantly improved the line sensitivity, uv-sampling, and noise uniformity across the galaxy disk. Our Cycle 9 observations confirm the presence of extended [C I] $^3P_1$--$^3P_0$ emission in NGC 7679, which was completely missed in the Cycle 6 observations due to insufficient sensitivity and uv-sampling. This highlights the basic technical challenges of estimating the total flux by interferometric observations with sparse uv-sampling.
#### Title:
          Tantalizing Evidence of Reionization Relics in the eBOSS DR16 Ly$\boldsymbolα$ Forest Correlations: a Preference for Early Reionization
 - **Authors:** Yifan Zheng, Paulo Montero-Camacho, Zheng Cai, Yi Mao
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Cosmic reionization of HI leaves enduring relics in the post-reionization intergalactic medium, potentially influencing the Lyman-$\alpha$ (Ly$\alpha$) forest down to redshifts as low as $z \approx 2$, which is the so-called ''memory of reionization'' effect. Here, we re-analyze the baryonic acoustic oscillation (BAO) measurements from Ly$\alpha$ absorption and quasar correlations using data from the extended Baryonic Oscillation Spectroscopic Survey (eBOSS) Data Release 16 (DR16), incorporating for the first time the memory of reionization in the Ly$\alpha$ forest. Three distinct scenarios of reionization timeline are considered in our analyses. We find that the recovered BAO parameters ($\alpha_\parallel$, $\alpha_\perp$) remain consistent with the original eBOSS DR16 analysis. However, models incorporating reionization relics provide a better fit to the data, with a tantalizing preference for early reionization, consistent with recent findings from the James Webb Space Telescope. Furthermore, the inclusion of reionization relics significantly impacts the non-BAO parameters. For instance, we report deviations of up to $3\sigma$ in the Ly$\alpha$ redshift-space distortion parameter and $\sim7\sigma$ in the linear Ly$\alpha$ bias for the late reionization scenario. Our findings suggest that the eBOSS Ly$\alpha$ data is more accurately described by models that incorporate a broadband enhancement to the Ly$\alpha$ forest power spectrum, highlighting the importance of accounting for reionization relics in cosmological analyses.
#### Title:
          R-JET: A postprocessing code for radiative transport in relativistic jets
 - **Authors:** Kouichi Hirotani, Hsien Shang, Ruben Krasnopolsky, Kenichi Nishikawa
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); Solar and Stellar Astrophysics (astro-ph.SR); Plasma Physics (physics.plasm-ph)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We describe a post-processing radiative transport code for computing the spectra, the coreshift, and the surface-brightness distribution of special relativistic jets with arbitrary optical thickness. The jet consists of an electron-positron pair plasma and an electron-proton normal plasma. Electrons and positrons are relativistic and composed of thermal and nonthermal components, while protons are non-relativistic and non-radiating. The fraction of a pair plasma, as well as the fraction of a nonthermal component can be arbitrarily chosen. Only the synchrotron process is considered for emission and absorption when the radiative-transfer equation is integrated along our lines of sight. We describe a suite of test problems, and confirm the frequency dependence of the coreshift in the Konigl jet model, when the plasma is composed of nonthermal component alone. Finally, we illustrate the capabilities of the code with model calculations, demonstrating that the jet will exhibit a limb-brightened structure in general when it is energized by the rotational energy of the black hole. It is also demonstrated that such limb-brightened jets show a ring-like structure in the brightness map when we observe the jet launching region nearly face-on.
#### Title:
          Temporal variability and obscuration effects in the X-ray emission of classical nova V339 Delphini (Nova Delphini 2013)
 - **Authors:** Songpeng Pei, Nataly Ospina, Xiaowan Zhang, Qiang Li, Ziwei Ou, Taozhi Yang, Yongzhi Cai
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 In this study, we present a detailed analysis of public archival soft X-ray data on the classical nova V339 Delphini (Nova Del 2013) during its outburst, obtained using the {\it Chandra} High-Resolution Camera Spectrometer (HRC-S) and Low Energy Transmission Grating (LETG), as well as {\it XMM-Newton} in 2013. The observations, spanning from day 85.2 to day 112.0 after the optical maximum, capture the nova during its luminous supersoft X-ray source (SSS) phase. The spectra reveal numerous absorption features with blue-shifted velocities ranging from $\sim$ 724 to $\sim$ 1474 km s$^{-1}$, with the majority of lines blue-shifted by approximately 1200 km s$^{-1}$. We confirm the presence of a short-period modulation of the X-ray flux with a period of approximately 54 seconds, as well as the drift of this period, which was detected on days 97.0 and 112.0 during the outburst with both {\it XMM-Newton} and {\it Chandra}. This period modulation is transient in nature, with significant variations in amplitude and pulse profile over timescales of a few thousand seconds, likely due to temporary obscuration events that affect the emission from the central hot source. The pulse profiles exhibit substantial deviations from a pure sinusoidal shape, which may be related to the period drift. Additionally, the modulation amplitude shows a possible anti-correlation with the count rates on day 97.0, likely also caused by temporary obscuration events influencing the central source's emission.
#### Title:
          Dust shells and dark linear structures on dust tails of historical and recent long-period comets
 - **Authors:** Fernando Moreno, Emmanuel Jehin
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Context. Dust halos or shells, along with linear dark structures along the axes of dust tails, are commonly observed in many long-period comets near perihelion. Examples range from the recent C/2023 A3 (Tsuchinshan-ATLAS) to historical comets such as the Great Comet of 1874, C/1874 H1 (Coggia). Aims. While dust halos can readily be modeled as spin-modulated activity originating from the comet nucleus, their possible connection to those dark linear features has, to our knowledge, not been investigated. The aim of this paper is to shed light on the formation of these remarkable structures by modeling a sample of six long-period comets, using similar dust physical properties and ejection parameters, to explore whether they share a common origin. Methods. To model the dust features, we employed a Monte Carlo procedure to generate synthetic images. The particles ejected from the comet nucleus follow a power-law size distribution and are released into interplanetary space at speeds determined by the ratio of solar radiation pressure to solar gravity, the heliocentric distance, and, as a new feature of the code, the solar zenith angle at the emission point. Results. We demonstrate that, in all the cases analyzed, the dust shells form as a result of short-term events characterized by cyclically varying ejection of very small particles from large surface areas on the rotating nucleus. These events are triggered as these areas become freshly exposed to solar radiation near perihelion due to the high obliquity of the spin axes of their nuclei. The dark linear stripes along the tail axes may arise from a specific dependence of the ejection speeds on the square root of the cosine of the zenith angle, as is predicted by hydrodynamical modeling, but their presence is also dependent on the extent of the latitude region of emission that defines the velocity vector field.
#### Title:
          Modelling subsonic turbulence with SPH-EXA
 - **Authors:** Rubén M. Cabezón, Domingo García-Senz, Osman Seckin Simsek, Sebastian Keller, Axel Sanz, Yiqing Zhu, Lucio Mayer, Ralf Klessen, Florina M. Ciorba
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The numerical simulation of subsonic turbulence with SPH has traditionally been hindered by E0 errors, inaccurate gradient evaluations, and excessive dissipation. In this work, we present numerical results of SPH simulations of subsonic turbulence and compare to state-of-the-art codes such as AREPO and GIZMO. For the first time, SPH can reproduce the results of such codes, showing a similar interval of wavenumber in the inertial range of the Kolmogorov cascade in the subsonic regime. We use the SPH-EXA code to perform these simulations, a GPU-based state-of-the-art SPH code with high performance and extreme scalability at its core. SPH-EXA is coupled with a modern SPH solver based on methods such as an integral approach to gradient calculation, artificial viscosity switches that include a linear field cleaner, a flexible family of pairing-resistant interpolation kernels, generalized volume elements, and a controlled handling of density jumps which maximizes Lagrangian compatibility. In addition, it includes a novel and extremely scalable gravity solver for astrophysical applications.
#### Title:
          Beyond monoculture: polydisperse moment methods for sub-stellar atmosphere cloud microphysics I. Examining properties of the exponential distribution
 - **Authors:** Elspeth K.H. Lee
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Observational data provided by JWST instruments continue to challenge theories and models of cloud formation in sub-stellar atmospheres, requiring more sophisticated approaches in an effort to understand their spatial complexity. However, to date, most cloud microphysical models using the moment method for sub-stellar atmospheres have assumed a monodisperse size distribution, neglecting polydisperse properties. We aim to extend beyond the common assumption of a monodisperse size distribution and analyse cloud microphysical processes assuming an exponential distribution. We derive expressions for the zeroth and first moments of condensation/evaporation and collisional growth processes under the assumption of an exponential size distribution. We then compare the differences between monodisperse and exponential distribution microphysics using a simple one-dimensional (1D) column model applied to a Y-dwarf KCl cloud scenario. We find that adopting an exponential distribution modifies condensation/evaporation rates by a factor of $\approx$0.9 and collisional growth rates by factors of $\approx$1.1 (Kn $\ll$ 1) and $\approx$0.92 (Kn $\gg$ 1) for Brownian coagulation and $\approx$0.85 for gravitational coalescence, compared to the monodisperse case. In our specific test cases, we find relative differences of a maximum 10-12% in total number density and 2-3% in mean radius of the cloud particles between the monodisperse and exponential distributions. Our results offer a simple way to take into account an assumed exponential size distribution for sub-stellar atmospheric cloud microphysics using the two-moment method. In follow up studies, we will examine more complex distributions, such as the log-normal and gamma distributions, that require more than two moments to characterise self-consistently.
#### Title:
          Simulating the shaping of point-symmetric structures in the jittering jets explosion mechanism
 - **Authors:** Jessica Braudo, Amir Michaelis, Muhammad Akashi, Noam Soker (Technion, Israel)
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We conduct three-dimensional hydrodynamical simulations of core-collapse supernovae by launching several pairs of jets into a collapsing core model and show that the jittering jets explosion mechanism (JJEM) can form a point-symmetric morphology that accounts for observed morphologies of many core-collapse supernovae (CCSN) remnants. Point-symmetric morphologies are composed of pairs of opposite structures around the center of the CCSN remnant. In the JJEM, the newly born neutron star launches several to a few tens of pairs of jets with stochastically varying directions, and these jets explode the star. In the simulations with the FLASH numerical code, we launch pairs of jets with varying directions, energies, opening angles, and durations into the massive stellar core and follow their evolution for about two seconds. We show that the jets form pairs of opposite filaments, clumps, bubbles, and lobes, namely, prominent point-symmetric morphologies. The interaction of the jets with the core leads to vigorous Rayleigh-Taylor instabilities and excites many vortices, which also shape clumps and filaments. Our results strengthen the claim that the JJEM is the primary explosion mechanism of CCSNe.
#### Title:
          Model-independent $H_0$ within FLRW: Joint constraints from GWTC-3 standard sirens and strong lensing time delays
 - **Authors:** Ji-Yu Song, Jing-Zhao Qi, Jing-Fei Zhang, Xin Zhang
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph); High Energy Physics - Theory (hep-th)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The Hubble tension has emerged as a critical crisis in cosmology, with the cause remaining unclear. Determining the Hubble constant ($H_0$) independently of cosmological models and distance ladders will help resolve this crisis. In this letter, we for the first time use 47 gravitational-wave (GW) standard sirens from the third Gravitational-Wave Transient Catalog to calibrate distances in the strong lensing system, RXJ1131-1231, and constrain $H_0$ through the distance-sum rule, with minimal cosmological assumptions. We assume that light propagation over long distances is described by the Friedmann-Lemaitre-Robertson-Walker metric and that geometrical optics holds, but we do not need to assume the universe's contents or the theory of gravity on cosmological scales. Fixing $\Omega_K=0$, we obtain $H_0=73.22^{+5.95}_{-5.43}$ ${\rm km}~{\rm s}^{-1}~{\rm Mpc}^{-1}$ and $H_0=70.40^{+8.03}_{-5.60}$ ${\rm km}~{\rm s}^{-1}~{\rm Mpc}^{-1}$ by using the deflector galaxy's mass model and kinematic measurements to break mass-sheet transform, respectively. When $\Omega_K$ is not fixed, the central value of $H_0$ increases further. We find that our results are still dominated by statistical errors, and at the same time, we notice the great potential of using GW dark sirens to provide calibration, owing to their higher redshifts. When using 42 binary black holes and RXJ1131-1231, we obtain a $8.46 \%$ $H_0$ constraint precision, which is better than that from the bright siren GW170817 using the Hubble law by about $40\%$. In the future, as the redshift range of GW dark sirens increases, more and more SGLTDs can be included, and we can achieve high-precision, model-independent measurements of $H_0$ without the need for GW bright sirens.
#### Title:
          The stochastic gravitational wave background from cosmic superstrings
 - **Authors:** Anastasios Avgoustidis, Edmund J. Copeland, Adam Moss, Juhan Raidal
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph); High Energy Physics - Theory (hep-th)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We study the stochastic gravitational wave background sourced by a network of cosmic superstrings and demonstrate that incorporating higher-mass string species, beyond the fundamental string, is crucial for accurately modeling the resulting gravitational wave spectrum across frequencies ranging from nanohertz to kilohertz. Using the multi-tension velocity-dependent one-scale model to evolve the cosmic superstring network, we perform several fits to the NANOGrav 15-year dataset and obtain expectation values for the fundamental string tension, string coupling and effective size of compact extra dimensions. We find that the cosmic superstring best-fits are comparable in likelihood to Supermassive Black Hole models, thought by many to be the leading candidate explanation of the signal. The implications of the best-fit spectra are discussed within the context of future gravitational wave experiments. We obtain expectation values for the fundamental string tension of $\log_{10}(G\mu_1)=-11.5^{+0.3}_{-0.3}$($-11.6^{+0.2}_{-0.3}$) for gravitational waves originating from large cuspy (kinky) cosmic superstring loops and $\log_{10}(G\mu_1)=-9.7^{+0.7}_{-0.7}$($-9.9^{+1.0}_{-0.5}$) for small cuspy (kinky) loops. We also place $2\sigma$ upper bounds on the string coupling, finding $g_s<0.65$ in all cases, and comment on the implication of our results for the effective size of the compact extra dimensions.
#### Title:
          Deep source separation of overlapping gravitational-wave signals and non-stationary noise artifacts
 - **Authors:** Niklas Houba
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); General Relativity and Quantum Cosmology (gr-qc); Data Analysis, Statistics and Probability (physics.data-an); Instrumentation and Detectors (physics.ins-det)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The Laser Interferometer Space Antenna (LISA) will observe gravitational waves in the millihertz frequency band, detecting signals from a vast number of astrophysical sources embedded in instrumental noise. Extracting individual signals from these overlapping contributions is a fundamental challenge in LISA data analysis and is traditionally addressed using computationally expensive stochastic Bayesian techniques. In this work, we present a deep learning-based framework for blind source separation in LISA data, employing an encoder-decoder architecture commonly used in digital audio processing to isolate individual signals within complex mixtures. Our approach enables signals from massive black-hole binaries, Galactic binaries, and instrumental glitches to be disentangled directly in a single step, circumventing the need for sequential source identification and subtraction. By learning clustered latent space representations, the framework provides a scalable alternative to conventional methods, with applications in both low-latency event detection and full-scale global-fit analyses. As a proof of concept, we assess the model's performance using simulated LISA data in a controlled setting with a limited number of overlapping sources. The results highlight deep source separation as a promising tool for LISA, paving the way for future extensions to more complex datasets.
#### Title:
          Protostellar Outflows at the EarliesT Stages (POETS). VII. Circumstellar gas kinematics traced by water masers inside the HC HII region NGC7538 IRS1
 - **Authors:** Luca Moscadelli, Ciriaco Goddi, Tomoya Hirota, Alberto Sanna
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR); Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 This article focuses on NGC7538 IRS1, one of the most luminous and studied HC HII regions in the northern hemisphere. Our aim is to identify the young stellar objects (YSOs) embedded within the ionized gas and study their kinematic structures. This work expands on a recent survey called "Protostellar Outflows at the EarliesT Stages" (POETS), which has been devoted to studying young outflow emission on scales of 10-100 au near luminous YSOs, before they start photoionizing the surrounding medium. We carried out multi-epoch Very Long Baseline Array observations of the 22 GHz water masers toward NGC7538 IRS1 to measure the maser 3D velocities, which, following POETS' findings, are reliable tracers of the protostellar winds. Recently, we reobserved the water masers in NGC7538 IRS1 with sensitive global very long baseline interferometry (VLBI) observations to map weaker maser emission. Our study confirms the presence of two embedded YSOs, IRS1a and IRS1b, at the center of the two linear distributions of 6.7 GHz methanol masers observed in the southern and northern cores of the HC HII region, which have been previously interpreted in terms of edge-on rotating disks. The water masers trace an extended (~200 au) stationary shock front adjacent to the inner portion of the disk around IRS1a. This shock front corresponds to the edge of the southern tip of the ionized core and might be produced by the interaction of the disk wind ejected from IRS1a with the infalling envelope. The water masers closer to IRS1b follow the same LSR velocity (Vlsr) pattern of the 6.7~GHz masers rotating in the disk, but the direction and amplitude of the water maser proper motions are inconsistent with rotation. We propose that these water masers are tracing a photo-evaporated disk wind, where the maser Vlsr traces mainly the disk rotation and the proper motions the poloidal velocity of the wind.
#### Title:
          A search for sterile neutrinos in interacting dark energy models using DESI baryon acoustic oscillations and DES supernovae data
 - **Authors:** Lu Feng, Tian-Nuo Li, Guo-Hong Du, Jing-Fei Zhang, Xin Zhang
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph); High Energy Physics - Theory (hep-th)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Sterile neutrinos can influence the evolution of the universe, and thus cosmological observations can be used to search for sterile neutrinos. In this study, we utilized the latest baryon acoustic oscillations data from DESI, combined with the cosmic microwave background data from Planck and the five-year supernova data from DES, to constrain the interacting dark energy (IDE) models involving both cases of massless and massive sterile neutrinos. We consider four typical forms of the interaction term $Q=\beta H \rho_{\rm de}$, $Q=\beta H \rho_{\rm c}$, $Q=\beta H_{0} \rho_{\rm de}$, and $Q=\beta H_{0} \rho_{\rm c}$, respectively. Our analysis indicates that the current data provide only a hint of the existence of massless sterile neutrinos (as dark radiation) at about the $1\sigma$ level. In contrast, no evidence supports the existence of massive sterile neutrinos. Furthermore, in IDE models, the inclusion of (massless/massive) sterile neutrinos has a negligible impact on the constraint of the coupling parameter $\beta$. The IDE model of $Q=\beta H \rho_{\rm c}$ with sterile neutrinos does not favor an interaction. However, the other three IDE models with sterile neutrinos support an interaction in which dark energy decays into dark matter.
#### Title:
          Transit Timing Variations of the Sub-Saturn Exoplanet HAT-P-12b
 - **Authors:** Kaviya Parthasarathy, Hsin-Min Liu, Ing-Guey Jiang, Li-Chin Yeh, Napaporn A-thano, Supachai Awiphan, Wen-Chi Cheng, Devesh P. Sariya, Shraddha Biswas, Devendra Bisht, Evgeny Griv, David Mkrtichian, Vineet Kumar Mannaday, Parijat Thakur, Aleksey Shlyapnikov
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We present Transit Timing Variations (TTVs) of HAT-P-12b, a low-density sub-Saturn mass planet orbiting a metal-poor K4 dwarf star. Using 14 years of observational data (2009-2022), our study incorporates 7 new ground-based photometric transit observations, three sectors of Transiting Exoplanet Survey Satellite (TESS) data, and 23 previously published light curves. A total of 46 light curves were analyzed using various analytical models, such as linear, orbital decay, apsidal precession, and sinusoidal models to investigate the presence of additional planets. The stellar tidal quality factor ($Q_\star' \sim$ 28.4) is lower than the theoretical predictions, making the orbital decay model an unlikely explanation. The apsidal precession model with a $\chi_r^2$ of 4.2 revealed a slight orbital eccentricity (e = 0.0013) and a precession rate of 0.0045 rad/epoch. Frequency analysis using the Generalized Lomb-Scargle (GLS) periodogram identified a significant periodic signal at 0.00415 cycles/day (FAP = 5.1$\times$10$^{-6}$ %), suggesting the influence of an additional planetary companion. The sinusoidal model provides the lowest reduced chi-squared value ($\chi_r^2$) of 3.2. Sinusoidal fitting of the timing residuals estimated this companion to have a mass of approximately 0.02 $M_J$ , assuming it is in a 2:1 Mean-Motion Resonance (MMR) with HAT-P-12b. Additionally, the Applegate mechanism, with an amplitude much smaller than the observed TTV amplitude of 156 s, confirms that stellar activity is not responsible for the observed variations.
#### Title:
          Self-interacting neutrinos in light of recent CMB and LSS data
 - **Authors:** Adèle Poudou, Théo Simon, Thomas Montandon, Elsa M. Teixeira, Vivian Poulin
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); High Energy Physics - Phenomenology (hep-ph)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We update constraints on a simple model of self-interacting neutrinos involving a heavy scalar mediator with universal flavor coupling. According to past literature, such a model is allowed by Cosmic Microwave Background (CMB) data, with some CMB and large-scale structure data even favoring a strongly-interacting neutrino (SI$\nu$) scenario over $\Lambda$CDM. In this work, we re-evaluate the constraints on this model in light of the new Planck NPIPE data, DESI BAO data, and the Effective Field Theory of Large Scale Structures (EFTofLSS) applied to BOSS data. We find that Planck NPIPE are more permissive to the SI$\nu$ scenario and that DESI data favor the SI$\nu$ over $\Lambda$CDM. However, when considering EFTofBOSS data, this mode is no longer preferred. Therefore, new DESI data analyzed under the EFTofLSS are particularly awaited to shed light on this disagreement.
#### Title:
          Irradiated Pulsar Planets and Companions as 511 keV Positron Annihilation Line Sources
 - **Authors:** Zachary Metzler, Zorawar Wadiasingh
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Millisecond pulsars (MSPs) are prolific GeV {\gamma}-ray emitters, and nearly 80% of Fermi-LAT MSPs reside in compact binaries. We demonstrate that the companions in these compact MSPs binaries are also 511 keV annihilation line emitters using MEGAlib simulations (a high energy radiation transport software built with Geant4) to compute the particle showers and resulting backsplash emission from the pulsar irradiation. The 511 keV signal exhibits strong flux modulation and red/blueshifts associated with a binary orbit, enabling powerful coherent searches. Measuring the 511 keV emission would enable direct {\gamma}-ray characterization of unusual pulsar exoplanets and companions, and allow one to identify the unambiguous presence of active pulsars whose beams do not intercept Earth. Intriguingly, the 511 keV flux is brightest for ultra-compact systems against which pulsar surveys are systematically biased. These ultra-compact systems are also possibly prime LISA galactic sources. This necessitates future joint LISA-MeV {\gamma}-ray techniques to characterize MSP binaries. These MSP binaries may also contribute to the puzzling source of the excess 511 keV photons near the galactic bulge and center.
#### Title:
          Knot reconstruction of the scalar primordial power spectrum with Planck, ACT, and SPT CMB data
 - **Authors:** Antonio Raffaelli, Mario Ballardini
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We investigate a non-parametric Bayesian method for reconstructing the primordial power spectrum (PPS) of scalar perturbations using temperature and polarisation data from the {\em Planck}, ACT, and SPT CMB experiments. This reconstruction method is based on linear splines for the PPS between nodes in $k$-space whose amplitudes and positions are allowed to vary. All three data sets consistently show no significant deviations from a power-law form in the range $0.005 \lesssim k\,\mathrm{Mpc} \lesssim 0.16$ independent of the number of knots adopted to perform the reconstruction. The addition of high-resolution CMB measurements from ACT and SPT slightly improves the range of scales of the scalar PPS which are well constrained around a power law up to $k \simeq 0.25\,\mathrm{Mpc}^{-1}$ and $k \simeq 0.2\,\mathrm{Mpc}^{-1}$, respectively. At large scales, a potential oscillatory feature in the primordial power spectrum appears when we consider six or more nodes. We test the robustness of the methodology and our results by varying the detailed number of knots from $N=2$ to $N=10$. We have used the reconstructed scalar PPS to derive several quantities related to inflationary related to inflationary dynamics, such as the effective scalar spectral index, which describes the dependence of the PPS on the scales and parameters associated with the effective field theory of inflation, to provide information on possible departures from the standard single-field canonical case. Finally, we investigate whether the excess of smoothing in the region of the region of the acoustic peaks of the CMB anisotropy temperature power spectrum in the \textit{Planck} PR3 data is degenerate with our reconstructions of the PPS, but find no significant correlation between them.


by olozhika (Xing Yuchen). 


2025-03-14
