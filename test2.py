import cell_mdl
reload(cell_mdl)
from enthought.mayavi import mlab
import numpy

Nx,Ny,Nz = 60,60,12

model = cell_mdl.Red3(Nx,Ny,Nz)

#anisotropie

pdg = model.Padding/2

h = numpy.ones((Nx+pdg*2,Ny+pdg*2,Nz+pdg*2,3))*model.hx
Ra = numpy.ones((Nx+pdg*2,Ny+pdg*2,Nz+pdg*2,3))*model.Rax
masktempo = numpy.ones((Nx+pdg*2,Ny+pdg*2,Nz+pdg*2,3))

#h[...,:round(Nz*2./5)+pdg,0] *= 3
#h[...,round(Nz*2./5)+pdg:round(Nz*3./5)+pdg,2] *= 3
#h[...,round(Nz*3./5)+pdg:,1] *= 3

model.hx = h[...,0]
model.hy = h[...,1]
model.hz = h[...,2]

Ra[...,:round(Nz*2./5)+pdg,0] *= 1
Ra[...,round(Nz*2./5)+pdg:round(Nz*3./5)+pdg,2] *= 1
Ra[...,round(Nz*3./5)+pdg:,1] *= 1

model.Rax = Ra[...,0]
model.Ray = Ra[...,1]
model.Raz = Ra[...,2]

masktempo[...,round(Nz*2./5):round(Nz*3./5),:] = 0
masktempo[round(Nx*1./10):round(Nx*2./10),round(Ny*1./10):round(Ny*2./10),round(Nz*2./5):round(Nz*3./5),:] = 1
masktempo[round(Nx*8./10):round(Nx*9./10),round(Ny*8./10):round(Ny*9./10),round(Nz*2./5):round(Nz*3./5),:] = 1

model.masktempo = masktempo

stimCoord = [round(Nx*5./10),round(Nx*6./10),round(Ny*2./10),round(Ny*8./10),pdg,pdg+1]

tmdl = cell_mdl.IntPara(model)
#tmdl = cell_mdl.IntSerial(model)
############################################
tmdl.compute(tmax=200,stimCoord=stimCoord)
############################################



tmdl.show()


