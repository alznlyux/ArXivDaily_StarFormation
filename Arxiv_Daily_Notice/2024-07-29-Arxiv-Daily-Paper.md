# New submissions for Monday, 29 July 2024 (showing 53 of 53 entries )
Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.


阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送

See `Usage.md` for instructions on how to personalize the repo. 


Keyword list: ['star formation', 'molecular cloud', 'interstellar medium', 'cloud', 'clump', 'core', 'filament', 'atomic gas', 'N-PDF', 'bubble', 'shell', 'HI']


Excluded: ['galaxies', 'galaxy cluster', 'AGN']


### Today: 25papers 
#### Title:
          A novel numerical method for mixed-frame multigroup radiation-hydrodynamics with GPU acceleration implemented in the QUOKKA code
 - **Authors:** Chong-Chong He (ANU), Benjamin D. Wibking (MSU), Mark R. Krumholz (ANU)
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); High Energy Astrophysical Phenomena (astro-ph.HE); Instrumentation and Methods for Astrophysics (astro-ph.IM); Plasma Physics (physics.plasm-ph); Space Physics (physics.space-ph)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Mixed-frame formulations of radiation-hydrodynamics (RHD), where the radiation quantities are computed in an inertial frame but matter quantities are in a comoving frame, are advantageous because they admit algorithms that conserve energy and momentum to machine precision and combine more naturally with adaptive mesh techniques, since unlike pure comoving-frame methods they do not face the problem that radiation quantities must change frame every time a cell is refined or coarsened. However, implementing multigroup RHD in a mixed-frame formulation presents challenges due to the complexity of handling frequency-dependent interactions and the Doppler shift of radiation boundaries. In this paper, we introduce a novel method for multigroup RHD that integrates a mixed-frame formulation with a piecewise powerlaw approximation for frequency dependence within groups. This approach ensures the exact conservation of total energy and momentum while effectively managing the Lorentz transformation of group boundaries and evaluation of group-averaged opacities. Our method takes advantage of the locality of matter-radiation coupling, allowing the source term for $N_g$ frequency groups to be handled with simple equations with a sparse Jacobian matrix of size $N_g + 1$, which can be inverted with $O(N_g)$ complexity. This results in a computational complexity that scales linearly with $N_g$ and requires no more communication than a pure hydrodynamics update, making it highly efficient for massively parallel and GPU-based systems. We implement our method in the GPU-accelerated RHD code QUOKKA and demonstrate that it passes a wide range of numerical tests. We demonstrate that the piecewise powerlaw method shows significant advantages over traditional opacity averaging methods for handling rapidly variable opacities with modest frequency resolution.
#### Title:
          Long-term radio monitoring of the fast X-ray transient EP240315a: evidence for a relativistic jet
 - **Authors:** R. Ricci, E. Troja, Y. Yang, M. Yadav, Y. Liu, H. Sun, X. Wu, H. Gao, B. Zhang, W. Yuan
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The recent launch of Einstein Probe (EP) in early 2024 opened up a new window onto the transient X-ray sky, allowing for real-time discovery and follow-up of fast X-ray transients (FXRTs). Multi-wavelength observations of FXRTs and their counterparts are key to characterize the properties of their outflows and, ultimately, identify their progenitors. Here, we report our long-term radio monitoring of EP240315A, a long-lasting ($\sim 1000$ s) high redshift ($z=4.9$) FXRT associated to GRB~240315C. Our campaign, carried out with the Australian Telescope Compact Array (ATCA), followed the transient's evolution at two different frequencies (5.5 GHz and 9~GHz) for three months. In the radio lightcurves we identify an unusual steep rise at 9 GHz, possibly due to a refreshed reverse shock, and a late-time rapid decay of the radio flux, which we interpret as a jet break due to the outflow collimation. We find that the multi-wavelength counterpart of EP240315A is well described by a model of relativistic jet seen close to its axis, with jet half-opening angle $\theta_j \approx 3 ^{\circ}$ and beaming-corrected total energy $E \simeq 4\times 10^{51}$~erg, typical of GRBs. These results show that a substantial fraction of FXRTs may be associated to standard GRBs and that sensitive X-ray monitors, such as Einstein Probe and the proposed HiZ-GUNDAM and Theseus missions, can successfully pinpoint their relativistic outflows up to high-redshifts.
#### Title:
          Establishing HI mass v.s. stellar mass and halo mass scaling relations using an abundance matching method
 - **Authors:** Yi Lu, Xiaohu Yang, Chengze Liu, Haojie Xu, Antonios Katsianis, Hong Guo, Xiaoju Xu, Yizhou Gu
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We combined data from the Sloan Digital Sky Survey (SDSS) and the Arecibo Legacy Fast ALFA Survey (ALFALFA) to establish the HI mass vs. stellar mass and halo mass scaling relations using an abundance matching method that is free of the Malmquist bias. To enable abundance matching, a cross-match between the SDSS DR7 galaxy group sample and the ALFALFA HI sources provides a catalog of 16,520 HI-galaxy pairs within 14,270 galaxy groups (halos). By applying the observational completeness reductions for both optical and HI observations, we used the remaining 8,180 ALFALFA matched sources to construct the model constraints. Taking into account the dependence of HI mass on both the galaxy and group properties, we establish two sets of scaling relations: one with a combination of stellar mass, $({g-r})$ color and halo mass, and the other with stellar mass, specific star-formation rate ($\rm sSFR$), and halo mass. We demonstrate that our models can reproduce the HI mass component as both a stellar and halo mass. Additional tests showed that the conditional HI mass distributions as a function of the cosmic web type and the satellite fractions were well recovered.
#### Title:
          Feasibility study of upper atmosphere density measurement on the ISS by observations of the CXB transmitted through the Earth rim
 - **Authors:** Takumi Kishimoto, Kumiko K. Nobukawa, Ayaki Takeda, Takeshi G. Tsuru, Satoru Katsuda, Nakazawa Kazuhiro, Koji Mori, Masayoshi Nobukawa, Hiroyuki Uchida, Yoshihisa Kawabe, Satoru Kuwano, Eisuke Kurogi, Yamato Ito, Yuma Aoki
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Measurements of the upper atmosphere at ~100 km are important to investigate climate change, space weather forecasting, and the interaction between the Sun and the Earth. Atmospheric occultations of cosmic X-ray sources are an effective technique to measure the neutral density in the upper atmosphere. We are developing the instrument SUIM dedicated to continuous observations of atmospheric occultations. SUIM will be mounted on a platform on the exterior of the International Space Station for six months and pointed at the Earth's rim to observe atmospheric absorption of the cosmic X-ray background (CXB). In this paper, we conducted a feasibility study of SUIM by estimating the CXB statistics and the fraction of the non-X-ray background (NXB) in the observed data. The estimated CXB statistics are enough to evaluate the atmospheric absorption of CXB for every 15 km of altitude. On the other hand, the NXB will be dominant in the X-ray spectra of SUIM. Assuming that the NXB per detection area of SUIM is comparable to that of the soft X-ray Imager onboard Hitomi, the NXB level will be much higher than the CXB one and account for ~80% of the total SUIM spectra.
#### Title:
          Accretion properties of soft X-ray transient XTE J1856+053 during its 2023 Outburst
 - **Authors:** Debjit Chatterjee, Arghajit Jana, Hsiang-Kuang Chang
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Soft X-ray transients are a subclass of the low mass X-ray binaries that occasionally show a sudden rise in their soft X-ray luminosity; otherwise, they remain in an extremely faint state. We investigate the accretion properties of the soft X-ray transient XTE J1856+053 during its 2023 outburst obtained by NICER and NuSTAR data in July. We present detailed results on the timing and spectral analysis of the X-ray emission during the outburst. The power spectral density shows no quasi-periodic oscillation features. The source's spectrum on July 19 can be well-fitted with a multi-color blackbody component, a power-law component, and a reflection component with a broadened iron emission line. NICER spectra can be well-fitted by considering a combination of a blackbody and a power-law. The source exhibits a transition within just five days from a soft state to an intermediate state during the outburst decline phase. The inner accretion disk has a low inclination angle ($\sim18^\circ$). The spectral analysis also suggests a high-spin ($a>0.9$) BH as the central accreting object.
#### Title:
          The foundation of "Saint V{\'e}ran-Paul Felenbok" astronomical observatory
 - **Authors:** Jean-Marie Malherbe
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 This paper is dedicated to the memory of Paul Felenbok (1936-2020) who was astronomer at Paris-Meudon observatory, and founded in 1974, fifty years ago, a high altitude station (2930 m), above Saint V{é}ran village in the southern Alps (Queyras). It was initially devoted to the study of the solar corona. Following solar eclipses (1970, 1973) observed with the Lallemand electronic camera, the main goal was to detect with this sensitive detector the structures of the far and hot corona in forbidden lines, using either narrow bandpass filters or spectroscopy. But everything had to be done prior to observations: a track, a house for astronomers, a dome and a complex instrument. We summarize here this fantastic adventure, which was partly successful in terms of scientific results and had to stop in 1982; however, the activity of the station resumed after 1989 under the auspices of the ``AstroQueyras'' association, which replaced the coronagraph by a 62 cm night telescope from Haute Provence observatory; the station extended later with two 50 cm telescopes, was rebuilt in 2015 and received the visit of thousands of amateurs.
#### Title:
          Twenty-three New Heartbeat Star Systems Discovered Based on TESS Data
 - **Authors:** Min-Yu Li, Sheng-Bang Qian, Ai-Ying Zhou, Li-Ying Zhu, Wen-Ping Liao, Er-Gang Zhao, Xiang-Dong Shi, Fu-Xing Li, Qi-Bin Sun
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Heartbeat stars (HBSs) are ideal astrophysical laboratories to study the formation and evolution of binary stars in eccentric orbits and the internal structural changes of their components under strong tidal action. We discover 23 new HBSs based on TESS photometric data. The orbital parameters, including orbital period, eccentricity, orbital inclination, argument of periastron, and epoch of periastron passage of these HBSs are derived by using a corrected version of Kumar et al.'s model based on the Markov Chain Monte Carlo (MCMC) method. The preliminary results show that these HBSs have orbital periods in the range from 2.7 to 20 days and eccentricities in the range from 0.08 to 0.70. The eccentricity-period relation of these objects shows a positive correlation between eccentricity and period, and also shows the existence of orbital circularization. The Hertzsprung-Russell diagram shows that the HBSs are not all located in a particular area. The distribution of the derived parameters suggests a selection bias within the TESS survey towards massive HBSs with shorter orbital periods, higher temperatures and luminosities. These objects are a very useful source to study the structure and evolution of eccentricity orbit binaries and to extend the TESS HBS catalog.
#### Title:
          Communicating the gravitational-wave discoveries of the LIGO-Virgo-KAGRA Collaboration
 - **Authors:** Hannah Middleton, Christopher P L Berry, Nicolas Arnaud, David Blair, Jacqueline Bondell, Nicolas Bonne, Debarati Chatterjee, Sylvain Chaty, Storm Colloms, Lynn Cominsky, Livia Conti, Isabel Cordero-Carrión, Zoheyr Doctor, Andreas Freise, Aaron Geller, Jen Gupta, Daniel Holz, William Katzman, David Keitel, Joey Shapiro Key, Nutsinee Kijbunchoo, Carl Knox, Coleman Krawczyk, Ryan N Lang, Shane L Larson, Chris North, Sascha Rieger, Aurore Simonnet, Andrew Spencer
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc); Physics Education (physics.ed-ph)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The LIGO-Virgo-KAGRA (LVK) Collaboration has made breakthrough discoveries in gravitational-wave astronomy, a new field of astronomy that provides a different means of observing our Universe. Gravitational-wave discoveries are possible thanks to the work of thousands of people from across the globe working together. In this article, we discuss the range of engagement activities used to communicate LVK gravitational-wave discoveries and the stories of the people behind the science using the activities surrounding the release of the third Gravitational Wave Transient Catalog as a case study.
#### Title:
          Towards unveiling the large-scale nature of gravity with the wavelet scattering transform
 - **Authors:** Georgios Valogiannis, Francisco Villaescusa-Navarro, Marco Baldi
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph); Data Analysis, Statistics and Probability (physics.data-an)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We present the first application of the Wavelet Scattering Transform (WST) in order to constrain the nature of gravity using the three-dimensional (3D) large-scale structure of the universe. Utilizing the Quijote-MG N-body simulations, we can reliably model the 3D matter overdensity field for the f(R) Hu-Sawicki modified gravity (MG) model down to $k_{\rm max}=0.5$ h/Mpc. Combining these simulations with the Quijote $\nu$CDM collection, we then conduct a Fisher forecast of the marginalized constraints obtained on gravity using the WST coefficients and the matter power spectrum at redshift z=0. Our results demonstrate that the WST substantially improves upon the 1$\sigma$ error obtained on the parameter that captures deviations from standard General Relativity (GR), yielding a tenfold improvement compared to the corresponding matter power spectrum result. At the same time, the WST also enhances the precision on the $\Lambda$CDM parameters and the sum of neutrino masses, by factors of 1.2-3.4 compared to the matter power spectrum, respectively. Despite the overall reduction in the WST performance when we focus on larger scales, it still provides a relatively $4.5\times$ tighter 1$\sigma$ error for the MG parameter at $k_{\rm max}=0.2$ h/Mpc, highlighting its great sensitivity to the underlying gravity theory. This first proof-of-concept study reaffirms the constraining properties of the WST technique and paves the way for exciting future applications in order to perform precise large-scale tests of gravity with the new generation of cutting-edge cosmological data.
#### Title:
          The Great Wave: Evidence of a large-scale vertical corrugation propagating outwards in the Galactic disc
 - **Authors:** E. Poggio, S. Khanna, R. Drimmel, E. Zari, E. D'Onghia, M. G. Lattanzi, P. A. Palicio, A. Recio-Blanco, L. Thulasidharan
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We analyse the three-dimensional structure and kinematics of two samples of young stars in the Galactic disc, containing respectively young giants ($\sim$16000 stars out to heliocentric distances of $\sim$7 kpc) and classical Cepheids ($\sim$3400 stars out to heliocentric distances of $\sim$15 kpc). Both samples show evidence of a large-scale vertical corrugation on top of the warp of the Milky Way, which has a vertical height of 150-200 pc, a radial width of about 3 kpc, and a total length of at least 10 kpc, possibly reaching 20 kpc with the Cepheid sample. The stars in the corrugation exhibit both radial and vertical systematic motions, with Galactocentric radial velocities towards the outer disc of about 10-15 km/s. In the vertical motions, once the warp signature is subtracted, the residuals show a large-scale feature of systematically positive vertical velocities, which is located radially outwards with respect to the corrugation, and whose line of maxima approximately coincides with the line of null vertical displacement, consistent with a vertical wave propagating towards the outer parts of the Galactic disc.
#### Title:
          Nova contributions to the chemical evolution of the Milky Way
 - **Authors:** Alex J. Kemp, Amanda I. Karakas, Andrew R. Casey, Benoit Cote, Robert G. Izzard, Zara Osborn
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Context. The explosive burning that drives nova eruptions results in unique nucleosynthesis that heavily over-produces certain isotopes relative to the solar abundance. However, novae are often ignored when considering the chemical evolution of our Galaxy due to their low ejecta masses. Aims. In this work, we use previously computed synthetic nova populations and the galactic chemical evolution code OMEGA+ to assess the impact that novae have on the evolution of stable elemental and isotopic abundances. Methods. We combine populations of novae computed using the binary population synthesis code binary_c with the galactic chemical evolution code OMEGA+ and detailed, white dwarf mass-dependent nova yields to model the nucleosynthetic contributions of novae to the evolution of the Milky Way. We consider three different nova yield profiles, each corresponding to a different set of nova yield calculations. Results. Despite novae from low-mass white dwarfs (WDs) dominating nova ejecta contributions, we find that novae occurring on massive WDs are still able to contribute significantly to many isotopes, particularly those with high mass numbers. We find that novae can produce up to 35% of the Galactic 13C and 15N mass by the time the model Galaxy reaches [Fe/H] = 0, and earlier in the evolution of the Galaxy (between [Fe/H] = -2 and -1) novae may have been the dominant source of 15N. Predictions for [13C/Fe], [15N/Fe], 12C/13C, and 14N/15N abundances ratios vary by up to 0.2 dex at [Fe/H] = 0 and by up to 0.7 dex in [15N/Fe] and 14N/15N between [Fe/H] = -2 and -1 (corresponding approximately to Galactic ages of 170 Myr and 1 Gyr in our model). The Galactic evolution of other stable isotopes (excluding Li) is not noticeably affected by including novae.
#### Title:
          ALMA-IMF XV: The core mass function in the high-mass star-formation regime
 - **Authors:** F. Louvet, P. Sanhueza, A. Stutz, A. Men'shchikov, F. Motte, R. Galván-Madrid, S. Bontemps, Y. Pouteau, A. Ginsburg, T. Csengeri, J. Di Francesco, P. Dell'Ova, M. González, P. Didelon, J. Braine, N. Cunningham, B. Thomasson, P. Lesaffre, P. Hennebelle, M. Bonfand, A. Gusdorf, R. H. Álverez-Gutiérrez, T. Nony, G. Busquet, F. Olguin, L. Bronfman, J. Salinas, M. Fernandez-Lopez, E. Moraux, H.L. Liu, X. Lu, V. Huei-Ru, A. Towner, M. Valeille-Manet, N. Brouillet, F. Herpin, B. Lefloch, T. Baug, L. Maud, A. Lopez-Sepulcre, B. Svodoba
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The stellar initial mass function (IMF) is critical to our understanding of star formation and the effects of young stars on their environment. On large scales, it enables us to use tracers such as UV or Halpha emission to estimate the star formation rate of a system and interpret unresolved star clusters across the universe. So far, there is little firm evidence of large-scale variations of the IMF, which is thus generally considered universal. Stars form from cores and it is now possible to estimate core masses and compare the core mass function (CMF) with the IMF, which it presumably produces. The goal of the ALMA-IMF large program is to measure the core mass function at high linear resolution (2700 au) in 15 typical Milky Way protoclusters spanning a mass range of 2500 to 32700 Msun. In this work, we used two different core extraction algorithms to extract about 680 gravitationally bound cores from these 15 protoclusters. We adopt per core temperature using the temperature estimate from the PPMAP Bayesian method. A power-law fit to the CMF of the sub-sample of cores above the 1.64 Msun completeness limit, 330 cores, through the maximum likelihood estimate technique yields a slope of 1.97 +/- 0.06, significantly flatter than the 2.35 Salpeter slope. Assuming a self-similar mapping between the CMF and the IMF, this result implies that these 15 high-mass protoclusters will generate atypical IMFs. This sample is the largest to date produced and analysed self-consistently, derived at matched physical resolution, with per-core temperature estimates and cores as massive as 150 Msun. We provide the raw source extraction catalogues and the source derived size, temperature, mass, and spectral indices in the 15 protoclusters.
#### Title:
          A Deep Reinforcement Learning Approach to Wavefront Control for Exoplanet Imaging
 - **Authors:** Yann Gutierrez, Johan Mazoyer, Olivier Herscovici-Schiller, Laurent M. Mugnier, Baptiste Abeloos, Iva Laginja
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Exoplanet imaging uses coronagraphs to block out the bright light from a star, allowing astronomers to observe the much fainter light from planets orbiting the star. However, these instruments are heavily impacted by small wavefront aberrations and require the minimization of starlight residuals directly in the focal plane. State-of-the art wavefront control methods suffer from errors in the underlying physical models, and often require several iterations to minimize the intensity in the dark hole, limiting performance and reducing effective observation time. This study aims at developing a data-driven method to create a dark hole in post-coronagraphic images. For this purpose, we leverage the model-free capabilities of reinforcement learning to train an agent to learn a control strategy directly from phase diversity images acquired around the focal plane. Initial findings demonstrate successful aberration correction in non-coronagraphic simulations and promising results for dark hole creation in post-coronagraphic scenarios. These results highlight the potential of model-free reinforcement learning for dark-hole creation, justifying further investigation and eventually experimental validation on a dedicated testbed.
#### Title:
          Revision of calcium and scandium abundances in Am stars based on NLTE calculations and comparison with diffusion stellar evolution models
 - **Authors:** L. I. Mashonkina, Yu. A. Fadeyev
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The homogeneous data sets for the calcium and scandium abundances accounting for departures from LTE were obtained for a sample of 54 metallic-line (Am) stars. The Ca and Sc abundances were found to correlate with effective temperature Teff, the abundance growth with increasing Teff being higher in stars with surface gravity log g < 4 than in those with log g > 4. No correlation was found between Ca or Sc abundances and the iron abundance or the velocity of axial rotation. Am stars exhibit on average the higher values of [Ca/H] than those of [Sc/H] as well as the abundance ratio [Ca/Sc] = 0.41 +/- 0.30. However, at Teff > 9500 K there is an allusion to the systematic difference between Am stars with surface gravity log g > 4 and log g < 4. The iron excess is nearly the same in the range 7200 K <= Teff <= 10030 K. Evolution diffusion models computed with the code MESA for stars with masses from 1.5 to 2Msun show the surface abundances that are in good agreement with Ca and Fe abundances observed in Am stars of the three open clusters with the age > 600 Myr. Additional mechanisms of chemical separation should be considered for explanation of the Am phenomenon in young stars of the Pleiades cluster. We tested the published diffusion stellar evolution models. The diffusion models by Richer et al. (2000) and Hui-Bon-Hoa et al. (2022) are shown to agree with observations of Am stars in the open clusters at large values of the free turbulence parameter: omega=1000 for Ca and Fe, omega=500 for Sc. There is no model with the mass and age of the Am-type star Sirius that could reproduce its surface abundances from He to Ni. The results presented in the paper may be of importance for understanding the chemical peculiarity of Am stars.
#### Title:
          The Double-Sided Silicon Strip Detector Tracker onboard the ComPair Balloon Flight
 - **Authors:** Nicholas Kirschner, Carolyn Kierans, Sambid Wasti, Adam J. Schoenwald, Regina Caputo, Sean Griffin, Iker Liceaga-Indart, Lucas Parker, Jeremy S. Perkins, Anna Zajczyk
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The ComPair balloon instrument is a prototype of the All-sky Medium Energy Gamma-ray Observatory (AMEGO) mission concept. AMEGO aims to bridge the spectral gap in sensitivity that currently exists from $\sim$100 keV to $\sim$100 MeV by being sensitive to both Compton and pair-production events. This is made possible through the use of four subsystems working together to reconstruct events: a double-sided silicon strip detector (DSSD) Tracker, a virtual Frisch grid cadmium zinc telluride (CZT) Low Energy Calorimeter, a ceasium iodide (CsI) High Energy Calorimeter, and an anti-coincidence detector (ACD) to reject charged particle backgrounds. Composed of 10 layers of DSSDs, ComPair's Tracker is designed to measure the position of photons that Compton scatter in the silicon, as well as reconstruct the tracks of electrons and positrons from pair-production as they propagate through the detector. By using these positions, as well as the absorbed energies in the Tracker and 2 Calorimeters, the energy and direction of the incident photon can be determined. This proceeding will present the development, testing, and calibration of the ComPair DSSD Tracker and early results from its balloon flight in August 2023.
#### Title:
          Deep learning interpretable analysis for carbon star identification in Gaia DR3
 - **Authors:** Shuo Ye, Wen-Yuan Cui, Yin-Bi Li, A-Li Luo, R.A. Hugh Jones
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Context. A large fraction of Asymptotic Giant Branch (AGB) stars develop carbon-rich atmospheres during their evolution. Based on their color and luminosity, these carbon stars can be easily distinguished from many other kinds of stars. However, a large number of G, K, and M giants are also distributed in the same region as carbon stars on the HR diagram. Their spectra have differences,especially in the prominent CN molecular bands. Aims. We aim to distinguish carbon stars from other kinds of stars using Gaia's XP spectra, while providing attribution explanations of key features necessary for identification, and even discovering additional new spectral key features. Methods. We proposed a classification model named `GaiaNet', an improved one-dimensional convolutional neural network specifically designed for handling Gaia's XP spectra. We utilized the SHAP interpretability model to calculate the SHAP value for each feature point in a spectrum, enabling us to explain the output of the `GaiaNet' model and provide further meaningful analysis Results. Compared to four traditional machine-learning methods, the `GaiaNet' model exhibits an average classification accuracy improvement of approximately 0.3% on the validation set, with the highest accuracy even reaching 100%. Utilizing the SHAP algorithm, we present a clear spectroscopic heatmap highlighting molecular band absorption features primarily distributed mainly around CN773.3 and CN895.0, and summarize five crucial feature regions for carbon star identification. Upon applying the trained classification model to the CSTAR sample with Gaia `xp_sampled_mean' spectra, we obtained 451 new candidate carbon stars as a by-product.
#### Title:
          TESSILATOR: a one-stop shop for measuring TESS rotation periods
 - **Authors:** A. S. Binks, H. M. Guenther
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR); Earth and Planetary Astrophysics (astro-ph.EP); Instrumentation and Methods for Astrophysics (astro-ph.IM)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We present a software package designed to produce photometric lightcurves and measure rotation periods from full-frame images taken by the Transiting Exoplanet Survey Satellite (TESS), which we name ``TESSILATOR''. TESSILATOR is the only publicly-available code that will run a full lightcurve and rotation period ($P_{\rm rot}$) analysis based on just a (list of) target identifier(s) or sky position(s) via a simple command-line prompt. This paper sets out to introduce the rationale for developing TESSILATOR, and then describes the methods, considerations and assumptions for: extracting photometry; dealing with potential contamination; accounting for natural and instrumental systematic effects; lightcurve normalisation and detrending; removing outliers and unreliable data; and finally, measuring the $P_{\rm rot}$ value and several periodogram attributes. Our methods have been tuned specifically to optimise TESS lightcurves and are independent from the pipelines developed by the TESS Science Processing Operations Center, meaning TESSILATOR can, in principle, analyse {\it any} target across the entire celestial sphere. We compare TESSILATOR $P_{\rm rot}$ measurements with TESS-SPOC-derived lightcurves of 1,560 (mainly FGKM-type) stars across four benchmark open clusters (Pisces-Eridanus, the Pleiades, the Hyades and Praesepe) and a sample of nearby field M-dwarfs. From a vetted subsample of 864 targets we find an excellent return of $P_{\rm rot}$ matches for the first 3 open clusters ($>85$ per cent) and a moderate ($\sim 60$ per cent) match for the 700 Myr Praesepe and MEarth sample, which validates TESSILATOR as a tool for measuring $P_{\rm rot}$. The TESSILATOR code is available at \url{this https URL}.
#### Title:
          Fundamental Tests of White Dwarf Cooling Physics with Wide Binaries
 - **Authors:** Manuel Barrientos, Mukremin Kilic, Pierre Bergeron, Simon Blouin, Warren R. Brown, Jeff J. Andrews
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 We present follow-up spectroscopy and a detailed model atmosphere analysis of 29 wide double white dwarfs, including eight systems with a crystallized C/O core member. We use state-of-the-art evolutionary models to constrain the physical parameters of each star, including the total age. Assuming that the members of wide binaries are coeval, any age difference between the binary members can be used to test the cooling physics for white dwarf stars, including potential delays due to crystallization and $^{22}$Ne distillation. We use our control sample of 14 wide binaries with non-crystallized members to show that this method works well; the control sample shows an age difference of only $\Delta$Age = $-0.03 \pm$ 0.15 Gyr between its members. For the eight crystallized C/O core systems we find a cooling anomaly of $\Delta$Age= 1.13$^{+1.20}_{-1.07}$ Gyr. Even though our results are consistent with a small additional cooling delay ($\sim1$ Gyr) from $^{22}$Ne distillation and other neutron-rich impurities, the large uncertainties make this result not statistically significant. Nevertheless, we rule out cooling delays longer than 3.6 Gyr at the 99.7% ($3\sigma$) confidence level for 0.6-0.9 $M_{\odot}$ white dwarfs. Further progress requires larger samples of wide binaries with crystallized massive white dwarf members. We provide a list of subgiant + white dwarf binaries that could be used for this purpose in the future.
#### Title:
          Binary orbit and disks properties of the RW Aur system using ALMA observations
 - **Authors:** N.T. Kurtovic, S. Facchini, M. Benisty, P. Pinilla, S. Cabrit, E.L.N. Jensen, C. Dougados, R. Booth, C.N. Kimmig, C.F. Manara, J.E. Rodriguez
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP); Instrumentation and Methods for Astrophysics (astro-ph.IM); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The dynamical interactions between young binaries can perturb the material distribution of their circumstellar disks, and modify the planet formation process. In order to constrain the impact and nature of the binary interaction in the RW Aur system (bound or unbound), we analyzed the circumstellar material at 1.3 mm wavelengths, as observed at multiple epochs by ALMA. We analyzed the disk properties through parametric visibility modeling, and we used this information to constrain the dust morphology and the binary orbital period. We imaged the dust continuum emission of RW Aur with a resolution of 3 au, and we find that the radius enclosing 90% of the flux (R90%) is 19 au and 14 au for RW Aur A and B, respectively. By modeling the relative distance of the disks at each epoch, we find a consistent trend of movement for the disk of RW Aur B moving away from the disk of RW Aur A at an approximate rate of 3 mas/yr (about 0.5 au/yr in sky-projected distance). By combining ALMA astrometry, historical astrometry, and the dynamical masses of each star, we constrain the RW Aur binary stars to be most likely in a high-eccentricity elliptical orbit with a clockwise prograde orientation relative to RW Aur A, although low-eccentricity hyperbolic orbits are not ruled out by the astrometry. Our analysis does not exclude the possibility of a disk collision during the last interaction, which occurred $295_{-74}^{+21}$ yr ago relative to beginning of 2024. Evidence for the close interaction is found in a tentative warp of 6 deg in the inner 3 au of the disk of RW Aur A, in the brightness temperature of both disks, and in the morphology of the gas emission. A narrow ring that peaks at 6 au around RW Aur B is suggestive of captured material from the disk around RW Aur A.
#### Title:
          Gravitational waves from a curvature-induced phase transition of a Higgs-portal dark matter sector
 - **Authors:** Andreas Mantziris, Orfeu Bertolami
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph); High Energy Physics - Theory (hep-th)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The study of interactions between dark matter and the Higgs field opens an exciting connection between cosmology and particle physics, since such scenarios can impact the features of dark matter as well as interfering with the spontaneous breaking of the electroweak symmetry. Furthermore, such Higgs-portal models of dark matter should be suitably harmonised with the various epochs of the universe and the phenomenological constraints imposed by collider experiments. At the same time, the prospect of a stochastic gravitational wave background offers a promising new window into the primordial universe, which can complement the insights gained from accelerators. In this study, we examined whether gravitational waves can be generated from a curvature-induced phase transition of a non-minimally coupled dark scalar field with a portal coupling to the Higgs field. The main requirement is that the phase transition is of first order, which can be achieved through the introduction of a cubic term on the scalar potential and the sign change of the curvature scalar. This mechanism was investigated in the context of a dynamical spacetime during the transition from inflation to kination, while also considering the possibility for inducing electroweak symmetry breaking in this manner for a sufficiently low reheating temperature when the Higgs-portal coupling is extremely weak. We considered a large range of inflationary scales and both cases of positive and negative values for the non-minimal coupling, while taking into account the bound imposed by Big Bang Nucleosythesis. The resulting gravitational wave amplitudes are boosted by kination and thus constrain the parameter space of the couplings significantly. Even though the spectra lie at high frequencies for the standard high inflationary scales, there are combinations of parameter space where they could be probed with future experiments.
#### Title:
          The accreted Galaxy: An overview of TESS metal-poor accreted stars candidates
 - **Authors:** Danielle de Brito Silva, Paula Jofré, Clare Worley, Keith Hawkins, Payel Das
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 The Milky Way is a mosaic of stars from different origins. In particular, metal-poor accreted star candidates offer a unique opportunity to better understand the accretion history of the Milky Way. In this work, we aim to explore the assembly history of the Milky Way by investigating accreted stars in terms of their ages, dynamical properties, and chemical abundances. We also aim to better characterize the impact of incorporating asteroseismic information on age and chemical abundance calculations of metal-poor accreted stars for which TESS data is available. In this study, we conducted an in-depth examination of 30 metal-poor accreted star candidates, using TESS and Gaia data, as well as MIKE spectra. We find satisfactory agreement between seismic and predicted/spectroscopic surface gravity (log g) values, demonstrating the reliability of spectroscopic data from our methodology. We found that while age determination is highly dependent on the log g and asteroseismic information used, the overall chemical abundance distributions are similar for different log g. However, we found that calcium (Ca) abundances are more sensitive to the adopted log g. Our study reveals that the majority of our stars have properties compatible to those reported for the Gaia-Sausage-Enceladus, with a minority of stars that might be associated to Splash. We found an age distribution with a median of 11.3 Gyr with lower and upper uncertainties of 4.1 and 1.3 Gyr respectively when including asteroseismic information. As regarding some key chemical signatures we note that these stars are metal-poor ([Fe/H]) < -0.8), alpha-rich ([alpha]/Fe] > 0.2), copper-poor ([Cu/Fe] < 0 ) and with chemical abundances typical of accreted stars. These findings illustrate the importance of multi-dimensional analyses in unraveling the complex accretion history of the Milky Way.
#### Title:
          Catalog of outbursts of neutron star LMXBs
 - **Authors:** Craig O. Heinke, Junwen Zheng, Thomas J. Maccarone, Nathalie Degenaar, Arash Bahramian, Gregory R. Sivakoff
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 Many X-ray binaries are transiently accreting. Having statistics on their recurrence times is helpful to address questions related to binary evolution and populations, as well as the physics of binary systems. We compile a catalog of known outbursts of neutron star (identified through bursts or pulsations) low-mass X-ray binaries, until late 2023. Most outbursts are taken from the literature, but we also identify some outbursts from public X-ray monitoring lightcurves. We find 109 outbursts not previously identified in the literature; most are from the frequent transients GRS 1747-312 and the Rapid Burster MXB 1730-335, though we suspect that two outbursts from Liller 1 may be from another transient, besides the Rapid Burster. We also find new outbursts for 10 other systems, and verify substantial quiescent intervals for XMM J174457-2850.3, XMMU J174716.1-281048, and AX J1754.2-2754. Outburst detection has been relatively efficient since 1996 for outbursts above $F_X$(2-10)$=3\times10^{-10}$ ergs/s/cm$^2$. While several systems have many known outbursts, 40 of the 85 systems we track have zero or one recorded outburst between 1996 and 2023. This suggests that faint Galactic Center X-ray binaries may be neutron star X-ray binaries, though we cannot completely rule out the proposition that most neutron star X-ray binaries undergo frequent outbursts below all-sky monitor detection limits.
#### Title:
          The comparison of an optical and X-ray counterpart of subparsec supermassive binary black holes
 - **Authors:** P. Jovanović, S. Simić, V. Borka Jovanović, D. Borka, L. Č. Popović
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 In this paper, we study and compare the optical and X-ray counterparts of subparsec supermassive black hole binaries (SMBHBs). With that aim, we simulated the profiles of optical spectral lines emitted from the broad line region (BLR) as well as X-ray spectral lines emitted from the relativistic accretion disks around both black holes and compared them with each other. The obtained results showed that SMBHBs could cause a specific, but different variability of the lines from the optical part and Fe K$\alpha$ line, leaving potentially detectable imprints in their profiles. Since these imprints depend on the orbital phase of the system, they could be used for reconstructing the Keplerian orbits of the components in the observed SMBHBs. Moreover, such signatures in the optical and X-ray line profiles of the observed SMBHBs could be used as a tool for the detection of these objects as well as for studying their properties.
#### Title:
          A comparative analysis of dissipation coefficients in warm inflation
 - **Authors:** F. B. M. dos Santos, R. de Souza, J. S. Alcaniz
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 In the warm inflation scenario, the early cosmic acceleration is driven by the inflaton coupled to thermal fields, decaying into radiation and leaving a hot universe populated by relativistic particles after the end of inflation. The interaction is usually modeled by a dissipation coefficient $\Upsilon$ that contains the microphysics of the model. In this work, we adopt a well-motivated potential $V(\phi)=\frac{\lambda}{4}\phi^4$ and constrain a variety of $\Upsilon$ parameterizations by using updated Cosmic Microwave Background data from the \textit{Planck} and \textit{BICEP/Keck Array} collaborations. We also use a Bayesian statistical criterion to compare the observational viability of these models. Our results show a significant improvement in the constraints over past results reported in the literature and also that some of these warm inflation models can be competitive compared to Starobinsky inflation.
#### Title:
          Hybrid summary statistics: neural weak lensing inference beyond the power spectrum
 - **Authors:** T. Lucas Makinen, Tom Charnock, Natalia Porqueres, Axel Lapel, Alan Heavens, Benjamin D. Wandelt
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO); Machine Learning (cs.LG); Computational Physics (physics.comp-ph); Machine Learning (stat.ML); Other Statistics (stat.OT)
 - **Arxiv link:** https://arxiv.org/abs/
 - **Pdf link:** https://arxiv.org/pdf/
 - **Abstract**
 In inference problems, we often have domain knowledge which allows us to define summary statistics that capture most of the information content in a dataset. In this paper, we present a hybrid approach, where such physics-based summaries are augmented by a set of compressed neural summary statistics that are optimised to extract the extra information that is not captured by the predefined summaries. The resulting statistics are very powerful inputs to simulation-based or implicit inference of model parameters. We apply this generalisation of Information Maximising Neural Networks (IMNNs) to parameter constraints from tomographic weak gravitational lensing convergence maps to find summary statistics that are explicitly optimised to complement angular power spectrum estimates. We study several dark matter simulation resolutions in low- and high-noise regimes. We show that i) the information-update formalism extracts at least $3\times$ and up to $8\times$ as much information as the angular power spectrum in all noise regimes, ii) the network summaries are highly complementary to existing 2-point summaries, and iii) our formalism allows for networks with smaller, physically-informed architectures to match much larger regression networks with far fewer simulations needed to obtain asymptotically optimal inference.


by olozhika (Xing Yuchen). 


2024-07-29
