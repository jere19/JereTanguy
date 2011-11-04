import cell_mdl
reload(cell_mdl)
from enthought.mayavi import mlab
import numpy

Nx,Ny,Nz = 80,120,0

model = cell_mdl.Red3(Nx,Ny,Nz)

tmdl = cell_mdl.IntPara(model)

shp = tmdl.mdl.Y.shape[:-1]
R = tmdl.mdl.Rax

tmdl.mdl.Rax = numpy.ones(shp) * R + numpy.random.uniform(-R/10,R/10,shp)
tmdl.mdl.Ray = numpy.ones(shp) * R + numpy.random.uniform(-R/10,R/10,shp)
tmdl.mdl.hx = 0.06
tmdl.mdl.hy = 0.06
tmdl.compute(tmax=1000,stimCoord=[3,42,4,6],stimCoord2=[40,82,95,97])

tmdl.show()
