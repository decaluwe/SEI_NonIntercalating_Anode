# Tungsten_SEI_2018

This repository contains the data and computational routines needed to reproduce the analysis and figures in our paper  (currently under review):

>"Direct, in operando observation of the bilayer solid electolyte interphase structure: Electrolyte reduction on a non-intercalating tungsten electrode," by C.H. Lee, A. LeBar, J.A. Dura, and S.C. DeCaluwe.  

While some data processing (particularly w/r/t the EQCM-D data) was done using commercial software, all analysis and figure preparation was carried out using freely-available open-source software.  The data is provided in post-processed form, so that access to the commercial software is not required.

This paper involved two operando techniques -- neutron reflectometry (NR) and electrochemical quartz crystal microbalance measurements with dissipation monitoring (EQCM-D) -- to analyze the solid electrolyte interphase (SEI) grown on a non-intercalating tunsten anode. Measurements were conducted in parallel on two different samples, and as such some degree of humility is required in directly correlating the data between the two techniques.

## Contents
### Data folder
This folder contains the NR and QCM data. 
* The NR data has been reduced using the NIST Center for Neutron Research's ReflPak software (https://www.ncnr.nist.gov/reflpak/), and fit using Refl1D (https://github.com/reflectometry/refl1d), as described in the manuscript.  Fitting was carried out using the model file `w3_3l2_w4_1l_generic_SiO2_FixRoughness.py` which can be re-produced by the interested reader by following the instructions in that folder's `README` file.  The data for Table 1 are derived from the file  `w3w4_TriFitReduced_eps_3kB_3kS_03222018/w3_3l2_w4_1l_generic_SiO2_FixRoughness.err`.
* The EQCM data was fit using Q-Tools software from Biolin scientific, to convert the frequency and dissipation shifts to mass uptake, viscosity, and shear profiles, as described in the manuscript.  The resulting values were then filtered using Matlab software to remove high-frequency noise, also as described in the manuscript.  The fitted and filtered QCM-D data are in the csv file `EQCM_Data/QCM_CV_0705_Data_filtered.csv`.
### Figures folder
This folder contains all files used to create all paper figures, and perform other data analysis. All software used is open source. `README` files in each folder provide more information.
* Figure 1: The experiment setup figure was created using Inskcape.
* Figure 2: The OCP trace plot was created using the Jupyter notebook included here, using the exported Gamry Data, also included here.
* Figure 3: The NR data was plotted using the Jupyter notebook included here.
* Figure 4 and Table 2: The EQCM-D data for Figure 4 and Table 2 was analyzed using the Jupyter notebook included here.
* Figure 5: The composition model logic figure was prepared using Inkscape.
* Figures 6 and 7: the composition model was run and the histograms plotted using the Jupyter notebook included here.
### Analysis workflow
The interested reader can therefore directly recreate nearly the entire workflow necessary to prepare the published manuscript:
* Re-reduce the NR data
* Run the NR fits using Refl1D
* Run the analysis and create the figures using the Jupyter Notebook files

