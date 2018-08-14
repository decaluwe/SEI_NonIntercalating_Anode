from refl1d.names import *
from numpy import arange, linspace

#----------------------------------------------------------------------------------

Probe.view = 'log'             # log, linear, fresnel, or Q**4

SiOx_SLD = 3.4688
SiOx_irho = 0.00000985

W_SLD = 3.072
W_irho = 0.03317

WOx_SLD = 4.141
WOx_irho = 0.009456

elyte_SLD = 4.558
elyte_irho = 0.001477

#Using Li2CO3 as reference for inner SEI
sei_inner_SLD = 3.483
sei_inner_irho = 0.06737

#Using elyte as reference for outer SEI
sei_outer_SLD = elyte_SLD
sei_outer_irho = elyte_irho

data_file_bare = '3bare_He.refl'
data_file_sei = 'w3ocv_first.refl'

instrument = NCNR.ANDR(Tlo=0.5, slits_at_Tlo=0.2, slits_below=0.05)

probe_bare = instrument.load(data_file_bare)
probe_sei = instrument.load(data_file_sei)

### SLDs
rho_SiOx = Parameter(name="SiOx_relDensity", value=1.0)
rho_W_bare = Parameter(name="W_bare_relDensity", value=1.0)
rho_W_sei = Parameter(name="W_sei_relDensity", value=1.0)
rho_WOx_bare = Parameter(name="WOx_bare_relDensity", value=1.0)
rho_SEI_inner = Parameter(name="SEI_inner_relDensity", value=1.0)
rho_SEI_outer = Parameter(name="SEI_outer_relDensity", value=1.0)
rho_elyte_sei = Parameter(name="elyte_relDensity_sei",value=1.0)

SiOx = SLD(name="SiOx", rho=rho_SiOx*SiOx_SLD, irho=rho_SiOx*SiOx_irho)

W_bare = SLD(name="W_bare", rho=rho_W_bare*W_SLD, irho=rho_W_bare*W_irho)
W_sei = SLD(name="W_sei", rho=rho_W_sei*W_SLD, irho=rho_W_sei*W_irho)

WOx_bare = SLD(name="WOx_bare", rho=rho_WOx_bare*WOx_SLD, irho=rho_WOx_bare*WOx_irho)

elyte_sei = SLD(name="elyte", rho=rho_elyte_sei*elyte_SLD, irho=rho_elyte_sei*elyte_irho)
sei_inner = SLD(name="sei_inner", rho=rho_SEI_inner*sei_inner_SLD, irho=rho_SEI_inner*sei_inner_irho)
sei_outer = SLD(name="sei_outer", rho=rho_SEI_outer*sei_outer_SLD, irho=rho_SEI_outer*sei_outer_irho)

### Interfaces
Si_SiOx = Parameter(name="Si:SiOx", value=0.0326474)
SiOx_W = Parameter(name="SiOx:W_bare", value=12.9251)
W_WOx_bare = Parameter(name="W:WOx_bare" ,value=0.273827)
WOx_air = Parameter(name="WOx:air", value=0.3)

W_inner = Parameter(name="W:inner_sei", value=0.3)
sei_inner_outer = Parameter(name="sei_inner:sei_outer", value=0.3)
sei_elyte = Parameter(name="sei:elyte", value=100)

### Thicknesses
SiOx_th = Parameter(name="SiOx_thickness", value=110.5)

W_th_bare = Parameter(name="W_thickness_bare",value=149.5)
W_th_sei = Parameter(name="W_thickness_sei",value=149.5)

WOx_th_bare = Parameter(name="WOx_thickness_bare",value=19)

sei_inner_th = Parameter(name="sei_inner_thickness",value=20)
sei_outer_th = Parameter(name="sei_outer_thickness",value=100)

### Samples
sample_bare = silicon(0,Si_SiOx*SiOx_th) | SiOx(SiOx_th,SiOx_W*SiOx_th) | W_bare(W_th_bare,W_WOx_bare*WOx_th_bare) | WOx_bare(WOx_th_bare,WOx_air*WOx_th_bare) | air

sample_sei = elyte_sei(0,sei_elyte*sei_outer_th) | sei_outer(sei_outer_th,sei_inner_outer*sei_inner_th) | sei_inner(sei_inner_th,W_inner*sei_inner_th) | W_sei(W_th_sei,SiOx_W*SiOx_th) | SiOx(SiOx_th,Si_SiOx*SiOx_th) | silicon

### Fitting Parameters

#SLDs
rho_SiOx.range(0.95, 1.1)
rho_W_bare.range(-0.32552, 1.6276)
rho_W_sei.range(-0.32552, 1.05)
rho_WOx_bare.range(-0.24149, 1.207438)
rho_SEI_inner.range(-0.3176, 1.0)
rho_SEI_outer.range(-0.2194, 1.09697)
rho_elyte_sei.range(0.75,1.25)


#Thicknesses
SiOx_th.range(95,125)
W_th_bare.range(60,200)
W_th_sei.range(60,200)

WOx_th_bare.range(5,40)

sei_inner_th.range(5,200)
sei_outer_th.range(5,200)

#Interfaces
Si_SiOx.range(0.001,0.45)
SiOx_W.range(0.001,0.45)
W_WOx_bare.range(0.001,0.45)
W_inner.range(0.001,0.45)
WOx_air.range(0.001,0.45)
sei_inner_outer.range(0.001,0.45)
sei_elyte.range(0.1,0.45)

#Experimental Parameters
theta_offset_bare = Parameter(name="Theta_offset_bare", value=0)
theta_offset_sei = Parameter(name="Theta_offset_sei", value=0)
intensity_bare = Parameter(name="Intensity_bare", value=1)
intensity_sei = Parameter(name="Intensity_sei", value=1)
background_bare = Parameter(name="Background_bare", value=1)
background_sei = Parameter(name="Background_sei", value=1)

probe_bare.theta_offset = theta_offset_bare
probe_bare.intensity = intensity_bare
probe_bare.background = background_bare*1e-6
probe_sei.theta_offset = theta_offset_sei
probe_sei.intensity = intensity_sei
probe_sei.background = background_sei*1e-6

theta_offset_bare.range(-0.005,0.005)
theta_offset_sei.range(-0.005,0.005)

intensity_bare.range(0.7,1.2)
intensity_sei.range(0.7,1.2)

background_bare.range(0,5)
background_sei.range(0,5)

M_bare = Experiment(probe=probe_bare, sample=sample_bare)
M_sei = Experiment(probe=probe_sei, sample=sample_sei)

problem = MultiFitProblem([M_bare, M_sei])
