# Showing new listings for Wednesday, 22 July 2026
Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.


阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送

See `Usage.md` for instructions on how to personalize the repo. 


Keyword list: ['star formation', 'molecular cloud', 'interstellar medium', 'dust', 'cloud', 'clump', 'core', 'filament', 'atomic gas', 'H$_2$', 'HI', 'N-PDF', 'bubble', 'shell', 'feedback', 'jet', 'outflow', 'protostar']


Excluded: ['galaxies', 'galaxy clusters', 'AGN', 'black hole', 'lensing', 'dark matter', 'dark energy', 'fast radio burst', 'pulsar', 'neutron star', 'white dwarf', 'AGB', ' z ', 'lightcurve']


### Today: 4papers 
#### Title:
          Capture of interstellar objects during stellar encounters
 - **Authors:** Sean N. Raymond, Nathan A. Kaib, Matthew J. Hopkins
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP); Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
- **Arxiv link:** [https://arxiv.org/abs/2607.18551](https://arxiv.org/abs/2607.18551)
- **Pdf link:** [https://arxiv.org/pdf/2607.18551.pdf](https://arxiv.org/pdf/2607.18551.pdf)
- **Abstract**
 As they orbit within the Galaxy, stars swim through a vast population of interstellar objects (ISOs). In this paper, we use N-body simulations to show that a fraction of ISOs within $\sim$1 pc of the Sun (its tidal radius) may be captured during the flyby of another star -- a mechanism that requires no planets. Capture is most efficient when the impulse imparted by the flyby is comparable to the escape speed at the widest stable orbit, which is roughly 0.1 km/s for the Sun. ISO capture is dominated by the few highest-impulse stellar flybys, typically involving relatively slow encounters with massive stars. Most ISOs are captured in the outer parts of the Oort cloud, with semimajor axes greater than $\sim$50,000 au. Using Monte Carlo simulations, we show that the Sun underwent only a small number of ISO-capturing flybys in its history (median [mean] of 1 [1.7]). Using the {Ō}tautahi-Oxford population model, we estimate that a few times $\sim$$10^{4}$ `Oumuamua-sized ISOs were likely captured by the Sun. This only represents a $\sim$$10^{-8\pm1}$ contribution to the total Oort cloud population, yet it contains roughly as many present-day captured ISOs as Jupiter-assisted capture provides. Given that flybys are unavoidable in the Galactic field, most stars should, at any given time, host have sparse Oort clouds populated with ISOs captured during stellar flybys. Massive stars are both the main drivers of capture when they fly by a given star, and more efficient at capturing ISOs around themselves than low-mass stars.
#### Title:
          Estimating stellar metallicities from Gaia DR3 XP data using LAMOST DR10
 - **Authors:** Divyansh Srivastava, Andrzej Niedzielski, Rodolfo Smiljanic
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
- **Arxiv link:** [https://arxiv.org/abs/2607.18707](https://arxiv.org/abs/2607.18707)
- **Pdf link:** [https://arxiv.org/pdf/2607.18707.pdf](https://arxiv.org/pdf/2607.18707.pdf)
- **Abstract**
 Gaia DR3 provides astrophysical parameters for hundreds of millions of stars, but the metallicities [M/H] from its GSP-Phot module suffer from systematic biases. We estimate stellar metallicities from Gaia DR3 data using the homogeneous spectroscopic iron abundances [Fe/H] of LAMOST DR10 as training labels. We cross-matched LAMOST DR10 with Gaia DR3 and trained a gradient-boosted decision-tree regressor (XGBoost) on 1.20 million AFGK stars using only Gaia-derived inputs and proxies. We validated the estimates on held-out LAMOST stars, GALAH DR4, APOGEE DR17, and 46 open clusters, and applied the model to measure the radial metallicity gradient of the Milky Way disk. On the held-out test set, the model achieves a mean absolute error of 0.052 dex and $R^2=0.94$ with negligible bias, compared with 0.242 dex for GSP-Phot on the same stars. The estimates transfer well to external surveys, with mean absolute errors of 0.066 dex for GALAH and 0.068 dex for APOGEE. For open clusters, the median difference between our estimated [Fe/H] and spectroscopic values is 0.041 dex, smaller than both GSP-Phot (0.248 dex) and a previous APOGEE-trained XGBoost model (0.067 dex). Applied to the Galactic disk, our model recovers a broken thin-disk radial gradient, with inner and outer slopes of $+0.119$ and $-0.058\,\mathrm{dex\,kpc^{-1}}$, respectively, and a break near 5.9 kpc, as well as an open-cluster gradient of $-0.066\,\mathrm{dex\,kpc^{-1}}$; both agree with previous high-resolution spectroscopic studies. Our [Fe/H] estimates are accurate to 0.05-0.07 dex for AFGK stars with $[\mathrm{Fe/H}]\gtrsim-2.5$; below this limit, the predictions should be treated as lower bounds. The catalogue and trained model are publicly available on Zenodo and are suitable for chemical studies of the Milky Way.
#### Title:
          Determination of the horizontal velocity field in the solar atmosphere: Method validation using 3D MHD model
 - **Authors:** Andrii Prysiazhnyi, Oleksandra Baran
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
- **Arxiv link:** [https://arxiv.org/abs/2607.19169](https://arxiv.org/abs/2607.19169)
- **Pdf link:** [https://arxiv.org/pdf/2607.19169.pdf](https://arxiv.org/pdf/2607.19169.pdf)
- **Abstract**
 We present an improved version and further validation of a method, originally introduced by Stodilka (2016), for reconstructing horizontal velocity fields in the solar atmosphere from physical parameters typically derived from spectroscopic observations through inversion techniques. This approach relies on the continuity equation and the assumption of negligible vertical vorticity. Several algorithmic modifications were implemented to allow application to large spatial grids, including the compact storage of a sparse matrix of the system of linear equations. The method was tested using snapshots from the realistic 3D MHD Bifrost simulation en024048_hion of the solar atmosphere, covering heights from 20 to 980 km. Horizontal velocities were reconstructed from model density and vertical velocity values. A sinc filter with a Lanczos window was applied to the reconstructed horizontal velocity maps to reduce artefacts related primarily to the use of horizontal periodic boundary conditions. In the photospheric layers, the reconstructed horizontal velocity fields show a high level of agreement with the model values, with the Pearson correlation coefficient in the range 0.8-0.9. The method performs best within granules, whereas larger discrepancies occur in intergranular lanes due to complex counter-streaming flows. In the chromospheric layers, the reconstruction quality decreases significantly with height, consistent with the increasing importance of vortex motions and the breakdown of the underlying assumption. The method provides a reliable and efficient tool for reconstructing horizontal flows in the solar photosphere. The proposed improvements make the method applicable to large observational datasets.
#### Title:
          Identifying and Determining Atmospheric Parameters of BHB Stars Based on LAMOST DR11
 - **Authors:** Xiao-Long Wang, Wen-Yuan Cui, Jie Ju, Guo-Zhen Hu, Min Fang, Shuai Zhang, Jia-Ming Liu
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
- **Arxiv link:** [https://arxiv.org/abs/2607.19175](https://arxiv.org/abs/2607.19175)
- **Pdf link:** [https://arxiv.org/pdf/2607.19175.pdf](https://arxiv.org/pdf/2607.19175.pdf)
- **Abstract**
 Large catalogs of blue horizontal-branch (BHB) stars are essential for studying substructures and kinematics of the Galactic halo. And accurate determination of atmospheric parameters for BHB stars provides insight into stellar evolution. In this work, we perform a systematic search for BHB stars based on LAMOST DR11, and identify $13\,988$ BHB spectra, corresponding to $10\,236$ unique BHB stars. We estimate an identification rate of $\sim80\%-90\%$, and a contamination rate of $\lesssim10\%$ for our sample. Atmospheric parameters for these BHB stars are estimated via the data-driven method named the Stellar LAbel Machine (SLAM). We demonstrate the necessity of including color indices in the spectral labeling to effectively break the degeneracy between effective temperature and surface gravity. We note a bump in the distribution of [Fe/H], and most of these metal-rich BHB stars belong to the disk population. We also provide a list of 4282 blue straggler (BS) stars with determined atmospheric parameters.


by Al.Zn (Xin Lyu). 


2026-07-22
