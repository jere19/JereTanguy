import cell_mdl
reload(cell_mdl)
from enthought.mayavi import mlab
import numpy

Nx,Ny,Nz = 0,0,0

model = cell_mdl.Red3(Nx,Ny,Nz)

#anisotropie


#tmdl = cell_mdl.IntPara(model)
tmdl2 = cell_mdl.IntSerial(model)
tmdl2.compute(tmax=10,stimCoord=[0])


#mlab.contour3d(v[...,-1])

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


##logY=open('save.npz','w')
##numpy.savez(logY,t=t,v=v)
##logY.close()
