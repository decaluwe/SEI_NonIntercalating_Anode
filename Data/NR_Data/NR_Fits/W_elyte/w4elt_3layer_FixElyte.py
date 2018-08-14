from refl1d.names import *
from numpy import arange, linspace

Probe.view = 'log'

SiOx_SLD = 3.4688
SiOx_irho = 0.00000985

W_SLD = 3.072
W_irho = 0.03317

WOx_SLD = 4.141
WOx_irho = 0.009456

elyte_SLD = 4.558
elyte_irho = 0.001477

#Using Li2CO3 as reference for inner SEI
inner_SLD = 3.483
inner_irho = 0.06737

#Using elyte as reference for outer SEI
outer_SLD = elyte_SLD
outer_irho = elyte_irho

data_file = 'w4elt.refl'

instrument = NCNR.ANDR(Tlo=0.5, slits_at_Tlo=0.2, slits_below=0.05)
probe = instrument.load(data_file)

### SLDs
rho_SiOx = Parameter(name="SiOx_relDensity", value=1.0)
rho_W = Parameter(name="W_relDensity", value=1.0)
rho_WOx = Parameter(name="WOx_relDensity", value=1.0)
rho_inner = Parameter(name="inner_surf_relDensity", value=1.0)
rho_outer = Parameter(name="outer_surf_relDensity", value=1.0)
rho_elyte = Parameter(name="elyte_relDensity", value=1.0)

SiOx = SLD(name="SiOx", rho=rho_SiOx*SiOx_SLD, irho=rho_SiOx*SiOx_irho)

W = SLD(name="W", rho=rho_W*W_SLD, irho=rho_W*W_irho)
WOx = SLD(name="WOx", rho=rho_WOx*WOx_SLD, irho=rho_WOx*WOx_irho)
inner = SLD(name="inner_surf", rho=rho_inner*inner_SLD, irho=rho_inner*inner_irho)
outer = SLD(name="outer_surf", rho=rho_outer*outer_SLD, irho=rho_outer*outer_irho)
elyte = SLD(name="elyte", rho=rho_elyte*elyte_SLD, irho=rho_elyte*elyte_irho)

### Interfaces
Si_SiOx = Parameter(name="Si:SiOx", value=0.0326474)
SiOx_W = Parameter(name="SiOx:W", value=12.9251)
# This is named generically because we want it to apply to all models (where the
#   specific layer at the interface will change names.
W_int = Parameter(name="W:Int" ,value=0.273827)
WOx_inner = Parameter(name="WOx:inner", value=0.3)
inner_outer = Parameter(name="inner:outer", value=0.3)
outer_elyte = Parameter(name="outer:elyte", value=100)

### Thicknesses
SiOx_th = Parameter(name="SiOx_thickness", value=23.0619)

W_th = Parameter(name="W_thickness",value=149.5)
WOx_th = Parameter(name="WOx_thickness",value=19)
inner_th = Parameter(name="inner_surf_thickness",value=20)
outer_th = Parameter(name="outer_surf_thickness",value=100)



sample = elyte(0,outer_elyte*outer_th) | outer(outer_th,inner_outer*inner_th) | inner(inner_th,WOx_inner*WOx_th) | WOx(WOx_th,W_int*WOx_th)  | W(W_th,SiOx_W*SiOx_th) | SiOx(SiOx_th,Si_SiOx*SiOx_th) | silicon
#sample = elyte(0,outer_elyte*outer_th) | outer(outer_th,inner_outer*inner_th) | inner(inner_th,WOx_inner*WOx_th) | WOx(WOx_th,W_int*WOx_th) | W(W_th,SiOx) | SiOx(SiOx_th,Si_SiOx*SiOx_th) | silicon

### Fitting Parameters

#SLDs
rho_SiOx.range(0.5, 2.)
rho_W.range(0.5, 2.)
rho_elyte.range(0.85,0.9)
rho_WOx.range(0.0, 1.207438)
rho_inner.range(-0.3176, 1.4355)
rho_outer.range(-0.2194, 1.09697)

#Thicknesses
SiOx_th.range(100,150)
W_th.range(120,180)
WOx_th.range(5,150)
inner_th.range(5,300)
outer_th.range(5,800)

#Interfaces
Si_SiOx.range(0.001,0.05)
SiOx_W.range(0.001,0.2)
W_int.range(0.001,0.45)
WOx_inner.range(0.001,0.45)
inner_outer.range(0.001,0.45)
outer_elyte.range(0.001,0.45)

theta_offset = Parameter(name='Theta_Offset',value=0)
theta_offset.range(-0.005,0.005)
probe.theta_offset = theta_offset

intensity = Parameter(name='Intensity',value=1.0)
intensity.range(0.7,1.2)
probe.intensity = intensity

BK = Parameter(name="Background", value=1)
BK.range(0,100)
probe.background = BK*1e-6


M = Experiment(probe=probe, sample=sample)
problem = FitProblem(M)
