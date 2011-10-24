import cell_mdl
reload(cell_mdl)
from enthought.mayavi import mlab
import numpy

Nx,Ny,Nz = 50,0,0

model = cell_mdl.Red3(Nx,Ny,Nz)
#model2 = cell_mdl.Red3(Nx,Ny,Nz)

#model.hx = 0.09
#model.Rax = 200
#model2.Dy = 0

#xyIstim = [5,6] 
#xyIstim1 = [5,6,0,54] 
#xyIstim2 = [40,82,95,97]
#tmdl = cell_mdl.IntPara(model)
tmdl = cell_mdl.IntSerial(model)
tmdl.compute(tmax=1000,stimCoord=[2,4])

import locale
locale.setlocale(locale.LC_NUMERIC, 'C')

import pylab

pylab.plot(tmdl.t,tmdl.Vm[5])
pylab.plot(tmdl.t,tmdl.Vm[15])
pylab.show()

#tmdl2 = cell_mdl.IntSerial(model2)
#tmdl2.compute(tmax=500,stimCoord=xyIstim1)

#logY=open('save.npz','w')
#numpy.savez(logY,t=tmdl2.t,Y=tmdl2.Vm)
#logY.close()

#tmdl2.show()
#mlab.imshow(tmdl2.Vm)

#v = tmdl.Vm[...,1:]

#s = mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(v[...,-2]),
#                            plane_orientation='z_axes',
#                            slice_index=3,
#                            vmin = v.min(),
#                            vmax = v.max()
#                        )

##s2 = mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(v[...,-2]),
##                            plane_orientation='y_axes',
##                            slice_index=round(Ny*2./10)+1,
##                            vmin = v.min(),
##                            vmax = v.max()
##                        )

#mlab.scalarbar(s,orientation='vertical',nb_labels=4,label_fmt='%.3f')
#mlab.outline()

###pour animation
#for i in range(v.shape[-1]):
#    s.mlab_source.scalars = v[...,i]
##    s2.mlab_source.scalars = v[...,i]



