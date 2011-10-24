import cell_mdl2
reload(cell_mdl2)
from enthought.mayavi import mlab
import numpy

Nx1,Ny1,Nz1 = 20,20,4
Nx2,Ny2,Nz2 = 20,20,4
Nx3,Ny3,Nz3 = 20,20,4

#model1 = cell_mdl2.Red3(Nx1,Ny1,Nz1,borders=[True,True,True,True,True,False])
#model2 = cell_mdl2.Red3(Nx2,Ny2,Nz2,borders=[True,True,True,True,False,False])
#model3 = cell_mdl2.Red3(Nx3,Ny3,Nz3,borders=[True,True,True,True,False,True])

model1 = cell_mdl2.Red3(Nx1,Ny1,Nz1,borders=[True,True,True,True,True,True])
model2 = cell_mdl2.Red3(Nx2,Ny2,Nz2,borders=[True,True,True,True,False,False])
model3 = cell_mdl2.Red3(Nx3,Ny3,Nz3,borders=[True,True,True,True,False,True])
##anisotropie

#pdg = model.Padding/2

#h = numpy.ones((Nx+pdg*2,Ny+pdg*2,Nz+pdg*2,3))*model.hx
#Ra = numpy.ones((Nx+pdg*2,Ny+pdg*2,Nz+pdg*2,3))*model.Rax
#masktempo = numpy.ones((Nx+pdg*2,Ny+pdg*2,Nz+pdg*2,3))

##h[...,:round(Nz*2./5)+pdg,0] *= 3
##h[...,round(Nz*2./5)+pdg:round(Nz*3./5)+pdg,2] *= 3
##h[...,round(Nz*3./5)+pdg:,1] *= 3

#model.hx = h[...,0]
#model.hy = h[...,1]
#model.hz = h[...,2]

#Ra[...,:round(Nz*2./5)+pdg,0] *= 1
#Ra[...,round(Nz*2./5)+pdg:round(Nz*3./5)+pdg,2] *= 1
#Ra[...,round(Nz*3./5)+pdg:,1] *= 1

#model.Rax = Ra[...,0]
#model.Ray = Ra[...,1]
#model.Raz = Ra[...,2]

#masktempo[...,round(Nz*2./5):round(Nz*3./5),:] = 0
#masktempo[round(Nx*1./10):round(Nx*2./10),round(Ny*1./10):round(Ny*2./10),round(Nz*2./5):round(Nz*3./5),:] = 1
#masktempo[round(Nx*8./10):round(Nx*9./10),round(Ny*8./10):round(Ny*9./10),round(Nz*2./5):round(Nz*3./5),:] = 1

#model.masktempo = masktempo

stimCoord = [3,5,3,5,2,4]

globalmodel = cell_mdl2.AnisoTissueModel(model1,model2,model3)

#tmdl = cell_mdl2.IntPara(globalmodel)
tmdl = cell_mdl2.IntSerial(globalmodel)
############################################
tmdl.compute(tmax=5,stimCoord=stimCoord)
############################################



tmdl.show()


